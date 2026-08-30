# Retained-State Selection — Category and Terminology Note v1.0

**Status:** Public positioning / terminology note  
**Date:** 30 August 2026  
**Author:** Marcos Verrell Moss Ross (M.R.) / Inappropriate Media Limited  
**Canonical status:** Non-canonical companion note. This file does **not** replace or modify the canonical Verrell’s Law mathematical specification.

---

## Purpose

This note defines a stable public vocabulary around **retained-state selection** without claiming invention of memory, state, path dependence, softmax, reinforcement learning, policy engines, hysteresis, retrieval, or other established mechanisms.

The aim is to make one narrower problem explicit:

> **How can information preserved from prior states be allowed to influence selection among presently available outcomes in a way that is measurable, bounded, testable and — in engineered systems — governable?**

That is the territory described here as **retained-state selection**.

---

## Working Definition

> **Retained-State Selection is the controlled study or process by which information preserved from prior states is permitted to influence selection among presently available candidate outcomes.**

The definition is intentionally substrate-neutral.

A retained state may be implemented through:

- software state;
- persistent records;
- learned parameters;
- neural or biological state;
- institutional precedent;
- physical configuration;
- environmental traces;
- another measurable persistence mechanism.

The existence of retained state alone is not the claim. The measurable question is what that retained state is allowed to **change at selection time**.

---

## Terminology Hierarchy

The following hierarchy should be used consistently across public Verrell’s Law and Collapse Aware AI material.

### Retained state

A broad pre-existing concept: information or state that persists across a meaningful boundary and can later be available to a system.

No originality claim is made over the general concept of retained state.

### Retained-State Selection

The category-level term used here for the explicit relationship:

```text
prior state
→ retained information
→ candidate-relative influence
→ selection
→ path-dependent consequence
```

The distinctive research emphasis is not storage by itself but **measurable influence over later selection**.

### Verrell’s Law

A proposed falsifiable research framework that asks whether retained-state compatibility predicts structured, directional changes in later selection under controlled conditions.

The canonical mathematical and falsification claims remain defined by the separate canonical specification.

### Governed Retained-State Selection

An engineering class in which retained-state influence is not automatic authority.

The system keeps a declared candidate or action boundary, applies retained-state influence under explicit rules, and preserves an independent selection/governance boundary.

### Collapse Aware AI (CAAI)

The proprietary engineering programme developed by Inappropriate Media Limited.

CAAI is one implementation track for **governed retained-state behavioural selection**. Its commercial value does not depend on Verrell’s Law being established as a law of nature.

---

## What Is Not Being Claimed

This note does not claim that Verrell’s Law or CAAI invented:

- stateful computation;
- memory systems;
- context windows;
- RAG;
- vector databases;
- long-term agent memory;
- Markov or semi-Markov state;
- hysteresis;
- Bayesian updating;
- reinforcement learning;
- candidate reranking;
- policy engines;
- action verification;
- deterministic execution controls;
- provenance or audit logs.

Those are established or independently developing areas.

The narrower contribution is the explicit framing of **retained history as a candidate-relative influence that can be isolated, ablated, measured and governed at selection time**.

---

## Independent Convergence — Adjacent, Not Validation

Several independent research directions now occupy neighbouring parts of this problem space.

These examples are useful because they show that history-conditioned selection, runtime authority and selective memory are becoming concrete engineering concerns. They do **not** prove Verrell’s Law and they do not establish that CAAI is the only implementation of related ideas.

### HAVE — History-Aware VErifier, CoRL 2025

Li et al. separate action generation from a history-aware verifier: a generator proposes multiple candidate robot actions and a verifier reasons over previous interactions to select the most promising candidate.

Reference: https://proceedings.mlr.press/v305/li25e.html

**Convergence:** multiple candidates + historical interaction context + downstream selection.

**Difference in scope:** robotics/action-quality verification rather than a general governed retained-state middleware architecture.

### Runtime Governance for AI Agents: Policies on Paths, 2026

Kaptein, Khan and Podstavnychy formalise runtime policy as a deterministic function of agent identity, partial execution path, proposed next action and organisational state.

Reference: https://arxiv.org/abs/2603.16586

**Convergence:** history/path matters at runtime and governance should evaluate proposed actions before execution.

**Difference in scope:** policy/compliance evaluation rather than an explicit retained-state candidate-selection framework.

### Aegis — Runtime Governance for Agentic AI, 2026

Aegis treats model outputs as action proposals and places final authority in a trusted runtime decision layer with provenance and fail-closed execution.

Reference: https://arxiv.org/abs/2608.16891

**Convergence:** model proposes; external runtime decides.

**Difference in scope:** action-boundary security/governance rather than retained-state weighting over a candidate set.

### Five Primitives for Governing Autonomous AI Agents at Runtime, 2026

Oswal and Cadeddu describe runtime mediation, per-tenant action vocabularies and evidence/attestation for agent actions.

Reference: https://arxiv.org/abs/2608.26696

**Convergence:** bounded action vocabulary + runtime mediation + durable evidence.

**Difference in scope:** runtime governance primitives rather than history-conditioned candidate-relative retained-state selection.

### Weighted Memory Tree, 2026

Dao, Kathalkar and Eaton introduce dynamic retention scores, folding and suppression for long-horizon agent memory. Their reported experiments show higher accuracy and lower prompt-token usage than linear history on their tested benchmarks.

Reference: https://arxiv.org/abs/2608.20631

**Convergence:** not all retained history should remain equally active; retention itself can be weighted and lifecycle-controlled.

**Difference in scope:** active-memory management and prompt construction rather than final governed action selection.

---

## Why the Category Is Useful

Modern systems increasingly separate three questions that are often collapsed together:

1. **What can be remembered?**
2. **What should be retrieved or remain active?**
3. **What should retained information be allowed to change?**

Retained-State Selection is primarily about the third question.

That makes the category relevant to:

- long-running AI agents;
- customer-service and voice systems;
- game/NPC behaviour;
- adaptive training and simulation;
- fraud / AML / risk intervention selection;
- regulated workflow automation;
- robotics;
- human-in-the-loop systems;
- institutional and legal path-dependence as an analytical model;
- biological or physical systems only where measurable variables and independent tests can be defined.

---

## Minimum Empirical Question

For a candidate outcome `y_i`, present conditions should be declared and held sufficiently matched while retained history is deliberately varied, ablated, randomised or otherwise controlled.

The minimum question is:

> **Does the declared retained-state difference predict a repeatable, directional change in candidate-relative selection beyond the matched present-state baseline?**

The canonical Verrell’s Law specification defines the stronger quantitative version of this question.

---

## Evidence Labels

Public discussion should distinguish at least four evidence classes.

### 1. Conceptual / mathematical framing

A coherent formal model or worked example.

This establishes testability, not truth.

### 2. Engineering conformance

A deliberately built selector behaves according to its declared retained-state mechanism.

This establishes implementation behaviour, not an independent law of nature.

### 3. Independent empirical support

A retained-state variable or preregistered proxy predicts later selection without being mechanically defined by the same selector that produces the outcome.

### 4. Cross-domain generalisation

Independent replication across materially different systems using separately defensible measurements.

No lower evidence class should be described as if it automatically establishes a higher one.

---

## Search / Naming Position

As of 30 August 2026, targeted public-web searches for the exact phrase **“retained-state selection”** return Verrell’s Law / CAAI material prominently and do not reveal an already-established external technical category using the exact phrase in the same sense.

That observation is a **search-position finding, not a novelty or exclusivity proof**.

Prior art may exist under different terminology, in patents, private systems, non-indexed literature or adjacent fields.

The sensible public position is therefore:

> **Use and define the category clearly; do not claim ownership of all stateful or history-conditioned computation.**

---

## Category Boundary in One Sentence

> **Memory answers what can persist; retained-state selection asks what that persistence is allowed to change when a later choice is made.**

---

## Canonical References

- [Verrell’s Law — Mathematical Foundations and Falsification Protocol v1.0](VERRELLS_LAW_MATHEMATICAL_FOUNDATIONS_AND_FALSIFICATION_PROTOCOL_v1.0.md)
- [Empirical Identification Clarification v1.0](VERRELLS_LAW_EMPIRICAL_IDENTIFICATION_CLARIFICATION_v1.0.md)
- [Retained-State Selection Framework](RETAINED_STATE_SELECTION_FRAMEWORK.md)
- [CAAI Engineering and Verrell’s Law Research Boundary](CAAI_ENGINEERING_AND_VERRELLS_LAW_RESEARCH_BOUNDARY.md)
- [Memory-Weighted Selection engineering paper](https://github.com/collapsefield/memory-weighted-selection)
- [CAAI Public Proof Pack](https://github.com/collapsefield/collapse-aware-ai-public-proof-pack)

---

**Version:** v1.0  
**Date:** 30 August 2026  
**Role:** terminology/category hardening and cross-field positioning; non-canonical companion note.
