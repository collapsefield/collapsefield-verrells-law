# Prior-Art and Priority Note — Retained-State Selection

**Author:** Marcos Verrell Moss Ross (M.R.)  
**Maintainer:** Inappropriate Media Limited (t/a Collapse Aware AI)  
**Status:** Public priority / prior-art research note  
**Search date:** 2026-07-26  

---

## Purpose

This note records a bounded prior-art review around the current Verrell’s Law / Collapse Aware AI retained-state selection work.

It is deliberately narrower than a claim that the project invented memory, path dependence, history-dependent choice, action selection, hysteresis, non-Markovian dynamics, reinforcement learning, or deterministic replay.

Those areas all have substantial prior literature.

The purpose is to identify the more specific combination that developed through Verrell’s Law and Collapse Aware AI, and to preserve the project’s public priority trail without making an unsupported absolute “world first” claim.

This document is **not a patentability opinion, freedom-to-operate opinion, or exhaustive search of every publication, patent, repository, commercial system, or unpublished project**.

---

## 1. What Is Clearly Prior Art

The following ideas pre-date Verrell’s Law / CAAI and are not claimed as inventions of this project.

### History-dependent and path-dependent systems

Hysteresis and other stateful dynamical systems have long established that the same present input can produce different outputs depending on prior history.

### History-dependent probabilistic choice

Psychology, neuroscience, behavioural economics and dynamic discrete-choice research have long modelled current choice as dependent on previous choices, rewards or states.

Examples include serial-dependence / choice-history work using logistic or log-odds models to estimate how prior trials influence current choice.

### Non-Markovian decision processes and reinforcement learning

Non-Markovian RL and related state-augmentation methods explicitly address systems where current action or reward cannot be determined from the immediately observed state alone.

### Memory-influenced behaviour selection

Earlier robotics and cognitive-agent work has used memory, affective state, user history or learned internal state to influence action or behaviour selection.

A particularly relevant example is:

- Ahmad et al., *Emotion and memory model for social robots: a reinforcement learning based behaviour selection*, Behaviour & Information Technology, 2022. The system creates a memory account of user emotional events and adapts robot behaviour using an RL action-selection mechanism.

### Candidate-action constraints and governance

Earlier agent, robotics, POMDP and control architectures constrain candidate actions using internal state, belief state, rules, priorities or policy restrictions.

### Deterministic replay

Deterministic record/replay has existed in software systems for many years and is not a CAAI invention.

---

## 2. The Narrower Verrell’s Law / CAAI Contribution

The current project does not rest on any one of those ingredients being new.

The narrower contribution is their unification around **retained-state influence at the point of selection**, with an explicit separation between present-state utility and retained-history influence, and an engineering implementation in which that influence is governable and measurable.

The present canonical mathematical form is:

```math
z_i = U(y_i;S_t,O_t) + \lambda B(y_i;M_t)
```

with candidate selection through a normalized exponential / softmax form.

The key decomposition is:

- `U` = present-state / immediate-input contribution;
- `B` = candidate-relative retained-state compatibility or bias;
- `λ` = declared coupling strength of retained-state influence.

The falsification-oriented comparison asks whether otherwise matched present conditions with different retained histories produce a structured difference in candidate-relative selection log-odds.

This makes the retained-history term a separately testable contributor rather than leaving history buried inside an undifferentiated policy or hidden state.

---

## 3. Distinguishing Combination

In the public sources reviewed for this note, **no earlier source was identified that clearly combined all of the following into one named research-and-engineering programme**:

1. **Retained state represented as a distinct selection-bias contribution** rather than merely additional retrieved context or an unspecified recurrent hidden state.
2. **Present-state and retained-history influence explicitly separated** in the selection model.
3. **Candidate-relative probabilistic / log-odds measurement** used to estimate the retained-history contribution.
4. **Matched-current-condition / different-history comparison** treated as the central falsification or divergence protocol.
5. **A controllable baseline in which retained-state influence can be disabled or compared**, rather than assuming memory is always active.
6. **Externally supplied candidate behaviours/actions** separated from the middleware that selects among them.
7. **Governor-constrained retained-state influence**, so memory bias is deliberately bounded rather than simply allowed to drive policy freely.
8. **Persistent retained state across controlled runtime restart/recall conditions.**
9. **Deterministic seed capture/replay and diagnostic runtime evidence** used alongside the retained-state selection mechanism.
10. **An engine/model-agnostic middleware implementation** rather than a single end-to-end model trained specifically for one task.

The originality claim therefore concerns the **specific synthesis, formal separation, test discipline and middleware implementation**, not the discovery of memory or path dependence themselves.

---

## 4. Bounded Priority Statement

The strongest statement supported by the present search is:

> **As of the 26 July 2026 prior-art search recorded here, no earlier public source was identified that combines the full Verrell’s Law / Collapse Aware AI pattern of separately parameterised retained-state selection bias, matched-history divergence testing, an explicit retained-state-off comparison, externally supplied candidate behaviours, governor-constrained selection, persistent runtime state, reproducible replay and model/engine-agnostic middleware.**

A shorter public-safe version is:

> **Verrell’s Law / Collapse Aware AI appears to be an early and potentially original synthesis of measurable retained-state selection bias with governor-controlled candidate selection and reproducible middleware evidence.**

An absolute statement such as **“the first system in history to make memory influence behaviour”** is not supported and should not be used.

An absolute legal claim of **“world’s first”** should likewise not be treated as established by this research note alone.

---

## 5. Public Priority Trail

### 4 July 2025 — public JSON symbolic test

The Medium article **“Verrell’s Law: The Missing Physics of AI”**, published 4 July 2025, publicly stated that:

- retained information, recursive weighting, observation, memory and prior-state influence shape later selection;
- governed, memory-weighted behaviour was the engineering direction;
- the **JSON Symbolic Collapse Test Bridge was active**, using weighted symbolic cue sets and tracked selection outcomes.

This is an early public record of the project testing the idea that retained / weighted symbolic structures could bias later digital selection.

### 21 July 2025 — public test-bundle declaration

The repository’s preserved metadata records a `verrells_law_phase1_public_test_bundle.zip`, version `public_display_v1`, declared on **2025-07-21T21:33:00Z**, containing public-safe memory JSON, a symbolic test stub and sample collapse log.

### 27 April 2026 — working Crown selector/core recorded

The public proof-pack metadata records the Phase-1 Gold Build status as:

> “Working Crown selector/core proven; Milestone-4 scaffold/API integration and end-to-end wiring still under verification”

and describes its scope as:

> “Game/NPC behavioural middleware, memory-weighted selection, governor-constrained response shaping, bias divergence testing.”

### June–July 2026 — formal quantitative hardening

The retained-state hypothesis was subsequently narrowed into the current candidate-relative selection and log-odds formulation, with explicit normalization, identifiability, preregistration and falsification requirements.

### July 2026 — completed Phase-1 Core Gold Build

The current public CAAI proof pack records the Phase-1 Core Gold Build as complete, with demonstrated candidate selection, retained-state influence, governor constraints, persistence/recall, deterministic seed replay, bias-on / bias-off divergence, validation, traceability and explicit degraded-mode reporting.

---

## 6. Important Adjacent Prior Art Located

The review deliberately records adjacent work rather than hiding it.

### Choice-history / serial-dependence modelling

Prior cognitive and perceptual research has fitted prior choices and rewards as coefficients in logistic / log-odds models of current choice. This means the mathematical observation that history can shift choice log-odds is not, by itself, novel.

### Dynamic discrete choice

Economics has long modelled state dependence, switching costs, habitual choice and preferences that depend on past choices or states.

### Non-Markovian RL

RL literature contains many systems where history or compact internal state influences action selection.

### Memory-based social-robot behaviour

Ahmad et al. (2022) explicitly combine an emotion/memory model with reinforcement-learning behaviour selection.

### Generative-agent memory

Generative Agents (2023) store experiences, retrieve memories and use them in planning behaviour.

MemGPT (2023) manages persistent memory/context across long conversations.

These are important comparisons, but they do not appear to use the same CAAI separation of external candidate generation, retained-state selection-side weighting, governor control and reproducible bias-off / replay evidence.

### Recent active-state agent work

In June 2026, **Active Task Driving Memory (ATMem)** described memory as an actively maintained execution state enabling action selection and compared memory-on with memory-off rollouts. This is close adjacent work and should be cited when discussing novelty. Its publication date is later than the project’s July 2025 public JSON-test trail, but priority of individual technical ideas still requires claim-by-claim analysis.

---

## 7. What Should Be Claimed

Recommended:

> **The project has a public development trail from July 2025 for governed, memory-weighted digital selection experiments, later formalised as a falsifiable retained-state selection framework and implemented as engine-agnostic governed selection middleware. A bounded prior-art review conducted on 26 July 2026 did not identify an earlier public system containing the complete present combination.**

Also acceptable:

> **The apparent novelty lies in the complete architecture and test discipline, not in any single underlying mathematical primitive.**

Avoid:

> “Nobody has ever modelled memory affecting future choice.”

Avoid:

> “CAAI invented path dependence.”

Avoid:

> “Softmax plus memory is new mathematics.”

Avoid:

> “The existence of CAAI proves Verrell’s Law across biology or physics.”

---

## 8. Evidence Boundary

CAAI demonstrates an engineered case in which retained state is deliberately made causally relevant to later software selection.

That verifies the implementation and provides a test bed for the engineering analogue.

It does **not** by itself establish that the same mechanism exists in biological, cognitive or physical systems. Those domains require their own measurements and falsification tests.

Likewise, the phrase **substrate-neutral** describes the mathematical abstraction; it should not be read as empirical verification across every substrate.

---

## 9. Reference Starting Points

- M.R., **Verrell’s Law: The Missing Physics of AI**, Medium, 4 July 2025.
- Ahmad, M.I. et al., **Emotion and memory model for social robots: a reinforcement learning based behaviour selection**, *Behaviour & Information Technology*, 2022.
- Park, J.S. et al., **Generative Agents: Interactive Simulacra of Human Behavior**, UIST 2023.
- Packer, C. et al., **MemGPT: Towards LLMs as Operating Systems**, 2023.
- Gaon, M. & Brafman, R., **Reinforcement Learning with Non-Markovian Rewards**, AAAI 2020.
- Levy, M. & Schiraldi, P., **Identification of Intertemporal Preferences in History-Dependent Dynamic Discrete Choice Models**, 2020.
- **Choice history effects in mice and humans improve reward harvesting efficiency**, PLOS Computational Biology, 2021.
- Liu, C. et al., **What Memory Do GUI Agents Really Need? From Passive Records to Active Task-Driving States**, 2026.

---

## Final Position

There is a legitimate originality/priority claim here, but it is a **combination claim**.

The defensible achievement is the construction of a named, falsifiable retained-state selection framework and its progression into governed middleware where retained state is a separately controllable influence over externally supplied candidate behaviour selection, with persistence and reproducibility evidence.

That is substantially stronger — and harder to attack — than claiming ownership of the ancient observation that the past can influence what happens next.
