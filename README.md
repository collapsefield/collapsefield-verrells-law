<div align="center">

# Verrell’s Law

### A Retained-State Selection Framework

**Memory shapes weighting. Weighting shapes selection. Selection shapes what follows.**

[**Read the foundations**](VERRELLS_LAW_MATHEMATICAL_FOUNDATIONS_AND_FALSIFICATION_PROTOCOL_v1.0.md) · [**2027 research roadmap**](2027_EXPERIMENTAL_RESEARCH_ROADMAP.md) · [**Historical document status**](ARCHIVED_DOCUMENT_STATUS.md)

</div>

---

**Research proposition:** Prior interactions may leave persistent state changes. Under matched present inputs, those retained differences may influence later weighting and selection. The aim is to make that influence measurable, falsifiable and distinguishable from established models.

**Formal starting point:** For fixed candidate sets, finite scores and common positive support, the exponential-tilt model gives an exact pairwise log-odds identity:

`Δ log-odds(a,b) = λ [R(a) − R(b)]`

This is an identity *within the model*, not by itself an empirical discovery. The next test is to fix retained-history scores independently, then evaluate predictions on unseen data against strong alternatives.

**Research route:** [Public reader guide](PUBLIC_READER_START_HERE.md) · [Current research status](VERRELLS_LAW_RESEARCH_STATUS_AND_TESTING_2026-11.md) · [Website](https://www.verrellslaw.org/)

**Scientific correspondence:** [hello@verrellslaw.org](mailto:hello@verrellslaw.org)

**Separate engineering track:** [Collapse Aware AI public proof pack](https://github.com/collapsefield/collapse-aware-ai-public-proof-pack). Commercial software behaviour is assessed independently of this research.

---

## Working framework status

Verrell’s Law develops a testable mathematical framework for how retained history may influence subsequent selection. The archive documents its evolving formulation, research results, experimental programme and original development record.

---

## Current research position

Verrell’s Law is presently framed around **retained-state selection**:

> **When present conditions are held equivalent, can different retained histories produce a measurable, directional and intervention-sensitive difference in what is selected next?**

The research contribution is a specific, testable formulation: retained history enters selection through a declared variable, measured against matched present-state conditions and examined through intervention, ablation and comparison with established history-sensitive models.

A null result is evidence about the tested regime. Measurement limits may matter to experimental design, but lack of detection is not evidence that an undetected mechanism exists.

---

## September 2026 technical edition

### [Verrell’s Law — A Framework for Non-Markovian Information Paths](VERRELLS_LAW_NON_MARKOVIAN_INFORMATION_PATHS_TECHNICAL_EDITION_2026-09.md)

This physics-facing edition develops a separate, stricter formulation using information thermodynamics, generalized open-system memory kernels and intervention-sensitive history tests.

**Research status:** Theoretical model and proposed experimental programme.

The distinctive physical question is not whether non-Markovian memory exists. It is whether a **predeclared weighting variable** identifies an additional, reproducible history-dependent contribution beyond the best conventional model.

Established non-Markovianity is therefore the baseline to beat, not evidence to count twice.

### [Recent Non-Markovian Research Alignment — 14 September 2026](2026-09-14_RECENT_NON_MARKOVIAN_RESEARCH_ALIGNMENT.md)

A dated literature-alignment note covering recent process-tensor, multitime-memory, causal-break and non-Markovian thermodynamics work that can sharpen controls and experimental design. These external studies provide comparison models and design guidance for testing the proposed additional history-weighted term.

---

## 2027 experimental research programme

[**2027 Experimental Research Roadmap**](2027_EXPERIMENTAL_RESEARCH_ROADMAP.md) — three coordinated research tracks: a neutral-memory selection experiment, a desk-only cross-domain mathematical test, and longer-term physical-mechanism investigations. The roadmap states competing models, independent review requirements and conditions under which predictions can fail. No canonical equation or earlier research claim is changed.

---

## November 2026 research-status update

[Research Status and Testing Note — 2 November 2026](VERRELLS_LAW_RESEARCH_STATUS_AND_TESTING_2026-11.md) — mathematical advances, model comparisons, experimental priorities and scoped corrections to exploratory extensions. The core retained-state proposition and canonical equations are unchanged.

---

## Core research documents

**[Mathematical Status and Structural Results — 11 November 2026](MATHEMATICAL_STATUS_AND_STRUCTURAL_RESULTS_2026-11-11.md)** — independently rerun structural checks, minimum-relative-entropy characterisation, monotonicity, distribution-shift bound, tilt composition and falsifiable model commitments. No canonical equations or physical claims are changed.

1. [Public Reader Start Here](PUBLIC_READER_START_HERE.md) — short orientation and claim boundary.
2. [Retained-State Selection Research Index](00_RETAINED_STATE_SELECTION_INDEX.md) — map of the current research programme.
3. [Mathematical Foundations and Falsification Protocol v1.0](VERRELLS_LAW_MATHEMATICAL_FOUNDATIONS_AND_FALSIFICATION_PROTOCOL_v1.0.md) — canonical retained-state selection specification.
4. [Mathematical Clarification Supplement v1.0](VERRELLS_LAW_MATHEMATICAL_CLARIFICATION_SUPPLEMENT_v1.0.md) — statistical estimation, score normalization, and evidential-verdict clarifications.
5. [Empirical Identification Clarification v1.0](VERRELLS_LAW_EMPIRICAL_IDENTIFICATION_CLARIFICATION_v1.0.md) — separates independent empirical evidence from engineering conformance and proxy inference.
6. [Retained-State Selection Framework](RETAINED_STATE_SELECTION_FRAMEWORK.md) — broader conceptual spine.
7. [Mathematical Reference v1.3](VERRELLS_LAW_MATHEMATICAL_REFERENCE_v1.3.md) — supporting notation and operational boundaries.
8. [Falsification Conditions](FALSIFICATION_CONDITIONS.md) — supporting failure conditions and null-verdict language.
9. [Exploratory Extensions](SPECULATIVE_EXTENSIONS.md) — further research into field, physical and consciousness-related mechanisms.
10. [Archived Document Status](ARCHIVED_DOCUMENT_STATUS.md) — guidance for interpreting older material.

---

## Analysis-validation research tool — v0.1.5 (17 October 2026)

**[Download the Python analysis-validation package v0.1.5](VERRELLS_LAW_ANALYSIS_VALIDATION_v0.1.5_APPROVED_FOR_PUBLICATION_20261017.zip)**

This standalone, reproducible **Route B synthetic analysis-validation tool** tests whether a declared analysis pipeline can recover a known retained-state coefficient, handle null and wrong-direction cases, screen nonlinear misspecification, and avoid certain spurious-history conclusions. The archive includes Python source, instructions, example output and automated tests; extract the ZIP and follow its bundled README.

The release-review suite passed **24/24 tests**, including a 2,000-replication null and confidence-interval coverage gate.

**Test scope:** synthetic data with oracle-known baseline offsets, declared linearity-equivalence tolerance and fail-closed near-separation screens. Domain-specific observations, independently estimated baselines, power planning and conventional-model comparisons form the subsequent empirical programme. See the package README for reproduction commands and detailed conditions.

---

## Minimal retained-state selection spine

The canonical exponential-tilt relation (exact under its specified selection model, an empirical hypothesis when applied to independent observations) is:

```math
\Delta L = \lambda\Delta R
```

where `ΔL` is the candidate-relative change in selection log-odds and `ΔR` is a preregistered, normalized retained-state compatibility difference.

For observed binary choices, with independently known baseline log-odds `b_k`, the confirmatory observation model is:

```math
Y_k\sim\mathrm{Bernoulli}(p_k),\qquad
\log\frac{p_k}{1-p_k}=b_k+\alpha+\lambda r_k,\qquad r_k=\Delta R_k.
```

Here `Y_k=1` denotes candidate `a`, `Y_k=0` denotes candidate `b`, and `α` allows identifiable baseline mismatch. Repeated choices require design-appropriate dependence treatment. Regression on independently measured `ΔL` remains a separate analysis route; its residual `ε_k` is not an extra noise term silently inserted into the logit. If the baseline is estimated rather than known, its model and uncertainty must be specified. See [Mathematical Clarifications and Open Problems v1.0, §2](MATHEMATICAL_CLARIFICATIONS_AND_OPEN_PROBLEMS_v1.0.md#2-exact-selection-identity-and-binary-evaluation-model).

The score definition, scale, sign convention, baseline, inclusion rules and analysis plan must be fixed appropriately before confirmatory testing.

For independent evidence, the rule producing `ΔR` must be frozen independently of the confirmatory selection outcome. Reusing a selector’s own internal score to demonstrate the behaviour it was designed to produce is an engineering conformance test unless an independent analysis route is supplied.

---

## Physics-facing extension

The research also investigates **field-mediated and physical memory effects**, including possible electromagnetic, biological, environmental and quantum-system contributions. These pathways remain open to measurement and comparison; see [Retained-State Mechanism and Field Boundary](RETAINED_STATE_MECHANISM_AND_FIELD_BOUNDARY.md).

The September 2026 technical edition asks a different but related laboratory question:

> When matched present reduced states have different controlled physical histories, does a predeclared measure of physical transition weight identify a reproducible contribution to the effective memory governing later dynamics?

The candidate decomposition is intentionally testable:

```math
K_{eff}(t,\tau \mid H,W)
=
K_0(t,\tau \mid C)
+
g(w(\tau),H(\tau);\theta)K_V(t,\tau)
```

Here `C` denotes measured controls; `w(τ)` is the time-resolved physical weight and `W` its history; `H` denotes the prepared retained-history condition, with `H(τ)` its time-resolved representation. Kernel scale, sign and identifiability restrictions are set out in [Mathematical Clarifications and Open Problems v1.0, §5](MATHEMATICAL_CLARIFICATIONS_AND_OPEN_PROBLEMS_v1.0.md#5-memory-kernel-decomposition-is-not-unique-without-restrictions).

A non-zero memory kernel alone does not support the proposed extension. The additional term must improve held-out prediction, follow the predeclared weighting relation and respond correctly to intervention on retained history or weight.

---

## Evidence ladder

The current physics-facing evidence ladder is cumulative:

1. **Formal identifiability** — the weighting variable, candidate kernel, null region and analysis are specified so the model can fail.
2. **Controlled history divergence** — matched present states with different randomised histories produce a held-out directional difference.
3. **Intervention and ablation** — erasing, scrambling or altering retained state changes the effect as predicted.
4. **Metrological and thermal convergence** — independent measurements support the same coupling timescale and direction.
5. **Independent replication** — a separate team reproduces the preregistered effect on another device and rules out the same conventional alternatives.

Possible verdicts should remain disciplined: **not supported**, **compatible**, **provisional support**, or **independent support** according to the evidence actually achieved.

---

## Claim boundaries

The current public framework does **not** establish:

- a new fundamental force or free-standing information substance;
- universal electromagnetic memory;
- non-local personal memory storage;
- consciousness-caused quantum collapse;
- modification of general relativity;
- a universal physical carrier shared across all domains;
- a universal sensor threshold;
- software behaviour as proof of a law of nature.

Physical, biological, cognitive and engineered systems may share abstract retained-state structure while using different mechanisms. Cross-domain similarity is a research question, not an assumption of identical physics.

---

## Associated engineering working paper

**[Memory-Weighted Selection: Middleware for Continuity and Governed Behaviour in LLM Systems](https://github.com/collapsefield/memory-weighted-selection)** develops a public reference formulation for host-supplied candidate selection under retained-state influence and explicit governance. It is a separate software-engineering programme; its worked examples are not independent experimental evidence for Verrell’s Law. The existing paper and its source are maintained in their dedicated repository.

---

## Engineering boundary

Software can be used to demonstrate and test deliberately constructed retained-state selection behaviour. Such behaviour is useful engineering evidence about that system.

It does **not** by itself establish that an equivalent mechanism exists independently in biology or physics.

The associated engineering programme is maintained separately from this research archive so that software evaluation and scientific claims can be judged on their own evidence.

---

## Archive status

This repository preserves earlier wording, exploratory notes and superseded mathematical attempts as part of its public development and provenance record.

Older material should not be treated as the current strongest position where later documents have narrowed, corrected or superseded it.

Use [Archived Document Status](ARCHIVED_DOCUMENT_STATUS.md) when reading historical files.

---

## Citation — September 2026 technical edition

> Ross, M. V. M. (2026). *Verrell’s Law: A Framework for Non-Markovian Information Paths*. Information Physics and Open Quantum Systems Edition, September 2026.

---

**README navigation refreshed:** 11 November 2026 · Underlying research documents retained.
