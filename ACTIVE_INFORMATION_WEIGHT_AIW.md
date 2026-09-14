# Active Information Weight (AIW)

**Subtitle:** A Measurement Principle for Retained-Information Influence in Future Selection  
**Author / originator:** Marcos Verrell Moss Ross (M.R.)  
**Status:** Public research / terminology note  
**First published publicly:** 13 May 2026  
**Updated:** 14 September 2026

---

## Definition

**Active Information Weight (AIW)** is a project term for the effective measurable influence that retained prior information exerts on later selection within a declared test context.

Short form:

> **Stored information is not automatically active. It becomes active, in this sense, when it measurably changes later selection.**

AIW is not presented as a new fundamental physical quantity and does not replace established probability, statistics, learning or control theory.

---

## Core test pattern

```text
same present condition
+ same candidate set
+ different retained history
→ test for measurable selection difference
```

A second comparison disables or removes the retained-state contribution to establish a reference condition.

The current framework therefore treats AIW as a measurement-facing description of retained-state influence, not as proof that a particular storage mechanism or physical carrier exists.

---

## Mathematical context

An illustrative candidate-selection form is:

```math
P(y_i \mid S_t,O_t,M_t)
=\frac{\exp(U(y_i;S_t,O_t)+\lambda B(y_i;M_t))}
{\sum_j \exp(U(y_j;S_t,O_t)+\lambda B(y_j;M_t))}
```

where:

- `U` represents the present-state / baseline contribution;
- `B` represents a retained-state compatibility or bias term;
- `λ` represents coupling under a declared scoring convention.

The later canonical retained-state specification focuses on candidate-relative log-odds and independently frozen retained-state measures. The value of `λ` has no scale-independent meaning unless the retained-state score scale is fixed.

---

## Baseline and divergence

A simple descriptive comparison can be written as:

```math
AIW(y_i)=P_M(y_i)-P_0(y_i)
```

where `P_M` is a retained-history condition and `P_0` is a declared reference condition.

For two histories:

```math
\Delta P(y_i)=P_A(y_i)-P_B(y_i)
```

These quantities are useful descriptions of observed selection change. They do not by themselves identify causality. Stronger evidence requires controlled history preparation, held-out prediction and intervention / ablation.

---

## Relationship to current terminology

```text
Retained-State Selection
= technical process / test category

AIW
= project term for effective retained-information influence

WEL
= project term for layered organisation of retained influence

Collapse Aware AI™
= separate engineering programme for governed retained-state selection
```

Engineering behaviour does not establish a universal physical law.

---

## Evidence boundary

AIW does **not** establish that:

- Verrell's Law is confirmed as a natural law;
- consciousness causes physical collapse;
- AI systems are conscious;
- retained information uses a universal electromagnetic carrier;
- a private software score is automatically an independent empirical variable.

For independent empirical evidence, the retained-state variable and analysis route must be identified independently of the confirmatory outcome or otherwise preregistered in a way that prevents circular confirmation.

---

## Current references

For the current mathematical and empirical-identification rules, use:

- [Mathematical Foundations and Falsification Protocol v1.0](VERRELLS_LAW_MATHEMATICAL_FOUNDATIONS_AND_FALSIFICATION_PROTOCOL_v1.0.md)
- [Empirical Identification Clarification v1.0](VERRELLS_LAW_EMPIRICAL_IDENTIFICATION_CLARIFICATION_v1.0.md)
- [Retained-State Selection Framework](RETAINED_STATE_SELECTION_FRAMEWORK.md)

---

## Attribution

Active Information Weight (AIW) is retained as terminology within the Verrell's Law research and associated engineering lineage.

**Marcos Verrell Moss Ross (M.R.)**  
Author / originator

Copyright © 2026 Marcos Verrell Moss Ross (M.R.).
