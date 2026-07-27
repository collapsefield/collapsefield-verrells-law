# Verrell’s Law — Frequency-Coupled Retained-State Extension
## Exploratory Mathematics v0.5 — Preregistration, Power and Mechanism Boundary

**Status:** Exploratory experimental-design work — non-canonical, unvalidated, and not evidence for the Principal Hypothesis.  
**Date:** 27 July 2026  
**Author:** M.R. (Marcos Verrell Moss Ross), Author of Verrell’s Law  
**Maintainer:** Inappropriate Media Limited (t/a Collapse Aware AI)

> **Boundary:** No empirical software-frequency effect has yet been established. This document defines what would have to be specified before a first evidence-bearing run.

This addendum should be read after v0.2, v0.3 and v0.4.

---

## 1. What Quantity Is Actually Regressed

The frequency programme inherits the canonical empirical-identification clarification:

[`VERRELLS_LAW_EMPIRICAL_IDENTIFICATION_CLARIFICATION_v1.0.md`](../VERRELLS_LAW_EMPIRICAL_IDENTIFICATION_CLARIFICATION_v1.0.md)

For any frequency experiment, the protocol must state explicitly whether `ΔR` is:

1. an **independent preregistered retained-state compatibility score**;
2. a **selector-internal score exported by the software that is already applying the same weighting equation**; or
3. an **independently measured proxy** for retained state.

These three routes estimate different things and carry different evidential weight.

A CAAI runtime check using the same internal score that drives its selector is an engineering conformance test unless an independent analysis route is used.

A proxy coefficient is not canonical `λ` unless the proxy-to-`R` mapping has been specified and identified.

---

## 2. Response Phase: Restore the One-Sided Minimum-Phase Falsifier Carefully

v0.4 correctly states that magnitude does not uniquely determine phase for every causal LTI system.

However, for a **stable, causal, minimum-phase LTI model** with a declared normalization and sufficiently characterised frequency band, the measured magnitude response implies a corresponding minimum-phase response.

Additional pure delay or stable all-pass / non-minimum-phase factors may add excess lag without changing magnitude.

Therefore the useful one-sided test is:

```text
measured phase consistent with minimum-phase prediction
or showing additional declared excess lag
→ compatible with the model class

measured response showing systematically less lag than the
minimum-phase model permits, after sign conventions,
phase unwrapping and declared delay treatment are fixed
→ inconsistent with that declared minimum-phase model class
```

This is **not** a universal falsifier of arbitrary causal systems.

It is a positive prediction only when the tested model has been declared minimum phase or when a specific transfer function has been preregistered.

Finite measurement bandwidth, phase-unwrapping error and noisy magnitude estimates must be included in the uncertainty analysis; a reconstructed phase curve should not be treated as exact outside the validated band.

---

## 3. Split the `β(ω_d)` Ambiguity Into Two Different Models

The notation:

```math
\beta=\beta(\omega_d)
```

can mean two different things. They must not be mixed.

### Model B1 — condition-dependent but constant-within-run decay

For the first evidence programme, use the simpler interpretation:

```math
\frac{dM}{dt}
=
-\beta_c M
+
\eta O(t),
```

where condition `c` corresponds to a preregistered drive-rate condition `ω_d`, and `β_c` is constant within that run.

The question is simply:

> Does the effective post-treatment retention/decay parameter differ reproducibly between preregistered drive-rate conditions after the full artifact-control stack is applied?

This is intentionally phenomenological.

A positive B1 result does **not** identify why drive rate altered the effective retention parameter.

### Model B2 — within-run periodically time-varying decay

A stronger mechanistic hypothesis would be:

```math
\beta(t)
=
\beta_0
+
\delta\beta\,g(\omega_d t+\phi),
```

with a frozen periodic waveform `g`.

Then:

```math
\frac{dM}{dt}
=
-\beta(t)M
+
\eta O(t)
```

is linear time-varying rather than LTI.

The LTI Bode/minimum-phase test above does not apply directly to this model. Periodic-coefficient analysis, including Floquet-style reasoning where appropriate, becomes the relevant mathematical tool.

B2 must not be fitted post hoc merely because B1 produced an interesting curve.

### Current decision

**The first evidence-bearing software experiment uses Model B1.**

B2 is deferred until one of the following exists:

- a reproducible B1 effect;
- an independently motivated software mechanism predicting within-run modulation;
- or direct runtime evidence that the decay/update parameter itself is periodically varying.

This keeps the first experiment identifiable and avoids importing a more flexible model before it is needed.

---

## 4. Mechanism Prior and Interpretation Boundary

No specific mechanism has yet been established for why a software drive frequency should alter retained-state coupling or persistence.

That fact must be stated explicitly.

The prior probability of a genuinely new frequency-specific effect should therefore be treated as **low until ordinary software timing mechanisms are excluded**.

Candidate ordinary mechanisms include:

- discrete decay/update cadence;
- scheduler quantisation;
- event batching;
- thresholding or clipping;
- gated refresh/overwrite rules;
- finite timer resolution;
- loop-to-drive phase locking;
- aliasing or beat structure;
- probe-induced state updates.

These are not evidence for Verrell’s Law, resonance, electromagnetic coupling or a new physical mechanism. They are the mundane explanations that must be tested first.

A purely phenomenological B1 result may still be worth reporting, but the permitted conclusion is limited to the tested software regime.

---

## 5. Power and Minimum Detectable Effect Must Be Fixed Before Confirmatory Runs

A heavily controlled experiment can still be useless if it is underpowered.

The crossed control design now includes retained-state snapshots, start phases, cadences, drive conditions, probe schedules and repetitions. The trial count must therefore be justified before confirmatory data are collected.

### Step 0 must now include

1. a declared **smallest effect size of interest** or minimum detectable effect;
2. the primary parameter/endpoint to which that effect size refers;
3. an estimated noise/variance model from engineering characterization or a separately labelled pilot dataset;
4. target statistical power;
5. significance/error-rate rule including multiplicity where applicable;
6. trials per cell;
7. total planned trial budget;
8. fixed stopping rule;
9. exclusion rule;
10. treatment of failed or corrupted runs.

For Model A, the effect may be expressed in the scale of `κ` or a preregistered change in `ΔL` attributable to the frequency term.

For Model B1, use a preregistered difference or ratio in decay parameter, persistence half-life, or another frozen retention endpoint.

Because the design is crossed and may be non-Gaussian, **simulation-based power analysis is preferred** over a simplistic single-cell formula.

Pilot data used to estimate variance or instrumentation noise must not be silently pooled into confirmatory evidence unless that pooling rule was itself preregistered.

### No optional stopping

The protocol must not continue collecting trials merely because the initial result is “almost significant” or stop early because an attractive effect appears, unless a valid sequential design and stopping boundary were preregistered.

A null result from an underpowered design is not a clean falsification; it is an uninformative result.

---

## 6. Predeclared Robustness Matrix

Before the first confirmatory run, define the exact matrix of:

- `M*` snapshots;
- drive-rate conditions;
- start phases or phase-randomisation rule;
- cadence conditions;
- jitter diagnostic;
- probe schedule;
- repetitions per cell.

The pass rule must be frozen as part of the power/design calculation.

Do not select `k-of-n` after inspecting the results.

If several robustness cells are diagnostic rather than part of the primary confirmatory endpoint, label them as diagnostics in advance rather than silently promoting whichever one succeeds.

---

## 7. Nested Search Rule Reaffirmed

Any search over:

- frequency;
- peak location;
- bandwidth;
- spline complexity;
- phase relationship;
- cadence interaction;
- snapshot subset;
- probe timing;
- or model family

must occur entirely inside training/discovery data.

Where cross-validation is used, the full search is nested inside each training fold.

The held-out fold is used once for the frozen rule.

This is mandatory. Otherwise the held-out claim is contaminated by model-selection leakage and the look-elsewhere problem returns.

---

## 8. Timeboxed First Programme

The exploratory software-frequency programme should not expand indefinitely before basic runtime feasibility is known.

### Gate 1 — runtime feasibility

Characterise:

- exact per-trial snapshot restore;
- read-only retained-state access;
- whether selection/probes mutate state;
- loop/update/sample cadence;
- timer resolution;
- reproducible timestamping.

If neither per-trial restore nor a defensible read-only/bounded-drift route exists, a clean Model-A test is blocked until that capability is added.

### Gate 2 — design feasibility

Compute the required trial budget for the declared minimum detectable effect.

If the required experiment is impractically large, narrow the question rather than running an underpowered version.

### Gate 3 — first evidence run

Only after Gates 1 and 2 pass should the preregistered B1 / Model-A experiment begin.

No richer frequency model should be introduced during that run.

---

## 9. What This Programme Can and Cannot Establish

A positive result could establish, within a declared software regime, that a preregistered drive-rate condition adds reproducible predictive information about retained-state coupling or persistence after the specified controls.

It would not by itself establish:

- a universal frequency law;
- a physical resonance mechanism;
- electromagnetic memory;
- consciousness effects;
- a new force;
- or Verrell’s Law as established universal physics.

A clean null would still be useful because it would rule out the tested frequency-specific model in the declared regime while leaving the canonical retained-state selection hypothesis logically separate.

---

## 10. Current Status

**Exploratory Mathematics v0.5**  
**Non-canonical**  
**Unvalidated**  
**First evidence-bearing model chosen: B1 (condition-dependent, constant-within-run decay)**  
**B2 time-varying/Floquet-style model deferred**  
**No established software-frequency mechanism yet**  
**Power analysis and runtime feasibility required before evidence collection**

The methodology is now sufficiently constrained that the next useful work is runtime characterization and preregistration, not additional free-form model expansion.

---

© Marcos Verrell Moss Ross (M.R.) / Inappropriate Media Limited. All rights reserved.  
Protected under Verrell-Solace Sovereignty Protocol. Intellectual and emergent rights reserved.
