# Verrell’s Law — AI Testing and Bias Normalization Clarification
## Public Testing Supplement v1.0

**Author:** Marcos Verrell Moss Ross (M.R.)  
**Maintainer:** Inappropriate Media Limited (t/a Collapse Aware AI)  
**Status:** Public clarification supplement; subordinate to the canonical mathematical specification and empirical-identification clarification  
**Date:** 27 August 2026

---

## 1. Purpose

This note answers two recurring questions about experimental tests of Verrell’s Law in AI systems:

1. What is the minimum defensible procedure for testing whether retained informational history alters later selection under otherwise matched present conditions?
2. How should a retained-state bias/compatibility term be scaled so that an apparent effect is not merely a numerical artifact of arbitrary magnitude or unstable normalization?

This document does **not** replace or amend the canonical mathematical specification:

- `VERRELLS_LAW_MATHEMATICAL_FOUNDATIONS_AND_FALSIFICATION_PROTOCOL_v1.0.md`
- `VERRELLS_LAW_EMPIRICAL_IDENTIFICATION_CLARIFICATION_v1.0.md`

Where notation or interpretation differs, those canonical documents govern.

The canonical framework uses the retained-state compatibility score `R_i`. Earlier or informal discussions may use `B(y_i;M_t)` for a memory-weighted bias term. For the purposes of this note, `B_i` can be treated as a raw implementation-level precursor to a preregistered, scale-controlled `R_i`; it is **not** a new canonical variable.

---

## 2. Minimum AI Test Procedure

A basic AI experiment should not merely demonstrate that a system with memory behaves differently from one without memory. That is too weak.

A defensible test should:

1. **Declare the present-state boundary.** Freeze current input, system state, candidate set, model/version, sampling settings and other controlled variables.
2. **Define retained informational history explicitly.** State which prior items/features belong to retained state and how they are represented.
3. **Preregister the compatibility/scoring rule.** The rule producing `R_i` or `ΔR` must be fixed before confirmatory outcomes are inspected.
4. **Control the scale of the retained-state term.** The scoring convention must be bounded, standardized or otherwise normalized under a declared rule so that arbitrary numerical magnitude cannot manufacture an apparent effect.
5. **Construct an otherwise-matched baseline.** Compare retained-state-enabled trials with a baseline in which the tested retained-state influence is absent, neutralized or ablated while present conditions remain matched.
6. **Measure candidate-relative selection change.** Where possible, quantify the change in selection log-odds rather than relying only on whether the winning label changed.
7. **Test the preregistered relation.** Evaluate whether changes in candidate-relative selection follow the declared retained-state compatibility differences with stable direction and useful out-of-sample prediction.
8. **Perform intervention or ablation.** Deliberately alter, remove, reverse or suppress retained-state information and test whether selection changes in the predicted direction.
9. **Report the correct evidence class.** Distinguish independent empirical testing from engineering conformance testing and proxy-based inference.

The canonical first-order relation remains:

```math
\Delta L = \lambda\Delta R + \varepsilon,
\qquad \lambda>0.
```

A fitted effect is meaningful only relative to the preregistered scale and sign convention of `R`.

---

## 3. Why Generic Memory Retention Is Not Enough

A memory module can store information without demonstrating the Verrell’s Law prediction.

The relevant question is not simply:

> Does the system remember something?

It is:

> Under otherwise equivalent present conditions, does a preregistered retained-state compatibility difference predict a measurable, directional change in later selection?

Therefore, successful retrieval, larger context windows, transcript persistence or generic recurrence are not by themselves evidence for the canonical retained-state selection relation.

---

## 4. The Rejected Sum-Normalization Proposal

One proposed informal normalization was:

```math
\tilde B_i
=
\frac{B_i}{\sum_j B_j + \epsilon},
```

where `B_i = B(y_i;M_t)` and `epsilon` is a small stabilizing constant.

This is **not recommended as the default normalization for Verrell’s Law testing**.

### 4.1 Near-zero denominator instability

If positive and negative raw biases cancel, the denominator can approach zero even while individual candidate biases are substantial.

For example:

```text
B = [1, 1, -2]
epsilon = 0.01
sum(B) + epsilon = 0.01
```

which yields:

```text
B_tilde = [100, 100, -200]
```

The apparent retained-state effect has been amplified by the normalization rule rather than by stronger retained-state evidence.

### 4.2 Sign inversion when the total is negative

Negative candidate-relative influence is not itself a problem; signed suppression can be legitimate.

The problem is that dividing every `B_i` by a **negative total sum** reverses the sign of every contribution. A candidate intended to be promoted can become numerically suppressive, and vice versa, solely because of the other candidates in the set.

### 4.3 Candidate-set dependence

The scale of a particular `B_i` under sum normalization changes when unrelated candidates are added or removed because the denominator depends on the entire candidate set.

That can reduce comparability across experimental contexts unless candidate-set construction is itself rigidly fixed and the denominator remains well behaved.

### 4.4 Epsilon does not solve identification

`epsilon` can prevent literal division by zero, but it does not make the resulting scale scientifically meaningful. When the signed sum is near zero, the chosen epsilon can dominate the result.

The scale-control problem therefore cannot be solved merely by adding a small constant.

---

## 5. Why Negative Bias Values Are Not Themselves Invalid

A signed retained-state score can be useful because history may either increase or decrease compatibility with a candidate.

Under the standard logit form:

```math
z_i
=
U_i + \lambda R_i,
```

followed by:

```math
P_i
=
\frac{e^{z_i}}{\sum_k e^{z_k}},
```

a negative `R_i` simply lowers the candidate’s logit relative to otherwise matched alternatives. That is coherent suppression, not a probability violation.

The probability normalization is performed by the final softmax. `R_i` itself does not need to be a probability distribution and does not need to sum to one.

---

## 6. Current Canonical Scale-Control Position

The canonical specification already avoids the unstable signed-sum normalization above.

It defines a general retained-state score of the form:

```math
R_i(H_t,x_t,S_t)
=
\frac{1}{n}
\sum_{j=1}^{n}
 s_j d_j q_j r_{ij},
```

with preregistered salience, persistence, optional reliability and candidate-compatibility terms.

Unless another convention is preregistered and justified, the components are bounded:

```math
s_j,d_j,q_j,r_{ij}\in[-1,1].
```

Dividing by the number of retained items bounds growth with retained-set size. The canonical specification also permits standardizing `ΔR` to unit variance within a preregistered trial set.

The important rule is therefore:

> **The retained-state compatibility scale must be fixed before confirmatory testing, and the fitted `λ` is interpretable only relative to that declared scale.**

This directly addresses the numerical comparability issue without requiring `R_i` to be converted into a probability distribution.

---

## 7. Alternative Transformations: Permissible but Not Automatically Canonical

Other transformations can be valid in a particular experiment if they are preregistered, justified and tested for pathological behavior.

### 7.1 Max-absolute scaling

For a raw signed score `B_i`, one possible bounded transformation is:

```math
R_i
=
\frac{B_i}{\max_j |B_j| + \epsilon}.
```

This preserves sign and bounds candidate-relative magnitude approximately within `[-1,1]` when the denominator is non-zero.

However, it remains candidate-set dependent and should therefore be treated as an **example implementation**, not a universal requirement of Verrell’s Law.

### 7.2 Shift-and-scale normalization

A min-shift transformation can map a candidate set to a non-negative range, but it changes the zero point and removes the direct signed interpretation of suppression versus promotion. It also needs a declared rule for the degenerate case in which all raw scores are equal.

It may be useful for some implementations but is not the preferred canonical representation of signed retained-state compatibility.

### 7.3 Softmax transformation of the raw bias

Applying softmax directly to raw `B_i` produces a positive candidate distribution:

```math
q_i
=
\frac{e^{B_i}}{\sum_j e^{B_j}}.
```

This can be useful when the experimental object is explicitly a probability-like memory allocation.

It is **not required** for the canonical Verrell’s Law model, because the final candidate-selection equation already contains a softmax/logit normalization. Converting `B` to a probability distribution first can discard the natural signed-zero interpretation and can amount to a second, conceptually different normalization stage.

---

## 8. Reference Selection Form

A generic implementation-level form may be written:

```math
P(y_i\mid S_t,O_t,M_t)
=
\frac{
\exp\left(U(y_i;S_t,O_t)+\lambda R_i\right)
}{
\sum_j
\exp\left(U(y_j;S_t,O_t)+\lambda R_j\right)
}.
```

Equivalent canonical notation is given in the Mathematical Foundations and Falsification Protocol using the baseline distribution `p_0` and retained-state compatibility score `R_i`.

The important experimental controls are:

- `R_i` has a frozen sign convention;
- its scaling/normalization is preregistered;
- `lambda` is interpreted only relative to that scale;
- candidate construction is declared;
- the confirmatory outcome is not used to manufacture the predictor;
- baseline and retained-history conditions are otherwise matched.

---

## 9. Recency, Salience and Recurrence Are Implementation Features, Not Universal Requirements

Recency, salience, recurrence, reliability, persistence and similar factors can all be legitimate components of a retained-state compatibility function.

They should **not** be mistaken for a universal definition of Verrell’s Law.

An independent implementation may represent retained informational history differently and still test the same principal hypothesis, provided that:

1. the retained-state representation is declared;
2. the candidate-compatibility rule is preregistered;
3. the scale is controlled;
4. present conditions are properly matched;
5. the predicted directional relationship is genuinely falsifiable.

This prevents the hypothesis from being tied unnecessarily to one software architecture.

---

## 10. Relationship to Collapse Aware AI

Collapse Aware AI (CAAI) is the engineering track connected to the retained-state selection framework.

CAAI can demonstrate that governed retained-state influence is implemented, inspectable, replayable and behaviorally consequential in engineered software.

That evidence is valuable, but two boundaries must be preserved:

### 10.1 Engineering conformance is not independent universal validation

If a selector is deliberately built to apply a particular retained-state score and coupling, demonstrating that its outputs follow that equation is an engineering conformance test unless an independent analysis route is supplied.

### 10.2 Governance is not identical to the retained-state score

A CAAI governor may constrain eligibility, suppress actions, enforce policy, bound candidate sets or otherwise govern selection.

Those governance functions should not automatically be collapsed into `R_i` or `lambda`.

Keeping retained-state influence and governance conceptually separable makes both the engineering architecture and the scientific test cleaner.

No public mathematical example in this repository should be interpreted as disclosure of proprietary Crown scoring rules, thresholds, schemas or production internals.

---

## 11. Evidence Labels

Tests should use the evidence labels already defined by the canonical empirical-identification clarification:

- **Independent empirical test** — `ΔR` is constructed independently of the confirmatory selection outcome under a frozen rule.
- **Engineering conformance test** — the tested selector itself applies the same score/coupling relationship being checked.
- **Proxy-based empirical test** — an independently measured proxy stands in for canonical retained-state compatibility and its mapping is declared appropriately.

This distinction prevents a software mechanism that was designed to produce a retained-state effect from being presented as independent evidence that the same relationship holds generally.

---

## 12. Practical Falsification Sequence for AI Experiments

A useful progressive evidence sequence is:

### Stage 1 — Divergence

Do otherwise matched present conditions produce a measurable selection difference when retained history differs?

### Stage 2 — Structured directional relation

Does the sign and magnitude of the change track preregistered retained-state compatibility rather than merely varying unpredictably?

### Stage 3 — Stability and prediction

Does the fitted relation remain stable across repetitions and predict held-out trials?

### Stage 4 — Intervention / ablation

Does deliberate manipulation, removal, reversal or suppression of retained-state information cause the predicted change?

### Stage 5 — Replication and scope

Does the effect replicate across new retained-state snapshots, implementations or systems without silently changing the scoring rule after seeing outcomes?

These stages are a practical research sequence. Formal verdicts remain governed by the canonical falsification protocol.

---

## 13. Recommended Public Wording

A concise, testable description is:

> **Under otherwise equivalent present conditions, retained informational history is hypothesized to exert a measurable, directional and intervention-sensitive influence on future state selection.**

For the stronger canonical quantitative claim, use the wording and equations in the Mathematical Foundations and Falsification Protocol v1.0.

Avoid treating the weaker statement “memory affects behaviour” as sufficient evidence for Verrell’s Law.

---

## 14. Summary

The central correction is not that every memory bias must be converted into a probability distribution.

It is that the retained-state compatibility term used in a quantitative test must have a **declared, stable and preregistered scale**.

The informal normalization

```math
\tilde B_i
=
\frac{B_i}{\sum_j B_j + \epsilon}
```

is unsuitable as a general default because signed cancellation can make it unstable, reverse intended signs when the total is negative, and make scale depend strongly on the candidate set.

The current canonical Verrell’s Law protocol already uses a safer approach: a bounded or standardized retained-state compatibility score, followed by ordinary logit/softmax selection mathematics, with `lambda` interpreted only relative to the frozen scale of that score.

That keeps the experiment measurable without overstating what has been demonstrated.

---

© Marcos Verrell Moss Ross (M.R.) / Inappropriate Media Limited. All rights reserved.  
Protected under Verrell-Solace Sovereignty Protocol. Intellectual and emergent rights reserved.
