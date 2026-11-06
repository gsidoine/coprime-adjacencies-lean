module

public import CoprimeAdjacencies

/-!
# Exact minimum number of coprime adjacencies — proof

The substantive proof is in `CoprimeAdjacencies.Proof`; the theorem
below is the Solution counterpart of `Challenge`.
-/

@[expose] public section

namespace CoprimeAdjacencies

/-- The exact finite-`n` formula, proved by the constructive path-cover argument. -/
theorem exact_minimum_coprime_adjacencies (n : ℕ) (hn : 4 ≤ n) :
    P010.h n = P010.target n := by
  exact P010.P010_exact n hn

#print axioms exact_minimum_coprime_adjacencies

end CoprimeAdjacencies
