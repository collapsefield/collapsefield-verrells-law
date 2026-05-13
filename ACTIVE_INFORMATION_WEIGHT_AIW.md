# Active Information Weight (AIW)

**Subtitle:** A Measurement Principle for Retained-Information Influence in Future Selection
**Author:** Marcos Verrell Moss Ross (M.R.)
**Organisation:** Inappropriate Media Limited / Collapse Aware AI
**Status:** Public theory-side provenance note
**First published publicly:** 2026-05-13
**Version:** AIW-PROV-001

---

## 1. Purpose

**Active Information Weight (AIW)** is the Verrell's Law measurement principle for describing how retained prior information can measurably influence future selection probability.

AIW gives a name to the measurable effect of retained informational history when it changes the probability of future outcomes compared with a matched memoryless or differently weighted baseline.

Canonical short definition:

> Active Information Weight is the measurable influence of retained prior information on future selection probability.

---

## 2. Core Claim

Given two systems with the same present input and the same present candidate set, different retained histories may produce different future selection probabilities.

In compact form:

```text
same present input
+ same candidate set
+ different retained information
= different future selection probabilities
```

AIW is the measurable weighting term that captures that difference.

---

## 3. Relationship to Verrell's Law

Verrell's Law proposes that retained information from prior states can bias future state selection.

AIW is the measurement-facing expression of that principle.

```text
Verrell's Law = retained information can bias future selection
AIW = measurable influence of that retained information
WEL = layered mechanism carrying that influence forward
Collapse Aware AI = middleware implementation branch using governed memory-weighted selection
```

AIW therefore sits between theory and measurement.

It does not replace probability theory. It identifies a specific kind of probabilistic influence: retained-information weighting across time.

---

## 4. Public Selection Form

A public-safe selection form is:

$$P(y_i \mid X_t, O_t, M_t) = \frac{\exp(U(y_i; X_t, O_t) + \lambda B(y_i; M_t))}{\sum_j \exp(U(y_j; X_t, O_t) + \lambda B(y_j; M_t))}$$

Where:

- `y_i` = candidate future output, behaviour, state, or selection possibility
- `X_t` = current system/runtime state
- `O_t` = current observation or input
- `M_t` = retained informational history or memory state
- `U(y_i; X_t, O_t)` = present-state utility or base preference
- `B(y_i; M_t)` = retained-information bias term
- `λ` = coupling strength controlling the influence of retained information

AIW is expressed through the measurable contribution of the retained-information bias term to the final selection probability.

---

## 5. Memoryless Baseline

AIW requires comparison against a baseline.

The simplest baseline is a memoryless or zero-coupling condition:

$$\lambda = 0$$

In that case:

$$P_0(y_i \mid X_t, O_t) = \frac{\exp(U(y_i; X_t, O_t))}{\sum_j \exp(U(y_j; X_t, O_t))}$$

This represents selection based on present-state utility alone.

When retained information is active:

$$\lambda > 0$$

selection becomes:

$$P_M(y_i \mid X_t, O_t, M_t) = \frac{\exp(U(y_i; X_t, O_t) + \lambda B(y_i; M_t))}{\sum_j \exp(U(y_j; X_t, O_t) + \lambda B(y_j; M_t))}$$

---

## 6. AIW as Measurable Probability Shift

A simple observable AIW effect can be written as:

$$AIW(y_i) = P_M(y_i \mid X_t, O_t, M_t) - P_0(y_i \mid X_t, O_t)$$

Where:

- `P_M` = memory-weighted selection probability
- `P_0` = memoryless baseline probability
- `AIW(y_i)` = measured probability shift attributable to retained-information weighting

Positive AIW means retained information increased the probability of candidate `y_i`.

Negative AIW means retained information reduced the probability of candidate `y_i`.

Near-zero AIW means retained information had little or no measurable effect under the tested condition.

---

## 7. Comparative AIW Between Two Histories

AIW can also compare two systems with identical present conditions but different retained histories:

$$\Delta P(y_i) = P_A(y_i \mid X_t, O_t, M_t^A) - P_B(y_i \mid X_t, O_t, M_t^B)$$

Where:

- `M_t^A` = retained history of system A
- `M_t^B` = retained history of system B
- `ΔP(y_i)` = divergence in selection probability caused by different retained histories

This is the operational test of path-dependent divergence.

If the present state and input are held constant while the retained history differs, any stable probability divergence becomes candidate evidence for retained-information weighting.

---

## 8. Relationship to Weighted Emergence Layering

AIW and WEL are connected but not identical.

```text
AIW = what is measured
WEL = how retained influence is layered and carried forward
```

WEL may organise retained information into layers such as:

- recency
- salience
- anchors
- recurrence traces
- continuity pressure
- governed persistence

AIW measures whether those retained layers produce a detectable shift in future selection probability.

---

## 9. Relationship to Bias

In this framework, bias means directional weighting.

Bias is not automatically an error.

A retained-information bias can be useful when it improves continuity, stability, recognition, or prediction. It can be harmful when it creates distortion, overfitting, hallucination, false confirmation, or unjustified preference.

AIW is therefore neutral as a measurement principle.

It asks:

```text
How much did retained information shift the selection probability?
```

It does not automatically say the shift was good, bad, true, false, safe, or unsafe.

Those judgements require separate evaluation and governance.

---

## 10. Worked Minimal Example

Assume one candidate `y_i` has present-state utility:

$$U(y_i) = 0.7$$

Memory coupling:

$$\lambda = 0.8$$

Two systems have different retained-information bias values:

$$B_A(y_i; M_t^A) = 0.5$$

$$B_B(y_i; M_t^B) = 0.1$$

The memory-weighted scores become:

$$Score_A = 0.7 + (0.8 \times 0.5) = 1.1$$

$$Score_B = 0.7 + (0.8 \times 0.1) = 0.78$$

Even with the same present utility, the retained histories create different future selection pressure.

The difference is not caused by the present input. It is caused by different retained informational weighting.

---

## 11. Prior-Art Boundary

AIW does not claim to invent:

- probability theory
- softmax functions
- Bayesian updating
- reinforcement learning
- Markov processes
- attention mechanisms
- memory systems
- utility scoring

Those existed before this framework.

The narrower claim is:

> Active Information Weight names and formalises the measurable influence of retained informational history on future selection probability within the Verrell's Law framework.

AIW is a retained-information influence principle, not a replacement for existing mathematical or computational tools.

---

## 12. Public Claim Boundary

This note does not claim that:

- Verrell's Law is established physical law
- consciousness has been proven to collapse physical states
- AI sentience has been created
- the quantum measurement problem has been experimentally solved
- retained information can steer arbitrary outcomes at will
- Collapse Aware AI Crown internals are disclosed
- private production scoring, thresholds, schemas, or implementation details are public

The correct public framing is:

> AIW is a measurable retained-information weighting principle within Verrell's Law, used to describe how prior informational history can alter future selection probability under controlled comparison.

---

## 13. Testing and Measurement Direction

AIW can be tested by comparing matched systems or matched runs where present inputs are held constant and retained histories differ.

A minimal valid AIW test requires at least two matched runs: one with retained history active and one with `λ = 0`, with all other inputs held constant.

Candidate measurements include:

- probability shift against memoryless baseline
- divergence between differently weighted histories
- decay of retained-information influence over time
- reactivation after repeated exposure
- salience-weighted probability change
- continuity signature prediction above baseline

The key requirement is controlled comparison.

Without a baseline, AIW becomes vague. With a baseline, AIW becomes measurable.

---

## 14. Relationship to Collapse Aware AI

Collapse Aware AI provides an applied software testbed for memory-weighted selection.

In public-safe terms:

```text
prior interaction history
→ retained memory weight
→ altered candidate scoring
→ governed selection
→ measurable behavioural divergence
```

AIW describes the measurable influence of retained history.

WEL describes the layered architecture carrying that influence.

The private Crown kernel, production weighting rules, thresholds, schemas, and implementation mechanics remain proprietary and are not disclosed by this note.

---

## 15. Provenance Statement

This document records Active Information Weight (AIW) as a core measurement principle of Verrell's Law, developed by Marcos Verrell Moss Ross (M.R.) through the Verrell's Law / Collapse Aware AI project lineage and Inappropriate Media Limited.

First published publicly as a standalone provenance note: 2026-05-13.

AIW was previously referenced in public Verrell's Law and Collapse Aware AI materials before this standalone note. This file consolidates the definition, notation, measurement role, and claim boundary into one canonical public reference.

---

## 16. Copyright and Use

Copyright © 2026 Marcos Verrell Moss Ross / Inappropriate Media Limited.
All rights reserved unless otherwise stated in the repository license.

This public note is provided for technical provenance, research discussion, and theory/middleware boundary clarification. It does not grant permission to reproduce, commercialise, rebrand, or incorporate the AIW framework into third-party systems without written permission.
