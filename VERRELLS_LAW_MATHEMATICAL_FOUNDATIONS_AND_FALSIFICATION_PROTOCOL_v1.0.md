# Verrell's Law
## Mathematical Foundations and Falsification Protocol
### Canonical Specification v1.0

**Author:** Marcos Verrell Moss Ross (M.R.)  
**Maintainer:** Inappropriate Media Limited (t/a Collapse Aware AI)  
**Status:** Canonical public mathematical specification  
**Date:** 2026-07-17

---

## 1. Purpose, Scope and Non-Trivial Claim

Verrell's Law is presented here as a falsifiable retained-state selection hypothesis.

The framework does **not** merely claim that memory can change behaviour. That broad claim is already established in many ordinary systems and would be too weak to distinguish Verrell's Law from generic context effects.

The narrower claim is:

> Under controlled conditions, changes in selection log-odds are predicted by a preregistered retained-state compatibility score through a stable, directional coupling within a declared test regime.

The framework does not assume that consciousness, electromagnetic fields, quantum collapse, or any specific physical substrate has already been established as the cause of the effect. Those remain separate hypotheses requiring separate evidence.

The core empirical question is:

> After present input, known state variables and test conditions are controlled, does retained prior state produce a reproducible, quantitatively structured and out-of-sample-predictive change in later selection?

---

## 2. Core Objects and Notation

Let:

- \(x_t\) denote the current observable input at time \(t\).
- \(S_t\) denote the controlled present system state.
- \(\mathcal{A}=\{a_1,\ldots,a_K\}\) denote the available candidate outcomes.
- \(H_t=\{m_1,\ldots,m_n\}\) denote the retained state available before selection.
- \(p_0(a_i\mid x_t,S_t)\) denote the baseline probability of selecting candidate \(a_i\) without the tested retained-state influence.
- \(R_i(H_t,x_t,S_t)\) denote the retained-state compatibility score for candidate \(a_i\).
- \(\lambda\) denote the retained-state coupling parameter under a declared normalization convention.
- \(p_\lambda(a_i\mid x_t,S_t,H_t)\) denote the resulting selection probability when the tested retained-state influence is present.

The boundary between present state \(S_t\) and retained state \(H_t\) must be declared before testing. Variables held matched across conditions belong to \(S_t\). Variables deliberately varied because of retained history belong to \(H_t\).

---

## 3. Retained-State Compatibility Score and Normalization

A general retained-state score may be defined as:

```math
R_i(H_t,x_t,S_t)
=
\frac{1}{n}
\sum_{j=1}^{n}
 s_j d_j q_j r_{ij},
```

where:

- \(s_j\) is the preregistered salience of retained item \(m_j\);
- \(d_j\) is its persistence weight;
- \(q_j\) is an optional reliability weight;
- \(r_{ij}\) is its preregistered relevance or compatibility with candidate \(a_i\).

Unless a different convention is preregistered and justified, use:

```math
s_j,d_j,q_j,r_{ij}\in[-1,1].
```

Dividing by \(n\) bounds the scale of \(R_i\) against arbitrary growth with the number of retained items. An alternative valid convention is to standardize \(\Delta R\) to unit variance within the preregistered trial set.

The normalization convention must be fixed before data collection. This is necessary because the predictions are unchanged under the joint rescaling

```math
R_i\rightarrow cR_i,
\qquad
\lambda\rightarrow \lambda/c.
```

Therefore, the magnitude of \(\lambda\) is interpretable only relative to the declared scoring and normalization convention.

An implementation may assign discrete persistence tiers to retained items. The specific tier values are implementation choices and are not part of Verrell's Law.

---

## 4. Principal Hypothesis: Retained-State Selection

Let two trials share identical current input, candidate set, model and version, sampling parameters, random seed where applicable, and all controlled variables listed in Section 10, differing only in a preregistered retained-state set \(H_t\).

Let \(R\) be computed under the declared normalization convention in Section 3, with the sign convention that larger \(R_i\) denotes greater retained-state compatibility of candidate \(a_i\).

Then Verrell's Law predicts:

```math
\Delta L = \lambda\Delta R + \varepsilon,
```

where:

- \(\lambda>0\) is constant within the tested regime;
- \(\varepsilon\) has zero mean;
- \(\varepsilon\) is uncorrelated with \(\Delta R\) under the preregistered scoring convention.

A **regime** is a fixed system, model version, configuration, candidate construction procedure, scoring convention, normalization rule and test environment. \(\lambda\) is not asserted to transfer unchanged across regimes.

The hypothesis is rejected for a tested system when, under the preregistered protocol, the best-supported \(\lambda\) is statistically compatible with zero, unstable across repetitions, directionally inconsistent, non-predictive out of sample, or when the falsification conditions in Section 12 are met.

This hypothesis is substantially narrower than the general statement that memory affects behaviour. Generic context effects predict only that outcomes may vary when history varies. Verrell's Law predicts a specific quantitative structure linking retained-state compatibility to changes in selection log-odds.

---

## 5. Selection Model

For multiple candidates:

```math
p_\lambda(a_i\mid x_t,S_t,H_t)
=
\frac{
p_0(a_i\mid x_t,S_t)
\exp\!\left(\lambda R_i\right)
}{
\sum_{k=1}^{K}
p_0(a_k\mid x_t,S_t)
\exp\!\left(\lambda R_k\right)
}.
```

Equivalent logit form:

```math
z_i
=
\log p_0(a_i\mid x_t,S_t)
+
\lambda R_i,
```

followed by:

```math
p_\lambda(a_i)
=
\frac{e^{z_i}}{\sum_k e^{z_k}}.
```

This uses standard probability and logit machinery. The proposed contribution is not the invention of softmax or logistic regression. It is the preregistered, controlled and falsifiable treatment of retained-state compatibility as an explicit selection covariate.

---

## 6. Binary Log-Odds Form

For two candidates \(a\) and \(b\):

```math
\log
\frac{p_\lambda(a\mid x_t,S_t,H_t)}
{p_\lambda(b\mid x_t,S_t,H_t)}
=
\log
\frac{p_0(a\mid x_t,S_t)}
{p_0(b\mid x_t,S_t)}
+
\lambda(R_a-R_b).
```

Define:

```math
\Delta L
=
\log
\frac{p_\lambda(a)}{p_\lambda(b)}
-
\log
\frac{p_0(a)}{p_0(b)},
```

and:

```math
\Delta R=R_a-R_b.
```

The first-order prediction is therefore:

```math
\Delta L=\lambda\Delta R.
```

In estimation, an intercept and residual term are included as diagnostics:

```math
\Delta L_k=\alpha+\lambda\Delta R_k+\varepsilon_k.
```

A valid controlled trial set should support \(\alpha\approx0\). A materially non-zero intercept indicates an uncontrolled systematic difference between the retained-state and baseline conditions.

---

## 7. Observable Definitions by System Class

### 7.1 Probabilistic systems

Where candidate probabilities or token-level log-probabilities are available, compute \(\Delta L\) directly from those declared outputs.

When probabilities are estimated by repeated sampling rather than exposed directly, the sample count, smoothing rule and confidence procedure must be preregistered. Zero cell counts must not be converted into infinite log-odds without a declared finite-sample correction.

### 7.2 Deterministic score-based selectors

A deterministic selector may output only a winning candidate and raw candidate scores. A single 0/1 decision is not sufficient for finite log-odds estimation.

For a deterministic score-based system, define a measurement distribution over declared raw scores:

```math
\tilde p_i(T)
=
\frac{\exp(s_i/T)}{\sum_k\exp(s_k/T)},
```

where:

- \(s_i\) is the declared raw candidate score;
- \(T>0\) is a fixed, preregistered measurement temperature.

The resulting \(\tilde p_i(T)\) is a measurement mapping for analysis. It does not imply that the production selector samples probabilistically.

Sensitivity analysis should report whether conclusions persist across a small preregistered range of plausible temperatures.

### 7.3 Deterministic systems without candidate scores

Where only the selected label is observable, estimate selection frequencies over repeated matched trials with controlled perturbations or seeds. A single deterministic output cannot identify \(\lambda\).

---

## 8. Null and Alternative Hypotheses

Under the declared sign convention, the primary null is:

```math
H_0:\lambda=0.
```

The directional alternative is:

```math
H_1:\lambda>0.
```

Under \(H_0\):

```math
p_\lambda(a_i\mid x_t,S_t,H_t)
=
p_0(a_i\mid x_t,S_t).
```

A robust negative estimate of \(\lambda\) is not counted as support for Verrell's Law under this directional formulation. It would indicate an inverse retained-state effect requiring separate explanation and a revised hypothesis.

---

## 9. Estimation and Uncertainty

For paired binary trials \(k=1,\ldots,N\), fit:

```math
\Delta L_k
=
\alpha
+
\lambda\Delta R_k
+
\varepsilon_k.
```

Estimate \(\alpha\) and \(\lambda\) by ordinary least squares, robust regression, or another preregistered estimator appropriate to the measurement process.

Confidence intervals should be obtained by bootstrap resampling over the preregistered trial units unless a stronger justified error model is specified in advance.

Required diagnostics include:

- whether \(\alpha\) is compatible with zero;
- whether \(\lambda\) is positive and distinguishable from zero;
- whether residuals show systematic structure;
- whether residuals are correlated with \(\Delta R\);
- whether the estimate is stable across repetitions;
- whether the fitted model predicts held-out trials.

For \(K>2\) candidates, estimate retained-state influence with multinomial logistic regression using candidate-relative \(R_i\) as the retained-state covariate, with the baseline and normalization fixed before testing.

---

## 10. Experimental Design and Controls

Use paired or twin-run trials wherever possible.

### Retained-state-off condition

The tested retained-state contribution is disabled, neutralized, ablated, randomized, or replaced by a preregistered matched control.

### Retained-state-on condition

The current input, candidates, model and version, sampling parameters, random seed where supported, and declared present-state variables are held fixed while the specified retained state is present.

The following must remain fixed or be explicitly modelled:

- current input;
- present system state;
- candidate set and candidate ordering;
- model and version;
- system and developer instructions;
- sampling parameters;
- random seed where supported;
- tool availability;
- hidden or cached system state;
- context length and truncation behaviour;
- software configuration;
- hardware configuration where relevant;
- scoring and normalization convention;
- stopping and exclusion rules.

A trial is invalid if retained-state-on and retained-state-off conditions differ in uncontrolled ways material to selection.

---

## 11. Preregistration Requirements

Before data collection, freeze and timestamp:

- the principal hypothesis and sign convention;
- the retained-state scoring function;
- all score ranges and normalization rules;
- the definition of the baseline condition;
- the tested regime;
- the candidate construction procedure;
- the trial count and stopping rule;
- the observable extraction method;
- the estimator and bootstrap procedure;
- exclusion and invalidation criteria;
- significance or decision thresholds;
- primary and secondary outcomes;
- the out-of-sample validation procedure.

Exploratory analyses may be reported, but they must be clearly separated from confirmatory preregistered tests.

---

## 12. Falsification Conditions

The hypothesis is weakened or rejected for the tested regime when one or more of the following holds:

1. The best-supported \(\lambda\) is statistically compatible with zero.
2. The fitted \(\lambda\) is reliably negative under the declared compatibility sign convention.
3. The measured relationship disappears under preregistered replication.
4. The estimate is unstable across equivalent repetitions within the declared regime.
5. Shuffled, irrelevant or adversarially mismatched retained states perform as well as the preregistered compatibility score.
6. The apparent effect is explained by prompt leakage, candidate leakage, ordinary context injection, truncation, hidden state or another uncontrolled variable.
7. A materially non-zero intercept indicates systematic mismatch between conditions.
8. Residuals remain systematically correlated with \(\Delta R\) or show strong preregistered model violation.
9. The result depends on post-hoc changes to scoring weights, exclusions, normalization or stopping rules.
10. A simpler baseline model explains the observations equally well or better.
11. The fitted relationship fails to predict held-out trials.
12. Independent replication fails under the same declared regime.

The correct verdict is:

> rejected or not supported in the tested regime.

It is not:

> disproven everywhere.

---

## 13. Linearity and Domain of Validity

The relation

```math
\Delta L=\lambda\Delta R
```

is a first-order modelling assumption.

Linearity must be checked through residual diagnostics and held-out prediction. A saturating, thresholded, asymmetric or higher-order response may indicate that the linear model has a bounded domain of validity.

Such findings do not automatically support the present law. They require a separately specified and preregistered alternative model.

---

## 14. What a Positive Result Would and Would Not Establish

A stable, positive, replicated and out-of-sample-predictive \(\lambda\) would support a retained-state selection effect in the tested regime under the declared scoring and normalization convention.

It would **not by itself establish**:

- consciousness;
- sentience;
- quantum wave-function collapse;
- electromagnetic causation;
- a universal physical law;
- biological equivalence;
- subjective experience;
- non-local memory;
- substrate independence.

Each of those would require additional hypotheses, controls and independent evidence.

---

## 15. Relationship to Collapse Aware AI

Collapse Aware AI is an engineering track inspired by retained-state selection principles.

It can demonstrate that governed retained-state influence can be implemented, measured and evaluated in software. It does not independently prove that the same mechanism occurs naturally in biological or physical systems.

The separation is:

```text
Verrell's Law
= empirical retained-state selection hypothesis

Collapse Aware AI
= engineering implementation of governed retained-state behavioural selection

Physical interpretation
= separate research layer requiring independent evidence
```

Proprietary production scoring, thresholds, schemas and implementation mechanics are not disclosed by this specification.

---

## 16. Minimum Evidence Standard

A credible confirmatory report should include:

- the complete preregistration;
- full protocol and regime definition;
- all variable and score definitions;
- normalization and sign conventions;
- raw or minimally processed trial data;
- baseline and retained-state observables;
- fitted \(\alpha\) and \(\lambda\);
- bootstrap confidence intervals;
- effect-size interpretation tied to the declared scale;
- residual and sensitivity diagnostics;
- shuffled and irrelevant-state controls;
- held-out predictive results;
- replication results;
- code, seeds and version identifiers where disclosure is possible.

---

## 17. Canonical Claim

> Verrell's Law proposes that, within a declared and controlled regime, candidate-relative retained-state compatibility produces a positive, quantitatively structured change in selection log-odds relative to a present-state baseline.

In first-order form:

```math
\Delta L=\lambda\Delta R,
\qquad
\lambda>0.
```

The claim is rejected for a tested regime when \(\lambda\) is zero, negative under the declared sign convention, unstable, non-predictive, attributable to uncontrolled variables, or otherwise fails the preregistered falsification conditions.

---

## 18. Closing Statement

The purpose of this specification is not to establish Verrell's Law as true. It is to define precisely the conditions under which the hypothesis can be supported, refined or rejected through reproducible measurement.

---

## Citation

**Ross, M. V. M. (2026). _Verrell's Law: Mathematical Foundations and Falsification Protocol — Canonical Specification v1.0_. Inappropriate Media Limited.**

---

Copyright © 2026 Marcos Verrell Moss Ross (M.R.) / Inappropriate Media Limited. All rights reserved.