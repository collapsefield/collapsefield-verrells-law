# Verrell’s Law — AI Testing and Bias Normalization Clarification
## Public Testing Supplement v1.0

**Author / originator:** Marcos Verrell Moss Ross (M.R.)  
**Status:** Public clarification supplement; subordinate to the canonical mathematical specification and empirical-identification clarification  
**Date:** 27 August 2026  
**Research attribution refresh:** 14 September 2026

---

## 1. Purpose

This note answers two recurring questions about experimental tests of Verrell’s Law in AI systems:

1. What is the minimum defensible procedure for testing whether retained informational history alters later selection under otherwise matched present conditions?
2. How should a retained-state bias/compatibility term be scaled so that an apparent effect is not merely a numerical artifact of arbitrary magnitude or unstable normalization?

This document does **not** replace or amend:

- `VERRELLS_LAW_MATHEMATICAL_FOUNDATIONS_AND_FALSIFICATION_PROTOCOL_v1.0.md`
- `VERRELLS_LAW_EMPIRICAL_IDENTIFICATION_CLARIFICATION_v1.0.md`

The canonical framework uses retained-state compatibility score `R_i`. Earlier `B(y_i;M_t)` notation can be treated as a raw implementation-level precursor, not a new canonical variable.

---

## 2. Minimum AI Test Procedure

A basic AI experiment should not merely demonstrate that a system with memory behaves differently from one without memory.

A defensible test should:

1. freeze the present-state boundary, current input, system state, candidate set, model/version and sampling settings;
2. define retained informational history explicitly;
3. preregister the rule producing `R_i` or `ΔR`;
4. control the scale of the retained-state term;
5. construct an otherwise-matched reference condition;
6. measure candidate-relative selection change;
7. test the preregistered directional relation;
8. perform intervention / ablation;
9. report the correct evidence class.

The canonical first-order relation remains:

```math
\Delta L=\lambda\Delta R+\varepsilon,
\qquad \lambda>0.
```

A fitted effect is meaningful only relative to the preregistered scale and sign convention of `R`.

---

## 3. Generic Memory Retention Is Not Enough

Successful retrieval, a larger context window, transcript persistence or generic recurrence do not by themselves demonstrate the canonical retained-state selection relation.

The relevant question is:

> **Under otherwise equivalent present conditions, does a preregistered retained-state compatibility difference predict a measurable, directional change in later selection?**

---

## 4. Rejected Signed-Sum Normalization

The informal transformation:

```math
\tilde B_i=\frac{B_i}{\sum_j B_j+\epsilon}
```

is **not recommended** as the default normalization.

Problems include:

- near-zero denominator instability when positive and negative values cancel;
- sign inversion when the total is negative;
- candidate-set dependence;
- arbitrary sensitivity to `epsilon` near zero.

The stabilizing constant prevents literal division by zero but does not make the scale scientifically meaningful.

---

## 5. Negative Retained-State Values Are Not Invalid

Under:

```math
z_i=U_i+\lambda R_i
```

followed by ordinary softmax selection, a negative `R_i` simply lowers that candidate’s logit relative to alternatives.

`R_i` is not itself required to be a probability distribution or sum to one.

---

## 6. Canonical Scale-Control Position

A general retained-state score can be written:

```math
R_i(H_t,x_t,S_t)
=\frac{1}{n}\sum_{j=1}^{n}s_jd_jq_jr_{ij}
```

with preregistered component definitions and bounded scales unless another convention is justified in advance.

An alternative is to standardize `ΔR` under a preregistered rule.

The governing principle is:

> **The retained-state compatibility scale must be fixed before confirmatory testing, and fitted `λ` is interpretable only relative to that declared scale.**

---

## 7. Alternative Transformations

Other transformations can be valid if preregistered, justified and tested for pathological behaviour.

Examples include max-absolute scaling, shift-and-scale transformations or softmax of a raw retained-state quantity when the experimental object genuinely requires a probability-like allocation.

None is automatically canonical. The transformation must preserve the interpretation being tested and must not be chosen after inspecting confirmatory outcomes.

---

## 8. Recency, Salience and Similar Features

Recency, salience, recurrence, reliability, persistence and related quantities can be legitimate components of a retained-state compatibility function.

They are **implementation or experimental-design choices**, not universal requirements of Verrell’s Law.

---

## 9. Relationship to Collapse Aware AI™

Collapse Aware AI™ is the separate engineering programme for governed retained-state selection.

Two boundaries must be preserved:

1. If a selector is built to apply a particular retained-state score, demonstrating the expected result is engineering conformance unless an independent analysis route is supplied.
2. Governance / permission logic should not automatically be collapsed into the retained-state score itself.

No public mathematical example in this repository should be read as disclosure of proprietary Core Gold scoring, thresholds or production internals.

---

## 10. Evidence Labels

Use:

- **Independent empirical test** — `ΔR` is constructed independently of the confirmatory outcome under a frozen rule.
- **Engineering conformance test** — the tested selector itself applies the relationship being checked.
- **Proxy-based empirical test** — an independent proxy stands in for canonical retained-state compatibility and its mapping is reported appropriately.

---

## 11. Practical Evidence Sequence

1. **Divergence** — matched present conditions, different retained history.
2. **Directional structure** — effect follows the preregistered retained-state relation.
3. **Stability / prediction** — repeated and held-out data behave as predicted.
4. **Intervention / ablation** — deliberate retained-state manipulation changes the effect.
5. **Replication / scope** — result transfers without post-hoc changes to the scoring rule.

Formal verdicts remain governed by the canonical falsification protocol.

---

## Recommended Public Wording

> **Under otherwise equivalent present conditions, retained informational history is hypothesized to exert a measurable, directional and intervention-sensitive influence on future state selection.**

---

Copyright © 2026 Marcos Verrell Moss Ross (M.R.).
