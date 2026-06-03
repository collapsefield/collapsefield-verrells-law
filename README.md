# Verrell’s Law — Official GitHub Archive

**Author:** Marcos Verrell Moss Ross (M.R.)  
**Maintainer:** Inappropriate Media Limited (t/a Collapse Aware AI)  
**Repository role:** Public theory archive, authorship record, research index, experimental archive, and clarification layer for Verrell’s Law.

---

## Overview

**Verrell’s Law** is a testable research framework proposing that the evolution of systems — biological, cognitive, physical, computational, and artificial — may be influenced not only by present conditions and inputs, but also by retained information from prior states.

In this framework, observation is treated as the entry point through which information enters a system. Retained information can then function as a bias term in selection dynamics: memory can weight future probabilities, shape behavioural selection, and produce path-dependent divergence between systems that otherwise share the same present-state inputs.

The core chain is:

```text
Observation → Information → Memory → Weighting → Bias → Selection → Outcome
```

Within this framework, **bias** means directional weighting, not automatically error. Observation does not have to mean mystical consciousness; it can mean measurement, interaction, attention, input, or state update depending on the system being discussed.

---

## Current Public Position

Verrell’s Law is **not presented as established physics**.

It is presented as a falsifiable memory-weighted selection framework with computational analogues, engineering implementations, and proposed physical tests.

**Collapse Aware AI should be evaluated as engineering.**  
**Verrell’s Law should be evaluated as research.**

This separation is deliberate. Collapse Aware AI does not depend on Verrell’s Law being proven as physics. It is an engineering application of memory-weighted behavioural control, continuity, governor logic, and drift reduction.

---

## Mathematical Reference v1.2

The latest public mathematical reference defines the current notation and falsifiability spine of the framework:

- Canonical Selection Equation
- Weighted Emergence Layering (WEL)
- Active Information Weight (AIW)
- Memory-Bias Decay
- Path-Dependent Divergence
- λ Recovery and Falsifiability
- Claim boundaries: no-signalling, reduction, prior art, and research status

Start here for the current mathematical framing:

- [Verrell’s Law — Mathematical Reference v1.2](VERRELLS_LAW_MATHEMATICAL_REFERENCE_v1.2.md)
- [Canonical Notation v1.0](CANONICAL_NOTATION_v1.0.md)
- [Active Information Weight (AIW)](ACTIVE_INFORMATION_WEIGHT_AIW.md)
- [WEL as Verrell’s Law Selection Bridge](WEL_AS_VERRELLS_LAW_SELECTION_BRIDGE.md)

Core selection equation:

$$
P(y_i \mid S_t, O_t, M_t) =
\frac{\exp\!\left( U(y_i; S_t, O_t) + \lambda\, B(y_i; M_t) \right)}
{\sum_j \exp\!\left( U(y_j; S_t, O_t) + \lambda\, B(y_j; M_t) \right)}
$$

Where \(B(y_i; M_t)\) is the **memory-derived bias term; encodes Active Information Weight (AIW)**.

The central falsifiable claim is that otherwise identical systems with different retained histories can diverge in future selection probability:

$$
\Delta P(y_i) \propto \lambda \cdot \left[B(y_i; M_t^A)-B(y_i; M_t^B)\right]
$$

If no repeatable divergence is observed when \(\Delta B \ne 0\), the AIW claim fails in that regime.

---

## New Readers

Start here first:

- [Public Reader Start Here](PUBLIC_READER_START_HERE.md)
- [CAAI Engineering and Verrell’s Law Research Boundary](CAAI_ENGINEERING_AND_VERRELLS_LAW_RESEARCH_BOUNDARY.md)
- [What We Know vs What We Are Investigating](WHAT_WE_KNOW_VS_WHAT_WE_ARE_INVESTIGATING.md)
- [Common Criticisms and Responses](COMMON_CRITICISMS_AND_RESPONSES.md)
- [Information, Memory, Weighting and Bias](INFORMATION_MEMORY_WEIGHTING_AND_BIAS.md)
- [WEL as Verrell’s Law Selection Bridge](WEL_AS_VERRELLS_LAW_SELECTION_BRIDGE.md)

---

## Key Documents

### Core notation and mathematical framing

- [Verrell’s Law — Mathematical Reference v1.2](VERRELLS_LAW_MATHEMATICAL_REFERENCE_v1.2.md)
- [Canonical Notation v1.0](CANONICAL_NOTATION_v1.0.md)
- [Verrell’s Law Core Mathematical Scaffold](verrells-law-core-mathematical-scaffold.md)
- [Updated Math Renders](UPDATED_MATH_RENDERS.md)

### Conceptual and research boundary documents

- [CAAI Engineering and Verrell’s Law Research Boundary](CAAI_ENGINEERING_AND_VERRELLS_LAW_RESEARCH_BOUNDARY.md)
- [What We Know vs What We Are Investigating](WHAT_WE_KNOW_VS_WHAT_WE_ARE_INVESTIGATING.md)
- [Common Criticisms and Responses](COMMON_CRITICISMS_AND_RESPONSES.md)
- [Information, Memory, Weighting and Bias](INFORMATION_MEMORY_WEIGHTING_AND_BIAS.md)
- [Verrell’s Law Position on Memory Storage](VERRELLS_LAW_POSITION_ON_MEMORY_STORAGE.md)

### Active Information Weight and WEL

- [Active Information Weight (AIW)](ACTIVE_INFORMATION_WEIGHT_AIW.md)
- [WEL as Verrell’s Law Selection Bridge](WEL_AS_VERRELLS_LAW_SELECTION_BRIDGE.md)
- [Memory Tuning and Distributed Retrieval](MEMORY_TUNING_AND_DISTRIBUTED_RETRIEVAL.md)

### Testing, validation, and experimental material

- [Verrell Law Test Protocols Phase 1 v1.0](Verrell_Law_Test_Protocols_Phase_1_v1.0.md)
- [Memory-Biased Collapse Measurement Problem](MEMORY_BIASED_COLLAPSE_MEASUREMENT_PROBLEM.md)
- [VL Optics Experiment Note v1](VL-Optics-Experiment-Note_v1.md)
- [VL Optics Experiment Note v1.1](VL-Optics-Experiment-Note_v1.1.md)

### Authorship, provenance, and priority record

- [Provenance](PROVENANCE.md)
- [Provenance and Priority Position](PROVENANCE_AND_PRIORITY_POSITION.md)
- [Prior Art and Authorship Position](PRIOR_ART_AND_AUTHORSHIP_POSITION.md)
- [IP Notice](IP_NOTICE.md)

---

## Weighted Emergence Layering (WEL)

**Weighted Emergence Layering (WEL)** is the public bridge between Verrell’s Law and Collapse Aware AI.

WEL describes how retained information becomes structured influence over future selection without requiring retraining of the underlying system. In Verrell’s Law, WEL is a research-stage selection framework. In Collapse Aware AI, it becomes an engineering principle for continuity, memory weighting, governor-mediated selection, and drift control.

WEL is retained as a core concept.

---

## Active Information Weight (AIW)

**Active Information Weight (AIW)** is the measurable influence of retained prior information on future selection probability.

In the current notation, AIW is encoded through the memory-derived bias term:

$$
B(y_i; M_t)
$$

The framework does not claim that softmax, Bayesian updating, reinforcement learning, or Markov processes are new inventions. The narrower claim is that retained informational history can be treated as an active, measurable probabilistic weighting on future selection, producing path-dependent divergence.

---

## Claim Boundaries

This repository uses explicit claim boundaries:

- **No-signalling:** any physical application requires local evaluation of the bias term.
- **Reduction:** the model must recover memoryless statistics at \(\lambda = 0\).
- **Prior art:** existing statistical and machine-learning methods are acknowledged.
- **Status:** λ, WEL decomposition, and memory-bias decay are testable hypotheses.

The public materials are intended to clarify what is being claimed, what is being tested, what remains speculative, and what belongs to engineering rather than physics.

---

## Repository Role

This repository is the public theory archive for Verrell’s Law. It should be read alongside the public Collapse Aware AI proof materials, but should not be confused with them.

Collapse Aware AI is the engineering track. Verrell’s Law is the research framework.

---

## Copyright and Notice

Copyright © Marcos Verrell Moss Ross (M.R.) / Inappropriate Media Limited.

Protected under Verrell-Solace Sovereignty Protocol. Intellectual and emergent rights reserved.