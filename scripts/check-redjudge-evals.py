#!/usr/bin/env python
"""Validate the RedJudge skill package assets.

This is a static package/eval validator. It does not call an LLM and does not
claim the review protocol is semantically perfect; it catches missing public
skill assets and malformed regression prompts.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def fail(message: str) -> None:
    print(f"FAIL {message}")
    raise SystemExit(1)


def warn(message: str) -> None:
    print(f"WARN {message}")


def ok(message: str) -> None:
    print(f"PASS {message}")


def read(path: Path) -> str:
    if not path.exists():
        fail(f"missing {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def main() -> int:
    skill = read(ROOT / "SKILL.md")
    readme = read(ROOT / "README.md")
    read(ROOT / "LICENSE")
    read(ROOT / "assets" / "redjudge-result-card.svg")
    read(ROOT / "examples" / "redjudge-result-card.md")

    if "name: redjudge" not in skill:
        fail("SKILL.md frontmatter does not declare name: redjudge")
    if "Evidence Boundary" not in skill or "Red Scan" not in skill or "continue / revise / abandon" not in skill:
        fail("SKILL.md is missing core RedJudge protocol terms")
    if "Do **not** use" not in skill and "Do not use" not in skill:
        fail("SKILL.md is missing negative trigger guidance")
    ok("SKILL.md contains core protocol and negative triggers")

    required_readme_terms = [
        "Risk verdicts, not vibes",
        "快速开始",
        "触发方式",
        "安全边界",
        "验证与测试",
        "npx skills add",
    ]
    missing = [term for term in required_readme_terms if term not in readme]
    if missing:
        fail("README.md missing terms: " + ", ".join(missing))
    ok("README.md contains hook, install, trigger, safety, and validation sections")

    eval_path = ROOT / "evals" / "evals.json"
    if not eval_path.exists():
        fail("missing evals/evals.json")
    data = json.loads(eval_path.read_text(encoding="utf-8"))
    if data.get("skill_name") != "redjudge":
        fail("evals/evals.json skill_name must be redjudge")
    evals = data.get("evals")
    if not isinstance(evals, list) or len(evals) < 5:
        fail("evals/evals.json must contain at least 5 evals")

    ids = set()
    for item in evals:
        eid = item.get("id")
        if eid in ids:
            fail(f"duplicate eval id: {eid}")
        ids.add(eid)
        for field in ["prompt", "expected_output", "expectations"]:
            if field not in item:
                fail(f"eval {eid} missing {field}")
        expectations = item["expectations"]
        if not isinstance(expectations, list) or not expectations:
            fail(f"eval {eid} expectations must be a non-empty list")

    prompts = "\n".join(item["prompt"] for item in evals)
    for required in ["strict", "quick", "AI 教育", "正面反馈", "article"]:
        if required not in prompts:
            fail(f"eval prompts missing coverage for {required!r}")
    ok("evals/evals.json has required shape and coverage")

    print("\nAll RedJudge package checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
