# Falsification Conditions

## Status

This document defines failure conditions for the retained-state form of Verrell's Law.

Verrell's Law is presented as a falsifiable retained-state selection framework, not as established physics.

The central testable claim is:

> Otherwise similar systems with different retained histories should show measurable divergence under matched present input if retained-state weighting is active.

---

## Required Test Structure

A valid test should define, before measurement:

1. the system or systems being compared;
2. the present input condition;
3. the retained-history condition;
4. the baseline or memory-ablated condition;
5. the candidate outcome set;
6. the retained-state feature or scoring rule;
7. the estimator used to infer retained-state influence;
8. the decision threshold for support or failure;
9. the known confounds to be checked;
10. the exact null-verdict wording.

The estimator route should be cross-referenced to `FALSIFIABLE_MEMORY_BIAS_ESTIMATOR.md` and the later canonical mathematical specification.

---

## Main Failure Conditions

### 1. No measurable divergence

Systems with different retained histories do not show measurable divergence under matched present inputs.

### 2. Retained-state influence is indistinguishable from null

The fitted retained-state influence is statistically or operationally indistinguishable from the preregistered null condition.

Because coupling and retained-state score are not separately identifiable without a fixed scoring convention, this condition must be evaluated using the precommitted estimator and baseline rather than an after-the-fact fitted explanation.

### 3. Divergence is explained by pre-enumerated confounds

Observed divergence is fully explained by known confounds fixed before the verdict.

Examples may include:

- prompt/input mismatch;
- candidate-set mismatch;
- sampling noise;
- model version change;
- hidden state leakage;
- training exposure;
- environmental variation;
- measurement artefact;
- ordinary stimulus-response effects not requiring retained-state weighting.

### 4. Retained-state-on and reference conditions do not diverge

Disabling, ablating, randomising or neutralising retained-state influence produces no measurable difference from enabling it where the framework predicts a difference.

### 5. Retained-state intervention does not alter later selection

A defined perturbation to retained state does not alter later selection in the preregistered direction under matched present input and fixed candidate conditions.

---

## Locked Null Wording

If the retained-state claim fails under the defined test, appropriate verdicts include:

> Verrell's Law was not supported in this tested regime.

or:

> The retained-state selection claim was refuted in this tested regime.

Avoid global overstatements such as “retained state never matters” unless the design genuinely supports such a generalisation.

---

## What Would Support the Claim

Evidence supports the retained-state framework in a tested regime where:

1. matched present inputs produce divergent outcomes across different retained-history conditions;
2. the divergence follows the predicted retained-state direction;
3. the effect survives preregistered confound checks;
4. retained history improves prediction beyond the declared baseline;
5. disabling or neutralising retained-state influence reduces or removes the predicted divergence;
6. the result generalises to held-out trials.

Support in one regime does not automatically establish the claim in all regimes.

---

## Engineering Boundary

Collapse Aware AI™ is a separate engineering programme for governed retained-state selection.

Engineering tests may demonstrate intentionally implemented retained-state behaviour, replay and evidence. They should not be presented as independent proof that the same mechanism occurs naturally in physics or biology.

---

**Version:** v1.1 research-attribution refresh  
**Date:** 2026-09-14  
**Author:** Marcos Verrell Moss Ross (M.R.)
