# Falsification Conditions

## Status

This document defines the failure conditions for the retained-state form of Verrell's Law.

Verrell's Law is currently presented as a falsifiable retained-state selection framework, not as established physics.

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

The estimator route should be cross-referenced to:

> `FALSIFIABLE_MEMORY_BIAS_ESTIMATOR.md`

---

## Main Failure Conditions

The retained-state claim fails in a tested regime where one or more of the following hold.

### 1. No measurable divergence

Systems with different retained histories do not show measurable divergence under matched present inputs.

### 2. Retained-state influence is indistinguishable from null

The fitted retained-state influence is statistically or operationally indistinguishable from the pre-registered null condition.

Because `λ` and `B(y_i;M_t)` are not separately identifiable without a pre-defined bias function, this condition should be evaluated using the pre-committed estimator and baseline definition, not an after-the-fact fitted explanation.

### 3. Divergence is explained by pre-enumerated confounds

Observed divergence is fully explained by known confounds that were listed before the test.

Examples may include, depending on the regime:

- prompt/input mismatch;
- candidate-set mismatch;
- sampling noise;
- model version change;
- hidden state leakage;
- training exposure;
- environmental variation;
- measurement artefact;
- ordinary stimulus-response effects not requiring retained-state weighting.

The confound list should be specific to the test and fixed before verdict.

### 4. Bias-off and bias-on conditions do not diverge

Disabling, ablating, randomising, or neutralising retained-state weighting produces no measurable difference from enabling it.

In the CAAI engineering analogue, this corresponds to comparing a retained-state-influenced condition against a controlled baseline condition without disclosing private implementation internals.

### 5. Memory/state perturbation does not alter later selection

A defined perturbation to retained state does not alter later selection in the predicted direction, under matched present input and fixed candidate conditions.

---

## Locked Null Wording

If the retained-state claim fails under the defined test, the correct verdict is:

> Verrell's Law was not supported in this tested regime.

or:

> The retained-state selection claim was refuted in this tested regime.

Avoid global overstatements such as:

> Verrell's Law is impossible.

or:

> Retained state never matters.

A failed test refutes the claim only within the tested regime unless the test is designed to generalise further.

---

## What Would Support the Claim

Evidence supports the retained-state framework in a tested regime where:

1. matched present inputs produce divergent outcomes across different retained-history conditions;
2. the divergence follows the predicted retained-state direction;
3. the effect survives pre-enumerated confound checks;
4. the retained-state term improves prediction beyond baseline input alone;
5. disabling or neutralising retained-state influence reduces or removes the divergence.

Support in one regime does not automatically establish the claim in all regimes.

---

## CAAI Boundary

Collapse Aware AI is the engineering track for governed retained-state behavioural selection.

CAAI evidence may demonstrate an engineering analogue of the retained-state framework, such as:

- bias-off/bias-on divergence;
- persistence across restart;
- candidate selection under retained-state influence;
- governor-constrained selection;
- diagnostic traceability.

CAAI evidence should not be presented as proof of new physics.

---

**Version:** v1.0 retained-state hardening pass  
**Date:** 2026-07-04  
**Author:** Marcos Verrell Moss Ross (M.R.) / Inappropriate Media Limited  
**Repository target:** `collapsefield/collapsefield-verrells-law`
