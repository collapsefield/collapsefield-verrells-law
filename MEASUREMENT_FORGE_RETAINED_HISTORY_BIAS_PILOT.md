# Measurement Forge — Retained-History Bias Pilot

**Project:** Verrell’s Law / Collapse Aware AI
**Author:** Marcos Verrell Moss Ross (M.R.)
**Company:** Inappropriate Media Limited
**Status:** Public-safe GitHub pre-registration candidate
**Version:** v1.0
**Purpose:** Define a minimal empirical pilot for measuring whether retained history can shift output selection under controlled conditions.

---

## 1. Purpose

This document defines a public-safe pilot measurement protocol for Verrell’s Law and Collapse Aware AI.

The core question is simple:

> **Does relevant retained history measurably shift later output selection?**

The pilot is designed to produce a controlled result with:

* an effect size
* uncertainty bounds
* a model-free distributional companion measure
* calibration checks
* a pre-committed verdict rule

This is not a consciousness claim.
This is not a claim about AGI.
This is not a disclosure of private Collapse Aware AI implementation logic.

It is a measurement protocol for testing whether retained history changes selection behaviour in a controlled runtime setting.

---

## 2. Core Hypothesis

Verrell’s Law proposes that retained information and memory can bias later selection.

In practical test form:

> **Relevant retained history should produce a measurable shift in output selection compared with matched irrelevant or scrambled history.**

The key contrast is not simply memory-on versus memory-off.

The key contrast is:

> **Relevant memory versus matched placebo memory.**

This matters because it controls for the obvious objection that a result may be caused merely by adding more text or context.

---

## 3. Experimental Conditions

Each test scenario is run under three conditions:

| Condition | Label              | Description                                                                       |
| --------- | ------------------ | --------------------------------------------------------------------------------- |
| A         | Memory OFF         | Empty or neutral memory slot                                                      |
| B         | Relevant Memory ON | A retained-history packet expected to bias selection toward a pre-named candidate |
| C         | Matched Placebo    | Irrelevant or scrambled memory matched in length to condition B                   |

The main result is measured using **B versus C**.

Condition A remains useful as a clean zero-memory reference, but the strongest test is whether relevant memory beats matched irrelevant memory.

---

## 4. Scenario Design

Each scenario must be frozen before any scored run.

A scenario contains:

* a fixed prompt or situation
* a fixed candidate set
* a relevant memory packet
* a matched placebo packet
* a pre-named expected-direction candidate

The candidate set should be small and discrete.

For the first pilot, a binary forced-choice setup is preferred because it produces the cleanest statistical result.

A stronger pilot may use three separate scenarios across different bias channels, such as:

* preference continuity
* risk posture
* tone or behavioural selection

The pilot should not expand beyond its purpose.
The purpose is to measure retained-history selection bias, not to test every part of the wider framework at once.

---

## 5. Controls

Mandatory controls:

* identical prompt across all conditions
* same model or backend configuration across runs
* matched token count between relevant memory and placebo memory
* fixed candidate set
* randomised or interleaved condition order
* logged model/config version
* logged seed where available
* fallback runs marked and excluded from estimation
* scoring rule frozen before the run

A fallback response must not be silently treated as a valid result.

If fallback occurs, it should be logged, flagged, excluded from estimation, and reported.

---

## 6. Logging Requirements

Each run should produce one logged row containing at least:

```text
timestamp
scenario_id
run_id
condition
seed
request_id
thread_id
input_hash
memory_state_hash
governor_mode
bias_enabled
candidate_set
selected_candidate
selection_score
latency_ms
fallback_used
model_version
config_version
```

The aim is to make the measurement repeatable, inspectable, and resistant to post-hoc interpretation.

---

## 7. Primary Effect Size

For a binary forced-choice setup, the preferred primary estimator is logistic regression.

The measured effect is the log-odds shift caused by relevant retained history compared with matched placebo history.

In simple terms:

> **λ measures how much relevant memory shifts the odds of selecting the expected candidate.**

λ should be reported with:

* standard error
* 95% confidence interval
* direction of effect
* sample size
* scenario identifier

For candidate sets larger than two, a multinomial logistic approach may be used.

---

## 8. Model-Free Companion Measure

A model-free companion measure should also be reported.

The recommended measure is **Jensen-Shannon divergence**, reported in bits, between the selection distribution under relevant memory and the selection distribution under matched placebo memory.

This provides a distributional measure of how much the output pattern changed.

For a balanced design, this can also be interpreted as a mutual-information style quantity:

> **bits of selection explained by the memory condition.**

Because plug-in information measures can be positively biased at small sample sizes, the pilot should include:

* bootstrap confidence intervals
* permutation testing
* observed value versus shuffled-label null

This prevents tiny random distributional differences from being overclaimed.

---

## 9. Calibration

The pilot should not only ask whether an effect exists.

It should also ask whether the estimate can be trusted.

Calibration should be tested using held-out folds.

Recommended process:

1. split runs into held-out folds
2. estimate the effect on training folds
3. evaluate predicted selection probabilities on held-out data
4. build a reliability diagram
5. report expected calibration error
6. check whether confidence intervals behave as expected across replications

A measured effect with poor calibration should be reported honestly as overconfident or unstable.

Poor calibration is not a failed experiment.
It is useful information about the measurement system.

---

## 10. Sample Size

Suggested minimum structure:

* 30 runs per condition for smoke testing only
* 300 runs per condition for a publishable pilot minimum
* two replications using different seeds or dates where possible

The smoke test should not be reported as the finding.
It is only a wiring and logging check.

The publishable pilot begins once the protocol, scenario, scoring rule, and decision thresholds are frozen.

---

## 11. Decision Rule

The verdict should be fixed before results are inspected.

Suggested verdict structure:

| Result Pattern                                                                                 | Verdict                      |
| ---------------------------------------------------------------------------------------------- | ---------------------------- |
| Effect confidence interval excludes zero and distributional shift exceeds permutation null     | DETECTED                     |
| Effect confidence interval includes zero and distributional shift sits inside permutation null | REFUTED IN THE TESTED REGIME |
| Estimate is unstable, underpowered, or replication disagrees                                   | INCONCLUSIVE                 |

“Refuted in the tested regime” is important wording.

A null result in one model, prompt, memory setup, or candidate set does not refute the whole framework.
It only bounds the claim inside that tested regime.

---

## 12. Public-Safe Boundary

This document does not disclose:

* private Collapse Aware AI source code
* sealed Crown architecture
* proprietary scoring internals
* private middleware schemas
* commercial deployment logic
* protected implementation details

This document records a public-facing measurement protocol.

It is designed to make the empirical claim testable without exposing the private build.

---

## 13. What the Pilot Should Produce

A completed pilot should produce:

1. λ effect size with 95% confidence interval
2. Jensen-Shannon divergence or mutual-information style companion measure in bits
3. bootstrap confidence interval
4. permutation-null comparison
5. calibration result
6. fallback/discard count
7. frozen pre-registration artifact
8. final verdict under the pre-committed rule

A clean result under this protocol would provide a measured runtime test of retained-history bias.

That is the Measurement Forge objective.

---

## 14. One-Line Summary

> **This pilot tests whether relevant retained history measurably shifts future selection compared with matched placebo history, using pre-registered conditions, effect-size estimation, information-theoretic comparison, and calibration checks.**

---

## Authorship and Rights

This measurement framing is authored by **Marcos Verrell Moss Ross (M.R.)** as part of the Verrell’s Law and Collapse Aware AI body of work.

© 2026 Marcos Verrell Moss Ross / Inappropriate Media Limited.
All rights reserved unless otherwise stated in the repository licence.

---

*Public-safe GitHub artifact. Pre-registration candidate. Not established proof.*
