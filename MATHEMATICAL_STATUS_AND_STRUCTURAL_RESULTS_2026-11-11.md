# Verrell’s Law — Mathematical Status and Structural Results

**Research note:** 11 November 2026  
**Originator:** M.R. (Verrell’s Law)  
**Mathematical review:** Derived and independently checked with AI-assisted analysis; Claude’s private structural note v1.1 and Solace’s independent numerical rerun  
**Scope:** Consequences of the existing canonical exponential-tilt selection family. This note adds **no** canonical equation, scoring rule, aggregation choice, decay mechanism or physical hypothesis.

> **Contribution:** The retained-state tilt has a precise minimum-relative-entropy characterisation, monotone expected-score response, exact relative-entropy measure of departure, a sharp probability-shift bound and order-independent composition under fixed scores. These results turn an assumed selection family into explicit, testable constraints.

## 1. Canonical selection family — unchanged

For a fixed finite candidate set with baseline probabilities `P₀,i > 0`, finite, independently specified retained-state compatibility scores `Rᵢ`, and common influence coefficient `λ`:

```math
P_{\lambda,i}=\frac{P_{0,i}\exp(\lambda R_i)}{Z(\lambda)},\qquad Z(\lambda)=\sum_jP_{0,j}\exp(\lambda R_j).
```

For candidates `a,b` on the same positive support, the pairwise identity is **exact**:

```math
\log\frac{P_{\lambda,a}}{P_{\lambda,b}}-\log\frac{P_{0,a}}{P_{0,b}}=\lambda(R_a-R_b).
```

“First-order” describes only the small-shift **probability-scale** approximation in a binary comparison, `ΔP ≈ λ P₀(1−P₀) ΔR`; it does **not** qualify the exact log-odds identity.

## 2. Five structural results

### Result 1 — Minimum departure from a specified baseline

For a feasible constraint `E_P[R] = r`, the corresponding exponential tilt uniquely minimises `D_KL(P || P₀)` among distributions satisfying that expected-score constraint, provided the constrained solution is in the positive-support interior. The coefficient `λ` is the constraint's Lagrange multiplier. Boundary constraints may arise as limits.

This is the classical minimum-discrimination-information / relative-entropy projection principle. It explains **why the tilt is a principled selection rule under that particular constraint**, not why any observed system must obey it.

### Result 2 — Monotone expected retained-score influence

```math
\frac{d}{d\lambda}\mathbb E_{\lambda}[R]=\mathrm{Var}_{\lambda}(R)\ge 0.
```

For fixed scores and baseline support, increasing `λ` cannot decrease the expected retained-state score. The derivative is strictly positive when the score is nonconstant on the supported candidates. Individual candidate probabilities need not all increase.

### Result 3 — Exact measure of distributional departure

```math
D_{KL}(P_{\lambda}\|P_0)=\lambda\mathbb E_{\lambda}[R]-\log Z(\lambda).
```

Near `λ = 0`:

```math
D_{KL}(P_{\lambda}\|P_0)=\frac{\lambda^2}{2}\mathrm{Var}_0(R)+O(\lambda^3).
```

KL divergence measures the departure in **nats**, without arbitrary probability units. Cross-system comparisons still require compatible candidate spaces, scoring conventions and baselines; it is not a universal physical measure of memory.

### Result 4 — Sharp bound on any event-probability shift

Let `ρ = maxᵢ Rᵢ − minᵢ Rᵢ`. For any event `A` consisting of a subset of the candidate set:

```math
|P_{\lambda}(A)-P_0(A)|\le\tanh\!\left(\frac{|\lambda|\rho}{4}\right).
```

The bound is sharp. In the two-candidate upward-shift case with `d = |λ|ρ > 0`, equality is attained at:

```math
P_0(A)=\frac{1}{1+e^{d/2}},\qquad P_{\lambda}(A)=\frac{1}{1+e^{-d/2}}.
```

**It is not generally attained at a 50/50 baseline.** The first-order binary probability response is largest at 50/50, whereas the exact maximum for a finite shift is displaced from 50/50 and depends on shift direction. A prospective influence cap based on this bound must constrain the declared score range and `λ`; the inequality itself is not an implemented software governor.

### Result 6 — Composition of fixed exponential tilts

For fixed candidate support, baseline, scores and coefficients, successive tilts commute:

```math
\operatorname{Tilt}(\operatorname{Tilt}(P_0,\lambda_1R^{(1)}),\lambda_2R^{(2)})
=\operatorname{Tilt}(P_0,\lambda_1R^{(1)}+\lambda_2R^{(2)}).
```

Reversing the order of these **static score contributions** does not alter selection probabilities. This result does not assert that history updates, retrieval, cueing, learning or candidate-set changes commute.

## 3. Testable commitments

The following are constraints of the canonical family **when baseline, candidate support, scoring and regime assumptions are held fixed**:

1. **Index sufficiency (Round 1):** Given the same baseline and `λ`, histories producing the same frozen candidate-relative retained scores imply the same predicted choice distribution. Unmodelled history-dependent differences after this matching challenge the specification.
2. **Baseline additivity (Round 1):** The retained-score term adds to baseline candidate-relative log-odds; the same `λΔR` yields the same log-odds shift across matched baseline conditions.
3. **Pairwise odds independence (Round 1):** Adding or removing another candidate does not change the odds ratio for `a` versus `b` **if** both candidates retain the same baseline odds ratio, scores and common `λ`. This is the classical Luce-style IIA property, not a claim that real candidate additions leave all inputs unchanged.
4. **Stable coupling within the declared regime (Round 1):** A single pre-specified `λ` should account for the declared held-out comparisons; score rescaling or changing regimes after seeing outcomes does not count as confirmation.
5. **Baseline-pattern test (structural result):** At fixed binary `λΔR`, the exact log-odds shift stays constant, while the probability shift follows the logistic transform. A first-order approximation peaks at baseline 50/50, but the exact finite-shift maximum is offset.
6. **Matched-score order test (structural result):** Different histories with identical fixed candidate scores, baseline, support and `λ` must give the same distribution. An order effect after those controls contradicts this static selection model in the tested regime; an effect mediated by a changed retained-state update does not.

These tests require independent construction of `R`, prospective measurement or recording of pre-choice score components where relevant, appropriate controls, held-out outcomes and comparisons with established aggregation, sampling, gain, threshold and learning models.

## 4. Numerical verification and scope

The private structural note v1.1 was checked using a 20,000-instance seeded NumPy script (2–7 candidates, `λ ∈ [−3,3]`). The script was independently rerun on 11 November 2026: the pairwise identity, score-shift and rescaling invariance, pairwise odds invariance, monotonic derivative, KL formula, sharp event-probability bound and tilt composition reproduced; the bound had **zero violations** in the generated cases. A separate grid check reproduced the exact probability-shift maximiser. Numerical verification supports implementation checks; the claims above rest on standard analytical identities and assumptions.

**Evidence boundary:** These are mathematical properties of an exponential-family selection model, **not** evidence that an independent human, biological or physical system obeys Verrell’s Law. A new empirical contribution requires frozen outcome-independent scores and predictions that survive prospective tests against conventional models.

## 5. Attribution and related documents

These mathematical principles have substantial prior art. Relevant foundations include **E. T. Jaynes** (maximum entropy), **S. Kullback** (information discrimination / KL divergence), **I. Csiszár** (information projections), **R. D. Luce** (choice axioms and independence of irrelevant alternatives) and **D. McFadden** (conditional logit and discrete choice). Their work is not claimed as newly invented here.

The contribution of this note is the explicit application and packaging of these restrictions as **testable commitments of Verrell’s Law's retained-state selection specification**.

- [Canonical Mathematical Foundations and Falsification Protocol](VERRELLS_LAW_MATHEMATICAL_FOUNDATIONS_AND_FALSIFICATION_PROTOCOL_v1.0.md)
- [Mathematical Clarification Supplement](VERRELLS_LAW_MATHEMATICAL_CLARIFICATION_SUPPLEMENT_v1.0.md)
- [Mathematical Clarifications and Open Problems](MATHEMATICAL_CLARIFICATIONS_AND_OPEN_PROBLEMS_v1.0.md)
- [Empirical Identification Clarification](VERRELLS_LAW_EMPIRICAL_IDENTIFICATION_CLARIFICATION_v1.0.md)

**Publication record:** 11 November 2026. New explanatory note only. Historical files, canonical formulas, author attribution and separate engineering records are unmodified.
