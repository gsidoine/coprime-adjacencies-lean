#!/usr/bin/env python3
"""Check exact correspondence of the Challenge definitions and P010 proof statement.

Palomar Comparator checks the theorem statement independently; this additional
regression check ensures its mathematical definitions remain textually identical
to the source proof's statement module.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read(path):
    return (ROOT / path).read_text(encoding="utf-8")

def fail(message):
    raise SystemExit("P010 statement-fidelity check: " + message)

challenge = read("Challenge.lean")
statement = read("CoprimeAdjacencies/Statement.lean")
proof = read("CoprimeAdjacencies/Proof.lean")
solution = read("Solution.lean")

if not challenge.startswith("module\n\npublic import Mathlib\n"):
    fail("Challenge must import Mathlib alone")
if challenge.count("sorry") != 1:
    fail("Challenge must have exactly one deliberate theorem placeholder")
if re.search(r"\bsorry\b|\baxiom\b|\bopaque\b|\bconstant\b", proof):
    fail("the substantive proof must have no placeholders or new axioms")

try:
    start = challenge.index("namespace P010\n")
    challenge_defs = challenge[start:challenge.index("\nend P010", start)].strip()
    start = statement.index("namespace P010\n")
    statement_defs = statement[start:statement.index("/-- The exact P010 assertion", start)].strip()
except ValueError as error:
    fail(f"unable to locate complete mathematical definitions: {error}")

if challenge_defs != statement_defs:
    fail("Challenge and proof-side mathematical definitions have diverged")
if "theorem exact_minimum_coprime_adjacencies (n : ℕ) (hn : 4 ≤ n)" not in challenge:
    fail("Challenge theorem header or domain restriction changed")
if "exact P010.P010_exact n hn" not in solution:
    fail("Solution must invoke the unconditional exact theorem")

root_toolchain = read("lean-toolchain").strip()
if read("docbuild/lean-toolchain").strip() != root_toolchain:
    fail("root and documentation Lean toolchains differ")
if root_toolchain != "leanprover/lean4:v4.35.0":
    fail("the pinned Lean toolchain was unexpectedly changed")

for path, expected_name in [("lake-manifest.json", "CoprimeAdjacencies"),
                            ("docbuild/lake-manifest.json", "docbuild")]:
    manifest = json.loads(read(path))
    if manifest["name"] != expected_name:
        fail(f"{path}: unexpected Lake package name")
    for package in manifest["packages"]:
        if package["type"] == "git" and not re.fullmatch(r"[0-9a-f]{40}", package["rev"]):
            fail(f"{path}: unpinned Git dependency")

print("P010 Challenge definitions, theorem bridge and dependency pins: verified")
