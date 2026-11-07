module

public import Mathlib

/-!
# Exact minimum number of coprime adjacencies

For a permutation `a` of `[1,n]`, let `adjacentCount a` be the
number of successive pairs having gcd one, and `h n` the least such
count over all permutations. The exact formula holds for every `n ≥ 4`.

Mathematical source: G. Sidoine, *The Minimum Number of Coprime
Adjacencies in a Permutation*, manuscript submitted to *Integers*.
https://github.com/gsidoine/the-scottish-book/blob/f73a76cd5e33ee822ae572953195f9549efec4ed/theorems/P010-exact-coprime-adjacencies.md
-/

@[expose] public section

namespace P010

/-- The list contains every integer in `[1, n]` exactly once. -/
def IsPermutation (n : ℕ) (a : List ℕ) : Prop :=
  a.Perm (List.range' 1 n)

/-- The number of adjacent coprime pairs in a list. -/
def adjacentCount (a : List ℕ) : ℕ :=
  (a.zip a.tail).countP (fun z => decide (Nat.Coprime z.1 z.2))

/-- The number of primes not exceeding `n`. -/
def pi (n : ℕ) : ℕ := Nat.primeCounting n

/-- The exact expression in the submitted manuscript, for `n ≥ 4`. -/
def target (n : ℕ) : ℕ :=
  (pi n - pi (n / 2)) +
    max 1 (((pi (n / 2) - pi (n / 3)) + 1) / 2)

/-- The nonempty set of possible adjacency counts. -/
def Attained (n k : ℕ) : Prop :=
  ∃ a : List ℕ, IsPermutation n a ∧ adjacentCount a = k

theorem attainable (n : ℕ) : ∃ k : ℕ, Attained n k := by
  refine ⟨adjacentCount (List.range' 1 n), List.range' 1 n, ?_, rfl⟩
  exact List.Perm.refl _

/-- The extremal quantity, defined as the least realized score. -/
noncomputable def h (n : ℕ) : ℕ := by
  classical
  exact Nat.find (attainable n)

end P010

namespace CoprimeAdjacencies

/--
The least possible number of coprime adjacent pairs in a permutation
of `{1, …, n}`, for `n ≥ 4`, is
`π(n) − π(⌊n/2⌋) + max(1, ⌈(π(⌊n/2⌋) − π(⌊n/3⌋))/2⌉)`.

Here natural-number division is floor division, and
`(k + 1) / 2` is the ceiling of `k/2`.
-/
theorem exact_minimum_coprime_adjacencies (n : ℕ) (hn : 4 ≤ n) :
    P010.h n = P010.target n := by
  sorry

end CoprimeAdjacencies
