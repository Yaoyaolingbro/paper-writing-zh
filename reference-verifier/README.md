# reference-verifier

`reference-verifier` is a Codex skill for checking whether paper references and BibTeX entries are real and internally consistent. It is intended for AI conference reviewer agents and paper-writing agents that need to detect hallucinated references, wrong DOI metadata, title-author-year mismatches, venue errors, and arXiv/formal-version confusion.

## Installation

Install as a Codex skill bundle, for example:

```text
~/.codex/skills/reference-verifier/
```

or inside a project:

```text
skills/reference-verifier/
```

From this repository, run:

```bash
./install.sh
```

## Usage

Verify a BibTeX file:

```bash
python reference-verifier/scripts/verify_references.py --input refs.bib --out-dir reports
```

Verify a plain reference list:

```bash
python reference-verifier/scripts/verify_references.py --input references.txt --citing-year 2025 --out-dir reports
```

Outputs:

```text
reports/reference_verification.json
reports/reference_verification.md
```

## Data Sources

The script uses public metadata services:

- Crossref REST API for DOI and scholarly metadata checks.
- OpenAlex API for works search, especially when DOI is missing.
- Semantic Scholar Academic Graph API for AI/CS paper metadata.
- DBLP publication search for computer science venue metadata.
- arXiv API for preprint ID checks.

The verifier uses external evidence chains and should not rely on LLM memory.

## Google Scholar

Google Scholar is not used as an automated primary source because it does not provide a stable official public API and automated bulk access is brittle. It can be used for manual fallback when the report marks a reference as ambiguous.

## Parser Limits

The bundled script intentionally uses only Python standard library modules. Its BibTeX parser handles common entries and fields but is not a full BibTeX implementation. Complex nested braces, macros, crossref inheritance, nonstandard field syntax, and heavily abbreviated references may require manual checking.

## Common False Positives

- Very new papers may not yet be indexed in all sources.
- arXiv preprints may later appear under different official titles.
- Workshop, Findings, demo, dataset, and benchmark papers may have incomplete venue metadata.
- Author initials and name order can reduce author-overlap scores.
- Conference acronyms may differ across DBLP, Crossref, OpenAlex, and Semantic Scholar.

## Reviewer Agent Integration

A reviewer agent should run this skill before making reference-validity claims. Use the JSON report for structured risk filtering and the Markdown report for human-readable review notes.

Recommended reviewer workflow:

1. Run the verifier on the `.bib` or reference text file.
2. Inspect `SUSPICIOUS` and `LIKELY_FABRICATED_OR_WRONG` items first.
3. Use evidence chains, not memory, when writing review comments.
4. Treat `NEEDS_MANUAL_CHECK` as unresolved until manually verified.
5. Do not accuse fabrication unless the evidence supports it.
