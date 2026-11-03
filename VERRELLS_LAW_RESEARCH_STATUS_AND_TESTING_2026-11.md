# Verrell's Law — Research Status and Testing Note
**Date:** 2 November 2026  
**Status:** Working research framework — mathematical review and next tests  
**Originator:** M.R.

## Research direction
Verrell's Law investigates whether retained histories produce measurable, directional differences in subsequent weighting and selection when present comparison conditions are matched. The framework develops an explicit retained-state selection model and a programme of comparative, intervention-sensitive tests. Physical-field and quantum extensions are investigated separately.

## Progress from the November mathematical reviews
The 1 November 2026 reviews sharpened the mathematical specification and experimental design. They:

- Confirmed the exact log-odds relationship within the defined exponential-tilt selection family.
- Clarified the requirements for independently constructed, fixed retained-state scores and identifiable model parameters.
- Compared active-mean, weighted-mean, sum, regularised-pool, gain, sampling, capacity and threshold mechanisms.
- Identified discriminating cases involving neutral memories, competing memories, retrieval, weight gradients and changes in remembered information.
- Developed a more precise route from mathematical modelling to held-out tests, intervention and comparison against established methods.

These advances strengthen the framework's internal specification and testability. The next research stage is to establish which models, if any, make distinctive predictions supported by independent observations.

## Mathematical selection family
The reviews rechecked:

```math
p_{\lambda,i}=\frac{p_{0,i}e^{\lambda R_i}}{\sum_j p_{0,j}e^{\lambda R_j}}
```

For a fixed candidate set, positive baseline support and finite scores, the pairwise result is:

```math
\Delta\log\mathrm{odds}(a,b)=\lambda(R_a-R_b).
```

This identity follows exactly from the declared model. Its empirical application requires scores constructed independently of the outcomes being predicted. Unrestricted scores could reproduce any target distribution with common positive support; fixed score construction, suitable conventional comparators and held-out evaluation therefore matter.

The reviewed formulations overlap, in part, with established averaging, ACT-R-style blending, episodic sampling and divisive-normalisation approaches. Comparison with those methods will help establish the scope and any distinctive predictive contribution of the proposed formulation.

## Research methods and current results
The November analyses used synthetic simulations to examine model behaviour, parameter recovery and alternative mechanisms. They did not include new human or physical measurements.

The provisional empirical protocol covers cued and uncued histories, matched present-state baselines, strength variation, competing memories, retrieval checks and reminder/update interventions. It is designed for future preregistration and execution. Language-model pilots may be useful engineering or methodological testbeds; claims about biological or physical behaviour require independent domain-specific observations.

Research must distinguish **stored**, **cued**, **retrieved**, **activated** and **influential** information. In the existing mathematical notation, `q_j` denotes **reliability**, while `w_j=s_j d_j q_j` combines salience, persistence and reliability. A five-memory example illustrates an experimental condition, not a fixed retrieval capacity. The reviews did not adopt a new canonical aggregation or retrieval rule.

## Next research programme
1. Define and freeze each candidate retained-state score independently of confirmatory outcomes.
2. Specify matched present-condition baselines, identifiable parameters and conventional comparison models.
3. Test differentiating predictions with held-out data, explicit uncertainty and controlled history interventions.
4. Examine whether an effect and its direction persist across independent systems and laboratories.
5. Extend into physical-domain experiments only with separately specified observables, mechanisms and consistency requirements.

A cross-domain relationship remains an investigation target. Each experiment should distinguish the tested prediction from alternative explanations and document inconclusive as well as positive results.

## Scope of exploratory physical extensions
A historical Born-rule outcome-reweighting construction reviewed in November can violate no-signalling for nonzero bias. This result concerns that particular nonlinear extension, **not** the retained-state selection formulation as a whole. Small bias does not restore exact no-signalling, so any revised quantum extension must establish physical consistency directly.

A candidate-independent term `-λ_τΔt` cancels during outcome normalisation when common to all candidates and therefore does not implement decay on its own. Historical informational-tensor expressions have further compatibility questions requiring explicit treatment. The original material remains in the archive with dated corrections.

## Relation to Collapse Aware AI
Collapse Aware AI (CAAI) is a separate proprietary engineering programme using governed retained-state behavioural selection. Software conformance and scientific tests have different evidence requirements. The November mathematical reviews did not evaluate the frozen Core Gold runtime or mandate an Evolution 2 implementation change.

Historical publications are retained as an authorship and development record. Read this note with the [canonical foundations](VERRELLS_LAW_MATHEMATICAL_FOUNDATIONS_AND_FALSIFICATION_PROTOCOL_v1.0.md), [clarification supplement](VERRELLS_LAW_MATHEMATICAL_CLARIFICATION_SUPPLEMENT_v1.0.md) and [31 October clarifications](MATHEMATICAL_CLARIFICATIONS_AND_OPEN_PROBLEMS_v1.0.md).
