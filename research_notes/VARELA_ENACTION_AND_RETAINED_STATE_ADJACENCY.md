# Francisco Varela, Enaction, and Retained-State Selection

**Status:** Conceptual adjacency note — non-canonical, non-evidential  
**Date:** 2026-08-27  
**Author:** Marcos Verrell Moss Ross (M.R.) / Inappropriate Media Limited  
**Repository:** `collapsefield/collapsefield-verrells-law`

---

## Purpose

This note records a useful conceptual adjacency between Francisco Varela’s work on autopoiesis and enactive cognition, Verrell’s Law, and Collapse Aware AI (CAAI).

It is not presented as evidence that Varela anticipated Verrell’s Law, endorsed CAAI, or supplied the mathematical basis of the framework. The relationship is narrower: both bodies of work treat system history, ongoing interaction, and internal organisation as relevant to what a system can do next.

The comparison is useful precisely because the differences are as important as the similarities.

---

## The Shared Intuition

A purely stateless description treats a system as though the present input alone determines the next outcome.

The enactive tradition associated with Varela instead emphasises that cognition is shaped through ongoing interaction between an organised system and its environment. A system does not simply receive neutral inputs; its present organisation reflects a history of prior coupling.

Verrell’s Law makes a narrower, explicitly testable retained-state claim:

> Prior interactions can leave persistent state changes. Those retained changes can bias future selection, producing path-dependent divergence under matched present input.

Its shortest public spine is:

```text
Memory shapes weighting.
Weighting shapes selection.
Selection shapes what follows.
```

This creates a meaningful conceptual bridge: **history is not merely background; retained history can become part of the operative state from which later selection occurs.**

---

## Where the Ideas Converge

### 1. History matters to present behaviour

In an enactive view, an organism’s present relationship to its environment depends on the structure and organisation produced through earlier interactions.

Verrell’s Law isolates a measurable version of that intuition. It asks whether different retained histories produce reproducible divergence when present input and declared system variables are held matched.

The canonical chain is:

```text
Observation / interaction
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

The important common ground is therefore **history-conditioned behaviour**, not any claim about a shared physical substrate.

### 2. Cognition is not well described as isolated input/output mapping

Enactive cognition places emphasis on ongoing interaction, organisation, and sense-making rather than treating cognition as a detached sequence of stimulus-response events.

Verrell’s Law similarly rejects the assumption that two apparently identical present inputs must imply identical effective selection conditions if the underlying retained state differs.

The law does not claim that all systems are enactive. It proposes that where retained state exists and participates in selection, present-input-only descriptions may be incomplete.

### 3. Current state is historically constructed

A system’s current organisation can encode the consequences of prior interaction.

That idea is central to the retained-state framing. Verrell’s Law does not require a universal memory field or a non-local store. Retained information can exist in whatever measurable substrate preserves history long enough to influence later selection: biological structure, software state, environmental traces, network configuration, or another experimentally identified mechanism.

The foundation is retained state, not field memory.

### 4. Adaptation can be understood through structured continuity

Enactive approaches emphasise that meaningful behaviour emerges through continuing interaction rather than from a single isolated computation.

CAAI explores an engineering analogue: a runtime can preserve selected historical information and govern how that retained state influences later behaviour, producing continuity without modifying the underlying model weights.

That is an engineering result, not evidence that artificial agents are living, autopoietic, conscious, or biologically equivalent.

---

## Where Verrell’s Law Becomes More Specific

The conceptual overlap stops before the central mathematical claim.

Verrell’s Law is not merely the statement that history affects behaviour. Its current canonical hypothesis predicts a particular quantitative structure between retained-state compatibility and selection change within a declared test regime.

At first order:

```math
\Delta L_k = \alpha + \lambda \Delta R_k + \varepsilon_k
```

where:

- `ΔL` is the change in candidate-relative selection log-odds;
- `ΔR` is a preregistered, normalized retained-state compatibility difference;
- `λ > 0` is the retained-state coupling within the tested regime;
- `α ≈ 0` is a control diagnostic;
- residual error must not systematically track `ΔR`.

The canonical specification further requires preregistration, declared normalization, controls, held-out prediction, falsification conditions, and an empirical-identification boundary.

Those commitments are specific to Verrell’s Law. They should not be attributed to Varela or to enactivism generally.

Canonical reference:

[Verrell’s Law — Mathematical Foundations and Falsification Protocol, Canonical Specification v1.0](../VERRELLS_LAW_MATHEMATICAL_FOUNDATIONS_AND_FALSIFICATION_PROTOCOL_v1.0.md)

Empirical-identification companion:

[Verrell’s Law — Empirical Identification Clarification v1.0](../VERRELLS_LAW_EMPIRICAL_IDENTIFICATION_CLARIFICATION_v1.0.md)

---

## Collapse Aware AI: The Engineering Adjacency

Collapse Aware AI is proprietary middleware for governed retained-state behavioural selection.

It does not implement autopoiesis and it does not claim to reproduce Varela’s theory of cognition.

The useful comparison is narrower:

```text
Prior interaction
      ↓
Retained state
      ↓
Current interpretation / candidate formation
      ↓
Governed weighting
      ↓
Final behavioural selection
      ↓
New retained consequences
```

CAAI turns history dependence into an inspectable engineering problem.

The runtime question is:

> Can retained state influence later behavioural selection in a governed, measurable and bounded way without retraining the underlying model?

That produces several practical consequences relevant to agent and NPC systems:

- continuity can persist across interactions;
- previously important events can remain behaviourally relevant;
- current decisions can depend on more than the immediately visible prompt;
- retained influence can be enabled, constrained, inspected, ablated or compared;
- final selection authority can remain outside the underlying model;
- the behaviour of the system can diverge because its retained history differs, even when present input is matched.

This is where the conceptual adjacency becomes commercially useful: **history-conditioned behaviour is not left as a philosophical description; it becomes a governed runtime capability.**

---

## What This Comparison Does Not Claim

This note does **not** claim that:

- Francisco Varela formulated Verrell’s Law;
- enactivism proves retained-state selection;
- Varela’s work validates CAAI;
- CAAI is autopoietic;
- CAAI is conscious or alive;
- the brain or an AI system is merely a receiver or tuning device;
- memory requires a non-local electromagnetic field;
- quantum collapse is required by either Verrell’s Law or CAAI;
- conceptual similarity constitutes empirical evidence.

The comparison is intellectual adjacency, not evidential inheritance.

---

## Why the Adjacency Matters

The significance of the comparison is that Verrell’s Law and CAAI sit within a broader family of attempts to move beyond purely stateless descriptions of cognition and behaviour.

Varela’s work helped establish that the organisation and history of an interacting system can matter to cognition and sense-making.

Verrell’s Law asks a different and more operational question:

> **Can the effect of retained history on later selection be defined, measured, preregistered and falsified?**

Collapse Aware AI asks the corresponding engineering question:

> **Can such retained-state influence be deliberately governed inside a runtime so that behavioural continuity is useful, bounded and inspectable?**

Those are not the same project as enactivism, but they occupy an intellectually compatible neighbourhood.

---

## Public Summary

A concise public description is:

> Francisco Varela’s enactive work and Verrell’s Law share an interest in history-conditioned systems: present behaviour is shaped by an organisation that has itself been formed through prior interaction. Verrell’s Law narrows that intuition into a falsifiable retained-state selection hypothesis, while Collapse Aware AI implements a governed engineering analogue in which retained state can measurably influence later behavioural selection without retraining the underlying model.

That is the appropriate level of connection: clear enough to be useful, narrow enough to remain defensible.

---

## Status Boundary

This document is a **conceptual research note**.

It does not modify the canonical mathematics, establish empirical support, or elevate enactivism into a required foundation of Verrell’s Law.

Where any wording in this note conflicts with the canonical mathematical specification or empirical-identification clarification, the canonical documents govern.
