# The Minimum Number of Coprime Adjacencies in a Permutation

[![CI](https://github.com/gsidoine/coprime-adjacencies-lean/actions/workflows/ci.yml/badge.svg)](https://github.com/gsidoine/coprime-adjacencies-lean/actions/workflows/ci.yml)

A Lean 4 formalization of an exact extremal formula for permutations of consecutive positive integers.

For a permutation \(a=(a_1,\ldots,a_n)\) of \(\{1,\ldots,n\}\), put

\[
c(a)=\#\{1\le i<n:\gcd(a_i,a_{i+1})=1\},\qquad
h(n)=\min_{a\in S_n} c(a).
\]

Write \(\pi(x)\) for the number of primes at most \(x\). The proved theorem is

\[
\boxed{h(n)=\pi(n)-\pi(n/2)+
\max\left\{1,\left\lceil\frac{\pi(n/2)-\pi(n/3)}{2}\right\rceil\right\}}
\qquad (n\ge4).
\]

The exact identity is proved without a prime-counting assumption. The consequence
\(h(n)\sim 7n/(12\log n)\), obtained using the prime number theorem, is **not**
separately formalized.

## Formalization

- [`Challenge.lean`](Challenge.lean): complete mathematical definitions and the exact theorem statement, independent of the proof development.
- [`Solution.lean`](Solution.lean): proved counterpart of the advertised theorem.
- [`CoprimeAdjacencies/Statement.lean`](CoprimeAdjacencies/Statement.lean): shared definitions on the Solution side, retained from the original formalization.
- [`CoprimeAdjacencies/Proof.lean`](CoprimeAdjacencies/Proof.lean): constructive kernel-checked proof.
- [`comparator.json`](comparator.json): Challenge/Solution comparison and permitted axioms.
- [`formalization.yaml`](formalization.yaml): mathematical provenance, automation, and scope.

The final theorem is `CoprimeAdjacencies.exact_minimum_coprime_adjacencies`.
Its proof depends only on Lean's standard foundational axioms
`propext`, `Classical.choice`, and `Quot.sound`.

The source mathematical proof and the original Lean certificate are recorded at a
[pinned Scottish Book revision](https://github.com/gsidoine/the-scottish-book/tree/f73a76cd5e33ee822ae572953195f9549efec4ed/formal/P010).
The submitted *Integers* manuscript is an unchanged archival submission; neither
journal acceptance nor historical priority is claimed.

## Verification

The toolchain and Mathlib dependencies are pinned at **Lean 4.35.0** and **Mathlib 4.35.0**.
To reproduce on a suitable Linux host with Lean, Lake, Ruby, and `bubblewrap`:

```sh
lake exe cache get
lake build
ruby scripts/validate-formalization.rb
./scripts/verify-comparator.sh
```

CI additionally builds the project documentation and checks the root licence
and submission metadata.

The deliberate `sorry` in `Challenge.lean` is a placeholder marking the
proposition under verification, **not** a dependency of the Solution theorem.
No `sorry` occurs in the substantive proof.

## Mathematical and authorship status

This is a source-based formalization of the exact theorem, not an assertion
of independent historical originality. It originated as P010 in
[The Scottish Book](https://github.com/gsidoine/the-scottish-book).
The proof development involved substantial AI-assisted Lean drafting and
incremental debugging. The checked result is a Lean kernel proof; it has not
been independently refereed.

Palomar registration, if pursued, requires successful Comparator verification,
editorial review, and an affirmative registration decision. This repository
does not claim registration until that process is complete.

Submission information: https://submit.palomar-registry.org/
