# Retained-State Dynamics and Live Weighting: Models, Identification and Tests

**Verrell’s Law — methods note**
**Author:** M.R.
**Version:** 0.5.1 methods note · **Date:** 15 November 2026
**Status:** Proposed operational models and mathematical verification. No empirical results and no experimental preregistration are reported. Every model below is an operational proposal for publication, not a canonical commitment. Published under M.R.’s authorisation following technical review.

## 1. Contribution and research question

Verrell’s Law investigates whether independently specified retained information predicts later weighting and selection when present inputs are matched. This note develops a family of candidate tests:

- fixed retained-state dynamics;
- a context-dependent readout weight, measured before selection;
- prospective comparisons against conventional history-sensitive models.

The contribution is a set of explicit modelling restrictions, their exact consequences, and the conditions needed to identify the models from data. A fixed leaky accumulator is the first comparator. It does not represent the whole framework, and its history effects are already conventional. A live-weighting model adds a conditional readout assumption to that comparator. Live weighting on its own is not claimed to be unique to Verrell’s Law or absent from established models.

Section 5.4 gives a structural test of the proposed decision-time weighting specialisation. It compares decision-time readout weighting with specified storage-gain and retention-change alternatives, under explicit controls. It does not establish that those alternatives exhaust possible mechanisms.

The retained-state proposition is unchanged. The candidate models do not replace the canonical equations and do not establish a cross-domain result. Their purpose is to turn an independently constructed score into predictions that can fail.

## 2. Selection form, variables and units

For fixed candidates, finite scores and common positive support, use the existing selection form:

$$z_i=U(y_i;S_t,O_t)+\lambda B(y_i;M_t),\qquad P_i=\frac{\exp(z_i)}{\sum_j\exp(z_j)}.$$

For candidates a and b, define the score contrast R_ab = B(a;M_t) − B(b;M_t). Then

$$L_t=\log\frac{P_t(a)}{P_t(b)}=U_{ab}(S_t,O_t)+\lambda R_{ab,t}.$$

This identity is exact within its specified model. Its empirical content depends on constructing the baseline and the score independently. A freely chosen score can reproduce any positive pairwise target distribution whenever the influence coefficient is nonzero. With more than two candidates, the pairwise log-odds equals the logit of the conditional probability of a given selection of a or b. It does not specify the unconditional probability of a.

**Variables.**

- S: declared present covariates.
- O: present input.
- M: retained state available before selection.

The S/M boundary, candidate orientation, score scale and reference distribution must all be specified before confirmation. Matching the observed S does not match the full physical state. Memory must never be defined after the fact as whatever the baseline failed to explain.

The public [Mathematical Clarifications and Open Problems](MATHEMATICAL_CLARIFICATIONS_AND_OPEN_PROBLEMS_v1.0.md), especially §§2, 3 and 5, sets out the existing identification boundary. Current vocabulary is indexed in [Information, Memory, Weighting and Bias](INFORMATION_MEMORY_WEIGHTING_AND_BIAS.md).

**Live weighting.** In this note, live weighting is a declared, context-dependent appraisal of how strongly retained information counts for the current selection. It is assigned for that decision before the outcome is observed, rather than fixed once and permanently at storage. Retained state and live weighting are kept as separate named terms.

This definition does not require every stored weight to change at every decision. Recording W in advance is necessary for the measurement-based tests below, but it does not by itself establish a causal mechanism. The operational definition does not establish that the framework is unique among conventional models.

## 3. Fixed-state comparator D1 and its kernel

For equally spaced steps and a scalar preparation input u_n:

$$m_{n+1}=\alpha m_n+\eta u_n,\qquad 0<\alpha<1,$$
$$L_n=U_{ab}(S_n,O_n)+\kappa m_n,\qquad \kappa=\lambda\zeta.$$

- ζ converts state into a score contrast. It is not the record reliability q_j.
- α is the retention per step.
- η has state/input units, and κ has inverse-state units, so log-odds are dimensionless.
- The current input O enters U immediately. The input u updates m at the next step. If one stimulus drives both pathways, both must be specified and controlled.

The exact solution is

$$m_n=\alpha^n m_0+\eta\sum_{j=0}^{n-1}\alpha^{n-1-j}u_j,$$
$$L_n-U_{ab}=\kappa\alpha^n m_0+\sum_{j=0}^{n-1}\mathcal K_{n-j}u_j,\qquad \mathcal K_\ell=\kappa\eta\alpha^{\ell-1},\quad \ell\ge1.$$

Different histories can change the state without changing this kernel. The initial-condition contribution must be kept. For bounded inputs:

$$|m_n|\le\alpha^n|m_0|+|\eta|u_{\max}\frac{1-\alpha^n}{1-\alpha}.$$

Two boundary cases are used as comparators:

- α = 0 retains only the last input.
- α = 1 is a perfect integrator, which can grow without bound under sustained input.

Linear state-space and convolution representations are established [1]. Eliminating hidden variables can produce reduced memory kernels, including in conventional Mori–Zwanzig models [2]. A kernel on its own does not identify the microscopic storage mechanism.

## 4. Identification, pulse calibration and held-out contrasts

Without extra measurements, only observable products are identified. The transformation (m, m₀, η, κ) → (c·m, c·m₀, c·η, κ/c), for any nonzero c, preserves all outputs. A negative c reverses the state orientation unless a physical sign convention rules it out. Pre-recording a weight does not remove this ambiguity. Either calibrate the state independently, or report the observable coupling together with its coordinate convention.

From a common reset state, compare five equal-length preparations: C = (0, +1), D = (0, 0), E = (+1, 0), A = (+1, −1) and B = (−1, +1). With U matched:

$$L_C-L_D=\kappa\eta,\qquad L_E-L_D=\alpha\kappa\eta,$$
$$L_A-L_D=(L_E-L_D)-(L_C-L_D),$$
$$L_A-L_B=2[(L_E-L_D)-(L_C-L_D)]=-2\kappa\eta(1-\alpha).$$

The factor of two separates the swapped-order contrast A − B from the one-history-versus-sham contrast A − D. Pulse calibration can estimate amplitude and retention. Order and delay trajectories that were not used in calibration then serve as confirmation. Under D1, the prediction of the order contrast from pulses is a test of superposition, and therefore of linearity. Joint fitting under a declared observation model is preferable to taking ratios of noisy estimates.

The immediate order effect is a recency signature: its magnitude is largest at α = 0 and zero at α = 1. After k common updates, the fixed linear model predicts

$$\Delta L_k=\alpha^k\Delta L_0.$$

This holds under any identical post-preparation input schedule, provided the direct readout conditions stay matched. Different common schedules must give the same contrast trajectory.

Persistence beyond the first update, and agreement at held-out delays, are separate tests. An immediate order effect on its own does not establish long retention. A fixed nonlinear update can break the common-schedule invariance, so a failure of that invariance does not uniquely identify adaptive kernels.

## 5. Candidate live-weighting model D3-w

At a specified readout, the proposed restricted operational score is

$$R_{ab,n}=W_n\zeta m_n,\qquad L_n=U_{ab}(S_n,O_n)+\kappa W_n m_n.$$

This is a candidate specialisation for review, not a new canonical requirement.

W is dimensionless. Its scale, orientation, range and measurement or assignment rule must be fixed independently, and its timing and uncertainty must be recorded. Three variables must be kept distinct:

- a randomly assigned context cue C;
- a prescribed numerical weight W(C);
- a measured appraisal W_obs.

Assigning a cue does not prove that the system implemented W(C).

### 5.1 Paired-probe prediction

Let the probe v enter the state-input channel at post-preparation step 0. In D1, the incremental state at readout k ≥ 1 is δm_k = η·α^(k−1)·v. If probe and sham share the same externally fixed W at that readout, and the direct response U is matched, D3-w predicts

$$\delta L_k=\kappa W\eta\alpha^{k-1}v.$$

D1 predicts the same expression without W. For histories with the same W at readout, their contrast is κ·W·Δm. Equal W across each comparison is a substantive condition. It does not follow from recording W before selection.

In general, probe and sham may have different weights and different direct responses:

$$\delta L_k=\delta U_k+\kappa[W_p m_p-W_s m_s]
=\delta U_k+\kappa[W_s\delta m_k+(W_p-W_s)m_p].$$

The extra term matters whenever the probe changes the appraisal. A pre-choice record can still be taken after the probe or after the context, so the term must not be dropped unless the design justifies it. Likewise, when W differs between histories, the contrast is κ·(W_A·m_A − W_B·m_B), not in general κ·W·Δm.

### 5.2 Controls and identification

Changing the context changes a present input. It is therefore not legitimate to claim that all present inputs are identical while the context varies. Instead:

- randomise the context;
- compare matched probe/sham and history contrasts *within* each context;
- then test their prespecified variation across contexts.

A cue may directly alter the baseline, gain, attention, retrieval or state. Identical stored history does not imply identical activated state.

Required controls are context-only, history-off, probe/sham and history-reversal conditions. Where possible, fix or independently measure the relevant state. Freeze the direct context/probe alternatives and the conventional context-sensitive gain and readout models before confirmation.

Measuring W before the choice is necessary for the proposed measurement-based test, but it is not sufficient for causal or parameter identification. Identification also needs adequate rank, independent variation, reliable measurement and a defensible baseline.

D2 may be a fixed nonlinear state or readout model. For example, the single fixed function G(C, m) = κ·C·m reproduces D3-w exactly when W = C. Even perfect proportional scaling cannot distinguish these unrestricted descriptions. The scientific target is therefore held-out advantage against *specified, restricted* comparators. It is not a claim that live weighting lies outside ordinary dynamics. Implementing W directly in a software selector shows conformance to that construction. It is not independent evidence of a naturally occurring mechanism.

### 5.3 Conditional regression and constrained predictions

At a fixed delay, take history H ∈ {0, 1}. Suppose m_pre = m_base + Δm·H and the probe response is η·α^(k−1)·v. For a fixed exogenous W, and a direct baseline U(W, S) with no history/probe interaction, the model is

$$L=U(W,S)+\kappa W[\alpha^k(m_{base}+\Delta_m H)+\eta\alpha^{k-1}v].$$

The restricted predictions are then:

- β_Wv = κ·η·α^(k−1);
- β_WH = κ·α^k·Δm;
- the history–probe interaction is zero in this fixed additive state model.

The signs come from the independently oriented coupling and the state/probe direction, so β_Wv is not automatically positive. If the context has a direct W–v interaction, its coefficient is confounded with the proposed memory-mediated β_Wv, unless that interaction is independently constrained or measured.

A factorial conditional regression can include the terms 1, H, v, Hv, W, Wv and WH, with a declared reference coding. The following must be frozen in advance:

- the link function;
- nuisance terms;
- clustering;
- the treatment of state and weight measurement uncertainty.

For binary outcomes, use a conditional or hierarchical observation model. For LLM logits, analyse the continuous candidate log-odds directly rather than inventing Bernoulli repetitions. A finite set of probe amplitudes does not establish linearity everywhere. The algebraic regression check below supplies no false-positive rate or power guarantee.

### 5.4 Locus of weighting: decision-time readout versus storage

For the proposed decision-time readout specialisation, retained information is weighted when the decision is made. This gives a structural prediction that differs from the specified pure post-context input-gain and retention-change alternatives below.

**Design.** Run the steps in this order:

1. Prepare the history.
2. Assign the context after preparation. In a temporally implemented experiment this prevents it from changing the original encoding retrospectively, but context may still alter subsequent state, retrieval or activation; these pathways require controls.
3. Apply the probe or sham.
4. Read out k steps later.

Within each context c, measure two contrasts:

- the history contrast h_c, under sham, between history on and history off;
- the probe effect p_c, under history off, between probe and sham.

Direct, additive context effects on U cancel inside both within-context contrasts.

**Predictions.** Assume a constant W_c for each context, shared across the four cells, and assume the probe does not change W. Require nonzero probe amplitude, informative nonzero history and probe contrasts, and positive retention for ratio comparisons. In particular, W_c=0 or a vanishing probe effect makes the ratio undefined. For decaying retention comparators require 0<alpha_c<1. Fit contrasts jointly rather than forming unstable sample ratios.

| Model | Where context acts | h_c | p_c | Ratio h_c/p_c across contexts |
|---|---|---|---|---|
| Readout (D3-w) | Weight on retained state at decision | κW_c α^k Δm | κW_c ηα^(k−1) v | **Invariant**: αΔm/(ηv) |
| Storage gain | Input gain η_c for post-context inputs only | κα^k Δm | κη_c α^(k−1) v | Varies as 1/η_c |
| Retention change | Retention α_c after context | κα_c^k Δm | κηα_c^(k−1) v | Varies as α_c |

Here Δm is the history state difference at the moment of context assignment.

Under pure readout weighting, context scales history and probe effects by the same factor, so their ratio does not change. Under the storage and retention alternatives, the ratio shifts with context. The common-scaling comparison does not require interpreting W=0 as a physical intervention. It still requires an independently fixed weight scale and nonzero informative contrasts in the contexts being compared.

**Interpretation and limits.**

- Test the prediction by jointly fitting a common-gain model against a model with separate gains, scored on held-out contexts. Do not divide noisy contrasts. Both history and probe contrasts must be informative, and the range of contexts must produce the independently specified nonzero scaling. Constant, flat effects or imprecise intervals do not distinguish these models.
- A reproducible change in the ratio rejects *pure* readout weighting in the tested regime. It does not exclude a mixture of readout and storage weighting.
- An invariant ratio together with the predicted nonzero joint scaling can favour readout weighting over the specified pure alternatives at the frozen precision. It is not evidence against a fixed readout-gain function G(C, m) = κ·g(C)·m, which makes the same prediction (§5.2). The comparison discriminates these restricted models under their assumptions; it does not uniquely locate an actual mechanism or place weighting outside ordinary dynamics.
- If the probe or context alters W differently across cells, the §5.1 extra term applies, and the invariance prediction must be re-derived.
- Coordinated input-gain and retention changes can also preserve the ratio. For example, alpha_c=alpha*g_c and eta_c=eta*g_c give h_c/p_c=alpha*Delta_m/(eta*v). At one fixed delay k, both contrasts scale as g_c^k, exactly matching a pure readout model with W_c=g_c^k. If a context’s readout W is constrained to remain the same across readout delays, held-out multiple-delay predictions can distinguish these particular constructions; unrestricted time-varying weights can restore the equivalence. The additional executable check demonstrates this counterexample.

## 6. A defensible route to a runnable experiment

The first step is a transparent state-space simulator. Use it to verify the measurement and inference pipeline under known truths, heterogeneous items and model misspecification. This tests the pipeline, not the framework.

An open-weights LLM can then serve as a separate exploratory test bench. The following can be frozen: history text, model revision, tokenizer, prompt template, labels, answer position and context cues. Several limits apply:

- The model's hidden state is not, by definition, the scalar m.
- Prompt position and token distance are not physical elapsed-time decay.
- Changing a context cue changes the model input and may alter internal activation.
- A generated self-rating is a noisy model output, not an independently calibrated internal weight.

Any mapping from text and cue to numerical variables must be frozen using calibration data. An assigned cue must never be equated with a measured mechanism. The §5.4 presentation order can be represented in this test bench: history appears in earlier turns, followed by context and then probe. That textual order does not establish the required hidden-state control. Unless state preservation or interventions are independently characterised, a result is a behavioural comparison of restricted models, not localisation of a physical weighting mechanism.

Before confirmation:

- select a domain;
- restrict D0 (memory-off), D1 (fixed linear), D2 (fixed nonlinear or context-conditioned), D3-w, and the §5.4 storage and retention comparators explicitly;
- choose between two targets: descriptive prediction from a pre-choice W, or the causal effect of an assigned intervention. These require different identification assumptions.

The frozen study package must specify:

- independent units and baseline;
- the measured state and weight, with their scale and timing;
- the calibration/confirmation split;
- the endpoint and practical tolerances;
- the predictive metric and the model-fitting and complexity rules;
- power, exclusions and stopping.

Report separately:

- whether history has an effect;
- whether the declared W relationship predicts held-out behaviour;
- whether the history/probe ratio is invariant across contexts (§5.4);
- whether the candidate out-predicts conventional alternatives.

Failure to detect an interaction is inconclusive unless the precision excludes the preregistered meaningful region. A comparator that predicts equally well means no distinctive advantage has been shown. That does not by itself falsify a mathematically compatible D3-w model. Reject a candidate in the tested regime for a sufficiently precise wrong-direction result, an outside-tolerance result, or another preregistered predictive failure. Report ties, weak identification and inconclusive results explicitly.

Publishing this methods note is not experimental preregistration. A later frozen experiment needs its own timestamped materials and an author expectation statement.

## 7. Maxwell Electrodynamics and Constitutive Memory

Maxwell’s equations describe how fields evolve, how charges and currents behave, and how both couple to matter. A material-memory experiment should start from unchanged Maxwell electrodynamics plus an explicitly specified constitutive response. In SI macroscopic notation:

$$\nabla\cdot\mathbf D=\rho_f,\quad \nabla\cdot\mathbf B=0,\quad
\nabla\times\mathbf E=-\partial_t\mathbf B,\quad
\nabla\times\mathbf H=\mathbf J_f+\partial_t\mathbf D,$$
$$\mathbf D=\epsilon_0\mathbf E+\mathbf P,\qquad
\mathbf B=\mu_0(\mathbf H+\mathbf M_{mag}).$$

Here M_mag denotes magnetisation, not the retained-state variable M_t, and **H** is the magnetic field intensity, not a history label. Polarisation, dielectric response and causal dispersion are standard electromagnetic material theory [3].

For a spatially local scalar polarisation component, a small-probe response about a prepared condition may be written

$$\delta P(t)=\epsilon_0\chi_{inst}(t)\delta E(t)+\epsilon_0\int_0^t\chi_{m_{pre}}(t,s)\delta E(s)\,ds.$$

The regular kernel has units of inverse time in this convention and vanishes for s > t. The direct susceptibility is dimensionless. Preparation-dependent initial terms and remanent polarisation belong to the unperturbed trajectory, and must be kept distinct from a changed incremental response. Stationarity is not assumed. Conventional frequency-domain dispersion constraints apply only under their usual assumptions.

As a worked conventional comparator, take constant W, χ_s and τ > 0, with p = P/ε₀:

$$\tau\dot p+p=\chi_s W E.$$

Its causal retarded kernel is χ_s·W·exp(−(t−s)/τ)/τ. For piecewise-constant input sampled every Δt, the exact update is

$$p_{n+1}=e^{-\Delta_t/\tau}p_n+\chi_s W(1-e^{-\Delta_t/\tau})E_n.$$

This gives a direct mathematical link between an ordinary electromagnetic response and the retained-state recurrence, with α = e^(−Δt/τ) and η = χ_s·W·(1 − α).

Here W parameterises a material response. Sharing the notation does not identify it with the selection weight. No map has been established from a selection log-odds coefficient to susceptibility, heat or physical kernel amplitude. For any chosen device, causality, admissible material parameters, preparation costs and energy accounting must be checked. This example proposes no correction to Maxwell’s equations and establishes no new electromagnetic mechanism.

A physical test would need:

- independently measured material state;
- randomised histories and identical probes;
- sham and reset controls;
- conventional dielectric, hysteretic and thermal comparators;
- held-out predictions for susceptibility or transition observables.

Existing material history effects are the comparison baseline. They are not, by themselves, evidence of a new law.

## 8. Verification, scope and attribution

The accompanying [verification script](verify_retained_state_dynamics.py) contains 22 executed mathematical check groups, including one explicitly labelled illustrative identity. They cover:

- full recurrent trajectories and boundary cases;
- superposition;
- a probe-induced-weight counterexample;
- a fixed context-conditioned comparator, shown as an illustrative identity;
- the conventional electromagnetic response update;
- the §5.4 contrasts between the specified readout, storage and retention models;
- a coordinated storage/retention counterexample showing that a constant ratio does not uniquely identify readout weighting.

Run `python -W error verify_retained_state_dynamics.py` with Python 3 and NumPy, with assertions enabled (do not use `-O`). The seed is `20261115`. [Recorded output](RETAINED_STATE_DYNAMICS_VERIFICATION_OUTPUT.txt) accompanies this release. Check 17 is an illustrative identity, not an independent falsification check.

The checks verify stated model consequences and counterexamples. They do not validate experimental inference, demonstrate novelty or provide empirical evidence.

The existing canonical equations and historical record remain intact. This note offers a proposed operational specialisation, not a settled, distinctive cross-domain prediction. Its falsifiable target is the prespecified relationship and comparative performance within a declared regime.

Drafting and computational checks were assisted by AI tools under M.R.’s direction. This version incorporates technical review and states its assumptions explicitly. Publication does not certify an independent physical experiment. Existing repository rights and licensing notices apply.

## References

1. K. J. Åström and R. M. Murray, *Feedback Systems*, author-hosted [linear systems material](https://www.cds.caltech.edu/~murray/FBS/Linear_Systems.html): state-space models, convolution, superposition and local linearisation.
2. H. Vroylandt and P. Monmarché, “Position-dependent memory kernel in generalized Langevin equations: theory and numerical estimation,” *J. Chem. Phys.* 156, 244105 (2022). [Paper](https://arxiv.org/abs/2201.02457), [DOI](https://doi.org/10.1063/5.0094566).
3. D. Tong, *Electromagnetism*, [author lecture notes](https://davidtong.org/teaching/electromagnetism/), particularly [Electromagnetism in Matter](https://davidtong.org/pdfs/teaching/electromagnetism/electro6.pdf).
4. M.R., [Mathematical Clarifications and Open Problems v1.0](MATHEMATICAL_CLARIFICATIONS_AND_OPEN_PROBLEMS_v1.0.md), 31 October 2026: baseline and score identification; nonunique kernel decomposition; independent empirical testing.

## Publication revision record

**0.5.1 — 15 November 2026:** final review of the author-supplied v0.5 clarified pairwise probabilities, restricted the locus-of-weighting interpretation, made nonzero-contrast and context/state assumptions explicit, and added the coordinated storage/retention counterexample. The conventional Maxwell treatment and canonical selection equations are unchanged. The verification script and actual output are published with the note.
