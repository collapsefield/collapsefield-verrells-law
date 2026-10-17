# Verrell’s Law — Mathematical Clarification Supplement v1.0

**Status:** Published clarification supplement — not experimental confirmation  
**Published:** 17 October 2026  
**Author/originator of research framework:** Marcos Verrell Moss Ross (M.R.)  
**Purpose:** Resolve statistical, normalization, identification and evidence-language ambiguities without changing the canonical retained-state selection equation.
**Versioning:** First issue of the *Mathematical Clarification Supplement* series (v1.0); distinct from the existing *Empirical Identification Clarification v1.0*.

## 0. Authority, scope and publication control

This supplement is a clarification to `VERRELLS_LAW_MATHEMATICAL_FOUNDATIONS_AND_FALSIFICATION_PROTOCOL_v1.0.md` and `VERRELLS_LAW_EMPIRICAL_IDENTIFICATION_CLARIFICATION_v1.0.md`, alongside `VERRELLS_LAW_MATHEMATICAL_REFERENCE_v1.3.md` and `FALSIFIABLE_MEMORY_BIAS_ESTIMATOR.md`. It is **not** a new physical law, a replacement for those historical files, experimental confirmation, or evidence that any real study has been preregistered. This document clarifies superseded or ambiguous guidance only where explicitly identified below. Existing files and their attribution trail remain preserved. No software implementation or independent scientific experiment is claimed.

A deliberately programmed retained-state simulator verifies implementation conformance (the existing Route B), **not** a physical retained-state hypothesis. Engineering evidence from software designed around retained-state weighting is Route B conformance; such evidence does not independently validate a physical hypothesis.

## 1. Canonical model and empirical interpretation

For candidate outcomes `a_i` and declared current-condition controls, define the baseline selection probability `p_0,i > 0`, and a frozen retained-state compatibility score `R_i`. The proposed exponential-tilt family is

```math
p_{\lambda,i}=\frac{p_{0,i}\exp(\lambda R_i)}{\sum_jp_{0,j}\exp(\lambda R_j)}.
```

For two candidates `a` and `b`, put `\Delta R=R_a-R_b` and

```math
\Delta L=\log\frac{p_{\lambda,a}}{p_{\lambda,b}}-\log\frac{p_{0,a}}{p_{0,b}}.
```

Then **exactly under this mathematical model**:

```math
\Delta L=\lambda\Delta R.
```

This is not merely a first-order approximation *within the stated exponential-tilt model*. Whether external observations obey this linear relationship over a given regime is a **falsifiable empirical modelling hypothesis**; saturation, thresholds, asymmetry, changing candidate sets, misspecification and unknown baseline mechanisms may violate it. “First-order” may describe an intended empirical approximation or a local expansion of an alternative model, but must not describe the algebraic identity under the stated family. This equation and conventional softmax/logit machinery are **not claimed as mathematically novel**.

Parameter `\lambda` is interpretable only relative to a fixed definition, scale and sign convention for `R`. Rescaling `R` rescales `\lambda`; the two cannot be independently identified without constraints.

**Evidence vocabulary (applies to research and engineering reports):**

1. **Score influence:** changes in raw candidate scores or analytical compatibility measures.
2. **Winner change:** an observed change in the actually selected candidate under specified selection rules.
3. **Choice-probability change:** a change in independently observed/model-provided choice probabilities, or in choice frequencies estimated with declared uncertainty.

Do not infer winner change from score change. Do not label a post-hoc softmax applied to deterministic raw scores as observed production choice probabilities. Do not infer probabilistic selection from a single deterministic winner.

## 2. Compatibility score domains and edge cases

The canonical illustrative aggregate is

```math
R_i=\frac{1}{n}\sum_{j=1}^{n}s_jd_jq_jr_{ij}.
```

Unless an alternative is preregistered, use the defensible sign convention:

- `s_j \in [0,1]`: nonnegative salience magnitude;
- `d_j \in [0,1]`: nonnegative persistence magnitude;
- `q_j \in [0,1]`: nonnegative reliability magnitude;
- `r_{ij}\in[-1,1]`: signed compatibility of item `j` with candidate `i`.

This removes accidental sign reversals caused by multiplying several supposedly magnitude-valued signed weights. If a proposed domain scientifically requires signed salience, persistence or reliability, justify and preregister that *different* model explicitly; it is not the default.

**Eligibility:** State before analysis which retained items are eligible, what `n` counts, whether an irrelevant but valid item (e.g. `r_ij = 0`) remains in `n`, and whether any item can be excluded by a preregistered quality threshold. Missing/non-finite/invalid values must not be silently clamped, zero-filled, dropped or normalized after seeing outcomes. Preregister one rule: invalidate a trial, use independently specified imputation plus missingness indicators, or omit only if eligibility rules are satisfied before outcome inspection. Record exclusions and sensitivity analyses.

**Empty retained set:** Set `R_i := 0` for all candidates when `n=0`, provided this is the declared neutral baseline; log the condition. This is a convention, not measured evidence for zero physical memory.

**Normalization is an estimand choice, not a universal repair:** Under `1/n`, appending eligible zero-compatibility items dilutes magnitude (e.g. one `r=0.8` becomes `0.4` with one new eligible zero item). This may or may not be desired. A permissible alternative with defined positive denominator is

```math
R_i=\frac{\sum_j w_jr_{ij}}{\sum_j w_j},\quad w_j=s_jd_jq_j\geq0,\quad \sum_jw_j>0.
```

If the sum of weights is zero, define `R_i:=0` under a preregistered neutral convention or mark invalid under a preregistered rule. **Do not automatically choose the weighted version.** It changes the meaning of `R`: average over all eligible items versus weighted compatible influence among nonzero weights. In particular, multiplying all strictly positive `w_j` by the same positive constant leaves the weighted mean unchanged (where the scaled values remain within the declared domain). Thus common scaling of all salience/persistence/reliability weights cannot strengthen aggregate influence under this normalization: those weights determine the *relative composition* of the score, while the overall contribution is governed by the separate coupling `\lambda` (or a separately preregistered amplitude term). Under `1/n`, changing weight magnitudes generally changes the score. The weighted mean excludes zero-weight items from the denominator but still dilutes `R_i` when positively weighted items have `r_ij=0`; it does **not** cure dilution by irrelevant-but-weighted items. This difference must be an explicit part of the estimand choice. Select the estimand, denominator, scale, item-count policy and zero-denominator behavior *before testing*. Report the item-count and dilution sensitivity on declared held-out or secondary analyses without changing the primary definition afterward.

## 3. Identification and causal design

The existing three routes remain authoritative:

- **Route A — independent score:** freeze a domain-specific function `R_i=g(H,x,S,a_i)` without consulting confirmatory outcomes. Preferred for independent empirical tests.
- **Route B — selector-internal score:** exporting and checking the exact score used by a software selector is engineering conformance, not independent physical evidence.
- **Route C — proxy:** independent measured proxy `X` requires a specified measurement map `R=g(X)`, or the estimated coefficient must be labelled a proxy-conditioned/composite effect rather than canonical `\lambda`.

Randomizing **assigned history** can support a causal estimate of the assignment's effect on choice under valid randomization and controls. It does not guarantee that a `R` constructed after the assignment is exogenous. Outcome-derived scores, conditioning on treatment-affected selection criteria or post-treatment covariates, selective attrition, leakage and hidden state can create bias. Distinguish intention-to-treat effects of assigned history from estimates of `\lambda` through a potentially endogenous measured score. Predeclare the mapping, timing of `R` measurement, blinding where possible, and the analysis target.

The statement `E[\varepsilon\mid\Delta R]=0` (or an analogous orthogonality requirement) is a modelling/identification assumption. Regression-fitted residual orthogonality in training data **cannot** verify it. Test the design through randomization checks, measurement independence, controls and negative controls; report sensitivity to plausible violations.

## 4. Estimators by observation type

There is **no universal estimator** applicable to all observation types. Predeclare the observation process, independent sampling units, clustering and nuisance parameters.

### 4.1 Observed probabilities / externally measured log-odds

When both baseline and conditioned candidate probabilities are genuinely available, form candidate-relative log-odds differences and fit the predeclared regression

```math
\Delta L_k=\alpha+\lambda\Delta R_k+\varepsilon_k.
```

An **intercept is primary** so baseline mismatch (`\alpha\ne0`) remains diagnosable; a through-origin restriction is a justified secondary/sensitivity analysis, not the default. If the probabilities were estimated rather than directly available, propagate their uncertainty and dependence rather than treating log-odds as equally precise direct observations. Use robust/clustered uncertainty as warranted by the trial design; do not bootstrap non-independent rows as though independent. Cluster or block bootstrap at the genuinely independent-unit level remains acceptable when justified by the sampling design.

### 4.2 Sampled binary or multinomial choices

When observing choices or counts instead of probabilities, primary inference should use the appropriate **binomial/conditional-logit or multinomial likelihood** with declared baseline log-odds/utility offsets when independently known, trial structure and covariate `\Delta R`. When baseline is not known, estimate it under an identifiable randomized/matched design and treat its uncertainty properly. Include an intercept or stratum-specific effects to diagnose baseline mismatch where identifiable; do not add an intercept that is confounded with fixed effects or offsets without specifying the design.

Repeated trials from the same subject, history snapshot or experimental unit require paired, cluster-robust, hierarchical or appropriately blocked inference. Empty choice cells require design-appropriate methods (e.g. penalization/exact or Bayesian sensitivity); arbitrary smoothing must not silently manufacture a finite effect. OLS of estimated log-odds is secondary and requires justified weighting and uncertainty propagation.

### 4.3 Deterministic systems with raw candidate scores

If the selector returns scores `s_i` and deterministically chooses `argmax_i(s_i)`, examine candidate-relative **raw score differences** directly, provided score scale and comparison conditions are frozen. An optional declared analytic mapping `softmax(s/T)` is **not** an observed sampling distribution: in a two-candidate comparison, mapped log-odds equal `(s_a-s_b)/T` exactly. Changing `T` merely rescales that mapped coefficient, so it is not an independent robustness test of the underlying mechanism. Drop automatic temperature-sensitivity requirements; do not claim score differences imply winner changes. When a constructed selector directly computes `z_i=z_{0,i}+\lambda R_i`, regressing its own candidate-relative score change on its exported `\Delta R` can recover the configured `\lambda` algebraically (and achieve near-perfect fit absent numerical/implementation differences). This is **Route B engineering conformance**, not independent empirical identification of a law. Report score scale, ties, margins, constraints and measured selected winners separately.

If a deterministic system exports winners alone, one matched decision is insufficient to estimate finite log-odds. Repeated decisions with preregistered perturbations can estimate frequencies over that intervention distribution; those frequencies are not intrinsic probabilities of an unchanged deterministic selector.

## 5. Diagnostics: replace vacuous in-sample score-equation checks

Do **not** use the in-sample raw-residual/predictor cross-product as a falsification diagnostic when the fitting method forces it to vanish. With OLS, the fitted predictor-residual cross-product is zero by the normal equations (with or without an intercept). With ordinary maximum-likelihood binomial logistic and multinomial/conditional-logit models, the relevant observed-minus-fitted choice residuals satisfy analogous score equations for included covariates at an interior optimum. These properties can hold even under substantial model misspecification. They do **not** establish exogeneity, calibration or correctness. The precise residual definition, weights and score equations depend on the estimator; do not assume all residual transformations share the property.

Preregister diagnostic methods appropriate to the observation type, including:

- out-of-sample residual or calibration analysis;
- binned residual/observed-minus-predicted patterns across `\Delta R`;
- predeclared nonlinear terms such as `\Delta R^2`, splines or a RESET-style specification test **where statistically appropriate**;
- intercept/baseline mismatch on genuinely independent observations;
- saturation, interaction, outlier, leverage and regime-heterogeneity diagnostics;
- held-out predictive fit and uncertainty, not training fit alone.

Nonlinear exploratory diagnostics do not automatically become confirmatory evidence: if inspection suggests a different model, preregister it for a separate untouched test.

## 6. Falsification, statistical power and verdicts

Before confirmatory observations, set: the primary test, direction/sign, null region, scientifically relevant minimum effect size `\delta`, desired power, sample size calculation/simulation, uncertainty method, significance/decision rule, stopping rule and data-validity criteria. The precision of `\lambda` depends on fixed `R` normalization. Sensitivity to measurement reliability and baseline uncertainty must enter power planning.

Use **three possible outcomes** for the *retained-state effect* in each declared regime:

1. **Retained-state effect supported in the tested regime:** the preregistered directional effect is identified with an appropriate estimator, sufficient uncertainty control, successful validity checks and held-out predictive performance relative to the no-history baseline. This does **not** by itself claim an advantage over conventional history-dependent models or establish a physical mechanism.
2. **Retained-state effect not supported / refuted in the tested regime:** a prespecified equivalence or other adequately powered test rules out an effect of at least the declared meaningful size, or a specified falsifier such as reliably wrong direction, failed causal manipulation or **adequately powered** failed held-out prediction applies. Failure to reject `\lambda=0` is **not** by itself evidence of absence.
3. **Indeterminate:** insufficient power, weak measurement reliability, intervals compatible with both null and meaningful effects, invalid protocol, failed identification or unresolved mismatch prevents a defensible verdict.

Report a **separate distinctive-model-advantage verdict**: *supported* only when the independently specified `R` beats the preregistered conventional history-model comparators under the prespecified held-out metric, uncertainty treatment, complexity controls and minimum margin; otherwise *not demonstrated* or *indeterminate* as appropriate. It is possible to support a retained-history effect while demonstrating **no distinctive advantage** for the proposed `R`. Do not conflate these two conclusions.

The word **refuted** must be scoped to the predeclared claim/regime and evidence quality; an underpowered null cannot be promoted to global falsification. Define exactly when an equivalence margin or smallest-effect threshold is used and which test supplies it.

**Revised interpretation of canonical falsification condition 1:** “Statistically compatible with zero” alone leads to **indeterminate** unless the design has adequate resolution to exclude the preregistered meaningful positive effect or a separate falsifier applies.

**Revised condition 8:** Replace “fitted residuals correlated with `\Delta R`” with “predeclared out-of-sample residual/calibration patterns or nonlinear specification checks demonstrate material model failure,” avoiding automatic in-sample OLS or canonical-link score-equation orthogonality.

## 7. Explicit conventional comparators and judging rules

Choose the applicable comparators **before** data collection, with fair access to the same allowed inputs and comparable training opportunities. Candidate families include:

- choice-kernel/perseveration models;
- Rescorla–Wagner updating and/or Q-learning with softmax selection;
- an exponential-decay recency kernel;
- a Markov model with an adequately specified augmented state;
- hysteresis models;
- a present-state-only baseline;
- where physical systems are involved, established non-Markovian/memory-kernel models appropriate to the apparatus.

Several comparators (including perseveration/choice-kernel models and softmax Q-learning) can themselves be written in exponential-tilt or additive-logit form. Accordingly, a substantive comparison often tests **which independently defined retained-state construction `R` predicts better**, rather than the novelty of softmax or a different functional form. Not every comparator is applicable to every domain; preregister the rationale and how each model's parameters are fitted. Compare **held-out log-likelihood**, proper predictive scores (e.g. log-loss/Brier where appropriate) or another prespecified, justified metric. Account for complexity through nested validation, penalization or a properly designed model-selection procedure, not an arbitrary after-the-fact preference for the proposed model. Fix minimum improvement margin, evaluation units and tie/non-inferiority rules before confirmatory trials. If a simpler comparator meets or exceeds the prespecified criterion, do not claim a distinctive retained-state model advantage, even if an effect of assigned history exists.

## 8. Multiple tests and generalizability

Declare a single primary confirmatory endpoint/test per study unless a formal multiple-primary strategy is preregistered. Treat additional snapshots, candidate pairs, regimes, comparators, score normalizations, nonlinear explorations and physical substrates as secondary, exploratory or multiplicity-adjusted confirmatory analyses. State correction/family definition before outcomes. Split training/tuning, validation and final untouched test data at the **independent unit** level to avoid history or subject leakage. Report heterogeneity and failures rather than pooling away contradictions; performance in one regime does not transfer automatically to others.

## 9. Preregistration and evidence boundaries

The archive contains **preregistration requirements**, not proof that a particular experiment has been preregistered. A future confirmatory study requires a real, externally timestamped protocol specifying the score-construction route, variables, exclusion rules, primary tests, power, analysis and deviations. Exploratory simulations and constructed examples must be clearly labelled as such.

A proposed simulator that numerically follows `\Delta L=\lambda\Delta R` is useful for verifying algebra, implementation, sensitivity and failure cases; it is **Route B engineering conformance**. It cannot establish independent physics, biological transfer or superiority over conventional models unless an independent experimental system, appropriately frozen predictors and valid controls are introduced.

## 10. Cross-reference updates

The publication includes minimal cross-reference updates and adjacent annotations, without wholesale historical rewrites:

1. `README.md`: link to this clarification beside the canonical foundations and empirical-identification clarification; change “canonical first-order relationship” to “canonical exponential-tilt relation (exact within the stated selection model; empirical outside it)” or equivalent precise wording.
2. `VERRELLS_LAW_MATHEMATICAL_FOUNDATIONS_AND_FALSIFICATION_PROTOCOL_v1.0.md`: add top-level pointer to this supplement. Cross-reference §3 for signed domains, empty set and normalization; §4 for exogeneity/causal identification; §§6/13 for exact-versus-empirical wording; §7 for raw-score vs probability distinction; §9 for appropriate estimators and held-out residual tests; §§8/12 for power and indeterminate verdict; §§10–11 for comparators and multiplicity. Insert **seven minimal inline errata pointers** at canonical §3 (old signed domains), §4 (old near-zero rejection rule), §7.2 (temperature sensitivity), §9 diagnostic bullet 4 (OLS residual correlation), §12 condition 1 (near-zero rejection), §12 condition 8 (OLS residual correlation), and §17 (old near-zero rejection rule), referencing the corresponding supplement sections. Do not silently rewrite original history.
3. `VERRELLS_LAW_EMPIRICAL_IDENTIFICATION_CLARIFICATION_v1.0.md`: short pointer preserving Routes A/B/C, noting post-treatment score risks and distinct score/winner/probability evidence.
4. `FALSIFIABLE_MEMORY_BIAS_ESTIMATOR.md`: add a pointer identifying the with-intercept specification and likelihood-based count models as primary where appropriate, and through-origin OLS as secondary.
5. `FALSIFICATION_CONDITIONS.md`: add pointer clarifying null-compatibility versus an adequately powered absence/equivalence result.
6. `VERRELLS_LAW_MATHEMATICAL_REFERENCE_v1.3.md`: link clarification; keep its historical reference intact.
7. `PUBLIC_READER_START_HERE.md`: add the supplement to reading order and retain “not established physics”.
8. Repository About descriptions (separate metadata edits; not part of this file commit):
   - Main research archive: **“Verrell’s Law: a proposed, falsifiable retained-state selection framework. Not established physics.”**
   - Historical tensor archive: **“Historical speculative physics extension of Verrell’s Law; not part of the current canonical framework.”**

Maintain the separation between the scientific research archive and unrelated software engineering or outreach materials. No engineering repositories or runtime packages are within the scope of this clarification.

## 11. Outstanding review decisions

- Which application domain will first supply a genuinely independent and preregistered `R`? A simulation coded to obey the proposed selection law is **not** an eligible independent test.
- Which normalization and meaningful effect margin apply to that domain? The supplement offers design choices, not universal numbers.
- What is the primary observation process (choice counts, model probabilities, independent outcomes or deterministic scores) and what is the independent unit for power calculations?
- **Publication disposition:** add short inline errata notes at all seven superseded canonical locations: §3 signed-weight defaults (this supplement §2); §4 near-zero rejection language (§6); §7.2 temperature sensitivity (§4.3); §9 residual-diagnostic bullet 4 (§5); §12 condition 1 (§6); §12 condition 8 (§5); and §17 near-zero rejection language (§6). Preserve historical text; add only a one-line adjacent pointer at each location.

## 12. Canonical errata annotations

Keep the superseded canonical sentences visible as historical text; the annotation for each is placed immediately after the affected sentence, bullet or condition:

| Canonical location | Adjacent one-line annotation |
|---|---|
| §3, default signed domains | *[Clarification: Mathematical Clarification Supplement v1.0 §2 supersedes the default sign domains; only candidate compatibility is signed by default.]* |
| §4, rejection on statistical compatibility with zero | *[Clarification: Mathematical Clarification Supplement v1.0 §6 requires power and an indeterminate verdict where meaningful effects cannot be ruled out.]* |
| §7.2, temperature sensitivity | *[Clarification: Mathematical Clarification Supplement v1.0 §4.3 explains why temperature rescaling alone is not a substantive robustness test.]* |
| §9, residual-correlation diagnostic bullet 4 | *[Clarification: Mathematical Clarification Supplement v1.0 §5 replaces vacuous in-sample residual orthogonality with held-out/calibration and nonlinear checks.]* |
| §12, falsification condition 1 | *[Clarification: Mathematical Clarification Supplement v1.0 §6 distinguishes adequately powered absence/equivalence from indeterminate null-compatible results.]* |
| §12, falsification condition 8 | *[Clarification: Mathematical Clarification Supplement v1.0 §5 replaces estimator-imposed residual orthogonality checks with valid specification diagnostics.]* |
| §17, rejection on zero coupling | *[Clarification: Mathematical Clarification Supplement v1.0 §6 requires adequate power, prespecified meaningful effects and a three-way verdict.]* |

These are the one-line annotations accompanying this supplement in the canonical document.

## Suggested citation and rights

Ross, M. V. M. (2026). *Verrell’s Law — Mathematical Clarification Supplement v1.0*. Research clarification, published 17 October 2026. Supplement to *Mathematical Foundations and Falsification Protocol v1.0*; not empirical confirmation.

Copyright © 2026 Marcos Verrell Moss Ross (M.R.). All rights reserved except as specified by the applicable repository licence when published.

