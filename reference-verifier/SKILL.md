---
name: reference-verifier
description: Use when checking paper references, BibTeX entries, or bibliographies for hallucinated citations, wrong DOI, title-author-year mismatch, venue mismatch, arXiv/formal-version confusion, or suspicious scholarly metadata.
---

# Reference Verifier

## Use When

- Reviewing a paper's `.bib` file or reference list.
- Checking AI-generated citations before submission.
- Supporting reviewer or paper-writing agents that need evidence-based reference validation.

Do **not** judge references from memory. Use external metadata evidence from Crossref, OpenAlex, Semantic Scholar, DBLP, and arXiv.

## Inputs

- `.bib` file, or plain text references.
- Optional citing paper year.

Run:

```bash
python scripts/verify_references.py --input refs.bib --out-dir reports
python scripts/verify_references.py --input references.txt --citing-year 2025 --out-dir reports
```

## Workflow

1. Parse references: key/citation, DOI, arXiv ID, title, authors, year, venue.
2. Query evidence sources:
   - Crossref for DOI and bibliographic metadata.
   - OpenAlex for no-DOI or fuzzy title metadata.
   - Semantic Scholar for AI/CS paper metadata.
   - DBLP for CS venue metadata.
   - arXiv for preprints.
3. Compare title similarity, author overlap, year, DOI, venue, and arXiv/formal-version signals.
4. Produce JSON and Markdown reports with evidence chains.

## Scoring Rubric

- `VERIFIED`: DOI/arXiv exact match or strong multi-source match; title, author, and year align.
- `LIKELY_REAL`: strong title/author/year match from at least one trusted source, but DOI or venue may be missing.
- `NEEDS_MANUAL_CHECK`: partial or conflicting metadata; no clear fabrication signal.
- `SUSPICIOUS`: DOI not found, weak fuzzy match only, author-year mismatch, venue mismatch, or arXiv/formal-version ambiguity.
- `LIKELY_FABRICATED_OR_WRONG`: no source can find the title, or DOI resolves to a substantially different work, or multiple critical mismatches appear.

## Output

The script writes:

- `reference_verification.json`
- `reference_verification.md`

Each item must include:

- input citation or BibTeX key
- status and confidence
- matched sources
- evidence chain
- mismatches
- recommended action

Google Scholar is not a main API source. Use it only for manual fallback.
