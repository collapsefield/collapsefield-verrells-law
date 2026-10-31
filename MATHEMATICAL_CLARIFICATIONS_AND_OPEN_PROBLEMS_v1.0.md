# Verrell's Law — Mathematical Clarifications and Open Problems v1.0

**Status:** Documentation addendum — not experimental confirmation.  
**Prepared:** 31 October 2026  
**Published:** 31 October 2026  
**Author / originator of Verrell's Law:** Marcos Verrell Moss Ross (M.R.)

## 1. Scope and existing authority

This note addresses remaining specification gaps. It does not replace the [canonical mathematical specification](VERRELLS_LAW_MATHEMATICAL_FOUNDATIONS_AND_FALSIFICATION_PROTOCOL_v1.0.md), the [17 October mathematical supplement](VERRELLS_LAW_MATHEMATICAL_CLARIFICATION_SUPPLEMENT_v1.0.md), or the [empirical-identification clarification](VERRELLS_LAW_EMPIRICAL_IDENTIFICATION_CLARIFICATION_v1.0.md). Their score definitions, Routes A/B/C, normalization safeguards, estimator guidance and three-way statistical verdicts remain applicable. Historical files, dates and authorship remain intact.

Verrell's Law is a proposed retained-state selection framework. Its physical extension is a separate, unconfirmed hypothesis. Ordinary memory, path dependence, non-Markovianity and conventional logistic mathematics are not claimed as new discoveries.

## 2. Exact selection identity and binary evaluation model

For a fixed finite candidate set, positive baseline probabilities and finite frozen scores, the canonical family is

```math
p_{\lambda,i}=\frac{p_{0,i}e^{\lambda R_i}}{\sum_j p_{0,j}e^{\lambda R_j}}.
```

For candidates a and b, define

```math
r=\Delta R=R_a-R_b,\qquad
\Delta L=\log\frac{p_{\lambda,a}}{p_{\lambda,b}}-\log\frac{p_{0,a}}{p_{0,b}}.
```

Then ΔL = λr is exact within this specified family. Its applicability to independent observations is an empirical hypothesis; it is not a derivation of physical dynamics. The October supplement already resolves the older “first-order” wording.

For a genuinely binary choice, let Y=1 mean a and Y=0 mean b. If the baseline log-odds are independently known as b_k, the corresponding observation model is

```math
Y_k\sim\mathrm{Bernoulli}(p_k),\qquad
\log\frac{p_k}{1-p_k}=b_k+\alpha+\lambda r_k.
```

Here b_k is an offset; α is an identifiable baseline-mismatch term when the design permits one. Alternatively, a jointly estimated baseline may be specified as

```math
\log\frac{p_k}{1-p_k}=\beta_0+\beta^\top S_k+\lambda r_k.
```

This alternative adds an assumption: the declared present-condition covariates adequately specify baseline log-odds. The coefficients β are nuisance parameters, not separately measured physical constants. A fitted intercept in this joint model is part of the baseline, not automatically evidence of mismatch. Baseline uncertainty must enter inference and held-out evaluation. An unrestricted history-dependent baseline can absorb λr and destroy identification.

The Bernoulli likelihood accounts for choice randomness. An additional ε inside the logit requires a separately specified latent-noise distribution and marginal likelihood; it must not be silently imported from the regression on measured ΔL. Repeated choices require the dependence treatment specified in the October supplement.

For K>2, the pairwise logistic expression describes the probability of a **conditional on selection being a or b**. It is not the unconditional probability of a; full-set outcomes require the corresponding multinomial model.

Across histories A and B with the same baseline, the predicted difference of log-odds is λ[r(A)−r(B)]. Candidate contrast r and between-history contrast r(A)−r(B) must not be interchanged.

## 3. What identifies λ

Freezing a score is necessary but insufficient. A study must also establish:

- **Independent operationalization:** R is candidate-relative compatibility computed from declared pre-choice retained information. It is neither “amount of history” nor thermodynamic entropy by definition. Record its construction, timing, measurement reliability, sign and fixed scale. If standardized, freeze the reference mean and scale using an independent calibration/training set or a fully predeclared reference distribution.
- **Informative variation:** r must vary beyond what is explained exactly by the intercept, controls and stratum effects. For the joint logistic model, the design matrix [1, S, r] must have full column rank after declared reference constraints. Constant r, or r identical to a subject/condition indicator already included, cannot identify a separate λ. Near-collinearity or saturation can leave very little precision even without exact confounding.
- **Finite estimability:** full rank does not prevent complete or quasi-separation. Ordinary maximum-likelihood coefficients can diverge. Predeclare design-appropriate bias reduction, exact inference or a Bayesian model with disclosed priors and sensitivity analysis; these methods do not manufacture information absent from the experiment.
- **A defensible causal target:** randomized assigned history identifies its assignment effect under the design assumptions. It does not automatically identify the causal coefficient of a noisy, post-treatment score. Report that distinction rather than equating the two.

Candidate-common score shifts cancel: R_i → R_i+c leaves all selection probabilities unchanged. Thus absolute score levels are not identified from choices. Rescaling R_i → cR_i and λ → λ/c also preserves predictions for nonzero c; the declared orientation and normalization remove that ambiguity. With dimensionless R, λ is dimensionless. With a unit-bearing score, λ has reciprocal score units. It is not automatically comparable across domains.

The directional hypothesis remains λ>0, but estimation should permit negative coefficients so wrong-direction evidence remains observable. A positivity restriction must not make the directional test self-fulfilling.

The tilt preserves baseline support: a candidate with p_0=0 cannot acquire positive probability through any finite λR. Hard exclusions, changing candidate sets and changing baseline supports require explicit treatment. They cannot be described as ordinary finite log-odds shifts.

## 4. Thermodynamic connection: established constraints and open mapping

For ideal reset of an initially unbiased symmetric one-bit memory, under the conventional thermal assumptions, the familiar bound on mean heat delivered to a reservoir is

```math
\langle Q_{\mathrm{bath}}\rangle\ge k_B T\ln 2.
```

More generally, under the standard initially uncorrelated memory/thermal-reservoir assumptions, a memory entropy reduction ΔH=H_initial−H_final in nats gives a bound of the form ⟨Q_bath⟩≥k_B TΔH. This does not license applying the one-bit expression unchanged to correlated, feedback-driven or nonequilibrium preparations. State the physical assumptions and full accounting [1].

Stochastic thermodynamics supplies trajectory-level work, heat and entropy-production descriptions for specified dynamics and reservoirs [2]. These are established quantitative relationships. Neither reference identifies the framework's R with physical entropy or determines its λ.

The [September technical paper](Verrells_Law_Non_Markovian_Information_Paths_2026.pdf), §05, already proposes

```math
\langle Q\mid H,W\rangle
=Q_{\mathrm{base}}(\mathrm{protocol,error,bath})+\Delta Q_V(H,W).
```

This is a phenomenological decomposition, not a derived history-dependent heat law. Unless the baseline, residual function and parameters are independently constrained, any discrepancy can be assigned to ΔQ_V after the fact.

A quantitative physical test still needs a specified substrate, Hamiltonian or transition dynamics, preparation and reset protocol, physical observables defining weight, parameter units, and a fixed prediction distinguishing the proposed contribution from conventional accounting. Include logical entropy, correlations, finite-time losses, preparation costs and instrument drift where relevant. History erasure itself can change temperature and work expenditure; sham interventions must address those changes.

No quantitative map from the selection coefficient λ to heat, entropy production or kernel amplitude is established by the reviewed documents. In particular, λr is a log-odds contribution, not an energy. Equations such as ΔQ_V=k_B Tλr or a universal λ proportional to temperature do not follow from the selection model or Landauer's bound.

Measuring reset heat, or a history-dependent thermal difference already predicted by conventional physics, does not establish the proposed additional physical contribution. Thermal and selection endpoints require separate preregistered estimands unless a validated joint model links them.

## 5. Memory-kernel decomposition is not unique without restrictions

The September formulation proposes

```math
K_{\mathrm{eff}}=K_0+g(H,W;\theta)K_V.
```

The paper already requires a fixed candidate basis, scale and sign. Those restrictions must be operationalized. Without them, g→cg and K_V→K_V/c preserve the product. If K_0 can absorb the same functional component, the split into “conventional” and “additional” terms is also non-unique.

A test therefore needs independently constrained conventional dynamics, a normalized candidate kernel with fixed units and support, and preparation/intervention conditions that distinguish the candidate contribution from nuisance parameters. Parameter sensitivity or rank checks should show that the planned observations contain separating information. Better training fit alone does not identify a new mechanism.

In the generalized master equation, changes in the time-local term, initial-correlation inhomogeneity, control response and measurement process must also be distinguished from changes in the kernel. Matching the reduced system state does not match the full system–environment state; differing bath correlations can produce conventional history dependence. Any quantum instantiation must preserve valid operational probabilities and state evolution on its stated preparation domain.

This kernel model and the candidate-choice tilt are different model classes. A relation between their parameters must be derived or independently calibrated for a specified experiment; common terminology does not supply that relation.

## 6. Engineering boundary and minimum next experiment

The [October 2026 Memory-Weighted Selection second edition](https://github.com/collapsefield/memory-weighted-selection/tree/34bac70019021a55d8940a053173181fd645f510) specifies a **public candidate-selection reference**, with hard eligibility filtering, optional soft penalties, deterministic ranking, tie rules and an empty-set abstention path. It explicitly distinguishes that reference from proprietary Crown implementation.

In the hypothetical token expression softmax((z_i+w EBT_i)/T), `i` indexes tokens, `z_i` is the baseline token logit, `w` is a bias coefficient, and `T>0` is temperature. Here `EBT_i` is used solely as a placeholder for a hypothetical retained-history-dependent token-bias score; it is not an operationally defined quantity in the canonical framework, and no acronym expansion or verified runtime variable is asserted. Its scoring rule and scale would have to be specified before testing. **Core Gold** denotes the Phase-1 Collapse Aware AI (CAAI) middleware build, whose runtime claims require separate engineering evidence. This hypothetical expression is not evidence that Core Gold modifies token logits. Candidate ranking, stochastic candidate sampling and direct token-logit modification are different mechanisms. No private source code is assessed or disclosed here, and no audit-pending runtime claim is changed.

The next independent experiment must supply what the existing documents intentionally leave domain-specific: a frozen independently justified R, identifiable baseline, independent sampling unit, primary endpoint, smallest meaningful effect, power calculation, controls and untouched evaluation data. The October v0.1.5 synthetic analysis package does not supply a validated human-data loader, real baseline estimator, power planner or conventional-comparator battery.

Sparse data, separation or uncertain measurement may justify an **indeterminate** verdict. A nonsignificant coefficient alone does not refute the tested claim. Adequately precise equivalence, wrong-direction evidence and predeclared predictive failures must be interpreted under the October supplement. Report retained-history effects and distinctive advantage over conventional history models separately.

No experiment is preregistered by publishing this note. It introduces no experimental results, new proof or physical validation.

## References and review basis

1. Reeb, D. & Wolf, M. M. (2014). *An improved Landauer principle with finite-size corrections*. New Journal of Physics 16, 103011. [Paper](https://arxiv.org/abs/1306.4352), [DOI](https://doi.org/10.1088/1367-2630/16/10/103011).
2. Seifert, U. (2012). *Stochastic thermodynamics, fluctuation theorems, and molecular machines*. Reports on Progress in Physics 75, 126001. [Paper](https://arxiv.org/abs/1205.4176), [DOI](https://doi.org/10.1088/0034-4885/75/12/126001).

Repository review baseline: research archive commit `b290be4fa5bbfb245231cf138437db6f33d72e68`; engineering working-paper commit `34bac70019021a55d8940a053173181fd645f510`. This note adds explicit qualifications; it does not retrospectively change the status of earlier publications.

Copyright © 2026 Marcos Verrell Moss Ross (M.R.). Existing repository licensing and rights notices remain applicable.
