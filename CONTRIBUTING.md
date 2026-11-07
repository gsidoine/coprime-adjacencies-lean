# Contributing

The mathematical statement is fixed by the cited exact theorem. A change
to the statement, its definitions, or the proof requires a clear explanation
of semantic equivalence, a green Lean build, and successful Palomar Comparator
verification. Do not replace the exact theorem with a weaker statement.

For ordinary contributions, use a pull request and include the theorem or
definition being changed, the reason for the change, and the relevant build
and comparison results. Preserve the source attribution and independently
review the correspondence between the Challenge and the mathematical text.

The project uses Lean 4.35.0 and Mathlib 4.35.0. It follows Palomar's source
and module-system requirements. Its AI assistance and proof-verification
limitations are documented in `formalization.yaml`.
