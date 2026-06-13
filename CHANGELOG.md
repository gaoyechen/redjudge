# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## v1.0.0 - 2026-06-13

First public GitHub release.

### Added

- Public repository packaging for RedJudge.
- `README.md` with hook, use cases, quick start, trigger phrases, safety boundary, showcase, and verification section.
- `LICENSE` under MIT.
- `evals/evals.json` with 5 regression prompts covering product strict, article review, vague-input boundary, quick mode, and positive-only near miss.
- `scripts/check-redjudge-evals.py` and `scripts/check-redjudge-evals.sh` for package validation.
- `examples/redjudge-result-card.md` as a screenshot-friendly result card.
- `assets/redjudge-result-card.svg` as a static visual showcase.
- `.github/workflows/validate.yml` for GitHub Actions validation.
- Versioning surface: version badge, current version note, version section, release notes, and `CHANGELOG.md`.
- Real public install command: `npx skills add gaoyechen/redjudge`.

### Included

- `SKILL.md`: evidence-aware adversarial review protocol with Evidence Boundary, Red Scan, Multi-Perspective Review, Value Confirmation, and Verdict flow.
- `references/`: dimension templates, verdict rubric, anti-sycophancy rules, and Luban audit notes.

### Validation

- Local package validation passed: `python scripts/check-redjudge-evals.py`.
- Public clone validation passed for the `v1.0.0` tag checkout.
- GitHub Actions validation succeeded before release publication.

### Notes

- `SKILL.md` frontmatter does not use a `version` field because the current `skill-creator` validator rejects unexpected keys.
- Versioning is handled via `README.md`, GitHub Releases, and this changelog.
- This release represents the first usable public packaging of RedJudge for external discovery and installation.
