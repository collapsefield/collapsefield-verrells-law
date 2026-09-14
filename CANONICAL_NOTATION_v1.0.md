# Verrell’s Law — Canonical Notation v1.0 (Historical Reference)

**Author / originator:** Marcos Verrell Moss Ross (M.R.)  
**Original date:** 11 May 2026  
**Current status:** Superseded supporting reference; preserved for provenance  
**Attribution refresh:** 14 September 2026

---

## Status

This file records an earlier notation system used during development of the retained-state selection framework.

It is retained for authorship and version-history purposes, but it is **not the current primary mathematical authority** where later specifications differ.

Current authority:

- [Mathematical Foundations and Falsification Protocol v1.0](VERRELLS_LAW_MATHEMATICAL_FOUNDATIONS_AND_FALSIFICATION_PROTOCOL_v1.0.md)
- [Empirical Identification Clarification v1.0](VERRELLS_LAW_EMPIRICAL_IDENTIFICATION_CLARIFICATION_v1.0.md)
- [Mathematical Reference v1.3](VERRELLS_LAW_MATHEMATICAL_REFERENCE_v1.3.md)

The original full v1.0 notation remains available in Git history.

---

## Historical mathematical form

An early memory-weighted candidate-selection expression used in the project was:

```math
P(y_i \mid S_t,O_t,M_t)
=\frac{\exp(U(y_i;S_t,O_t)+\lambda B(y_i;M_t))}
{\sum_j \exp(U(y_j;S_t,O_t)+\lambda B(y_j;M_t))}
```

with:

- `y_i` — candidate outcome / action / state;
- `S_t` — present system state;
- `O_t` — present observation / input;
- `M_t` — retained history;
- `U` — present-state utility / baseline term;
- `B` — retained-state bias / compatibility term;
- `λ` — regime-specific coupling under a fixed scoring convention.

The enduring idea is that present-state selection and retained-state influence should be separable enough to compare and test.

---

## Current identifiability boundary

The value of `λ` has no scale-independent meaning unless the retained-state score scale is fixed.

For independent empirical evidence, the rule producing the retained-state compatibility variable must be frozen independently of the confirmatory selection outcome. A selector demonstrating the effect it was deliberately programmed to produce is engineering conformance, not independent confirmation of the wider hypothesis.

---

## Current terminology

**Retained-State Selection** is the controlled study or process by which information preserved from prior states is permitted to influence selection among presently available candidate outcomes.

**Active Information Weight (AIW)** remains a project term for effective retained-information influence, but it should not be mistaken for an independently established physical quantity.

**Weighted Emergence Layering (WEL)** remains an architectural / conceptual term associated with layered retained influence; it is not evidence of a universal physical mechanism.

---

## Attribution

**Marcos Verrell Moss Ross (M.R.)**  
Author / originator of Verrell’s Law

Copyright © 2026 Marcos Verrell Moss Ross (M.R.).
