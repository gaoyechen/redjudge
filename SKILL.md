---
name: redjudge
description: |
  Use RedJudge whenever the user asks for a rigorous critique, red-team review, adversarial review, risk assessment, decision evaluation, or structured judgment of an idea, article, product, proposal, plan, strategy, draft, PRD, or pitch. Trigger even if the user only says 评价、评审、挑毛病、靠不靠谱、风险、判断一下、RedJudge, /RedJudge, devil's advocate, red team this, or poke holes in this. RedJudge delivers an evidence-aware verdict — continue / revise / abandon — by setting an Evidence Boundary, scanning risks before praise, labeling facts vs assumptions, using matched reviewer roles, scoring with a rubric, and giving exactly one next validation. Do not use for encouragement-only feedback, open-ended brainstorming, factual lookup, direct execution, ordinary copyediting, or positive-only polishing unless the user explicitly wants critique.
---

# RedJudge — Evidence-Aware Adversarial Review

RedJudge turns “帮我看看靠谱吗” into a structured risk verdict. It is a review gate, not a comfort layer: risks first, evidence labels always, value confirmation only after the strongest objections have been named.

RedJudge is **not** an objective-truth machine. It is a disciplined red-team protocol that makes criticism harder to avoid while keeping it evidence-aware. If the evidence is weak, say so; do not invent problems to sound sharp.

## Operating stance

- **Risk before reassurance.** Start with Red Scan, not praise.
- **Evidence before drama.** Every material risk must carry an evidence level and a concrete basis.
- **Unknown stays unknown.** Do not fill missing market, legal, pricing, technical, or competitor facts with confident prose.
- **Verdict must bind to score.** Never give `continue` below the rubric threshold or with an unresolved Fatal risk.
- **One next move.** The final validation should be the highest-leverage next action, not a generic checklist.

## When to use / when not to use

Use when the user submits an idea, article, product, proposal, plan, strategy, PRD, pitch, draft, or decision and asks for evaluation, critique, red-teaming, risk assessment, “挑毛病”, “靠不靠谱”, or a hard judgment.

Do **not** use when the user asks for:

- brainstorming without critique;
- encouragement-only or positive-only feedback;
- factual lookup or summarization;
- direct execution such as writing code, editing files, sending messages, or publishing;
- ordinary polishing/copyediting where no judgment is requested.

If the user asks for positive-only feedback, do not silently run RedJudge. Say that RedJudge is a critique protocol and ask whether they want a risk review.

## Resource loading

Load bundled references only when needed:

- Read `references/dimension-templates.md` after identifying the object type.
- Read `references/verdict-rubric.md` before scoring or giving a final verdict.
- Read `references/anti-sycophancy-rules.md` when using `/RedJudge strict`, when the output starts becoming overly positive, or when the user asks for maximum adversarial review.
- Read `references/luban-audit-2026-06-13.md` when improving, packaging, publishing, or auditing RedJudge itself.
- Use files in `examples/` only as style calibration. Examples are not facts.
- Use `evals/evals.json` and `scripts/check-redjudge-evals.py` when validating the skill package.

## Modes

Mode modifiers compose. Example: `/RedJudge product strict` means product dimensions plus strict risk count and positive-section cap.

| Mode | Use when | Output difference |
|---|---|---|
| `/RedJudge` | User asks for critique without object type | Infer type, full review |
| `/RedJudge idea` | Early concept, strategy, plan, personal decision | Use idea dimensions unless a custom frame fits better |
| `/RedJudge article` | Essay, post, article thesis, argument draft | Use article dimensions and source/argument checks |
| `/RedJudge product` | Product, MVP, pricing, growth, UX, launch | Use product dimensions and buyer/user/technical/growth roles |
| `/RedJudge strict` | User wants maximum adversarial review | Target 5 evidence-backed risks; Value Confirmation <= 25% |
| `/RedJudge quick` | User wants fast triage | Output only Review Object, Red Scan, Verdict, Next Validation |

## Workflow

```text
Stage 0: Scope and Evidence Check
  -> Decide whether RedJudge should run
  -> Classify object: idea / article / product / other
  -> Ask for context if the input is too vague
  -> State Evidence Boundary and verification status

Stage 1: Red Scan
  -> Find 3 evidence-backed risks by default; 5 in strict mode
  -> Do not force extra risks if evidence is insufficient
  -> No praise, reassurance, or softening language here

Stage 2: Multi-Perspective Review
  -> Use 3-4 roles matched to the object type
  -> Roles are simulated lenses, not factual sources
  -> Each role must identify a distinct concern

Stage 3: Value Confirmation
  -> Confirm only value points that survived Stage 1
  -> Positive section <= 40% by default; <= 25% in strict mode

Stage 4: Verdict
  -> Score dimensions 1-10
  -> Compute weighted total
  -> Choose continue / revise / abandon according to rubric
  -> Give exactly one highest-leverage next validation
```

## Stage 0: Scope and Evidence Check

Before criticizing, classify the object:

- **Product**: features, users, MVP, pricing, launch, UX, growth.
- **Article**: thesis, evidence, argument, paragraphs, readers, narrative.
- **Idea**: early concept, plan, business direction, personal strategy.
- **Other**: build 4-6 custom dimensions from “what could make this fail even if the user executes competently?”

If the input is under 50 Chinese characters or too vague to identify an object, do not produce a full review. Ask for 3-4 missing facts: object, target audience/user, goal, constraints/materials, and preferred evaluation angle.

### Evidence levels

| Evidence Level | Meaning | How to use |
|---|---|---|
| Input Evidence | Directly quoted or paraphrased from the user’s material | Strongest basis from the current prompt |
| Verified External Fact | Checked against a current/reliable source | Use for market, legal, pricing, technical, competitor, API, or date-sensitive claims |
| Reasoned Inference | Logical conclusion from the input | Mark as inference, not fact |
| Unverified Assumption | Plausible but not checked | Use only as a risk hypothesis, not as settled fact |

### External fact verification ladder

When the verdict depends on current facts — competitors, laws, prices, product capabilities, APIs, dates, market size, technical constraints, safety, security, medical/legal/financial claims — do one of the following:

1. **Verify** with a reliable source when tools and time are available.
2. **Label as Unverified Assumption** when verification is unavailable or out of scope.
3. **Lower evidence confidence** if the claim is central and unverified.
4. **Refuse a settled verdict** if the unverified claim is fatal and cannot be checked from the input.

Never treat a simulated role opinion as a verified fact.

## Stage 1: Red Scan

Find key risks that could materially weaken or invalidate the object.

Rules:

1. Target at least 3 evidence-backed risks by default; `/RedJudge strict` targets 5.
2. Do not fabricate or stretch. If fewer risks are supportable, write: `Red Scan only found N evidence-backed risks; additional criticism would be speculative.`
3. Each risk must include evidence level, specific evidence, and why it matters.
4. Avoid praise, reassurance, and softening language in this stage.
5. Use severity labels narrowly:
   - 🔴 Fatal: if true and unresolved, the core object fails.
   - 🟡 Severe: requires major revision.
   - 🟠 Moderate: requires local adjustment.

Bad: “这个想法可能有一些问题。”

Good: “证据等级：Input Evidence。用户只写了`目标用户是知识工作者`，没有说明具体使用场景、现有替代方案或付费触发点；需求真实性无法成立。”

## Stage 2: Multi-Perspective Review

Use role views to reveal distinct failure modes. Pick roles from `references/dimension-templates.md` or create roles suited to the object.

Rules:

1. Each role writes in first person.
2. Each role must name one distinct concern.
3. Do not let one role cite another role.
4. Do not treat role opinions as verified facts unless separately sourced.

## Stage 3: Value Confirmation

Confirm value only after Red Scan and role review.

Rules:

1. Positive section <= 40% of total output; `/RedJudge strict` <= 25%.
2. Confirm only value points not invalidated in Stage 1.
3. Positive claims also need evidence levels.
4. Do not cushion the verdict with “虽然有问题但总体不错” style language.

## Stage 4: Verdict

Read `references/verdict-rubric.md` before final scoring. Score dimensions 1-10, then compute:

```text
weighted_total = round(sum(dimension_score * dimension_weight_fraction) * 10)
```

Example: `4*0.25 + 6*0.20 + 5*0.20 + 7*0.20 + 3*0.15 = 4.65`, so weighted total is `47`.

| Verdict | Required conditions |
|---|---|
| continue | weighted total >= 65, no unresolved 🔴 Fatal risk, no dimension with weight >=25% scores < 4, and evidence quality is adequate |
| revise | weighted total 40-64, or one major dimension with weight >=25% scores < 4, or a fixable 🔴 Fatal risk exists, or evidence quality is too weak for continue |
| abandon | weighted total < 40, or two dimensions with weight >20% score < 3, or an unresolved 🔴 Fatal risk has no credible fix path |

Never give `continue` when the weighted total is below 65 or when an unresolved Fatal risk remains. If the verdict is `revise`, give exactly one highest-leverage change. If the verdict is `abandon`, give one restart direction instead of a revision checklist.

## Output format — full review

```markdown
# RedJudge Review

## Review Object
**Type**: [idea / article / product / other]
**Summary**: [one sentence]
**Evidence Boundary**: [what was evaluated from input; what external facts are verified, unverified, or out of scope]

## 🔴 Red Scan

1. **[Risk Title]** [🔴/🟡/🟠]
   - Evidence level: [Input Evidence / Verified External Fact / Reasoned Inference / Unverified Assumption]
   - Evidence: "[specific quote, fact, or inference basis]"
   - Why it matters: [2-3 direct sentences]

2. **[Risk Title]** [🔴/🟡/🟠]
   - Evidence level: [...]
   - Evidence: [...]
   - Why it matters: [...]

3. **[Risk Title]** [🔴/🟡/🟠]
   - Evidence level: [...]
   - Evidence: [...]
   - Why it matters: [...]

## 👥 Multi-Perspective Review

**[Role 1]**: I am [identity]. [50-100 Chinese characters or 1-3 direct English sentences]

**[Role 2]**: I am [identity]. [...]

**[Role 3]**: I am [identity]. [...]

**[Role 4]**: I am [identity]. [...]

## 🟢 Value Confirmation

[Only value points that survived Red Scan, with evidence levels.]

## ⚖️ Verdict

**Verdict**: [continue / revise / abandon]

Core reason: [1-2 sentences]

| Dimension | Score | Reason |
|---|---:|---|
| [dimension 1] | [1-10] | [one sentence] |
| [dimension 2] | [1-10] | [one sentence] |

**Weighted total**: [1-100]

[If continue] Biggest remaining risk: [one risk]
[If revise] Highest-leverage change: [one concrete change]
[If abandon] Restart direction: [one concrete direction]

## 📋 Next Validation

[One validation action the user can perform immediately. Prefer a 5-30 minute action unless the domain demands deeper validation.]
```

## Output format — quick mode

For `/RedJudge quick`, output only:

```markdown
# RedJudge Quick Review

## Review Object
**Type**: [...]
**Evidence Boundary**: [...]

## 🔴 Risk Scan
1. ...
2. ...
3. ...

## ⚖️ Verdict
**Verdict**: [continue / revise / abandon]
**Weighted total**: [1-100 or "not scored due to insufficient evidence"]
Core reason: [...]

## 📋 Next Validation
[one action]
```

## Final self-check before responding

Before finalizing, verify:

- Evidence Boundary is present.
- Every Red Scan item has evidence level, evidence, and why it matters.
- Red Scan does not contain praise or reassurance.
- Roles are labeled as perspectives, not factual sources.
- Value Confirmation appears after Red Scan and does not exceed the mode cap.
- Verdict obeys the score/risk rules.
- `revise` has exactly one highest-leverage change; `abandon` has one restart direction.
- If evidence is insufficient, the output says so instead of manufacturing certainty.

## Package validation

When maintaining or publishing this skill, run:

```bash
python scripts/check-redjudge-evals.py
```

The package should include `README.md`, `LICENSE`, `evals/evals.json`, examples, references, and a visible showcase artifact before public release.
