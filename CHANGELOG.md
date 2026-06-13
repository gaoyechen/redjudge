# Changelog

## v1.0.0 (2026-06-13)

First public GitHub release.

### Highlights

- Published `redjudge` as a public repository.
- Delivered public packaging assets: `README.md`, `LICENSE`, `evals/evals.json`, showcase card, and GitHub Actions validation workflow.
- Replaced placeholder install instructions with the real public install path: `npx skills add gaoyechen/redjudge`.
- Added versioning surface: version badge, current version note, versioning section, and GitHub Release `v1.0.0`.

### Included

- `SKILL.md`: evidence-aware adversarial review protocol.
- `references/`: dimension templates, verdict rubric, anti-sycophancy rules, Luban audit notes.
- `evals/evals.json`: 5 regression prompts covering product strict, article, vague input, quick mode, and positive-only near miss.
- `scripts/`: `check-redjudge-evals.py` and `check-redjudge-evals.sh` for package validation.
- `examples/`: review style examples and a result-card showcase.
- `assets/`: static SVG result card.

### Validation

- Local package validation passed:
  - `python scripts/check-redjudge-evals.py`
- Public clone validation passed for the tag `v1.0.0` checkout.
- GitHub Actions validation succeeded before release publication.

### Notes

- `SKILL.md` frontmatter does not use a `version` field because the current `skill-creator` validator rejects unexpected keys.
- Versioning is handled via `README.md` plus GitHub Releases and this changelog.
