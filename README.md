# Verrell’s Law — Official GitHub Archive

**Verrell’s Law** is a testable framework proposing that system evolution may be influenced not only by present conditions and inputs, but also by retained information from prior states. In this framework, memory functions as a bias term in selection dynamics, shaping the probability of future outcomes and producing path-dependent divergence.

**Author:** Marcos Verrell Moss Ross (M.R.)  
**Maintainer:** Inappropriate Media Ltd (t/a Collapse Aware AI)  
**Contact:** collapseawareai@gmail.com  
**Last updated:** 2026-04-27  

**DOI:** https://doi.org/10.5281/zenodo.17392582  
**Related DOI:** https://doi.org/10.5281/zenodo.17416435

---

## New Readers

Start here first: [`PUBLIC_READER_START_HERE.md`](PUBLIC_READER_START_HERE.md)

This orientation note explains what Verrell’s Law claims, what it does not claim, how it relates to Collapse Aware AI, and the current evidence status.

---

## Latest Public Research Additions

| File | Why it matters | Status |
|---|---|---|
| [`Verrell_Law_Test_Protocols_Phase_1_v1.0.md`](Verrell_Law_Test_Protocols_Phase_1_v1.0.md) | Five falsifiable Phase 1 validation protocols covering memory-driven divergence, decay/reactivation, coherence under noise, symbolic salience, and continuity signature prediction. | Published Test Framework |
| [`metadata_public_proof_pack_2026_04_27.json`](metadata_public_proof_pack_2026_04_27.json) | Public metadata record for the sanitized Collapse Aware AI proof-pack reference archive, including authorship, scope boundaries, omitted private components, and VMR-Core rights marker. | Public Reference Metadata |

---

## What This Repository Is

This repository is the public theory archive, research index, and authorship/provenance record for Verrell’s Law.

It preserves:

- canonical definitions and terminology
- formal notes and mathematical structures
- memory-position clarifications
- experimental blueprints
- symbolic test frameworks
- public proof materials
- links between Verrell’s Law and Collapse Aware AI
- historical development records and authorship trail

This repository should be read as the theory and archive layer. The applied middleware work sits alongside it as an engineering instantiation, not as proof that the full theoretical or physical form of Verrell’s Law has been scientifically confirmed yet.

---

## What This Repository Is Not

This repository is **not**:

- a claim of completed experimental proof
- a claim that consciousness or sentience has been proven
- a rejection of biological memory or established neuroscience
- a replacement for established physics
- an open-source implementation of Collapse Aware AI
- a release of proprietary Crown kernel logic

The framework is best read as a structured, testable hypothesis under active development.

---

## Core Principle

At its most compact, Verrell’s Law proposes:

> Retained information from prior states can influence future state selection even when present inputs are held constant.

The core working claim is:

- memory is treated as structured retained information
- retained information can bias later emergence or selection
- systems with different histories may diverge even under matched present-state conditions

In stronger theoretical formulations, this framework is extended into field-based and informational interpretations of memory, observation, and emergence. Those broader interpretations remain under investigation and should be distinguished from the narrower formal systems claim.

---

## Core Selection Model

The current working mathematical form treats future selection as a probability distribution shaped by both present utility and retained memory bias:

```math
P(y_i \mid S_t, O_t, M_t) =
\frac{
\exp\left(U(y_i;\, S_t, O_t) + \lambda B(y_i;\, M_t)\right)
}{
\sum_j \exp\left(U(y_j;\, S_t, O_t) + \lambda B(y_j;\, M_t)\right)
}
```

Where:

| Symbol | Meaning |
|---|---|
| `S_t` | Present system state at time `t` |
| `O_t` | Current observation or input |
| `M_t` | Retained memory state |
| `U(y_i; S_t, O_t)` | Present-state utility of candidate output `y_i` |
| `B(y_i; M_t)` | Memory-weighted bias term |
| `λ` | Memory coupling strength |

If `λ = 0`, memory has no influence.

If `λ > 0`, retained memory contributes to future selection.

---

## Canonical Public Documents

| File | Purpose |
|---|---|
| [`PUBLIC_READER_START_HERE.md`](PUBLIC_READER_START_HERE.md) | First-read orientation note and public framing guardrail. |
| [`VERRELLS_LAW_CANONICAL.md`](VERRELLS_LAW_CANONICAL.md) | Canonical statement of the Law, claim boundaries, and terminology. |
| [`VERRELLS_LAW_POSITION_ON_MEMORY_STORAGE.md`](VERRELLS_LAW_POSITION_ON_MEMORY_STORAGE.md) | Clarifies biological memory, local traces, and the field-access hypothesis. |
| [`MEMORY_TUNING_AND_DISTRIBUTED_RETRIEVAL.md`](MEMORY_TUNING_AND_DISTRIBUTED_RETRIEVAL.md) | Refined memory model: local storage, reconstructive recall, and field-tuned retrieval. |
| [`Verrells_Law_Conference_Clean_Formal_Note_v2.md`](Verrells_Law_Conference_Clean_Formal_Note_v2.md) | Clean formal note with canonical notation, selection law, memory dynamics, and falsifiability criteria. |
| [`VERRELLS_LAW_FORMAL_CLARIFICATION_V1.md`](VERRELLS_LAW_FORMAL_CLARIFICATION_V1.md) | Additional formal clarification and constraint notes. |
| [`Verrells_Law_White_Paper_v1.0_2025-08-29.md`](Verrells_Law_White_Paper_v1.0_2025-08-29.md) | Foundational white paper introducing the collapse-bias framework. |
| [`VL-Optics-Experiment-Note_v1.1.md`](VL-Optics-Experiment-Note_v1.1.md) | Optical interference test design for field-bias validation. |
| [`worlds_first_symbolic_collapse_test_framework.md`](worlds_first_symbolic_collapse_test_framework.md) | Symbolic JSON collapse test suite and protocol notes. |
| [`NOT_MORPHIC_RESONANCE.md`](NOT_MORPHIC_RESONANCE.md) | Clarifies distinction from morphic resonance claims. |
| [`LICENSE`](LICENSE) | Repository rights and usage restrictions. |

---

## Additional Research and Archive Materials

| File / Folder | Purpose |
|---|---|
| [`Verrell_Law_Test_Protocols_Phase_1_v1.0.md`](Verrell_Law_Test_Protocols_Phase_1_v1.0.md) | Phase 1 Validation Suite: five empirical protocols for testing memory-weighted selection, behavioural divergence, temporal decay/reactivation, coherence under noise, symbolic salience, and continuity signatures. |
| [`metadata_public_proof_pack_2026_04_27.json`](metadata_public_proof_pack_2026_04_27.json) | Public proof-pack metadata record documenting release scope, authorship, public-safe technical position, omitted private components, and VMR-Core rights marker. |
| [`verrells-law-core-mathematical-scaffold.md`](verrells-law-core-mathematical-scaffold.md) | Core mathematical scaffold and symbol definitions. |
| [`verrells-law-psi-field-framework.md`](verrells-law-psi-field-framework.md) | Ψ field framework documentation. |
| [`UPDATED_MATH_RENDERS.md`](UPDATED_MATH_RENDERS.md) | Updated math render notes and visual assets index. |
| [`consciousness_gradient_v1.md`](consciousness_gradient_v1.md) | Gradient model of observer density across systems. |
| [`2025-10-17_Dust_Battery_Seed_Fields_and_Verrells_Law.md`](2025-10-17_Dust_Battery_Seed_Fields_and_Verrells_Law.md) | Dust Battery hypothesis and micro-field retention note. |
| [`field-interference-hypothesis.md`](field-interference-hypothesis.md) | Field-interference hypothesis working note. |
| [`light_biased_collapse_v1.md`](light_biased_collapse_v1.md) | Light-biased collapse working note. |
| [`docs/`](docs/) | Auxiliary documents, historical clarifications, and supporting notes. |
| [`Verrells_Law/docs/`](Verrells_Law/docs/) | Additional nested documentation, including Ψ tensor framework materials. |

PDF, image, DOCX, ZIP, JSON, and legacy files are retained for provenance and historical continuity. The Markdown files above should be treated as the current public navigation layer.

---

## Phase 1 Validation Suite

The Phase 1 Validation Suite defines five empirical protocols for testing the central claim of Verrell’s Law:

> Retained structured memory from prior states biases future selection outcomes in a measurable, statistically significant, and reproducible manner.

The five protocols are:

| Protocol | Focus | Primary Measurement |
|---|---|---|
| 1. Measurable Divergence Under Identical Present Conditions | Whether different memory histories produce different output distributions under identical present input. | KL / JS divergence |
| 2. Memory Decay and Reactivation Curves | Whether memory influence decays structurally and can be reactivated. | Bias score and recovery curve |
| 3. Field Coherence Under Noise and Perturbation | Whether memory-weighted systems resist noise-induced drift better than memoryless baselines. | Coherence degradation slope |
| 4. Symbolic Salience Weighting and Emotional Bias | Whether high-salience prior information creates stronger future bias than neutral information. | Salience Bias Index |
| 5. Continuity Signature Detection and Prediction | Whether prior memory state leaves an extractable predictive signature in current outputs. | Prediction gain over baseline |

Together, these protocols create a falsifiable test framework for evaluating whether Verrell’s Law has measurable empirical support.

---

## Relation to Collapse Aware AI

Collapse Aware AI (CAAI) is the engineering branch associated with this framework.

In CAAI, the core idea is instantiated as middleware and governed behavioural selection logic. The applied system treats memory as a weighted influence on runtime selection, continuity, and behavioural divergence.

Public-safe wording:

> Verrell’s Law motivates the architecture. Collapse Aware AI implements the principle as software middleware.

CAAI is therefore a practical engineering implementation of memory-weighted selection, not experimental proof that the full physical or theoretical form of Verrell’s Law has been confirmed.

Related public proof-pack repository:

[`collapsefield/collapse-aware-ai-public-proof-pack`](https://github.com/collapsefield/collapse-aware-ai-public-proof-pack)

---

## Experimental Work and Notes

Current themes include:

- optical interference and field-bias test designs
- symbolic collapse simulations and JSON-based behavioural test harnesses
- field-memory bias modelling
- particulate or electrostatic retention hypotheses
- continuity and observer-dependent divergence models
- memory tuning and reconstructive recall models
- memory-weighted selection validation protocols
- continuity signature extraction and prediction tests

Some associated logs, exploratory notes, and authorship records remain archived privately and are not published in full here.

---

## Evidence Status

Current public evidence includes:

- internal simulations and symbolic tests
- formal mathematical notes
- public timestamped GitHub records
- Zenodo deposits
- experimental blueprints
- Phase 1 falsifiability and validation protocols
- applied middleware documentation through Collapse Aware AI

These support plausibility, structure, and authorship provenance.

They do **not** yet constitute independent experimental proof.

External controlled validation remains required.

---

## Authorship and Verification

This repository forms part of the public authorship and provenance record for Verrell’s Law.

Associated authorship and provenance measures include:

- timestamped public releases
- GitHub commit history
- Zenodo deposits
- lexical markers and authorship fingerprints
- continuity across public notes, proof packs, and repository records

These materials exist to establish development chronology, authorship, and prior-art positioning.

---

## Scientific and Technical Direction

Current and planned directions include:

- expansion of formal falsifiability and testability criteria
- additional collapse-bias simulations and comparative baselines
- Bayesian weighting and posterior-based bias modelling
- structured memory update rules and class-specific dynamics
- tighter linkage between theory notes and middleware results
- external pilot testing of the Phase 1 Validation Suite
- eventual formal publication or preprint consolidation

This work should be understood as an evolving research and engineering programme, not a closed or completed scientific theory.

---

## Licensing and Rights

All materials in this repository are proprietary unless stated otherwise.

Copyright © 2023–2026 Marcos Verrell Moss Ross (M.R.) / Inappropriate Media Ltd.

No permission is granted to reproduce, modify, distribute, publish, sublicense, create derivative works from, or commercially exploit repository contents without prior written permission from the rights holder.

See [`LICENSE`](LICENSE) for the repository’s current rights and restrictions.

---

## Citation

If citing the associated public framework record, use:

Verrell, M. (2025). *Collapse-Aware AI: Middleware for Resonance-Biased Emergence in Neural Architectures (Verrell’s Law Psi-mu-nu Framework) (v1.1b).* Zenodo. https://doi.org/10.5281/zenodo.17416435

---

## Contact

For technical, academic, or licensing enquiries:

**collapseawareai@gmail.com**

---

## Index Terms

Verrell’s Law · Collapse Aware AI · memory-weighted selection · path-dependent divergence · informational bias · behavioural middleware · field-memory hypothesis · collapse-bias framework · Phase 1 Validation Suite · continuity signatures · salience weighting · Marcos Verrell Moss Ross · Inappropriate Media Ltd
