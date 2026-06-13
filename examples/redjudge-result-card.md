# RedJudge Result Card — Showcase Example

This is a screenshot-friendly result card for README/showcase use. It is based on the public eval prompt `product-strict-ai-job-coach` and is not a claim about real market data.

```text
┌─────────────────────────────────────────────┐
│ RedJudge Verdict                            │
│                                             │
│ Object: AI 求职陪练 App                     │
│ Mode: product strict                        │
│ Evidence Boundary: 输入材料 + 未核实市场假设 │
│                                             │
│ Top Risks                                   │
│ 1. 目标用户过宽，核心场景不成立 🔴          │
│ 2. 四个大功能并列，MVP 焦点被稀释 🟡       │
│ 3. 49 元/月 + 投流的商业账未成立 🟡        │
│                                             │
│ Verdict: revise                            │
│ Weighted total: 40                          │
│                                             │
│ Highest-leverage change:                    │
│ 收窄到“转行产品经理的模拟面试 + 简历追问”   │
│                                             │
│ Next Validation:                            │
│ 24 小时小红书测试，验证 2 人是否愿付定金    │
└─────────────────────────────────────────────┘
```

## Why this is a good RedJudge output

- It starts from the evidence boundary instead of assuming market facts.
- It names risks before value.
- It uses a verdict tied to a score.
- It gives one next validation, not a broad advice list.
