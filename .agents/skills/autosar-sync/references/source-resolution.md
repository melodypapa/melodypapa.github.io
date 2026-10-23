# Source resolution — AUTOSAR standard documents

Decide where the authoritative source text for a sync comes from, in this
order. Always record which source (and release) you used in the issue and PR
text — reviewers rely on it.

## 1. Primary: markdown conversion, R23-11

```
~/Workspace/autosar_standard/markdown/Classic_Platform/Releases/R23-11/<Category>/AUTOSAR_CP_<TYPE>_<Name>.md
```

- Confirm this root exists on the machine before relying on it; it lives
  outside the repo.
- `<TYPE>` is one of `SWS` (module specification — the structural source for
  module articles), `EXP` (explanatory guides), `SRS` (requirements — only for
  requirement-coverage checks), `RS` (feature requirements), `TPS` (templates).
- `<Category>` is the standard taxonomy directory, e.g. `Communication`,
  `Crypto`, `Diagnostics`, `General`, `IO`, `Libraries`, `MCAL`, `Memory`,
  `MethodologyAndTemplates`, `ModeManagement`, `RTE`, `SystemServices`,
  `ApplicationInterfaces`, `GlobalTime`, `Security`, `Safety`, `SWArch`,
  `BSWGeneral`.
- Sidecar directories named `*_artifacts` hold the figure images; the site
  convention omits figures, so ignore them.

## 2. Fallback: nearest available release in the markdown tree

Available releases have historically been `R23-11`, `R25-11`, `R4.3.1`,
`R3.2.3` (no R22-11). If the user names a release that is absent, pick the
nearest release, say so explicitly, and note content differences you notice
(added/removed chapters vs the requested release) in the PR text.

## 3. Last resort: bundled PDFs in the repo

```
docs/autosar_pdf/AUTOSAR_CP/<Release>/<Category>/<AUTOSAR_<TYPE>_<Name>>.pdf
```

Releases currently bundled: `R22-11`, `R4.3.1` (226 PDFs; ~124 SWS-class).
Extraction recipe with pypdf (no `pdftotext` on this machine):

```bash
python3 - <<'EOF'
from pypdf import PdfReader
r = PdfReader("docs/autosar_pdf/AUTOSAR_CP/R22-11/IO/AUTOSAR_SWS_ICUDriver.pdf")
print("\n".join((p.extract_text() or "") for p in r.pages))
EOF
```

Fidelity warnings when translating from PDF extraction:

- Requirement tables (Description / Rationale / Dependencies rows) come out
  jumbled and split across pages — reconstruct each requirement's table row by
  row from context, and prefer translating the prose semantics over
  reproducing table layout.
- Figures are lost (site convention omits them anyway).
- Page headers/footers and `glyph[...]` artifacts pepper the text; strip them.
- If `R4.3.1` markdown exists for the same document in the markdown tree, use
  it to disambiguate garbled table structure — but keep the R22-11 wording as
  the content source and say both releases in the PR text.

## Which document type to pick

| Article kind | Source doc |
| --- | --- |
| Module article (`<module>/index.md`) | `SWS_<ModuleName>` |
| Guide article (e.g. 模式管理指南) | `EXP_<...Guide>` |
| Requirement-gap check | `SRS_<...>` as a checklist only |
| Feature-level questions | `RS_Features` via the spec's tracing table |
