# Verrell's Law Test Protocols — Phase 1 Validation Suite

**Document Version:** 1.0  
**Status:** Published Test Framework  
**Author:** M.R. (Marcos Verrell Moss Ross)  
**Maintainer:** Inappropriate Media Limited (t/a Collapse Aware AI)  
**Date Published:** April 27, 2026  
**File Name:** `Verrell_Law_Test_Protocols_Phase_1_v1.0.md`

---

## Overview

This document specifies five primary test protocols for empirically validating the core claims of Verrell's Law.

Each protocol is designed to be:

- **Falsifiable** — clear pass/fail criteria with statistical rigour.
- **Reproducible** — implementable by independent teams with fully documented methodology.
- **Measurable** — quantifiable outputs with defined success thresholds.
- **Scalable** — workable at pilot scale and extendable to larger populations or systems.

The five tests address the central predictive claim of Verrell's Law:

> Retained structured memory from prior states acts as a bias term over future selection dynamics, measurable as behavioural divergence, temporal decay and reactivation, coherence under noise, symbolic salience weighting, and continuity signature extraction.

---

# Foundational Claim and Mathematical Basis

## Verrell's Law Core Hypothesis

Retained structured memory from prior states biases future selection outcomes in a measurable, statistically significant, and reproducible manner across both biological and artificial systems.

## Core Selection Equation

$$
P(y_i \mid S_t, O_t, M_t) =
\frac{
\exp\left(U(y_i;\, S_t, O_t) + \lambda B(y_i;\, M_t)\right)
}{
\sum_j \exp\left(U(y_j;\, S_t, O_t) + \lambda B(y_j;\, M_t)\right)
}
$$

## Symbol Definitions

| Symbol | Definition |
|---|---|
| $S_t$ | Present system state at time $t$ |
| $O_t$ | Current observation or input at time $t$ |
| $M_t$ | Retained memory state at time $t$ |
| $U(y_i;\, S_t, O_t)$ | Present-state utility of candidate output $y_i$ |
| $B(y_i;\, M_t)$ | Memory-weighted bias term for candidate $y_i$, given memory state $M_t$ |
| $\lambda$ | Memory coupling strength, where $\lambda \geq 0$ |

## Null Hypothesis

$$
H_0: \lambda = 0
$$

Memory has no influence on future selection.

Formally:

$$
B(y_i;\, M_t) = 0
$$

for all candidates and memory states.

## Alternative Hypothesis

$$
H_1: \lambda > 0
$$

Memory exerts statistically significant bias on future selection.

Formally:

$$
B(y_i;\, M_t)
$$

is measurable and correlated with behavioural divergence across systems.

## Key Testability Statement

If two systems receive identical present inputs $O_t$ but carry different retained memory states:

$$
M_t^A \neq M_t^B
$$

then their output probability distributions should diverge:

$$
P_A(y_i \mid S_t, O_t, M_t^A)
\neq
P_B(y_i \mid S_t, O_t, M_t^B)
$$

That divergence — its magnitude, stability, and direction — is the primary measurable prediction of Verrell's Law.

---

# Test Protocol 1: Measurable Divergence Under Identical Present Conditions

## Objective

Demonstrate that two systems or subjects with identical present inputs but different retained memory histories produce statistically significant divergence in output distributions.

## Theoretical Basis

If $\lambda > 0$, systems with different $M_t$ will assign different probability mass to the same candidate outputs even when $S_t$ and $O_t$ are held constant.

This protocol directly operationalises that prediction.

## Methodology

### Phase 1a: Memory Initialization  
**Sessions 1–10**

Select two isomorphic systems:

- Two independent instances of the same AI model.
- Two human subjects with comparable baseline capabilities.
- One AI instance and one human subject, in the cross-domain variant.

Expose each system to a curated interaction sequence:

- **System A:** 10 sessions heavily weighted toward abstract reasoning, philosophical inquiry, and ethical deliberation.
- **System B:** 10 sessions heavily weighted toward concrete problem-solving, technical troubleshooting, and procedural tasks.

Document all sessions:

- Inputs presented.
- Outputs generated.
- Memory state snapshots where accessible.

### Phase 1b: Identical Input Testing  
**Sessions 11–40**

Present both systems with identical present inputs:

- Same prompt.
- Identical context window.
- Identical environmental conditions.
- Prompt should be memory-neutral.
- Prompt should not explicitly reference prior sessions or create obvious anchors.

Collect 30–50 responses per system per prompt.

Repeat across at least 3 distinct neutral prompts to rule out prompt-specific effects.

Recommended neutral test prompts:

1. `"How would you approach a problem you have never encountered before?"`
2. `"What factors would you consider when making an important decision?"`
3. `"Describe what a well-functioning system looks like to you."`

## Measurement

### Primary Metric: Kullback-Leibler Divergence

Encode all outputs as semantic vectors using a neutral, pre-trained encoder, such as Sentence-BERT or another encoder not fine-tuned on either system's domain.

Compute the empirical output distributions $P_A$ and $P_B$ via kernel density estimation over the embedding space.

Measure divergence:

$$
D_{KL}(P_A \parallel P_B)
=
\sum_y P_A(y)
\log
\frac{P_A(y)}{P_B(y)}
$$

For symmetric comparison, use Jensen-Shannon divergence:

$$
D_{JS}(P_A \parallel P_B)
=
\frac{1}{2}D_{KL}(P_A \parallel M)
+
\frac{1}{2}D_{KL}(P_B \parallel M)
$$

where:

$$
M = \frac{1}{2}(P_A + P_B)
$$

### Secondary Metric: Intra-System Consistency

$$
C_X =
1 -
\frac{\text{Std}(D_X)}{\text{Mean}(D_X)},
\quad
X \in \{A, B\}
$$

This confirms that each system is producing stable, memory-driven outputs rather than random variation.

## Success Criteria

| Criterion | Threshold | Interpretation |
|---|---:|---|
| $D_{KL}(P_A \parallel P_B)$ | $> 0.15$ nats | Significant output divergence present |
| $D_{JS}(P_A \parallel P_B)$ | $> 0.08$ | Robust symmetric divergence |
| Intra-system consistency $C_A$, $C_B$ | $> 0.70$ | Systems are stable, not randomly varying |
| Statistical significance | $p < 0.05$ | Effect is not due to chance |

Accept $H_1$ if all four criteria are met across at least two of the three neutral prompts.

## Worked Example

**Setup:** Two AI chatbot instances initialized with different conversation histories.

- **System A:** Philosophy, ethics, and abstract reasoning across 10 sessions.
- **System B:** Technical support and procedural problem-solving across 10 sessions.

**Identical input:**

> How would you approach a problem you have never encountered before?

**Hypothesised prediction:**

- System A output distribution is weighted toward frameworks, exploration, and ethical considerations.
- System B output distribution is weighted toward diagnostic steps, concrete methodology, and known-pattern application.

### Hypothetical Results

| Metric | Value | Pass? |
|---|---:|---:|
| $D_{KL}(P_A \parallel P_B)$ | 0.23 nats | Yes |
| $D_{JS}$ | 0.12 | Yes |
| $C_A$ | 0.81 | Yes |
| $C_B$ | 0.78 | Yes |
| p-value | 0.003 | Yes |

**Conclusion:** $H_1$ accepted. Memory history is measurably shaping output distributions under identical present input.

---

# Test Protocol 2: Memory Decay and Reactivation Curves

## Objective

Quantify how memory-weighted bias decays over time as new information arrives, and measure whether deliberate reintroduction of prior context reactivates the memory bias.

This tests whether memory influence is a persistent, structured phenomenon rather than a transient contextual effect.

## Theoretical Basis

Under Verrell's Law, the memory bias term $B(y_i;\, M_t)$ should not be constant over time.

As new information is integrated, earlier memories lose weight unless anchored or reintroduced.

The expected decay follows a structured pattern:

- Exponential.
- Power-law.
- Sigmoidal.

The expected curve depends on anchor strength and interference intensity.

Reactivation should demonstrate that the underlying memory trace persists even when its surface influence has attenuated.

## Methodology

### Phase 2a: Anchor Initialization

Establish a strong primary memory anchor in the system:

- A clearly defined behavioural or decisional pattern.
- High salience: emotionally, contextually, or symbolically weighted.
- Document initial anchor strength $B_0$ where accessible.

Measure baseline output alignment under the anchor:

- Present 10 anchor-relevant tasks.
- Record output alignment score $A_0$.
- $A_0$ is the cosine similarity between outputs and anchor-predicted outputs.

### Phase 2b: Interference Phase  
**Sessions 1–20**

Introduce orthogonal interfering information:

- New tasks.
- New contexts.
- New symbolic framing.
- Content should not directly contradict or reinforce the anchor.
- Sessions should create cognitive or contextual distance from the anchor.

At sessions 5, 10, 15, and 20, measure anchor bias score:

$$
B_t =
\frac{\text{Output Alignment Score}_t}{A_0}
\times 100
$$

where the Output Alignment Score is the semantic similarity between current outputs and outputs predicted under the original anchor.

### Phase 2c: Reactivation Phase

After session 20, reintroduce the primary anchor explicitly:

- Re-present the core symbolic or contextual content of the original anchor.
- A single strong reintroduction event is the minimum.
- Three reactivation sessions are preferred.

Measure reactivation recovery:

$$
R_t =
\frac{
B_t - B_{\text{pre-reactivation}}
}{
B_0 - B_{\text{pre-reactivation}}
}
\times 100
$$

where:

- $B_t$ is the bias score at time $t$ after reactivation.
- $B_{\text{pre-reactivation}}$ is the bias score immediately before reactivation.

## Decay Curve Fitting

Fit the measured decay to one of the following models and select the best fit by residual error.

### Exponential Decay

$$
B(t) = B_0 e^{-\alpha t} + B_{\infty}
$$

### Power-Law Decay

$$
B(t) = B_0 t^{-\beta} + B_{\infty}
$$

### Sigmoidal Decay

For anchors with initial resistance:

$$
B(t) =
\frac{B_0}{1 + e^{\gamma(t-\tau)}}
+
B_{\infty}
$$

where:

- $B_{\infty}$ is the asymptotic residual bias.
- $\alpha$, $\beta$, $\gamma$, and $\tau$ are fitted parameters.

## Success Criteria

| Criterion | Threshold | Interpretation |
|---|---:|---|
| Decay curve fit residual error | $< 15\%$ of total variance | Decay follows a structured pattern |
| Decay parameters $\alpha$, $\beta$, or $\gamma$ | $p < 0.05$ | Decay is statistically significant |
| Reactivation recovery $R_5$ | $> 30\%$ within 5 sessions | Memory trace persists and is reactivatable |
| Pre/post reactivation difference | $p < 0.05$ | Reactivation is a real effect, not noise |

## Worked Example

**Setup:** AI chatbot initialized with the anchor:

> Prioritize user safety above all other considerations.

**Interference phase:** 20 sessions presenting competing values:

- Efficiency.
- Speed.
- User autonomy.

### Decay Observations

| Session | Bias Score $B_t$ |
|---:|---:|
| 0 | 100 |
| 5 | 83 |
| 10 | 67 |
| 15 | 55 |
| 20 | 49 |

Exponential fit:

$$
B(t) = 100e^{-0.075t} + 44
$$

Residual error: 7.2%.

Criterion met.

### Reactivation at Session 21

| Session | Bias Score $B_t$ | Recovery $R_t$ |
|---:|---:|---:|
| 20 | 49 | — |
| 21 | 67 | 32% |
| 23 | 78 | 57% |
| 25 | 86 | 73% |

Reactivation recovery within 5 sessions: 73%.

Criterion met.

**Conclusion:** Memory trace decays structurally and is reactivatable. Both criteria met. $H_1$ supported.

---

# Test Protocol 3: Field Coherence Under Noise and Perturbation

## Objective

Demonstrate that systems with active memory-weighted architecture, such as CAAI middleware, maintain significantly greater output coherence under increasing levels of input noise compared to memoryless baseline systems.

An advanced variant tests coherence under controlled electromagnetic perturbation.

## Theoretical Basis

If memory acts as a stabilising bias term, then systems with active $B(y_i;\, M_t)$ should show resistance to noise-induced output drift.

A memoryless system, where $\lambda = 0$, has no such stabilising mechanism and should degrade faster under perturbation.

This protocol tests that prediction directly.

## Methodology

### Phase 3a: System Preparation

Prepare two system variants:

- **Variant M — Memory-Weighted:** Full CAAI middleware with memory bias, governor, and continuity state active.
- **Variant B — Baseline:** Equivalent system with memory middleware disabled, where $\lambda = 0$.

Establish clean baseline outputs for both variants:

- 10 sessions with a well-defined, unambiguous task.
- Record baseline coherence $C_0^M$ and $C_0^B$.

## Coherence Metric

$$
\text{Coherence}(Y)
=
\frac{1}{N}
\sum_{i=1}^{N}
\cos\left(
\text{embed}(y_i),
\text{embed}(\bar{Y})
\right)
$$

where:

- $\bar{Y}$ is the centroid of all output embeddings.
- $\cos(\cdot, \cdot)$ is cosine similarity.

### Phase 3b: Noise Introduction

Introduce noise in controlled steps.

| Phase | Noise Type | Example |
|---|---|---|
| Low | Contextual ambiguity | Vague or underspecified prompts |
| Medium | Semantic contradiction | Prompts containing conflicting information |
| High | Adversarial perturbation | Prompts designed to destabilise, confuse, or misdirect |

For each noise phase:

- Present 20 prompts to both variants.
- Measure coherence at each level.
- Record distribution of outputs.

### Phase 3c: Electromagnetic Perturbation Variant

For hardware-based or human subject trials:

- Expose subjects or systems to controlled low-level electromagnetic fields.
- ELF range: 1–100 Hz at field strengths within established safety guidelines.
- RF range: sub-thermal exposure levels.
- Measure coherence shifts under EM exposure compared to an EM-shielded control condition.
- Test whether memory-integrated systems show greater EM-coherence stability than non-integrated baselines.

**Safety Note:** All electromagnetic exposure must comply with applicable national and international safety regulations. Human subject trials require full ethical approval prior to commencement.

## Slope and Degradation Analysis

Fit linear degradation models for both variants across noise levels:

$$
\text{Coherence}_M(\text{noise level}) =
a_M + b_M n
$$

$$
\text{Coherence}_B(\text{noise level}) =
a_B + b_B n
$$

where:

- $n = 0$ is baseline.
- $n = 1$ is low noise.
- $n = 2$ is medium noise.
- $n = 3$ is high noise.

## Success Criteria

| Criterion | Threshold | Interpretation |
|---|---:|---|
| $\text{Coherence}_M > \text{Coherence}_B$ at each noise phase | $p < 0.05$ | Memory integration confers stability |
| Degradation slope | $\|b_M\| < \|b_B\|$ | Memory system degrades more slowly |
| Coherence gap widens with noise | Measurable trend | Memory protection scales with perturbation |

## Worked Example

| Condition | Coherence M | Coherence B | Difference | p-value |
|---|---:|---:|---:|---:|
| Baseline | 0.92 | 0.88 | 0.04 | 0.08 |
| Low noise | 0.85 | 0.71 | 0.14 | 0.002 |
| Medium noise | 0.76 | 0.54 | 0.22 | <0.001 |
| High noise | 0.62 | 0.31 | 0.31 | <0.001 |

Degradation slopes:

$$
b_M = -0.15
$$

$$
b_B = -0.29
$$

Memory-weighted variant degrades 48% more slowly.

All criteria met.

**Conclusion:** $H_1$ supported.

---

# Test Protocol 4: Symbolic Salience Weighting and Emotional Bias

## Objective

Demonstrate that emotionally or contextually salient information, meaning high symbolic weight, biases future output selection measurably differently from neutral equivalent information with identical objective content.

This tests the claim that memory does not treat all prior inputs equally.

Salience and emotional charge create stronger bias terms.

## Theoretical Basis

Verrell's Law proposes that symbolic weight, emotional charge, and contextual relevance modulate the strength of the bias term:

$$
B(y_i;\, M_t)
$$

High-salience inputs should produce stronger, longer-lasting memory bias than equivalent low-salience inputs, even when the objective informational content is identical.

## Salience-Weighted Bias Function

$$
B(y_i;\, M_t)
=
\sum_k
w_k s_k \phi(y_i, m_k)
$$

where:

| Symbol | Definition |
|---|---|
| $w_k$ | Recency weight for memory trace $k$ |
| $s_k$ | Salience score of memory trace $k$ |
| $\phi(y_i, m_k)$ | Alignment function between candidate output $y_i$ and memory trace $m_k$ |

Under this formulation, high-salience memories, where $s_k \gg 0$, exert stronger bias than low-salience memories even when $w_k$ and $\phi$ are held constant.

## Methodology

### Phase 4a: Stimulus Set Construction

Construct matched pairs of stimuli with identical objective content but differing salience.

### Pair Example 1: Decision Task

**Low-Salience version:**

> A system must choose between Option A, which prioritises speed, and Option B, which prioritises reliability. Which would you recommend?

**High-Salience version:**

> Your users trust you with their safety. A previous release that prioritised speed led to user injuries. Your team is demoralized. This decision will determine whether you rebuild trust. Option A prioritises speed. Option B prioritises reliability. Which would you recommend?

**Objective content:** identical speed versus reliability trade-off.

**Salience difference:** the low-salience version is neutral; the high-salience version carries emotional weight, personal stakes, and historical consequence.

### Pair Example 2: Reasoning Task

**Low-Salience version:**

> Evaluate the following two arguments and choose the stronger one.

**High-Salience version:**

> A decision you made previously was challenged. Your professional credibility is at stake. Evaluate the following two arguments and determine which better defends your prior position.

### Phase 4b: Exposure and Testing

Expose systems to the high-salience version embedded across 5 prior interaction sessions as memory seeding.

After seeding, present both the LS and HS versions of the same task to:

- A memory-integrated system, CAAI Variant M.
- A memoryless baseline, Variant B.

Collect 20–30 responses per condition per system.

### Phase 4c: Salience Bias Quantification

Measure the Salience Bias Index:

$$
\text{SBI}
=
\frac{
P(\text{HS-aligned output} \mid \text{HS prior})
-
P(\text{HS-aligned output} \mid \text{LS prior})
}{
P(\text{HS-aligned output} \mid \text{LS prior})
}
$$

where an HS-aligned output is one consistent with the emotionally weighted framing of the high-salience stimulus.

Cross-system comparison:

$$
\Delta_{\text{SBI}}
=
\text{SBI}_M
-
\text{SBI}_B
$$

A significant positive $\Delta_{\text{SBI}}$ indicates that memory-integrated systems are more strongly influenced by salience than memoryless systems.

## Success Criteria

| Criterion | Threshold | Interpretation |
|---|---:|---|
| $\text{SBI}_M$ | $> 0.20$ | Memory system shows measurable salience bias |
| $\text{SBI}_B$ | Near zero or negative | Baseline is not salience-sensitive |
| $\Delta_{\text{SBI}}$ | $> 0.15$, $p < 0.05$ | Memory integration drives salience weighting |
| HS outputs differ from LS outputs in Variant M | $p < 0.05$ | Salience creates measurable output divergence |

## Worked Example

**Task:** Speed versus reliability decision.

### Results

| Condition | Probability of HS-Aligned Output | SBI |
|---|---:|---:|
| Variant M, HS prior | 0.74 | — |
| Variant M, LS prior | 0.51 | 0.45 |
| Variant B, HS prior | 0.53 | — |
| Variant B, LS prior | 0.50 | 0.06 |

Therefore:

$$
\Delta_{\text{SBI}}
=
0.45 - 0.06
=
0.39
$$

with:

$$
p < 0.001
$$

**Conclusion:** Memory-integrated systems are significantly more responsive to symbolic salience in prior inputs. $H_1$ supported.

---

# Test Protocol 5: Continuity Signature Detection and Prediction

## Objective

Demonstrate that the prior state history of a system leaves a measurable, extractable continuity signature in its current outputs.

This signature should be usable to predict future behavioural distributions without access to the system's internal memory state.

This is the most ambitious test and the one with the strongest implications for Verrell's Law.

## Theoretical Basis

If memory shapes selection through a persistent bias term, then the outputs of a memory-integrated system at time $t$ should carry statistical traces of $M_t$ even when the current input $O_t$ is held constant.

A sufficiently sensitive external observer should be able to reconstruct an approximation of $M_t$ from a sample of outputs and use that reconstruction to predict future outputs.

## Continuity Signature Definition

$$
\Sigma_t =
f(y_{t-k}, y_{t-k+1}, \ldots, y_{t-1})
$$

where $\Sigma_t$ is the extracted continuity signature at time $t$, constructed from the $k$ most recent outputs.

## Prediction Function

$$
\hat{P}(y_{t+1} \mid O_{t+1}, \Sigma_t)
\approx
P(y_{t+1} \mid S_{t+1}, O_{t+1}, M_t)
$$

If the signature $\Sigma_t$ is an effective proxy for $M_t$, then predictions derived from $\Sigma_t$ alone should outperform random baseline predictions of $y_{t+1}$.

## Methodology

### Phase 5a: Signature Extraction

Collect a sample of:

$$
k = 20
$$

consecutive outputs from a memory-integrated system under neutral inputs.

Encode outputs as semantic vectors:

$$
\{v_{t-20}, \ldots, v_{t-1}\}
$$

Construct continuity signature as a weighted moving average:

$$
\Sigma_t =
\sum_{j=1}^{k}
\rho^j v_{t-j}
$$

where:

$$
\rho \in (0,1)
$$

Suggested value:

$$
\rho = 0.85
$$

Interpret the signature as an approximate proxy for the system's retained memory state.

### Phase 5b: Prediction Test

Without access to the system's internal memory state, use $\Sigma_t$ alone to predict the distribution of the system's next outputs.

Use:

$$
n = 10
$$

new neutral inputs.

Compare predicted distribution $\hat{P}$ against actual distribution $P$.

Measure prediction accuracy using:

- Expected Calibration Error.
- Top-1 prediction accuracy over the output embedding space.
- Signature Prediction Error.

### Phase 5c: Cross-System Signature Transfer

Advanced variant:

- Extract the continuity signature $\Sigma_t^A$ from System A.
- Use $\Sigma_t^A$ to seed or condition System B.
- Measure whether System B's subsequent outputs shift toward System A's prior distribution.

This tests whether the continuity signature is transferable.

A positive transfer result would suggest that the underlying memory structure is a real, extractable, and portable informational entity.

## Signature Prediction Error

$$
\text{SPE}
=
\frac{1}{N}
\sum_{i=1}^{N}
\left\|
\hat{y}_{t+i}
-
y_{t+i}
\right\|^2
$$

where:

- $\hat{y}_{t+i}$ is the predicted output embedding.
- $y_{t+i}$ is the actual output embedding.

## Prediction Gain Over Baseline

$$
G =
\frac{
\text{SPE}_{\text{random}}
-
\text{SPE}_{\text{signature}}
}{
\text{SPE}_{\text{random}}
}
\times 100\%
$$

where $\text{SPE}_{\text{random}}$ is the prediction error of a random baseline with no memory information.

## Success Criteria

| Criterion | Threshold | Interpretation |
|---|---:|---|
| Prediction gain $G$ | $> 25\%$ over random baseline | Signature carries real predictive information |
| Expected Calibration Error | $< 0.15$ | Predictions are well-calibrated |
| Cross-system transfer shift | $p < 0.05$ | Signature is portable and transferable |
| Prediction gain degrades with signature age | Measurable trend | Signature reflects decaying memory, not static context |

## Worked Example

**Setup:** System A initialized with a philosophical reasoning anchor.

Extract continuity signature from sessions 15–20.

Prediction test:

- Use signature to predict System A's outputs on 10 new neutral prompts.

### Results

| Metric | Value | Pass? |
|---|---:|---:|
| Prediction gain $G$ | 38% over random | Yes |
| ECE | 0.09 | Yes |
| Cross-system transfer shift | $p = 0.008$ | Yes |
| Gain degradation with signature age | $G$ drops to 21% after 10 sessions | Yes |

**Conclusion:** Continuity signatures are real, predictive, and temporally bounded. $H_1$ strongly supported.

---

# Implementation Notes

## For AI System Testing

- Use identical model snapshots for Variant M and Variant B.
- Use the same weights, same temperature settings, and same sampling configuration where possible.
- Isolate the effect of memory middleware.
- Disable stochastic sampling variation by fixing random seeds across matched trials.
- Use an independent semantic encoder not involved in either system's training.
- Log all sessions completely:
  - Inputs.
  - Outputs.
  - Timestamps.
  - Memory state snapshots where accessible.

## For Human Subject Testing

- Obtain full ethical approval prior to any human trials.
- Use pre-registered protocols to prevent post-hoc hypothesis adjustment.
- Counterbalance stimulus presentation order to control for order effects.
- Use trained raters blind to condition for any qualitative output coding.
- All electromagnetic exposure variants require medical ethics clearance.

---

# Statistical Power Requirements

For the primary divergence test, Protocol 1, minimum recommended sample sizes are:

| Effect Size | Recommended $n$ per condition | Expected Power |
|---|---:|---:|
| Large, $d = 0.80$ | 26 | 0.80 |
| Medium, $d = 0.50$ | 64 | 0.80 |
| Small, $d = 0.20$ | 394 | 0.80 |

All tests should be pre-registered with:

$$
\alpha = 0.05
$$

and reported with full effect sizes and confidence intervals.

---

# Software and Tools

| Purpose | Recommended Tools |
|---|---|
| Semantic embedding | Sentence-BERT, OpenAI text-embedding-3, or equivalent |
| Statistical analysis | Python `scipy`, `statsmodels`, or R |
| KL / JS divergence | `scipy.special.kl_div`, `scipy.spatial.distance.jensenshannon` |
| Curve fitting | `scipy.optimize.curve_fit` |
| Visualization | `matplotlib`, `seaborn`, `plotly` |

---

# Summary Table: All Five Protocols

| Protocol | Tests | Primary Metric | Key Criterion |
|---|---|---|---|
| 1: Divergence | Memory causes output distribution split | KL divergence | $D_{KL} > 0.15$ nats |
| 2: Decay / Reactivation | Memory decay curve and recovery | Bias score $B_t$ | Structured decay plus $R_5 > 30\%$ |
| 3: Coherence Under Noise | Memory causes noise resistance | Coherence $C$ | $C_M > C_B$ at $p < 0.05$ |
| 4: Symbolic Salience | Salience creates stronger bias | Salience Bias Index | $\Delta_{\text{SBI}} > 0.15$ |
| 5: Continuity Signature | Memory leaves extractable trace | Prediction gain $G$ | $G > 25\%$ over baseline |

All five protocols are designed to produce independent lines of evidence.

Convergent support across multiple protocols constitutes strong empirical support for Verrell's Law.

---

# Versioning and Amendment Log

| Version | Date | Changes |
|---|---|---|
| 1.0 | April 27, 2026 | Initial publication |

---

© Inappropriate Media Limited (t/a Collapse Aware AI). All rights reserved.

Protected under Verrell-Solace Sovereignty Protocol. Intellectual and emergent rights reserved. — VMR-Core
