#!/usr/bin/env python3
"""Verify references against public scholarly metadata APIs.

This is a small, dependency-free verifier intended for Codex skill use. It is
not a full bibliographic database client or a full BibTeX parser.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field, asdict
from difflib import SequenceMatcher
from typing import Any, Dict, Iterable, List, Optional, Tuple


STATUS_VERIFIED = "VERIFIED"
STATUS_LIKELY_REAL = "LIKELY_REAL"
STATUS_NEEDS_MANUAL_CHECK = "NEEDS_MANUAL_CHECK"
STATUS_SUSPICIOUS = "SUSPICIOUS"
STATUS_LIKELY_WRONG = "LIKELY_FABRICATED_OR_WRONG"

USER_AGENT = "reference-verifier/0.1 (mailto:metadata-check@example.com)"


@dataclass
class Reference:
    raw: str
    key: str = ""
    entry_type: str = ""
    title: str = ""
    authors: List[str] = field(default_factory=list)
    year: Optional[int] = None
    venue: str = ""
    doi: str = ""
    arxiv_id: str = ""
    fields: Dict[str, str] = field(default_factory=dict)


@dataclass
class SourceEvidence:
    source: str
    query: str
    found: bool
    title: str = ""
    authors: List[str] = field(default_factory=list)
    year: Optional[int] = None
    venue: str = ""
    doi: str = ""
    arxiv_id: str = ""
    url: str = ""
    title_similarity: float = 0.0
    author_overlap: float = 0.0
    year_match: Optional[bool] = None
    doi_match: Optional[bool] = None
    error: str = ""


@dataclass
class VerificationResult:
    input_id: str
    input_citation: str
    parsed: Dict[str, Any]
    status: str
    confidence: float
    risk_score: float
    matched_sources: List[str]
    evidence: List[Dict[str, Any]]
    mismatches: List[str]
    recommended_action: str


def http_json(url: str, timeout: int = 15) -> Tuple[Optional[Dict[str, Any]], str]:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8", errors="replace")), ""
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, json.JSONDecodeError) as exc:
        return None, str(exc)


def http_text(url: str, timeout: int = 15) -> Tuple[Optional[str], str]:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return response.read().decode("utf-8", errors="replace"), ""
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as exc:
        return None, str(exc)


def strip_latex(value: str) -> str:
    value = value.replace("\n", " ")
    value = re.sub(r"\\[a-zA-Z]+\*?(?:\[[^\]]*\])?(?:\{([^{}]*)\})?", r"\1", value)
    value = value.replace("{", "").replace("}", "")
    value = re.sub(r"\s+", " ", value)
    return value.strip(" ,.;")


def normalize_space(value: str) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def normalize_title(value: str) -> str:
    value = strip_latex(value).lower()
    value = re.sub(r"https?://\S+", " ", value)
    value = re.sub(r"[^a-z0-9]+", " ", value)
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def normalize_author_name(value: str) -> str:
    value = strip_latex(value).lower()
    value = re.sub(r"[^a-z\s,-]", " ", value)
    value = re.sub(r"\s+", " ", value).strip()
    if "," in value:
        value = value.split(",", 1)[0]
    parts = [p for p in value.split() if len(p) > 1]
    return parts[-1] if parts else value


def title_similarity(a: str, b: str) -> float:
    a_norm = normalize_title(a)
    b_norm = normalize_title(b)
    if not a_norm or not b_norm:
        return 0.0
    return SequenceMatcher(None, a_norm, b_norm).ratio()


def author_overlap(input_authors: Iterable[str], matched_authors: Iterable[str]) -> float:
    left = {normalize_author_name(a) for a in input_authors if normalize_author_name(a)}
    right = {normalize_author_name(a) for a in matched_authors if normalize_author_name(a)}
    if not left or not right:
        return 0.0
    return len(left & right) / max(1, min(len(left), len(right)))


def extract_doi(text: str) -> str:
    match = re.search(r"\b(10\.\d{4,9}/[-._;()/:A-Za-z0-9]+)", text or "", re.I)
    if not match:
        return ""
    return match.group(1).rstrip(".,;)").lower()


def extract_arxiv_id(text: str) -> str:
    patterns = [
        r"10\.48550/arXiv\.([0-9]{4}\.[0-9]{4,5}(?:v\d+)?)",
        r"arXiv[:\s]+([0-9]{4}\.[0-9]{4,5}(?:v\d+)?)",
        r"arxiv\.org/(?:abs|pdf)/([0-9]{4}\.[0-9]{4,5})(?:v\d+)?",
        r"\b([a-z-]+(?:\.[A-Z]{2})?/[0-9]{7})(?:v\d+)?\b",
    ]
    for pattern in patterns:
        match = re.search(pattern, text or "", re.I)
        if match:
            return match.group(1)
    return ""


def parse_authors(value: str) -> List[str]:
    value = strip_latex(value)
    if " and " in value:
        return [normalize_space(v) for v in re.split(r"\s+and\s+", value) if normalize_space(v)]
    pieces = [p.strip() for p in value.split(",") if p.strip()]
    if len(pieces) > 2:
        return pieces
    return [value] if value else []


def split_bib_entries(text: str) -> List[str]:
    entries: List[str] = []
    pos = 0
    while True:
        start = text.find("@", pos)
        if start == -1:
            break
        brace = text.find("{", start)
        if brace == -1:
            break
        depth = 0
        end = brace
        while end < len(text):
            ch = text[end]
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    end += 1
                    break
            end += 1
        entries.append(text[start:end])
        pos = end
    return entries


def parse_bib_fields(body: str) -> Dict[str, str]:
    fields: Dict[str, str] = {}
    i = 0
    n = len(body)
    while i < n:
        while i < n and body[i] in " \n\r\t,":
            i += 1
        name_start = i
        while i < n and re.match(r"[A-Za-z0-9_-]", body[i]):
            i += 1
        name = body[name_start:i].lower()
        while i < n and body[i].isspace():
            i += 1
        if not name or i >= n or body[i] != "=":
            i += 1
            continue
        i += 1
        while i < n and body[i].isspace():
            i += 1
        if i >= n:
            break
        if body[i] == "{":
            depth = 0
            value_start = i + 1
            while i < n:
                if body[i] == "{":
                    depth += 1
                elif body[i] == "}":
                    depth -= 1
                    if depth == 0:
                        fields[name] = body[value_start:i].strip()
                        i += 1
                        break
                i += 1
        elif body[i] == '"':
            i += 1
            value_start = i
            escaped = False
            while i < n:
                if body[i] == '"' and not escaped:
                    fields[name] = body[value_start:i].strip()
                    i += 1
                    break
                escaped = body[i] == "\\" and not escaped
                if body[i] != "\\":
                    escaped = False
                i += 1
        else:
            value_start = i
            while i < n and body[i] not in ",\n\r":
                i += 1
            fields[name] = body[value_start:i].strip()
    return fields


def parse_bibtex(text: str) -> List[Reference]:
    refs: List[Reference] = []
    for index, entry in enumerate(split_bib_entries(text), start=1):
        header = re.match(r"@(\w+)\s*\{\s*([^,]+)\s*,", entry, re.S)
        if not header:
            continue
        entry_type = header.group(1)
        key = header.group(2).strip()
        body = entry[header.end() : entry.rfind("}")]
        fields = parse_bib_fields(body)
        venue = fields.get("venue") or fields.get("booktitle") or fields.get("journal") or fields.get("publisher") or ""
        year_text = fields.get("year", "")
        year_match = re.search(r"(19|20)\d{2}", year_text)
        doi = fields.get("doi") or extract_doi(entry)
        arxiv_id = fields.get("eprint") if fields.get("archiveprefix", "").lower() == "arxiv" else extract_arxiv_id(entry)
        if not arxiv_id and doi.lower().startswith("10.48550/arxiv."):
            arxiv_id = doi.split("arXiv.", 1)[-1] if "arXiv." in doi else doi.rsplit(".", 1)[-1]
        refs.append(
            Reference(
                raw=entry,
                key=key or f"bib-{index}",
                entry_type=entry_type,
                title=strip_latex(fields.get("title", "")),
                authors=parse_authors(fields.get("author", "")),
                year=int(year_match.group(0)) if year_match else None,
                venue=strip_latex(venue),
                doi=doi.lower(),
                arxiv_id=arxiv_id,
                fields=fields,
            )
        )
    return refs


def parse_text_references(text: str) -> List[Reference]:
    chunks = [c.strip() for c in re.split(r"\n\s*\n", text) if c.strip()]
    if len(chunks) == 1:
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        if len(lines) > 1:
            chunks = lines
    refs: List[Reference] = []
    for index, raw in enumerate(chunks, start=1):
        year_match = re.search(r"\b(19|20)\d{2}\b", raw)
        year = int(year_match.group(0)) if year_match else None
        before_year = raw[: year_match.start()] if year_match else raw[:120]
        authors = parse_authors(re.sub(r"^\[\d+\]\s*", "", before_year).strip(" ."))
        doi = extract_doi(raw)
        arxiv_id = extract_arxiv_id(raw)
        title = ""
        quoted = re.search(r"[\"“](.+?)[\"”]", raw)
        if quoted:
            title = quoted.group(1)
        elif year_match:
            after = raw[year_match.end() :]
            after = re.sub(r"^[).,\s]+", "", after)
            title = re.split(r"\.\s+|\s+In\s+|//", after, maxsplit=1)[0]
        if not title:
            title = raw
        venue = ""
        after_title = raw.split(title, 1)[-1] if title and title in raw else ""
        venue_match = re.search(r"(?:In\s+)?([^.,;]*?(?:Conference|Proceedings|Journal|Transactions|ACL|EMNLP|NeurIPS|ICLR|ICML|CVPR|AAAI|KDD|SIGIR|WWW)[^.,;]*)", after_title, re.I)
        if venue_match:
            venue = venue_match.group(1).strip()
        refs.append(
            Reference(
                raw=raw,
                key=f"ref-{index}",
                title=strip_latex(title),
                authors=authors,
                year=year,
                venue=strip_latex(venue),
                doi=doi,
                arxiv_id=arxiv_id,
            )
        )
    return refs


def parse_references(path: str) -> List[Reference]:
    with open(path, "r", encoding="utf-8", errors="replace") as handle:
        text = handle.read()
    if path.lower().endswith(".bib") or re.search(r"@\w+\s*\{", text):
        refs = parse_bibtex(text)
        if refs:
            return refs
    return parse_text_references(text)


def source_from_crossref_item(item: Dict[str, Any], query: str, ref: Reference) -> SourceEvidence:
    authors = []
    for author in item.get("author", []) or []:
        name = " ".join([author.get("given", ""), author.get("family", "")]).strip()
        if name:
            authors.append(name)
    title = " ".join(item.get("title") or [])
    year = None
    for key in ("published-print", "published-online", "created", "issued"):
        parts = (((item.get(key) or {}).get("date-parts") or [[None]])[0])
        if parts and parts[0]:
            year = int(parts[0])
            break
    venue = " ".join(item.get("container-title") or [])
    doi = (item.get("DOI") or "").lower()
    evidence = SourceEvidence(
        source="Crossref",
        query=query,
        found=True,
        title=title,
        authors=authors,
        year=year,
        venue=venue,
        doi=doi,
        url=item.get("URL", ""),
    )
    enrich_evidence_scores(evidence, ref)
    return evidence


def query_crossref(ref: Reference) -> List[SourceEvidence]:
    if ref.doi:
        url = "https://api.crossref.org/works/" + urllib.parse.quote(ref.doi)
        data, error = http_json(url)
        if data and data.get("message"):
            return [source_from_crossref_item(data["message"], ref.doi, ref)]
        return [SourceEvidence(source="Crossref", query=ref.doi, found=False, error=error or "DOI not found")]
    if not ref.title:
        return []
    query = urllib.parse.urlencode({"query.title": ref.title, "rows": 3})
    data, error = http_json("https://api.crossref.org/works?" + query)
    if not data:
        return [SourceEvidence(source="Crossref", query=ref.title, found=False, error=error)]
    items = (data.get("message") or {}).get("items") or []
    return [source_from_crossref_item(item, ref.title, ref) for item in items[:3]]


def query_openalex(ref: Reference) -> List[SourceEvidence]:
    if not ref.title and not ref.doi:
        return []
    search = ref.title if ref.doi.lower().startswith("10.48550/arxiv.") else (ref.doi or ref.title)
    query = urllib.parse.urlencode({"search": search, "per-page": 3})
    data, error = http_json("https://api.openalex.org/works?" + query)
    if not data:
        return [SourceEvidence(source="OpenAlex", query=search, found=False, error=error)]
    results = []
    for item in data.get("results", [])[:3]:
        authors = []
        for authorship in item.get("authorships", []) or []:
            name = ((authorship.get("author") or {}).get("display_name") or "").strip()
            if name:
                authors.append(name)
        ids = item.get("ids") or {}
        evidence = SourceEvidence(
            source="OpenAlex",
            query=search,
            found=True,
            title=item.get("title") or "",
            authors=authors,
            year=item.get("publication_year"),
            venue=((item.get("primary_location") or {}).get("source") or {}).get("display_name", ""),
            doi=(ids.get("doi") or "").replace("https://doi.org/", "").lower(),
            url=ids.get("openalex", ""),
        )
        enrich_evidence_scores(evidence, ref)
        results.append(evidence)
    return results or [SourceEvidence(source="OpenAlex", query=search, found=False, error="No results")]


def query_semantic_scholar(ref: Reference) -> List[SourceEvidence]:
    if not ref.title and not ref.doi:
        return []
    if ref.arxiv_id:
        paper_id = "ARXIV:" + ref.arxiv_id
        fields = "title,authors,year,venue,externalIds,url"
        url = "https://api.semanticscholar.org/graph/v1/paper/" + urllib.parse.quote(paper_id) + "?" + urllib.parse.urlencode({"fields": fields})
        data, error = http_json(url)
        if data and data.get("title"):
            return [semantic_item_to_evidence(data, ref.arxiv_id, ref)]
        if not ref.doi:
            return [SourceEvidence(source="Semantic Scholar", query=ref.arxiv_id, found=False, error=error or "arXiv ID not found")]
    if ref.doi:
        paper_id = "DOI:" + ref.doi
        fields = "title,authors,year,venue,externalIds,url"
        url = "https://api.semanticscholar.org/graph/v1/paper/" + urllib.parse.quote(paper_id) + "?" + urllib.parse.urlencode({"fields": fields})
        data, error = http_json(url)
        if data and data.get("title"):
            evidence = semantic_item_to_evidence(data, ref.doi, ref)
            return [evidence]
        return [SourceEvidence(source="Semantic Scholar", query=ref.doi, found=False, error=error or "DOI not found")]
    query = urllib.parse.urlencode({"query": ref.title, "limit": 3, "fields": "title,authors,year,venue,externalIds,url"})
    data, error = http_json("https://api.semanticscholar.org/graph/v1/paper/search?" + query)
    if not data:
        return [SourceEvidence(source="Semantic Scholar", query=ref.title, found=False, error=error)]
    return [semantic_item_to_evidence(item, ref.title, ref) for item in data.get("data", [])[:3]] or [
        SourceEvidence(source="Semantic Scholar", query=ref.title, found=False, error="No results")
    ]


def semantic_item_to_evidence(item: Dict[str, Any], query: str, ref: Reference) -> SourceEvidence:
    external = item.get("externalIds") or {}
    evidence = SourceEvidence(
        source="Semantic Scholar",
        query=query,
        found=True,
        title=item.get("title") or "",
        authors=[a.get("name", "") for a in item.get("authors", []) if a.get("name")],
        year=item.get("year"),
        venue=item.get("venue") or "",
        doi=(external.get("DOI") or "").lower(),
        arxiv_id=external.get("ArXiv") or "",
        url=item.get("url") or "",
    )
    enrich_evidence_scores(evidence, ref)
    return evidence


def query_dblp(ref: Reference) -> List[SourceEvidence]:
    if not ref.title:
        return []
    query = urllib.parse.urlencode({"q": ref.title, "format": "json", "h": 3})
    data, error = http_json("https://dblp.org/search/publ/api?" + query)
    if not data:
        return [SourceEvidence(source="DBLP", query=ref.title, found=False, error=error)]
    hits = (((data.get("result") or {}).get("hits") or {}).get("hit") or [])[:3]
    results = []
    for hit in hits:
        info = (hit.get("info") or {})
        authors_raw = (info.get("authors") or {}).get("author") or []
        if isinstance(authors_raw, dict):
            authors = [authors_raw.get("text", "")]
        else:
            authors = [a.get("text", "") if isinstance(a, dict) else str(a) for a in authors_raw]
        evidence = SourceEvidence(
            source="DBLP",
            query=ref.title,
            found=True,
            title=info.get("title") or "",
            authors=[a for a in authors if a],
            year=int(info["year"]) if str(info.get("year", "")).isdigit() else None,
            venue=info.get("venue") or "",
            doi=(info.get("doi") or "").lower(),
            url=info.get("url") or "",
        )
        enrich_evidence_scores(evidence, ref)
        results.append(evidence)
    return results or [SourceEvidence(source="DBLP", query=ref.title, found=False, error="No results")]


def query_arxiv(ref: Reference) -> List[SourceEvidence]:
    if not ref.arxiv_id:
        return []
    url = "http://export.arxiv.org/api/query?" + urllib.parse.urlencode({"id_list": ref.arxiv_id})
    text, error = http_text(url)
    if not text:
        return [SourceEvidence(source="arXiv", query=ref.arxiv_id, found=False, error=error)]
    try:
        root = ET.fromstring(text)
    except ET.ParseError as exc:
        return [SourceEvidence(source="arXiv", query=ref.arxiv_id, found=False, error=str(exc))]
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    entries = root.findall("atom:entry", ns)
    results = []
    for entry in entries[:1]:
        title = normalize_space(entry.findtext("atom:title", default="", namespaces=ns))
        authors = [normalize_space(a.findtext("atom:name", default="", namespaces=ns)) for a in entry.findall("atom:author", ns)]
        published = entry.findtext("atom:published", default="", namespaces=ns)
        year = int(published[:4]) if re.match(r"\d{4}", published) else None
        evidence = SourceEvidence(
            source="arXiv",
            query=ref.arxiv_id,
            found=True,
            title=title,
            authors=[a for a in authors if a],
            year=year,
            venue="arXiv",
            arxiv_id=ref.arxiv_id,
            url=entry.findtext("atom:id", default="", namespaces=ns),
        )
        enrich_evidence_scores(evidence, ref)
        results.append(evidence)
    return results or [SourceEvidence(source="arXiv", query=ref.arxiv_id, found=False, error="No arXiv entry")]


def enrich_evidence_scores(evidence: SourceEvidence, ref: Reference) -> None:
    evidence.title_similarity = round(title_similarity(ref.title, evidence.title), 3)
    evidence.author_overlap = round(author_overlap(ref.authors, evidence.authors), 3)
    evidence.year_match = None if ref.year is None or evidence.year is None else ref.year == evidence.year
    evidence.doi_match = None if not ref.doi or not evidence.doi else ref.doi.lower() == evidence.doi.lower()


def collect_evidence(ref: Reference, delay: float = 0.15) -> List[SourceEvidence]:
    sources = []
    for query_func in (query_arxiv, query_crossref, query_openalex, query_semantic_scholar, query_dblp):
        try:
            results = query_func(ref)
            sources.extend(results)
        except Exception as exc:  # Defensive graceful degradation.
            sources.append(SourceEvidence(source=query_func.__name__, query=ref.title or ref.doi, found=False, error=str(exc)))
        time.sleep(delay)
    return sources


def best_found_evidence(evidence: List[SourceEvidence]) -> List[SourceEvidence]:
    return sorted(
        [e for e in evidence if e.found],
        key=lambda e: (e.doi_match is True, e.title_similarity, e.author_overlap, e.year_match is True),
        reverse=True,
    )


def venue_mismatch(input_venue: str, matched_venue: str) -> bool:
    if not input_venue or not matched_venue:
        return False
    left = normalize_title(input_venue)
    right = normalize_title(matched_venue)
    if not left or not right:
        return False
    return SequenceMatcher(None, left, right).ratio() < 0.45 and left not in right and right not in left


def classify(ref: Reference, evidence: List[SourceEvidence], citing_year: Optional[int]) -> VerificationResult:
    found = best_found_evidence(evidence)
    mismatches: List[str] = []
    risk = 0.55

    arxiv_doi = ref.doi.lower().startswith("10.48550/arxiv.")
    arxiv_verified = bool(ref.arxiv_id and any(e.source == "arXiv" and e.found and e.title_similarity >= 0.80 for e in evidence))

    if ref.doi and not arxiv_doi and any(e.source == "Crossref" and not e.found for e in evidence):
        mismatches.append("DOI not found")
        risk += 0.25
    elif arxiv_doi and arxiv_verified:
        risk -= 0.20

    if not found:
        mismatches.append("title not found in any source")
        risk = 0.95
    else:
        best = found[0]
        risk -= min(0.35, best.title_similarity * 0.25)
        risk -= min(0.20, best.author_overlap * 0.15)
        if best.year_match is True:
            risk -= 0.10
        elif best.year_match is False:
            mismatches.append("author-year mismatch" if best.author_overlap >= 0.4 else "year mismatch")
            risk += 0.15
        if ref.doi and not arxiv_doi:
            if any(e.doi_match is True for e in found):
                risk -= 0.20
            elif any(e.doi for e in found):
                mismatches.append("DOI resolves to a different title or identifier")
                risk += 0.25
        elif arxiv_doi and not arxiv_verified:
            mismatches.append("arXiv DOI should be checked against arXiv metadata")
            risk += 0.10
        if best.title_similarity < 0.70:
            mismatches.append("only weak fuzzy match found")
            risk += 0.20
        elif best.title_similarity < 0.86:
            mismatches.append("title match is partial")
            risk += 0.08
        if ref.authors and best.authors and best.author_overlap < 0.34:
            mismatches.append("author mismatch")
            risk += 0.18
        if venue_mismatch(ref.venue, best.venue):
            mismatches.append("venue mismatch")
            risk += 0.12
        if ref.arxiv_id and any(e.source != "arXiv" and e.found and e.title_similarity > 0.86 for e in found):
            mismatches.append("arXiv/formal-version metadata should be checked")

    if citing_year and ref.year and ref.year > citing_year:
        mismatches.append("publication year after citing paper year")
        risk += 0.30

    risk = max(0.0, min(1.0, risk))
    confidence = round(1.0 - risk, 3)

    if risk <= 0.18:
        status = STATUS_VERIFIED
        action = "Accept metadata; keep DOI/arXiv and venue fields normalized."
    elif risk <= 0.36:
        status = STATUS_LIKELY_REAL
        action = "Likely real; manually normalize missing DOI or venue if needed."
    elif risk <= 0.58:
        status = STATUS_NEEDS_MANUAL_CHECK
        action = "Manually check metadata and compare against publisher or anthology page."
    elif risk <= 0.78:
        status = STATUS_SUSPICIOUS
        action = "Do not rely on this citation until DOI/title/author/venue conflicts are resolved."
    else:
        status = STATUS_LIKELY_WRONG
        action = "Treat as likely fabricated or wrong unless manual verification finds authoritative metadata."

    return VerificationResult(
        input_id=ref.key,
        input_citation=ref.raw,
        parsed={
            "title": ref.title,
            "authors": ref.authors,
            "year": ref.year,
            "venue": ref.venue,
            "doi": ref.doi,
            "arxiv_id": ref.arxiv_id,
        },
        status=status,
        confidence=confidence,
        risk_score=round(risk, 3),
        matched_sources=sorted({e.source for e in found}),
        evidence=[asdict(e) for e in evidence],
        mismatches=sorted(set(mismatches)),
        recommended_action=action,
    )


def render_markdown(results: List[VerificationResult]) -> str:
    counts = {status: 0 for status in [STATUS_VERIFIED, STATUS_LIKELY_REAL, STATUS_NEEDS_MANUAL_CHECK, STATUS_SUSPICIOUS, STATUS_LIKELY_WRONG]}
    for result in results:
        counts[result.status] = counts.get(result.status, 0) + 1

    lines = [
        "# Reference Verification Report",
        "",
        "## Summary",
        f"- Total references: {len(results)}",
        f"- Verified: {counts[STATUS_VERIFIED]}",
        f"- Likely real: {counts[STATUS_LIKELY_REAL]}",
        f"- Needs manual check: {counts[STATUS_NEEDS_MANUAL_CHECK]}",
        f"- Suspicious: {counts[STATUS_SUSPICIOUS]}",
        f"- Likely fabricated or wrong: {counts[STATUS_LIKELY_WRONG]}",
        "",
        "## High-risk references",
        "",
    ]
    high_risk = [r for r in results if r.status in {STATUS_SUSPICIOUS, STATUS_LIKELY_WRONG}]
    if not high_risk:
        lines.append("No high-risk references detected.")
    for result in high_risk:
        lines.extend(render_result_item(result, compact=True))

    lines.extend(["", "## Full results", ""])
    for result in results:
        lines.extend(render_result_item(result, compact=False))
    return "\n".join(lines).rstrip() + "\n"


def render_result_item(result: VerificationResult, compact: bool) -> List[str]:
    title = result.parsed.get("title") or result.input_id
    lines = [
        f"### {result.input_id}: {title}",
        "",
        f"- Input citation / BibTeX key: `{result.input_id}`",
        f"- Status: `{result.status}`",
        f"- Confidence: {result.confidence}",
        f"- Matched sources: {', '.join(result.matched_sources) if result.matched_sources else 'None'}",
        f"- Mismatches: {', '.join(result.mismatches) if result.mismatches else 'None'}",
        f"- Recommended action: {result.recommended_action}",
    ]
    if compact:
        lines.append("")
        return lines
    lines.extend(["- Evidence:"])
    for evidence in result.evidence:
        found = "found" if evidence.get("found") else "not found"
        detail = evidence.get("title") or evidence.get("error") or "no detail"
        lines.append(
            f"  - {evidence.get('source')}: {found}; title_sim={evidence.get('title_similarity')}; "
            f"author_overlap={evidence.get('author_overlap')}; year_match={evidence.get('year_match')}; "
            f"doi_match={evidence.get('doi_match')}; detail={detail}"
        )
    lines.append("")
    return lines


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Verify BibTeX or reference text against scholarly metadata APIs.")
    parser.add_argument("--input", required=True, help="Path to .bib or plain text references.")
    parser.add_argument("--out-dir", default="reports", help="Directory for JSON and Markdown reports.")
    parser.add_argument("--citing-year", type=int, default=None, help="Optional citing paper year for future-publication checks.")
    args = parser.parse_args(argv)

    refs = parse_references(args.input)
    if not refs:
        print("No references parsed.", file=sys.stderr)
        return 2

    os.makedirs(args.out_dir, exist_ok=True)
    results: List[VerificationResult] = []
    for ref in refs:
        evidence = collect_evidence(ref)
        results.append(classify(ref, evidence, args.citing_year))

    payload = {
        "input": args.input,
        "citing_year": args.citing_year,
        "total_references": len(results),
        "results": [asdict(result) for result in results],
    }

    json_path = os.path.join(args.out_dir, "reference_verification.json")
    md_path = os.path.join(args.out_dir, "reference_verification.md")
    with open(json_path, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)
    with open(md_path, "w", encoding="utf-8") as handle:
        handle.write(render_markdown(results))

    print(f"Wrote {json_path}")
    print(f"Wrote {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
