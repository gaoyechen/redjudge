# RedJudge Dimension Templates

Use these templates after classifying the review object. Adjust dimensions only when the user's object clearly needs a custom frame.

## Idea

| Dimension | Check | Weight | Typical Risk Signal |
|---|---|---:|---|
| Feasibility | Are there technical, resource, legal, or time constraints that block execution? | 30% | Depends on unavailable infrastructure or unrealistic solo execution |
| Demand Reality | Is this a real need with evidence, or only a plausible story? | 25% | No interviews, usage evidence, willingness to pay, or urgent pain |
| Defensibility | How easily can others copy it? | 20% | Core logic is easy to reproduce and has no data/network/process moat |
| Cost-Benefit | Does the likely return justify the required effort? | 15% | High ongoing cost with unclear upside |
| Timing | Why now rather than earlier or later? | 10% | Market window is stale, premature, or unsupported |

Suggested roles:

- Target user: cares about urgency, alternatives, friction.
- Executor: cares about constraints, sequencing, hidden work.
- Competitor: cares about copyability and weak positioning.
- Investor/sponsor: cares about upside, focus, opportunity cost.

## Article

| Dimension | Check | Weight | Typical Risk Signal |
|---|---|---:|---|
| Argument Strength | Does the thesis rely on unproven jumps? | 30% | Correlation is treated as causation; premise does not support conclusion |
| Factual Accuracy | Are facts, data, and quotes verified? | 25% | Source is missing, outdated, or used with the wrong interpretation |
| Logical Integrity | Are concepts stable and causality clear? | 20% | Concept switching, survivorship bias, false dichotomy |
| Narrative Quality | Can readers follow and finish it? | 15% | Weak opening, scattered structure, no payoff |
| Bias Control | Does the author ignore counterevidence? | 10% | Only supportive evidence appears |

Suggested roles:

- Skeptical reader: cares about why they should believe the thesis.
- Domain expert: cares about factual and conceptual correctness.
- Editor: cares about structure, clarity, and publishability.
- Casual reader: cares about attention and relevance.

## Product

| Dimension | Check | Weight | Typical Risk Signal |
|---|---|---:|---|
| Core Value | Why would users choose this over existing options? | 25% | Existing tools solve most of the problem already |
| User Experience | Can a new user understand value quickly? | 20% | Needs explanation before value appears |
| Business Logic | Can revenue cover acquisition and operating costs? | 20% | No pricing logic, weak margins, CAC/LTV uncertainty |
| Technical Feasibility | Can the product be built and operated reliably? | 20% | Depends on fragile integrations, latency, data quality, or unavailable APIs |
| Growth Path | Is the 0-to-1 acquisition path credible? | 15% | No seed channel or distribution wedge |

Suggested roles:

- New user: cares about immediate value and friction.
- Paying customer/buyer: cares about ROI and budget.
- Technical owner: cares about reliability, scope, dependencies.
- Competitor PM: cares about differentiation and copyability.

## Custom Object

Build 4-6 dimensions from this question:

> What could make this fail even if the user executes competently?

Rules:

- Put the most premise-breaking dimension first.
- Use weights that sum to 100%.
- Avoid dimensions that merely rephrase each other.
- Include at least one evidence/validation dimension when the input is speculative.
