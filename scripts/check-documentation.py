#!/usr/bin/env python3
"""Verify the mathematical documentation without generating all of Mathlib's HTML API."""

from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
readme = (root / "README.md").read_text(encoding="utf-8")
challenge = (root / "Challenge.lean").read_text(encoding="utf-8")
statement = (root / "CoprimeAdjacencies/Statement.lean").read_text(encoding="utf-8")
proof = (root / "CoprimeAdjacencies/Proof.lean").read_text(encoding="utf-8")
metadata = (root / "formalization.yaml").read_text(encoding="utf-8")

required_paths = (
    "Challenge.lean", "Solution.lean", "CoprimeAdjacencies/Statement.lean",
    "CoprimeAdjacencies/Proof.lean", "comparator.json", "formalization.yaml",
    "docbuild/lakefile.toml",
)
for path in required_paths:
    if not (root / path).is_file():
        raise SystemExit(f"Missing documented source: {path}")

# Verify that Markdown links to repository-local files resolve.
for path in sorted(root.rglob("*.md")):
    if ".lake" in path.parts:
        continue
    content = path.read_text(encoding="utf-8")
    for target in re.findall(r"(?<!!)\[[^\]]*\]\(([^)]+)\)", content):
        target = target.split("#", 1)[0].split("?", 1)[0]
        if not target or re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I):
            continue
        if not (path.parent / target).exists():
            raise SystemExit(f"{path.relative_to(root)}: broken local link: {target}")

for term in ("\\pi(", "n\\ge4", "CoprimeAdjacencies.exact_minimum_coprime_adjacencies"):
    if term not in readme:
        raise SystemExit(f"README missing mathematical statement or theorem: {term}")
for name in ("IsPermutation", "adjacentCount", "pi", "target", "Attained", "h"):
    if not re.search(rf"/--[^\n]*-/(?:\s+)(?:noncomputable )?def {name}\b", challenge):
        raise SystemExit(f"Missing documented Challenge definition: {name}")
if "theorem exact_minimum_coprime_adjacencies" not in challenge:
    raise SystemExit("Missing advertised exact theorem in Challenge")
if "P010_exact" not in proof or "Nat.primeCounting" not in statement:
    raise SystemExit("Mathematical source definitions or proof reference changed")
if "f73a76cd5e33ee822ae572953195f9549efec4ed" not in metadata:
    raise SystemExit("Missing original versioned source citation")
if "PalomarTemplate" in readme or "TEMPLATE:" in metadata:
    raise SystemExit("Unreplaced documentation/template metadata")
print("Mathematical documentation, links and original-source attribution: valid")
