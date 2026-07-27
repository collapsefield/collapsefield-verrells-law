# Verrell’s Law — Frequency-Coupled Retained-State Extension
## Exploratory Mathematics v0.4 — Experimental Identification Addendum

**Status:** Exploratory experimental-control work — non-canonical, unvalidated, and not evidence for the Principal Hypothesis.  
**Date:** 27 July 2026  
**Author:** M.R. (Marcos Verrell Moss Ross), Author of Verrell’s Law  
**Maintainer:** Inappropriate Media Limited (t/a Collapse Aware AI)  
**Repository:** `collapsefield/collapsefield-verrells-law`

> **Boundary:** This addendum is not part of canonical Verrell’s Law. It adds stricter rules for software-frequency experiments and makes no claim that a frequency effect, physical resonance, electromagnetic mechanism or universal law has been observed.

---

## 1. Purpose

This addendum tightens the exploratory programme defined in:

- [`FREQUENCY_COUPLED_RETAINED_STATE_EXPLORATORY_MATHEMATICS_v0.2.md`](FREQUENCY_COUPLED_RETAINED_STATE_EXPLORATORY_MATHEMATICS_v0.2.md)
- [`FREQUENCY_COUPLED_RETAINED_STATE_EXPLORATORY_MATHEMATICS_v0.3_CONTROL_ADDENDUM.md`](FREQUENCY_COUPLED_RETAINED_STATE_EXPLORATORY_MATHEMATICS_v0.3_CONTROL_ADDENDUM.md)

It closes five remaining experimental-identification issues:

1. retained state must not drift across Model-A trials merely because the selector itself updates memory;
2. a coefficient estimated at one retained-state snapshot is conditional on that operating state and should not be assumed to transfer across the retained-state space;
3. software start-phase controls must be kept separate from response-phase predictions of an explicitly declared causal LTI memory model;
4. robustness checks must be preregistered as pass/fail rules rather than chosen after seeing which settings work;
5. Model-B probing must not silently alter the decay process being measured.

The canonical Verrell’s Law specification remains unchanged.

---

## 2. Model-A State Reset Must Be Per Trial Unless the State Is Read-Only

### 2.1 Why a block-level snapshot is not sufficient by default

v0.3 requires a frozen retained-state snapshot `M*` before frequency assignment. That is necessary but not always sufficient.

If running a selection trial can itself update retained state, then after the first trial:

```math
M_{n+1}
=
F(M_n, O_n, y_n),
```

and later trials in the same block no longer start from the same `M*`.

This creates a route by which Model-B-like state evolution leaks back into a nominal Model-A coupling test.

### 2.2 Current Model-A rule

A clean Model-A trial must use one of the following, declared in advance:

**Preferred — per-trial restore**

```text
restore exact M*
→ assign / apply frequency condition
→ run one declared selection probe
→ record output
→ discard trial-mutated state
→ restore exact M* again
```

**Alternative — explicit read-only retained state**

The selector may read `M*` but is technically prevented from updating it during the test window.

**Last-resort bounded-drift design**

If neither restore nor read-only operation is possible, the protocol must independently bound state drift over the test window and justify why that bound is negligible for the declared endpoint. This is weaker evidence and must be labelled as such.

### 2.3 Verification

Where possible, each trial should record:

- snapshot identifier;
- hash/checksum or canonical serialized-state digest;
- state version;
- whether the trial was read-only;
- whether any post-trial mutation occurred.

A Model-A result is not cleanly interpretable if compared frequency conditions begin from systematically different retained states.

---

## 3. Snapshot Dependence: Do Not Treat One `M*` as Universal

### 3.1 What one frozen state can establish

At a fixed retained-state snapshot, a frequency experiment can estimate a conditional effect within that operating state.

Write this explicitly as:

```math
\kappa = \kappa(M^*)
```

when discussing transfer beyond the tested snapshot.

This notation is a reminder about **scope**, not a claim that `κ` must mathematically vary with `M`.

Likewise, canonical `λ` remains a regime-specific coupling coefficient. It is not automatically a derivative of `B` with respect to `M`, and nonlinearity of `B(M)` does not by itself turn `λ` into a local slope.

### 3.2 Generalisation test across retained-state operating points

A claim that a frequency effect is robust across retained-state conditions should repeat the complete trial-reset design at multiple independently defined snapshots.

For an initial robustness programme, use at least three preregistered retained-state operating points spanning a meaningful range of the declared system state, unless the system design supplies a stronger principled stratification.

For each `M*_q`, estimate the same frozen endpoint and report:

```math
\kappa_q.
```

A transferable-effect claim requires a preregistered rule for acceptable heterogeneity across the `\kappa_q` values.

If `κ` differs across snapshots, the correct conclusion is not automatically “curvature in `B`.” Possible explanations include:

- a genuine interaction between retained state and frequency condition;
- non-separability of the proposed model;
- state-dependent scoring or normalization;
- hidden state drift;
- or misspecification.

The heterogeneity itself becomes a result requiring a narrower model.

---

## 4. Response Phase Is Different from Software Start Phase

v0.3 correctly introduced software start phase:

```math
\phi_n
=
(\omega_d t_n + \phi_0)\bmod 2\pi,
```

which tests alignment with update, scheduler and sampling clocks.

That is an artifact/interaction control.

A different quantity is the **phase lag of a measured dynamical response relative to a declared oscillatory input**.

These must not be conflated.

### 4.1 When a response-phase prediction is legitimate

A response-phase prediction is required only when the software memory dynamics are explicitly modelled as a causal linear time-invariant system over the tested range.

For a declared transfer function:

```math
H(\Omega)
=
|H(\Omega)|e^{i\theta(\Omega)},
```

measure both magnitude and response phase where the time series supports doing so.

Causality constrains the complex response, but **magnitude alone does not generally determine phase for an arbitrary causal system**.

A Hilbert-transform / Bode gain-phase reconstruction from log-magnitude is valid only under the additional minimum-phase assumptions required by that theorem. Pure delay and all-pass / non-minimum-phase components can add phase without changing magnitude.

Therefore:

- do not use “phase mismatch” as a universal falsifier of every causal LTI model;
- do use a predeclared minimum-phase prediction as a falsifier when minimum phase is part of the claimed model;
- separately estimate and report any transport delay or excess/all-pass phase rather than silently removing it after looking at the data.

### 4.2 Positive phase prediction for a first-order memory kernel

For the explicitly first-order linear memory model:

```math
\frac{dM}{dt}
=
-\beta M
+
\eta O(t),
```

with constant `β>0` and `η` within one declared condition, the transfer function from input `O` to state `M` is:

```math
H(\Omega)
=
\frac{\eta}{\beta+i\Omega}.
```

Hence:

```math
|H(\Omega)|
=
\frac{|\eta|}{\sqrt{\beta^2+\Omega^2}},
```

and:

```math
\theta(\Omega)
=
-\arctan\!\left(\frac{\Omega}{\beta}\right)
```

for positive `η` under the usual sign convention.

This is a monotone first-order low-pass response. Its phase approaches `-90°` as analysis frequency increases. It does not contain an intrinsic resonance peak in `|H(Ω)|`.

### 4.3 Important distinction: analysis frequency `Ω` versus experimental drive parameter `ω_d`

The no-resonance result above is about the transfer function as a function of **analysis/input frequency `Ω`** for a fixed first-order kernel.

It does **not** by itself forbid an experimentally imposed drive parameter `ω_d` from changing the kernel parameter:

```math
\beta = \beta(\omega_d).
```

A non-monotone dependence of `β` on `ω_d` would be a separate parametric hypothesis requiring its own mechanism, controls and held-out evidence.

Therefore the programme must never confuse:

```text
peak in |H(Ω)| of a first-order LTI kernel
```

with:

```text
structured change in β as an externally varied condition ωd changes.
```

If a resonant peak is claimed in the first sense, a first-order kernel is insufficient. A higher-order, oscillatory, feedback, nonlinear or time-varying state model — or an artifact explanation — would be required and must be specified before confirmatory testing.

---

## 5. Predeclare the Robustness Matrix and Pass Rule

Cadence, start phase, snapshot, jitter and probe schedule are scientific controls, but they are also researcher degrees of freedom if their interpretation is chosen after results are visible.

Before confirmatory data collection, preregister:

- the number and exact values/ranges of cadence conditions;
- the number and construction of start-phase conditions;
- the retained-state snapshots or snapshot-generation strata;
- any timing-jitter diagnostic;
- the primary endpoint;
- the effect direction if directional;
- the minimum number `k` of `n` declared conditions that must satisfy the replication criterion;
- the tolerance for effect-size heterogeneity;
- exclusions and failure rules.

Do not decide after the run that “3 of 5 settings is enough.”

The actual `k` and `n` should be chosen from the experimental design and power/precision requirements before data are inspected; this note does not invent universal values.

### 5.1 Held-out validation must include the entire search

If frequency structure, `ω₀`, `Γ`, spline complexity, bins, phase relationship, cadence interaction or any other model feature is selected from data, **all of that selection must occur using training/discovery data only**.

For cross-validation, the complete search procedure must be nested inside each training fold.

Test-fold information must not be used to:

- choose the candidate frequency;
- choose the peak centre or width;
- choose the spline/bins;
- choose which phase or cadence looks best;
- choose exclusions;
- or decide which model family to score.

Only the frozen training-derived rule may be evaluated on the held-out fold.

Otherwise the held-out route no longer protects against post-selection / look-elsewhere bias.

---

## 6. Model-B Probes Are Potentially Reactive

### 6.1 The problem

Model B uses the post-intervention trajectory of retained state as evidence.

But if observing that trajectory requires selection probes, and those probes themselves update retained state, then the measurement process changes the quantity being measured.

Schematically:

```math
M_{n+1}
=
F(M_n, O^{probe}_n, y_n).
```

The measured decay may then combine natural retention dynamics with probe-induced updates.

### 6.2 Preferred solutions

Use one of these, declared in advance:

1. **read-only probe** — measure the declared state/readout without changing retained state;
2. **fixed probe schedule** — use exactly the same probe inputs, timings and candidate structure in every condition so probe effects are common-mode;
3. **paired probe-control condition** — estimate the effect of the probe schedule itself under an otherwise matched no-treatment condition.

The probe schedule must not be adapted after seeing the decay trajectory.

### 6.3 Input-scale identifiability

For a linear state equation such as:

```math
\frac{dM}{dt}
=
-\beta M
+
\eta O(t),
```

only the product of input scale and gain is observable unless the scale of `O` is fixed or independently calibrated.

Therefore the protocol must declare and freeze the amplitude/normalization of `O`, or report `η` only relative to an explicitly defined input scale.

This is analogous to the existing requirement to freeze the scales of `R`, `h`, and measurement temperature before interpreting `λ` or `κ`.

---

## 7. Revised Minimum Sequence Before First Evidence Run

Before collecting a result intended as evidence:

### Step 0 — runtime characterization

Measure and document:

- whether a selection trial mutates retained state;
- whether exact snapshot serialization/restore is available;
- whether a read-only mode is available;
- effective loop/update/sample cadence;
- timer resolution;
- probe behaviour and whether probing mutates state.

Do not preregister numerical frequency bands until these facts are known.

### Step 1 — choose the identification path

For Model A:

```text
per-trial restore of identical M*
(or explicit read-only M*)
→ randomized condition
→ one declared probe
```

For Model B:

```text
controlled state formation / retention treatment
→ fixed or read-only probe schedule
→ post-treatment decay measurement
```

### Step 2 — freeze the robustness matrix

Declare snapshots, cadence settings, phase handling, jitter diagnostic, repetitions, endpoint and pass/fail rule before the run.

### Step 3 — run the on/off/on discriminator

Use the v0.2/v0.3 randomized/blinded protocol with the stricter per-trial reset and probe-reactivity rules above.

### Step 4 — only then screen frequency structure

Search only within training/discovery data and score the completely frozen rule on untouched data.

### Step 5 — only then propose a richer dynamical model

A resonant, higher-order or physical interpretation is permitted only after the simple first-order / artifact explanations have been tested and rejected under preregistered criteria.

---

## 8. Added Failure Conditions

In addition to v0.2 and v0.3, a proposed frequency-specific interpretation is not supported or must be narrowed when:

1. nominal Model-A trials do not begin from the same restored/read-only retained state;
2. trial-induced memory updates explain the apparent condition effect;
3. a result from one `M*` is presented as transferable across retained-state space without a cross-snapshot test;
4. snapshot-dependent `κ` heterogeneity is silently averaged away;
5. a general causal system is rejected solely because phase differs from a minimum-phase reconstruction when minimum phase was never assumed;
6. a first-order LTI kernel is claimed to generate an intrinsic resonance peak in `|H(Ω)|` without an additional dynamical mechanism;
7. analysis frequency `Ω` and experimental drive parameter `ω_d` are conflated;
8. cadence, phase, snapshot, jitter or pass thresholds are chosen after results are inspected;
9. any frequency/model search uses held-out data during model selection;
10. Model-B probes differ across conditions or materially perturb retained state without a matched probe-control design;
11. input amplitude/normalization is free while `η` is interpreted as an independently identified gain.

---

## 9. Relationship to Earlier Versions

The exploratory hierarchy is now:

```text
Canonical Verrell’s Law v1.0
        ↓ governs all conflicts
v0.2 — exploratory frequency mathematics
        ↓
v0.3 — retained-state conditioning + software start-phase controls
        ↓
v0.4 — per-trial reset + snapshot scope + response-phase boundary
       + preregistered robustness + reactive-probe controls
```

v0.4 does not replace the mathematical models in v0.2. It supplies the strictest current experimental-identification rules.

Where any exploratory document conflicts with the canonical specification, the canonical specification governs.

---

## 10. References and Technical Basis

1. Montgomery, J. M., Nyhan, B., & Torres, M. (2018). **How Conditioning on Posttreatment Variables Can Ruin Your Experiment and What to Do about It.** *American Journal of Political Science*, 62(3), 760–775. https://doi.org/10.1111/ajps.12357
2. Bechhoefer, J. (2005). **Feedback for physicists: A tutorial essay on control.** *Reviews of Modern Physics*, 77, 783–836. https://doi.org/10.1103/RevModPhys.77.783
3. Davies, R. B. (1977, 1987, 2002). Nuisance-parameter-under-the-alternative results cited in v0.2.
4. Nyquist/aliasing and sampling controls as cited in v0.2/v0.3.

These references support experimental-design and linear-systems constraints. They do not endorse Verrell’s Law and do not imply that a frequency effect exists.

---

## 11. Current Status

**Exploratory Mathematics v0.4 Experimental Identification Addendum**  
**Non-canonical**  
**Unvalidated**  
**No empirical frequency effect claimed**  
**No physical resonance mechanism claimed**  
**No universal `κ` across retained-state snapshots assumed**  
**First evidence run not yet performed**

The next useful step is empirical only after the runtime has been characterized well enough to freeze a preregistered protocol.

---

© Marcos Verrell Moss Ross (M.R.) / Inappropriate Media Limited. All rights reserved.  
Protected under Verrell-Solace Sovereignty Protocol. Intellectual and emergent rights reserved.
