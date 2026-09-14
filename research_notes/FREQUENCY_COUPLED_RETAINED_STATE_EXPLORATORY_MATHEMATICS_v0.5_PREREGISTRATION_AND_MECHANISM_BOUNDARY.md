# Verrell’s Law — Frequency-Coupled Retained-State Extension
## Exploratory Mathematics v0.5 — Preregistration, Power and Mechanism Boundary

**Status:** Exploratory experimental-design work — non-canonical, unvalidated, and not evidence for the Principal Hypothesis  
**Date:** 27 July 2026  
**Author / originator:** Marcos Verrell Moss Ross (M.R.)  
**Research attribution refresh:** 14 September 2026

> **Boundary:** No empirical software-frequency effect has been established. This document defines what would have to be specified before a first evidence-bearing run.

---

## 1. What quantity is actually regressed

Any frequency experiment must state whether `ΔR` is:

1. an **independent preregistered retained-state compatibility score**;
2. a **selector-internal score** exported by software already applying the same weighting equation; or
3. an **independently measured proxy** for retained state.

These routes carry different evidential weight.

A runtime check using the same internal score that drives its selector is an engineering conformance test unless an independent analysis route is used.

A proxy coefficient is not canonical `λ` unless the proxy-to-`R` mapping has been specified and identified.

---

## 2. Response phase boundary

For a **stable, causal, minimum-phase LTI model** with declared normalization and a sufficiently characterised frequency band, measured magnitude constrains a corresponding minimum-phase response.

Additional pure delay or stable all-pass / non-minimum-phase factors can add excess lag without changing magnitude.

Therefore phase becomes a useful falsifier only when the model class and delay treatment are declared in advance. It is not a universal test of arbitrary causal systems.

Finite bandwidth, phase-unwrapping error and noisy magnitude estimates must be included in uncertainty analysis.

---

## 3. Two different decay models

### Model B1 — condition-dependent, constant-within-run decay

```math
\frac{dM}{dt}=-\beta_c M+\eta O(t)
```

where condition `c` corresponds to a preregistered drive-rate condition and `β_c` is constant within the run.

The question is whether the effective post-treatment retention/decay parameter differs reproducibly between preregistered drive-rate conditions after artifact controls.

A positive result is phenomenological. It does not identify why drive rate altered the effective parameter.

### Model B2 — periodically time-varying decay

```math
\beta(t)=\beta_0+\delta\beta\,g(\omega_d t+\phi)
```

with:

```math
\frac{dM}{dt}=-\beta(t)M+\eta O(t)
```

This is linear time-varying rather than LTI. The LTI phase test does not directly apply.

**Current decision:** the first evidence-bearing software experiment uses **B1**. B2 remains deferred unless simpler evidence or an independently motivated mechanism justifies it.

---

## 4. Mechanism prior

No specific mechanism has been established for why a software drive frequency should alter retained-state coupling or persistence.

Ordinary software explanations must be tested first, including:

- update cadence;
- scheduler quantisation;
- event batching;
- thresholding/clipping;
- refresh/overwrite rules;
- timer resolution;
- phase locking;
- aliasing / beat structure;
- probe-induced state updates.

These are mundane alternatives, not evidence for resonance, electromagnetic coupling or a new physical mechanism.

---

## 5. Power and minimum detectable effect

Before confirmatory runs, fix:

1. the smallest effect size of interest;
2. the primary endpoint;
3. the noise/variance model;
4. target power;
5. error-rate / multiplicity rule;
6. trials per cell;
7. total trial budget;
8. stopping rule;
9. exclusion rule;
10. treatment of failed/corrupted runs.

Because the design may be crossed and non-Gaussian, simulation-based power analysis is preferred where appropriate.

Pilot data used for variance estimation must not be silently pooled into confirmatory evidence unless preregistered.

No optional stopping is permitted without a preregistered sequential design.

---

## 6. Robustness matrix

Before the first confirmatory run, define the exact matrix of:

- retained-state snapshots;
- drive-rate conditions;
- start phases / phase-randomisation rule;
- cadence conditions;
- jitter diagnostics;
- probe schedules;
- repetitions per cell.

Primary and diagnostic cells must be labelled in advance.

---

## 7. Nested search rule

Any search over frequency, peak location, bandwidth, spline complexity, phase, cadence interaction, snapshot subset, probe timing or model family must occur entirely inside discovery/training data.

The held-out set is used only for the frozen rule.

---

## 8. Timeboxed first programme

### Gate 1 — runtime feasibility

Characterise exact per-trial restore, read-only retained-state access, mutation caused by selection/probes, loop/update cadence, timer resolution and timestamping.

### Gate 2 — design feasibility

Compute the trial budget for the declared minimum detectable effect. If impractical, narrow the question rather than run an underpowered experiment.

### Gate 3 — first evidence run

Only after Gates 1 and 2 pass should the preregistered B1 / Model-A experiment begin.

No richer model should be introduced during that confirmatory run.

---

## 9. What this programme can establish

A positive result could show, **within a declared software regime**, that a preregistered drive-rate condition adds predictive information about retained-state coupling or persistence after specified controls.

It would not by itself establish:

- a universal frequency law;
- physical resonance;
- electromagnetic memory;
- consciousness effects;
- a new force;
- Verrell’s Law as universal established physics.

A clean null is still useful because it constrains the tested frequency-specific model while leaving the canonical retained-state selection hypothesis logically separate.

---

## 10. Current status

**Exploratory Mathematics v0.5**  
**Non-canonical**  
**Unvalidated**  
**First evidence-bearing model: B1**  
**B2 deferred**  
**No established software-frequency mechanism**  
**Power analysis and runtime feasibility required before evidence collection**

---

Copyright © 2026 Marcos Verrell Moss Ross (M.R.).
