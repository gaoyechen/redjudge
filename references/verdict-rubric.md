# RedJudge Verdict Rubric

Use this reference before final scoring or verdict selection.

## Verdict Definitions

### continue

Meaning: the core logic is currently viable and the known risks are manageable.

Required conditions:

- Weighted total >= 65
- No unresolved 🔴 Fatal risk
- No dimension with weight >=25% scores below 4
- Evidence quality is adequate for the review scope

Output requirements:

- Name the biggest remaining risk
- Give one immediate next action

### revise

Meaning: the object has potential, but a structural issue must be fixed before continued investment.

Triggered by any of:

- Weighted total 40-64
- Any dimension with weight >=25% scores below 4
- A 🔴 Fatal risk exists but has a credible fix path
- Evidence quality is too weak for a confident continue verdict

Output requirements:

- Give exactly one highest-leverage change
- Explain the expected scoring improvement direction
- Give a validation method for that change

### abandon

Meaning: the object has a root problem whose repair cost likely exceeds restarting.

Triggered by any of:

- Weighted total < 40
- Two or more dimensions with weight >20% score below 3
- An unresolved 🔴 Fatal risk has no credible fix path
- The necessary evidence contradicts the core premise

Output requirements:

- State the core reason in 1-2 sentences
- Give one restart direction
- Do not give a revision checklist

## Dimension Scoring

| Score | Meaning | Judgment Basis |
|---|---|---|
| 9-10 | Excellent | Strong evidence, few material risks |
| 7-8 | Good | Minor issues, core logic holds |
| 5-6 | Mixed | Noticeable risks need attention |
| 3-4 | Weak | Structural issues affect viability |
| 1-2 | Failing | Dimension is mostly unsupported or contradicted |

Use integer scores only. Half points create false precision.

## Weighted Total

Use weight fractions, then scale to 100:

```
weighted_total = round(sum(score * weight_fraction) * 10)
```

Example:

```
4*0.25 + 6*0.20 + 5*0.20 + 7*0.20 + 3*0.15 = 4.65
weighted_total = round(4.65 * 10) = 47
```

## Evidence Quality Override

If the score depends on unverified external facts, do not present the verdict as settled. Use one of:

- `revise` if validation can resolve the uncertainty
- `abandon` only if verified evidence already contradicts the core premise
- `continue with validation gate` only when total >=65 and the remaining uncertainty is not core to the premise

## Role Conflict Handling

If role perspectives conflict:

1. Mark the conflict explicitly.
2. Weight the role closest to the object goal more heavily:
   - Idea: executor and target user usually outrank investor unless fundraising is the goal.
   - Article: skeptical reader and domain expert outrank editor.
   - Product: target user outranks investor and competitor unless monetization is the review focus.
3. Let score, evidence quality, and unresolved Fatal risks decide the verdict.
