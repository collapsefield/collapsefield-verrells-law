# Verrell’s Law — Empirical Identification Clarification
## Canonical Clarification Supplement v1.0

**Status:** Canonical clarification supplement to the Mathematical Foundations and Falsification Protocol v1.0  
**Date:** 27 July 2026  
**Author:** M.R. (Marcos Verrell Moss Ross), Author of Verrell’s Law  
**Maintainer:** Inappropriate Media Limited (t/a Collapse Aware AI)

> **Purpose:** Resolve what quantity is actually regressed in empirical tests of `ΔL = λΔR`, and distinguish an independent empirical test from an engineering conformance test of a selector that already uses the same retained-state score internally.

This supplement does **not** change the canonical first-order equation, sign convention, normalization requirement or falsification conditions. Where wording is ambiguous, this clarification governs the empirical interpretation of `R` and `ΔR`.

---

## 1. Canonical Equation Unchanged

The canonical first-order relation remains:

```math
\Delta L
=
\lambda\Delta R
+
\varepsilon,
\qquad \lambda>0.
```

with:

```math
\Delta R = R_a-R_b.
```

The important empirical question is how `R` is obtained.

---

## 2. `R` Must Be a Preregistered Analysis Quantity, Not an Outcome-Fitted Label

For an independent empirical test of Verrell’s Law, `R_i` is a **preregistered retained-state compatibility score** computed from declared retained-state information and candidate compatibility under a frozen scoring and normalization rule.

The rule used to construct `R_i` must not be chosen, tuned or relabelled after observing the trial’s selection outcome.

At minimum:

1. retained-state items/features are declared before outcome analysis;
2. salience, persistence, reliability and compatibility/relevance rules are frozen before confirmatory data are inspected;
3. normalization is frozen;
4. candidate labels and sign convention are frozen;
5. the scoring procedure does not use the observed `ΔL` from the same confirmatory trials to manufacture `ΔR`.

A scoring rule learned from data may be used only when the learning/tuning occurs entirely inside a discovery/training set and the complete rule is then frozen before untouched validation data are evaluated.

---

## 3. Three Distinct Identification Routes

### Route A — Independent retained-state compatibility score

This is the preferred route for an empirical test of the Verrell’s Law claim.

A declared analysis procedure computes:

```math
R_i
=
g(H_t,x_t,S_t,a_i)
```

from retained history, current controlled state and candidate compatibility without using the confirmatory selection outcome.

Then:

```math
\Delta L_k
=
\alpha
+
\lambda\Delta R_k
+
\varepsilon_k
```

is an empirical regression in which `λ` is estimated relative to the frozen scale of `R`.

This remains falsifiable because the observed `ΔL` need not follow the preregistered `ΔR` pattern.

### Route B — Selector-internal score reused as the predictor

Suppose the software under test literally implements:

```math
z_i
=
z_{0,i}
+
\lambda R_i
```

and the same internal `R_i` is then exported and regressed against the resulting `ΔL`.

That exercise is useful, but its interpretation is narrower.

It can test:

- implementation correctness;
- calibration;
- routing/instrumentation consistency;
- whether the observed runtime output conforms to the declared selector equation.

It is **not, by itself, independent empirical evidence that an externally occurring system obeys Verrell’s Law**, because the tested software was constructed to apply the same score to selection.

For Collapse Aware AI, such a test is properly described as an **engineering conformance / implementation validation** unless `R` is supplied by an independent frozen analysis route or the test system is not mechanically forced to obey the equation being evaluated.

### Route C — Independently measured proxy for retained state

Sometimes the experiment cannot observe canonical `R` directly and instead measures a proxy `X` for retained state.

If:

```math
R = g(X),
```

then the regression coefficient of `ΔL` directly on `X` is not automatically canonical `λ`.

Under a local linear approximation around an operating point `X*`:

```math
R(X)
\approx
R(X^*)
+
g'(X^*)(X-X^*),
```

so the local coefficient on `X` is approximately:

```math
\lambda\,g'(X^*).
```

In a more general nonlinear or multivariate proxy mapping, the corresponding Jacobian/measurement model must be stated.

Therefore a proxy-based study must either:

1. preregister and validate the mapping from proxy to `R`; or
2. report the fitted coefficient as a **proxy-conditioned composite effect**, not as canonical `λ`.

---

## 4. Internal Score Does Not Make Every Test Tautological

The presence of a mathematically defined `R` in the theory does not itself make `ΔL = λΔR` a definition.

The distinction is:

```text
R specified independently of confirmatory outcome
→ empirical prediction

R used by the tested selector to manufacture the same outcome being regressed
→ engineering conformance test

proxy X substituted for R without a validated mapping
→ composite/local proxy effect
```

This distinction must be stated in any evidence report.

---

## 5. Cross-Snapshot Scope

Even when canonical `R` is used directly, one retained-state operating point should not be assumed to establish transfer across the whole retained-state space.

A regime-level claim should therefore test multiple preregistered retained-state conditions or snapshots when the intended scope spans materially different retained states.

Heterogeneity across snapshots should be reported rather than silently pooled.

This is a scope/generalisation requirement; it does not redefine canonical `λ` as a derivative of the memory-bias function.

---

## 6. Minimum Evidence Labels

Public or internal evidence should use one of these labels:

### Independent empirical test

Use when `ΔR` was constructed independently of the confirmatory selection outcome under a frozen analysis rule.

### Engineering conformance test

Use when the tested selector itself applies the same `R` and `λ` relationship being checked.

### Proxy-based empirical test

Use when an independently measured proxy stands in for `R`; report the proxy mapping and do not call the raw proxy coefficient canonical `λ` unless that mapping has been identified.

---

## 7. Relationship to Collapse Aware AI

Collapse Aware AI can provide strong engineering evidence that retained-state influence is implemented, governed, inspectable, replayable and behaviorally consequential.

That is commercially and scientifically useful evidence about the software.

It should not be presented as independent proof that Verrell’s Law holds generally merely because CAAI was designed around retained-state weighting.

A stronger Verrell’s Law test requires an independent frozen `R` construction or a system whose observed selection relation is not mechanically guaranteed by the same equation being evaluated.

---

## 8. Status

**Canonical empirical-identification clarification**  
**Canonical first-order equation unchanged**  
**Distinguishes empirical prediction, engineering conformance and proxy-based inference**  
**No new physical claim introduced**

---

© Marcos Verrell Moss Ross (M.R.) / Inappropriate Media Limited. All rights reserved.  
Protected under Verrell-Solace Sovereignty Protocol. Intellectual and emergent rights reserved.
