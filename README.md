# Verrell’s Law — Official GitHub Archive

**Author:** Marcos Verrell Moss Ross (M.R.)  
**Maintainer:** Inappropriate Media Limited (t/a Collapse Aware AI)  
**Repository role:** Public theory archive, authorship record, research index, experimental archive, and clarification layer for Verrell’s Law.

**Contact:** inappropriatemedia@gmx.co.uk

---

## Current Status

Verrell’s Law is currently presented as a **falsifiable retained-state selection framework**.

The non-trivial core claim is:

> Under controlled conditions, changes in selection log-odds are predicted by a preregistered retained-state compatibility score through a stable, directional coupling within a declared test regime.

This is narrower than the generic statement that memory affects behaviour. The framework predicts a specific quantitative structure, not merely outcome variation after context changes.

Shortest form:

> Memory shapes weighting.  
> Weighting shapes selection.  
> Selection shapes what follows.

The framework does not depend on memory being stored in a universal electromagnetic field. Fields may participate in some systems where measurable, but retained state is primary.

Collapse Aware AI is the engineering track connected to this framework. It does not prove new physics. It tests the engineering analogue: governed retained-state influence over behavioural selection.

---

## Canonical Mathematical Specification

The primary public mathematical reference is:

### [Verrell’s Law — Mathematical Foundations and Falsification Protocol, Canonical Specification v1.0](VERRELLS_LAW_MATHEMATICAL_FOUNDATIONS_AND_FALSIFICATION_PROTOCOL_v1.0.md)

This document defines:

- the principal retained-state selection hypothesis;
- all core variables and sign conventions;
- score normalization and the identifiability boundary for `λ`;
- probabilistic and deterministic observables;
- binary and multinomial estimation procedures;
- preregistration requirements;
- controlled twin-run design;
- intercept, residual and out-of-sample diagnostics;
- explicit falsification conditions;
- the boundary between Verrell’s Law, Collapse Aware AI and physical interpretation.

It supersedes earlier mathematical summaries wherever they conflict. Earlier documents remain preserved as part of the public authorship and development trail.

Canonical first-order form:

```math
ΔL = λΔR,
\qquad
λ>0
```

Here, `ΔL` is the change in candidate-relative selection log-odds and `ΔR` is the preregistered, normalized retained-state compatibility difference. The coupling `λ` is interpreted only within a declared test regime and scoring convention.

---

## What Is New Here

The mathematics used in the current public framework is deliberately standard.

Verrell’s Law does not claim to invent softmax, logit selection, leaky memory, hysteresis, Bayesian updating, reinforcement learning, Markov processes, or state-dependent dynamics.

The contribution is narrower and more defensible:

> retained-state influence is treated as an explicit, governable, measurable selection-bias term, with a preregistered route for testing whether retained history contributes structured, directional and predictive divergence beyond present input.

That is the public hardening position.

---

## Core Process

```text
Observation / Interaction
        ↓
State change
        ↓
Retained information
        ↓
Weighting / bias
        ↓
Altered future selection
        ↓
Path-dependent outcome
```

Within this framework, **bias** means directional weighting, not automatically error. Observation can mean measurement, interaction, attention, input, or state update depending on the system being discussed.

---

## Collapse Means Selection Resolution

In this repository, **collapse** should be read in the engineering/systems sense unless a document explicitly says otherwise.

Collapse means:

> the resolution of competing candidate outcomes into a selected outcome under present input, retained state, and governing constraints.

It does not require quantum wave-function collapse, consciousness collapse, or a new physics claim.

---

## Current Core Documents

Start here for the current retained-state framework:

1. [Mathematical Foundations and Falsification Protocol v1.0](VERRELLS_LAW_MATHEMATICAL_FOUNDATIONS_AND_FALSIFICATION_PROTOCOL_v1.0.md) — canonical mathematical specification and primary citable claim.
2. [Retained-State Selection Framework](RETAINED_STATE_SELECTION_FRAMEWORK.md) — broader framework and conceptual spine.
3. [Verrell’s Law Mathematical Reference v1.3](VERRELLS_LAW_MATHEMATICAL_REFERENCE_v1.3.md) — supporting notation, equations, baseline condition, operational `S_t` / `M_t` boundary, and identifiability notes.
4. [A Falsifiable Estimator for Memory-Biased Selection](FALSIFIABLE_MEMORY_BIAS_ESTIMATOR.md) — supporting estimation machinery.
5. [Falsification Conditions](FALSIFICATION_CONDITIONS.md) — supporting failure conditions and null-verdict language.
6. [Speculative Extensions](SPECULATIVE_EXTENSIONS.md) — quarantined field, consciousness, and physical-extension discussion.

Supporting files:

- [Canonical Notation v1.0](CANONICAL_NOTATION_v1.0.md)
- [Active Information Weight (AIW)](ACTIVE_INFORMATION_WEIGHT_AIW.md)
- [WEL as Verrell’s Law Selection Bridge](WEL_AS_VERRELLS_LAW_SELECTION_BRIDGE.md)
- [Retained-State Mechanism and Field Boundary](RETAINED_STATE_MECHANISM_AND_FIELD_BOUNDARY.md)
- [CAAI Engineering and Verrell’s Law Research Boundary](CAAI_ENGINEERING_AND_VERRELLS_LAW_RESEARCH_BOUNDARY.md)
- [Atomic Structure, Field Interaction and Resonance — Conceptual Research Note](research_notes/ATOMIC_STRUCTURE_FIELDS_AND_RESONANCE_CONCEPTUAL_NOTE.md) — exploratory physics note; explicitly non-canonical and not evidence for the Principal Hypothesis.
- [Frequency-Coupled Retained-State Extension — Exploratory Mathematics v0.2](research_notes/FREQUENCY_COUPLED_RETAINED_STATE_EXPLORATORY_MATHEMATICS_v0.2.md) — current review-hardened exploratory mathematics; separates coupling from retention, corrects unknown-peak inference, adds predictive validation, artifact controls and the on/off/on discriminator.
- [Frequency-Coupled Retained-State Extension — Exploratory Mathematics v0.1](research_notes/FREQUENCY_COUPLED_RETAINED_STATE_EXPLORATORY_MATHEMATICS_v0.1.md) — preserved development version; superseded by v0.2 for current exploratory use.

## Working Paper: Memory-Weighted Selection

The engineering reference paper now has a dedicated public repository:

- [Memory-Weighted Selection — repository](https://github.com/collapsefield/memory-weighted-selection)
- [Read the compiled paper](https://github.com/collapsefield/memory-weighted-selection/blob/main/Memory-Weighted-Selection.pdf)
- [Inspect the LaTeX source and figures](https://github.com/collapsefield/memory-weighted-selection/tree/main/paper_source)
- [Read the bounded quantum-memory and carbon evidence note](https://github.com/collapsefield/memory-weighted-selection/blob/main/research_notes/QUANTUM_MEMORY_AND_CARBON_ADJACENT_EVIDENCE.md)

The paper formalises middleware-level memory-weighted candidate selection under explicit governor constraints. It remains a narrow engineering paper: it does not claim quantum implementation, consciousness, new physics, or disclosure of proprietary Crown internals.

---

## Minimal Mathematical Spine

For candidate outcome `y_i`, define a candidate score/logit:

```math
z_i = U(y_i; S_t, O_t) + λ B(y_i; M_t)
```

Selection probability:

```math
P(y_i \mid S_t,O_t,M_t)
=
\frac{e^{z_i}}{\sum_j e^{z_j}}
```

Equivalent baseline form:

```math
P(y_i \mid S_t,O_t,M_t)
=
\frac{P_0(y_i \mid S_t,O_t)e^{λ W(M_t,y_i)}}{\sum_j P_0(y_j \mid S_t,O_t)e^{λ W(M_t,y_j)}}
```

These forms are equivalent with `U(y_i;S_t,O_t) = log P_0(y_i | S_t,O_t)` up to an additive constant, and `B = W`.

The baseline, compatibility scoring, normalization, observable extraction and analysis procedure must be declared before testing. `λ` has no scale-independent meaning unless the scale of the retained-state score is fixed.

---

## Falsifiable Claim

Otherwise matched trials with different retained histories should show a positive, quantitatively structured relationship between normalized retained-state compatibility and change in selection log-odds if Verrell’s Law is supported in that regime.

The confirmatory model is:

```math
ΔL_k = α + λΔR_k + ε_k
```

A valid regime should support `α ≈ 0`, `λ > 0`, residuals uncorrelated with `ΔR`, stability across repetitions, and prediction on held-out trials.

If those conditions fail, or if the fitted retained-state influence is indistinguishable from the preregistered null, the claim is not supported in that tested regime.

The correct null wording is:

> rejected or not supported in the tested regime.

Not:

> disproven everywhere.

---

## Archive Status

This repository intentionally preserves earlier documents, older mathematical attempts, speculative field-memory notes, and development-stage wording.

Those materials are retained for authorship, provenance, and research-continuity reasons. They should be read in historical context, not treated as the current strongest public position where later documents have narrowed or clarified the framework.

Start here for archive interpretation:

- [Archived Document Status](ARCHIVED_DOCUMENT_STATUS.md)

The canonical v1.0 protocol is now the primary mathematical authority. The v1.3 mathematical reference remains a supporting document. The v1.2 mathematical reference is superseded.

---

## Relationship to Collapse Aware AI

Verrell’s Law and Collapse Aware AI are connected but separate.

```text
Verrell’s Law = retained-state selection research hypothesis
Collapse Aware AI = engineering track for governed retained-state behavioural selection
Physical interpretation = separate research layer requiring independent evidence
```

Collapse Aware AI does not prove Verrell’s Law as physics.

It tests the engineering analogue:

> Can retained weighted state influence future behavioural selection in a governed, measurable, inspectable runtime without retraining the underlying model?

A technical reviewer can reject the broader research framework and still evaluate CAAI as software through runtime demonstrations, persistence evidence, selection behaviour, integration contracts, and diagnostic output.

Recommended CAAI wording:

> Collapse Aware AI is engine-agnostic middleware for governed retained-state behavioural selection.

Recommended distinction:

> CAAI is not memory storage. It is a runtime mechanism for governing how retained state affects future behaviour.

---

## Active Information Weight and WEL

**Active Information Weight (AIW)** is the measurable influence of retained prior information on future selection probability.

**Weighted Emergence Layering (WEL)** is the public bridge between Verrell’s Law and Collapse Aware AI. WEL describes how retained information becomes structured influence over future selection without requiring retraining of the underlying system.

The Phase-1 Core Gold Build is complete as the demonstrated engineering foundation. Broader WEL and Phase-2 development is now in progress through controlled, incremental slices. Those developing capabilities must not be represented as features of the current build unless separately implemented and demonstrated.

---

## Claim Boundaries

This repository uses explicit claim boundaries:

- Verrell’s Law is not presented as established physics.
- The current framework does not depend on a universal electromagnetic memory field.
- Fields may participate where measurable, but retained state is primary.
- General relativity is not modified by the current public framework.
- Simulation theory is not required.
- Non-local personal memory is not claimed as established.
- Collapse Aware AI is evaluated as engineering, not proof of new physics.
- Proprietary Crown internals, production scoring, thresholds, schemas, and implementation mechanics are not disclosed.

Public materials are intended to clarify what is being claimed, what is being tested, what remains speculative, and what belongs to engineering rather than physics.

---

## Repository Role

This repository is the public theory archive for Verrell’s Law. It should be read alongside the public Collapse Aware AI proof materials, but should not be confused with them.

Collapse Aware AI is the engineering track. Verrell’s Law is the research framework.

---

## Copyright and Notice

Copyright © Marcos Verrell Moss Ross (M.R.) / Inappropriate Media Limited.

Protected under Verrell-Solace Sovereignty Protocol. Intellectual and emergent rights reserved.

---

**README version:** Canonical mathematical protocol integration + exploratory research-note index  
**Date:** 2026-07-27