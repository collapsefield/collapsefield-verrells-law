# Verrell’s Law — Official GitHub Archive

**Author:** Marcos Verrell Moss Ross (M.R.)  
**Maintainer:** Inappropriate Media Limited (t/a Collapse Aware AI)  
**Repository role:** Public theory archive, authorship record, research index, experimental archive, and clarification layer for Verrell’s Law.

**Contact:** inappropriatemedia@gmx.co.uk

---

## Current Status

Verrell’s Law is currently presented as a **falsifiable retained-state selection framework**, not as established physics.

The core claim is:

> Prior interactions can leave persistent state changes. Those retained changes can bias future selection, producing path-dependent divergence even when present inputs appear similar or unchanged.

Shortest form:

> Memory shapes weighting.  
> Weighting shapes selection.  
> Selection shapes what follows.

The framework does not depend on memory being stored in a universal electromagnetic field. Fields may participate in some systems where measurable, but retained state is primary.

Collapse Aware AI is the engineering track connected to this framework. It does not prove new physics. It tests the engineering analogue: governed retained-state influence over behavioural selection.

---

## What Is New Here

The mathematics used in the current public framework is deliberately standard.

Verrell’s Law does not claim to invent softmax, logit selection, leaky memory, hysteresis, Bayesian updating, reinforcement learning, Markov processes, or state-dependent dynamics.

The contribution is narrower and more defensible:

> retained-state influence is treated as an explicit, governable, measurable selection-bias term, with a pre-committed route for estimating whether retained history contributes measurable divergence beyond present input.

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

1. [Retained-State Selection Framework](RETAINED_STATE_SELECTION_FRAMEWORK.md) — canonical current framework and mathematical spine.
2. [Verrell’s Law Mathematical Reference v1.3](VERRELLS_LAW_MATHEMATICAL_REFERENCE_v1.3.md) — notation, equations, baseline condition, operational `S_t` / `M_t` boundary, and identifiability notes.
3. [A Falsifiable Estimator for Memory-Biased Selection](FALSIFIABLE_MEMORY_BIAS_ESTIMATOR.md) — estimation machinery for retained-state influence.
4. [Falsification Conditions](FALSIFICATION_CONDITIONS.md) — failure conditions and null-verdict language.
5. [Speculative Extensions](SPECULATIVE_EXTENSIONS.md) — quarantined field, consciousness, and physical-extension discussion.

Supporting files:

- [Canonical Notation v1.0](CANONICAL_NOTATION_v1.0.md)
- [Active Information Weight (AIW)](ACTIVE_INFORMATION_WEIGHT_AIW.md)
- [WEL as Verrell’s Law Selection Bridge](WEL_AS_VERRELLS_LAW_SELECTION_BRIDGE.md)
- [Retained-State Mechanism and Field Boundary](RETAINED_STATE_MECHANISM_AND_FIELD_BOUNDARY.md)
- [CAAI Engineering and Verrell’s Law Research Boundary](CAAI_ENGINEERING_AND_VERRELLS_LAW_RESEARCH_BOUNDARY.md)

---

## Minimal Mathematical Spine

For candidate outcome `y_i`, define a candidate score/logit:

```math
z_i = U(y_i; S_t, O_t) + \lambda B(y_i; M_t)
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
\frac{P_0(y_i \mid S_t,O_t)e^{\lambda W(M_t,y_i)}}{\sum_j P_0(y_j \mid S_t,O_t)e^{\lambda W(M_t,y_j)}}
```

These forms are equivalent with `U(y_i;S_t,O_t) = log P_0(y_i | S_t,O_t)` up to an additive constant, and `B = W`.

The baseline condition must be defined before testing. In an engineering test, it may be the same system with retained-state weighting disabled, ablated, randomised, or held neutral.

---

## Falsifiable Claim

Otherwise similar systems with different retained histories should show measurable divergence under matched present input if retained-state weighting is active.

If no repeatable divergence appears under controlled conditions, or if the fitted retained-state influence is indistinguishable from the pre-registered null condition, the claim is not supported in that tested regime.

The correct null wording is:

> refuted in the tested regime.

Not:

> disproven everywhere.

---

## Archive Status

This repository intentionally preserves earlier documents, older mathematical attempts, speculative field-memory notes, and development-stage wording.

Those materials are retained for authorship, provenance, and research-continuity reasons. They should be read in historical context, not treated as the current strongest public position where later documents have narrowed or clarified the framework.

Start here for archive interpretation:

- [Archived Document Status](ARCHIVED_DOCUMENT_STATUS.md)

The v1.2 mathematical reference has been superseded by `VERRELLS_LAW_MATHEMATICAL_REFERENCE_v1.3.md`.

---

## Relationship to Collapse Aware AI

Verrell’s Law and Collapse Aware AI are connected but separate.

```text
Verrell’s Law = retained-state selection research framework
Collapse Aware AI = engineering track for governed retained-state behavioural selection
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

Public materials should not imply that every future WEL capability is already present in the Phase-1 Gold Build Core unless separately demonstrated.

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

**README version:** retained-state hardening pass  
**Date:** 2026-07-04
