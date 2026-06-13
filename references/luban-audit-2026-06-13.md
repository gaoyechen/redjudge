# RedJudge Luban Audit Notes — 2026-06-13

Use this reference when improving, packaging, or publishing RedJudge as a public skill. It records the Luban-style audit findings from a real polishing session.

## Current position

RedJudge is viable as a private Hermes skill. Its core method is sound: Evidence Boundary → Red Scan → multi-perspective review → Value Confirmation → verdict with weighted score → Next Validation.

The main gap is not methodology; it is public-skill packaging and regression proof.

## Structural check results

`luban/tools/check-skill-repo.sh <redjudge-skill-dir>` returned:

- PASS: 4
- WARN: 5
- FAIL: 2

Key findings:

- `SKILL.md` exists and has agent-facing workflow keywords.
- `examples/` exists with article/product/idea examples.
- `README.md` is missing.
- `scripts/` is missing.
- `LICENSE` is missing.
- `.claude-plugin/marketplace.json` is missing.
- demo GIF/video is missing.
- one-line `npx skills add` install path is missing.
- skills.sh badge is missing.

Interpretation: private-use quality is acceptable; public-release readiness is not.

## Dry-run behavior

Three test prompts were run through the current skill:

1. `/RedJudge product strict` on an AI job-coaching app idea.
   - Passed: Evidence Boundary, 5 Red Scan risks, evidence levels, roles, Value Confirmation, verdict, weighted total, Next Validation.
   - Verdict: `revise`, weighted total around 40.

2. `/RedJudge article` on an article claiming young people should stop learning programming because AI writes code.
   - Passed: unverified external claims were correctly labeled instead of treated as fact.
   - Verdict: `revise`, weighted total around 41.

3. Vague prompt: `帮我评估一下：AI 教育。`
   - Passed: correctly refused full review and asked for more context because the input was under-specified.

## Differentiation found in ecosystem scan

Relevant neighboring skills and frameworks:

- Architecture Critic — https://clawhub.ai/skills/architecture-critic
  - Learn: pre-build gate positioning, explicit verdict states, independent reviewer stance.
  - Do not copy: code/architecture-only scope.

- Red Team Review Loop — https://skillsmp.com/skills/richfrem-project-sanctuary-agents-skills-red-team-review-skill-md
  - Learn: review loop, approval gate, context bundle, iteration records.
  - Do not copy: heavy multi-agent/process overhead for the base RedJudge skill.

- Red Team Tribunal — https://skillsmp.com/skills/aegntic-cldcde-claude-skills-red-team-tribunal-skill-md
  - Learn: memorable tribunal metaphor and role-based reviewers.
  - Do not copy: dependency on multi-agent consensus for every use.

- adversarial-review — https://skills.rest/skill/adversarial-review
  - Learn: concise public hook, quick start, flaw-finding positioning.
  - Do not copy: generic plan-review phrasing that loses RedJudge’s evidence discipline.

- Critique Review Skill — https://www.critique.sh/skills/critique-review
  - Learn: findings-first output, risk triage, public skill packaging.
  - Do not copy: code-review-only assumptions.

- anti-sycophancy — https://clawhub.ai/0xcjl/anti-sycophancy
  - Learn: anti-confirmation-bias triggers and “challenge assumptions first”.
  - Do not copy: making RedJudge only an anti-sycophancy style rule without verdict machinery.

## Recommended positioning

One-line positioning:

> RedJudge is an evidence-aware adversarial judge: it sets the evidence boundary, scans fatal risks first, and returns a continue / revise / abandon verdict.

Public hook candidates:

- `Risk verdicts, not vibes.`
- `先划证据边界，再给风险裁决。`
- `不要安慰性建议，要可执行裁决。`

## Priority backlog

### P0 — required for public release

- Add `README.md` with hook, use cases, output example, quick start, trigger phrases, safety boundary, verification section.
- Add `LICENSE`.
- Add `test-prompts.json` or `evals/evals.json` with representative prompts and expected properties.
- Add a visible result card or example report suitable for screenshots.
- Add one-line install command and “first prompt after install”.

### P1 — improves usefulness and trigger reliability

- Strengthen frontmatter description with explicit should-trigger and should-not-trigger cases.
- Add a compact mode table for default / strict / quick / object-specific modes.
- Add a verification ladder for current external facts: verify if high-stakes or time-sensitive; otherwise label as unverified.
- Add near-miss examples where RedJudge should not run.

### P2 — packaging polish

- Add `.claude-plugin/marketplace.json` if targeting plugin marketplaces.
- Add skills.sh badge when published.
- Add demo GIF or static showcase if publishing to a marketplace.

## Three improvement paths

- A — Fine-tune private skill: adjust SKILL.md, add tests. Low risk, private-use focused.
- B — Public-skill polish: README, LICENSE, evals, result card, frontmatter refinement. Recommended.
- C — Skill suite: split into RedJudge product/article/code/skill variants. Too early unless maintenance capacity is available.

## B implementation update — 2026-06-13

The recommended B path was executed for the installed Hermes skill directory.

Added or updated:

- `README.md` with public positioning, quick start, trigger phrases, safety boundary, file structure, verification steps, and publish checklist.
- `LICENSE` using MIT terms.
- `evals/evals.json` with 5 regression prompts covering product strict, article claims, vague input boundary, quick mode, and positive-only near miss.
- `examples/redjudge-result-card.md` as a screenshot-friendly textual showcase.
- `assets/redjudge-result-card.svg` as a static visual result card.
- `scripts/check-redjudge-evals.py` and `scripts/check-redjudge-evals.sh` for package/eval validation.
- `SKILL.md` with stronger trigger description, mode table, external fact verification ladder, quick-mode output format, and final self-check.

Validation after B implementation:

- `python scripts/check-redjudge-evals.py` passed.
- `luban/tools/check-skill-repo.sh <redjudge>` returned `PASS: 10`, `WARN: 3`, `FAIL: 0`.

Remaining warnings are intentional because they require publication targets rather than local skill editing:

- `.claude-plugin/marketplace.json` is still absent.
- There is a static SVG showcase, but no GIF/video recording yet.
- skills.sh badge is absent until the skill has a real published `<owner>/<repo>` location.

## GitHub publication update — 2026-06-13

RedJudge was published as a public GitHub repository:

- Repository: https://github.com/gaoyechen/redjudge
- Owner: `gaoyechen`
- Visibility: public
- Default branch: `main`
- Initial publish commit: `8b206c9becbfb4e9b802964bc23ffa5b0860f31c`
- Topics: `agent-skills`, `ai-agents`, `critique`, `red-team`, `risk-assessment`
- CI: `.github/workflows/validate.yml` runs `python scripts/check-redjudge-evals.py` and JSON validation on push/PR.

Post-publish validation:

- Public clone from `https://github.com/gaoyechen/redjudge.git` succeeded.
- `python scripts/check-redjudge-evals.py` passed in the public clone.
- GitHub Actions run `27454082065` completed successfully.
- README contains the real install command: `npx skills add gaoyechen/redjudge`.

Remaining publishing work:

- Do not add a skills.sh badge yet: `https://skills.sh/b/gaoyechen/redjudge` returned a real SVG response but the badge text was `resource not found` at publish time, so adding it would mislead readers.
- Add `.claude-plugin/marketplace.json` only if targeting Claude plugin marketplace / ClawHub-style distribution.
- Add a GIF or VHS tape if doing a marketplace showcase beyond the static SVG result card.
