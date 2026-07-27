# Verrell’s Law — Frequency-Coupled Retained-State Extension
## Exploratory Mathematics v0.3 — Conditioning and Phase-Control Addendum

**Status:** Exploratory research control addendum — non-canonical, unvalidated, and not evidence for the Principal Hypothesis.  
**Date:** 27 July 2026  
**Author:** M.R. (Marcos Verrell Moss Ross), Author of Verrell’s Law  
**Maintainer:** Inappropriate Media Limited (t/a Collapse Aware AI)  
**Repository:** `collapsefield/collapsefield-verrells-law`

> **Boundary:** This addendum is not part of canonical Verrell’s Law and makes no claim that a physical resonance effect exists.

---

## 1. Purpose

This addendum closes two remaining experimental-control gaps identified during adversarial review of:

[`FREQUENCY_COUPLED_RETAINED_STATE_EXPLORATORY_MATHEMATICS_v0.2.md`](FREQUENCY_COUPLED_RETAINED_STATE_EXPLORATORY_MATHEMATICS_v0.2.md)

The two additions are:

1. the **retained-state conditioning confound**: a frequency intervention cannot be interpreted as changing downstream coupling if the same intervention also changed the retained state being coupled;
2. the **phase / clock-alignment check**: in software-frequency experiments, an apparent frequency effect can depend on arbitrary alignment between the periodic intervention and the system update/sampling clock.

All unchanged statistical, identifiability, on/off/on, Nyquist, held-out-prediction and Track-S/Track-P boundaries in v0.2 remain in force.

The canonical Verrell’s Law specification remains unchanged.

---

## 2. Retained-State Conditioning Confound

### 2.1 The problem

Model A in v0.2 asks whether frequency changes the strength with which an already-formed retained state influences selection:

```math
\lambda_{\mathrm{eff}}(\omega_d)
=
\lambda_0+\kappa h(\omega_d).
```

That interpretation requires the retained state presented to the selector to be held fixed or demonstrably matched across the frequency conditions being compared.

If the same frequency intervention is active while the retained state is being formed, then the state itself may become frequency-dependent:

```math
M_t = M_t(\omega_d).
```

The observable relation is then more accurately written schematically as:

```math
\Delta L(\omega_d)
=
[\lambda_0+\kappa h(\omega_d)]
\,\Delta R[M_t(\omega_d)].
```

A change in `ΔL` can therefore arise from:

- changed coupling `κ`;
- changed retained-state content, strength or persistence through `M_t(ω_d)`;
- or both.

Without separating those paths, a frequency-dependent result cannot be assigned uniquely to Model A.

### 2.2 Do not repair this by naively conditioning on post-intervention `M`

If the intervention can itself alter `M`, then statistically controlling for the observed post-intervention value of `M` is not automatically a valid fix. Conditioning on a variable affected by the intervention can bias causal-effect estimates.

The preferred solution is therefore **design-stage separation**, not post-hoc statistical conditioning.

### 2.3 Model-A design rule — freeze history before frequency assignment

For a clean Model-A test:

```text
COMMON HISTORY FORMATION
        ↓
freeze / snapshot retained state M*
        ↓
randomize frequency condition ωd
        ↓
selection test
```

Where the implementation permits it, use the same serialized retained-state snapshot `M*` for every compared frequency condition.

Recommended controls:

1. form retained state under a common, frequency-neutral condition;
2. serialize or otherwise freeze the retained state before assigning `ω_d`;
3. verify the same state snapshot, hash/checksum or declared state summary is supplied to each comparison run;
4. randomize the frequency condition only after the snapshot has been restored;
5. hold candidate set, present input, baseline model/version, seed policy and scoring convention fixed;
6. repeat across independently formed retained-state snapshots rather than relying on one history.

If exact state cloning is impossible, the experiment must use the strongest available matched-history procedure and report the residual uncertainty.

### 2.4 Model-B design rule — intervention during retention is deliberate

Model B asks a different question: whether the intervention changes the retained state itself.

For Model B, applying the frequency condition during history formation, storage or retention is not a confound; it is the treatment of interest.

A clean separation is therefore:

```text
MODEL A
same frozen M* → vary frequency during selection

MODEL B
vary frequency during formation/retention → measure resulting M or persistence
```

This timing distinction should be preregistered before data collection.

### 2.5 Joint-effect fallback

If the design cannot separate state formation from downstream selection, do not label the result a pure Model-A coupling effect.

Use the narrower wording:

> **Within the tested system, the frequency condition changed the combined retained-state/selection process. The experiment did not identify whether the effect arose from altered retained state, altered downstream coupling, or both.**

That result may justify a better experiment, but not a mechanistic claim.

---

## 3. Software Phase and Clock-Alignment Check

### 3.1 Why phase matters in Track S

In a software periodicity experiment, the intervention is generated and observed by discrete clocks: update loops, timers, schedulers, event queues and sampling routines.

For a periodic software drive evaluated at event/sample times `t_n`, define the drive phase as:

```math
\phi_n
=
(\omega_d t_n + \phi_0)\bmod 2\pi,
```

where `φ₀` is the start phase relative to the relevant software clock.

Two runs with the same nominal frequency but different `φ₀` can stimulate different update positions. A nominal frequency can also become phase-locked to a loop or scheduler when their periods are commensurate.

An apparent frequency peak can therefore be produced by:

- fixed start-phase alignment;
- rational frequency ratios with the update loop;
- scheduler quantization;
- timer resolution;
- event batching;
- aliasing;
- beat frequencies between the drive and the loop/sample clock.

### 3.2 Phase is not automatically an artifact

A real software mechanism may genuinely depend on phase relative to a discrete update cycle.

Therefore phase dependence is not automatically evidence against a Track-S effect.

It does, however, invalidate a **frequency-only** interpretation if the effect appears only at one arbitrary clock alignment and disappears when start phase is randomized.

The claim must match what was identified:

- robust across phase → frequency-structured effect is plausible within the tested software regime;
- reproducibly phase-dependent → report a frequency-and-phase timing effect;
- disappears under phase randomization → treat the original peak as likely clock-locking / alignment structure rather than a robust frequency effect.

### 3.3 Required Track-S phase controls

For software-frequency experiments:

1. record the effective loop/update/sample rate;
2. record the timestamping and timer resolution used to generate the periodic intervention;
3. randomize `φ₀` across blocks unless a phase is explicitly preregistered for mechanistic reasons;
4. repeat candidate frequencies across multiple start phases;
5. where practical, include approximately separated phases such as `0`, `π/2`, `π`, `3π/2`, or use randomized continuous phase;
6. repeat candidate effects after changing the loop/update cadence;
7. add small preregistered timing jitter in a diagnostic run where doing so does not change the intended mechanism;
8. check whether the apparent peak tracks physical/declared `ω_d` or instead tracks a ratio to loop/scheduler frequency.

### 3.4 Phase-marginalised frequency effect

Where the intended claim is frequency-only, the primary frequency comparison should average or otherwise marginalize over randomized start phase rather than relying on a single `φ₀`.

Conceptually:

```math
\mu(\omega_d)
=
\mathbb{E}_{\phi_0}
[\Delta L\mid\omega_d,\phi_0].
```

A frequency effect that exists only at one hand-selected phase should not be presented as phase-independent evidence.

### 3.5 Separate software phase from physical-response phase

This addendum does not replace the physical phase/transfer requirement already stated in v0.2.

The two uses of phase are different:

```text
Track S phase
= alignment of software drive with discrete update / scheduler / sampling clocks

Track P phase
= phase of a measured physical response relative to a physical causal drive
```

Track-P causal linear-response claims remain subject to the complex-response and phase/dispersion constraints already stated in v0.2.

---

## 4. Revised A/B Experimental Order

The preferred first sequence is now:

### A. History-control check

Before any frequency comparison, demonstrate that the Model-A path can restore the same retained-state snapshot or sufficiently matched retained history across conditions.

### B. On/off/on discriminator

Run the existing randomized/blinded on/off/on test.

### C. Software phase-control pass

For Track S, repeat candidate conditions across randomized start phase and at least one altered loop/update cadence before interpreting a frequency peak.

### D. Broad frequency screen

Only after A–C are stable, run the broad preregistered frequency-structure screen with held-out validation.

### E. Parametric or physical characterization

Only after reproducible localized structure exists should a frozen parametric response or physical causal-resonance interpretation be attempted.

---

## 5. Added Falsification / Interpretation Boundaries

In addition to the v0.2 falsification conditions, a proposed frequency-specific interpretation is not supported when:

1. the frequency intervention was allowed to alter retained-state formation and the analysis nevertheless attributes the result uniquely to downstream coupling;
2. an apparent Model-A effect disappears when the same retained-state snapshot is restored across frequency conditions;
3. a claimed frequency-only Track-S effect exists only at one arbitrary start phase and fails under preregistered phase randomization;
4. the apparent peak shifts predictably with loop/update cadence or scheduler frequency;
5. a timing-jitter diagnostic destroys the effect in a manner consistent with clock locking rather than the declared mechanism;
6. phase was searched post hoc and the selected phase was then treated as though it had been fixed in advance.

A reproducible phase-dependent software effect may still be scientifically interesting, but it must be reported as a timing/phase-dependent effect rather than silently relabelled as pure frequency dependence.

---

## 6. Relationship to v0.2 and Canonical Verrell’s Law

This file is a **control addendum** to v0.2. It does not alter:

- the canonical Principal Hypothesis;
- canonical `ΔL = λΔR`;
- canonical normalization and sign conventions;
- the Davies-type unknown-peak boundary;
- the held-out-prediction requirement;
- the Model-A/Model-B distinction;
- the Track-S/Track-P separation;
- the physical causal-response boundary.

Where this addendum and v0.2 differ on experimental control, this addendum supplies the stricter current exploratory rule.

Where any exploratory document conflicts with the canonical specification, the canonical specification governs.

---

## 7. References and Control Basis

- Montgomery, J. M., Nyhan, B., & Torres, M. (2018). **How Conditioning on Posttreatment Variables Can Ruin Your Experiment and What to Do about It.** *American Journal of Political Science*, 62(3), 760–775. https://doi.org/10.1111/ajps.12357
- National Instruments. **Acquiring an Analog Signal: Bandwidth, Nyquist Sampling Theorem, and Aliasing.** Sampling-rate, aliasing and beat/false-frequency controls used here are standard signal-processing constraints.
- [`FREQUENCY_COUPLED_RETAINED_STATE_EXPLORATORY_MATHEMATICS_v0.2.md`](FREQUENCY_COUPLED_RETAINED_STATE_EXPLORATORY_MATHEMATICS_v0.2.md)
- [`VERRELLS_LAW_MATHEMATICAL_FOUNDATIONS_AND_FALSIFICATION_PROTOCOL_v1.0.md`](../VERRELLS_LAW_MATHEMATICAL_FOUNDATIONS_AND_FALSIFICATION_PROTOCOL_v1.0.md)

These references support experimental-control principles. They do not endorse Verrell’s Law or imply that a frequency effect exists.

---

## 8. Current Status

**Exploratory Mathematics v0.3 Control Addendum**  
**Non-canonical**  
**Unvalidated**  
**No empirical frequency effect claimed**  
**No physical resonance mechanism claimed**  
**Adds retained-state conditioning control and software phase/clock-alignment control**

The research question remains deliberately narrow: test first, separate mechanisms second, and reject stronger interpretation when the design cannot identify it.

---

© Marcos Verrell Moss Ross (M.R.) / Inappropriate Media Limited. All rights reserved.  
Protected under Verrell-Solace Sovereignty Protocol. Intellectual and emergent rights reserved.
