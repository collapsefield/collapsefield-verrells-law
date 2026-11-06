# Verrell's Law — 2027 Experimental Research Roadmap

**Originator:** Marcos Verrell Moss Ross (M.R.)  
**Issued:** 6 November 2026  
**Status:** Public research plan — investigations planned, not completed experimental findings  
**Scope:** Retained-state selection, cross-domain modelling, and separate physical investigations

## Research position entering 2027

The central proposition remains unchanged: prior interactions can leave persistent state changes; retained information may alter subsequent weighting and selection under comparable present conditions.

The mathematical programme has established an exact relation *within a defined exponential-tilt selection model* and improved its score-construction, parameter-identification and falsification requirements. Mathematical identities and synthetic model recovery are not independent human or physical observations. The research objective for 2027 is to obtain an independently interpretable result that can distinguish predeclared predictions from existing alternatives.

The programme proceeds on **three coordinated tracks**, with different evidence requirements and budgets. The associated Collapse Aware AI (CAAI) middleware is a separate proprietary engineering and commercial undertaking. Its frozen Core Gold audit and commercial readiness take operational priority; software conformance is not evidence for a natural law.

## Track I — Retained-state selection: primary empirical programme

**First target: neutral-memory influence on later choice.** A controlled task will investigate whether bringing to mind a contextually relevant but choice-neutral memory changes the influence of other memories on selection, and if so, by how much.

The test must distinguish **storage, cueing, retrieval, activation, lasting updating and influence on choice**. Contextual relevance is not the same as favouring a particular candidate. The five-memory example is not a general capacity claim; adding a sixth item does not automatically imply dilution.

Competing explanations include additive evidence integration, averaging, regularised pooling, gain changes, episodic sampling, retrieval-capacity limits and threshold rules. Bayesian evidence accumulation, ACT-R/instance-based methods, information integration, reinforcement learning and divisive normalisation are prior-art comparators, not findings originating in this programme.

**Test sequence:**

1. Independently review the available synthetic code and its simulation assumptions. Resolve weak effects, null behaviour, lapse/noise, participant heterogeneity, fatigue, carry-over and model misspecification.
2. Freeze a small **software feasibility pilot** using specified open-weights model, version, prompts, sampling configuration, seeds, candidate scores, control arms and analysis scripts. Include positive, null, weak and deliberately misspecified cases. This assesses pipeline recovery and behaviour in that model, not human memory or physical processes.
3. Invite an independent cognitive scientist or methodologist to review a short technical brief and the runnable pilot before committing to a larger human protocol.
4. Subject to funding, feasibility and appropriate ethics review, conduct a human discovery pilot with matched present conditions, cued/uncued baselines, neutral and opposing memories, strength gradients and reminder/update controls.
5. Preregister a narrower confirmatory prediction, score-construction method, conventional comparators, meaningful effect size, primary outcome and stop criteria; test on **fresh held-out participants**.

**Decision rule:** A well-powered absence of the preregistered reminder effect counts against that prediction *in the tested regime*. If the effect occurs but established models explain it equally well, the effect may be supported but no distinctive advantage has been shown. A specific prediction cannot be repeatedly redefined after a miss and still count as a confirmed result. Publish adequately established negative findings as well as positive ones.

## Track II — Cross-domain mathematics: bounded, desk-only investigation

A general law needs more than the same logistic or exponential equation appearing in different systems. The immediate problem is to specify a transferable **rule for classifying candidate support versus neutrality and measuring retained-state weight** in at least two different domains *before viewing the outcomes*.

Research tasks:

- Define comparable observables, state-matching criteria and outcome-blind score construction across two example systems.
- Identify which transformations are measurement conventions rather than substantive predictions; compare invariant log-odds differences, retention measures and information-theoretic quantities where well-defined.
- Test whether a fixed rule predicts held-out changes without arbitrary per-domain fitting. Include ordinary causal-state and history-sensitive models as stronger comparators.
- Require clear failure conditions: non-portable scores, uncontrolled rescaling, or conventional models matching or outperforming the proposed rule all count against a claimed general cross-domain advantage.

**Information-budget constraint.** The data-processing inequality and conditional screening-off identities are established information theory, **not a distinctive Verrell's Law prediction**. They can help diagnose missing observed carriers or poorly conditioned causal models. Apparent violations primarily demand investigation of measurement, assumptions, confounding and missing state; none would by itself prove a new field or force.

This track is mathematical and computational only until its assumptions and discriminating predictions withstand external criticism.

## Track III — Physical mechanisms: longer-term exploratory programme

Continue examining physically instantiated retained information, open-system history dependence, electromagnetic participation, material memory and quantum measurement under separately specified conditions. **Retained state is primary; no universal electromagnetic-memory field is required.**

The defensible wording when a proposed physical mechanism is unresolved is **“carrier not identified”**, not an assertion that history acts without a physical carrier. Established hysteresis, non-Markovian quantum dynamics, instrument memory, thermodynamics and measurement backaction are baselines to account for.

Physical simulation and consistency checks come before equipment or claims of novel physical effects. Any future experimental proposal must specify energy and state controls, known carriers, detector limits, intervention/erasure conditions, reproducibility and compatibility with physical constraints including no-signalling where applicable.

This track will not adopt the historical Born-rule or tensor proposals as confirmed physics.

## Mathematical authority — unchanged

For declared present conditions `S_t,O_t`, retained history `M_t`, candidates `y_i` and fixed score construction:

```math
z_i=U(y_i;S_t,O_t)+\lambda B(y_i;M_t),\qquad P_i=\frac{\exp(z_i)}{\sum_j\exp(z_j)}.
```

Equivalently `p_{\lambda,i}\propto p_{0,i}\exp(\lambda R_i)`; on common positive support with finite frozen scores the exact pairwise identity is:

```math
\Delta\log\mathrm{odds}(a,b)=\lambda(R_a-R_b).
```

It is algebraically true under its assumptions. Unrestricted `R_i` can fit any positive target distribution on the same support: therefore a test must fix its construction **independently of confirmatory outcomes** and assess predictive performance against declared alternatives. Existing memory-weight factors `w_j=s_jd_jq_j` retain their meanings (salience, persistence, reliability). No aggregation or retrieval rule is newly authorised here.

## Milestones and evidence register

| Milestone | Current status as of 6 November 2026 | Next evidence required |
|---|---|---|
| Mathematical tilt and log-odds relation | Exact within model; audited mathematically | Outcome-independent predictive scores |
| Candidate model discrimination | Synthetic comparisons and draft human protocol | Independent code audit and robust null/weak/misspecified cases |
| Frozen open-weights software pilot | Planned, not completed | Versioned runnable artefact and logged results |
| Independent academic collaboration | Not yet secured | External critique and experiment feasibility |
| Human discovery and confirmatory studies | Not executed | Ethics, funding, recruitment, registered predictions, fresh data |
| Common cross-domain prediction | Not established | One frozen rule that transfers and survives comparators |
| Physical mechanism / law status | Investigations ongoing; no confirming physical result | Separate consistency tests, controlled observations and replication |

## Publication, attribution and boundaries

This roadmap is a **dated declaration of research priorities**, not evidence that the proposed tests have succeeded. The foundational work and historical authorship remain attributed to M.R. Private audit reports, personal observational material, unreleased experimental methods and proprietary CAAI code are outside this publication.

Researchers should consult the [canonical mathematical foundations](VERRELLS_LAW_MATHEMATICAL_FOUNDATIONS_AND_FALSIFICATION_PROTOCOL_v1.0.md), the [October mathematical clarification](MATHEMATICAL_CLARIFICATIONS_AND_OPEN_PROBLEMS_v1.0.md), the [November research status](VERRELLS_LAW_RESEARCH_STATUS_AND_TESTING_2026-11.md), and [archived document status](ARCHIVED_DOCUMENT_STATUS.md). Earlier versions are preserved; a dated change of emphasis does not rewrite historical claims.

**M.R. — 6 November 2026**
