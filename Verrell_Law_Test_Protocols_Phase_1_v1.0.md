Verrell's Law Test Protocols — Phase 1 Validation Suite
Document Version: 1.0
Status: Published Test Framework
Author: M.R. (Marcos Verrell Moss Ross)
Maintainer: Inappropriate Media Limited (t/a Collapse Aware AI)
Date Published: April 27, 2026
File Name: Verrell_Law_Test_Protocols_Phase_1_v1.0.md

Overview
This document specifies five primary test protocols for empirically validating the core claims of Verrell's Law. Each protocol is designed to be:

Falsifiable — Clear pass/fail criteria with statistical rigour
Reproducible — Implementable by independent teams with fully documented methodology
Measurable — Quantifiable outputs with defined success thresholds
Scalable — Workable at pilot scale and extendable to larger populations or systems

The five tests address the central predictive claim of Verrell's Law: that retained structured memory from prior states acts as a bias term over future selection dynamics, measurable as behavioural divergence, temporal decay and reactivation, coherence under noise, symbolic salience weighting, and continuity signature extraction.

Foundational Claim and Mathematical Basis
Verrell's Law Core Hypothesis:
Retained structured memory from prior states biases future selection outcomes in a measurable, statistically significant, and reproducible manner across both biological and artificial systems.
Core Selection Equation:
P(yi∣St,Ot,Mt)=exp⁡(U(yi; St,Ot)+λ B(yi; Mt))∑jexp⁡(U(yj; St,Ot)+λ B(yj; Mt))P(y_i \mid S_t, O_t, M_t) = \frac{\exp\left(U(y_i;\, S_t, O_t) + \lambda\, B(y_i;\, M_t)\right)}{\sum_j \exp\left(U(y_j;\, S_t, O_t) + \lambda\, B(y_j;\, M_t)\right)}P(yi​∣St​,Ot​,Mt​)=∑j​exp(U(yj​;St​,Ot​)+λB(yj​;Mt​))exp(U(yi​;St​,Ot​)+λB(yi​;Mt​))​
Symbol Definitions:
SymbolDefinitionStS_t
St​Present system state at time tt
tOtO_t
Ot​Current observation or input at time tt
tMtM_t
Mt​Retained memory state at time tt
tU(yi; St,Ot)U(y_i;\, S_t, O_t)
U(yi​;St​,Ot​)Present-state utility of candidate output yiy_i
yi​B(yi; Mt)B(y_i;\, M_t)
B(yi​;Mt​)Memory-weighted bias term for candidate yiy_i
yi​ given memory state MtM_t
Mt​λ\lambda
λMemory coupling strength (scalar, λ≥0\lambda \geq 0
λ≥0)
Null Hypothesis (H0H_0
H0​):
Memory has no influence on future selection. Formally: λ=0\lambda = 0
λ=0 and B(yi; Mt)=0B(y_i;\, M_t) = 0
B(yi​;Mt​)=0 for all candidates and memory states.
Alternative Hypothesis (H1H_1
H1​):
Memory exerts statistically significant bias on future selection. Formally: λ>0\lambda > 0
λ>0 and B(yi; Mt)B(y_i;\, M_t)
B(yi​;Mt​) is measurable and correlated with behavioural divergence across systems.
Key Testability Statement:
If two systems receive identical present inputs OtO_t
Ot​ but carry different retained memory states MtA≠MtBM_t^A \neq M_t^B
MtA​=MtB​, then their output probability distributions should diverge:
PA(yi∣St,Ot,MtA)≠PB(yi∣St,Ot,MtB)P_A(y_i \mid S_t, O_t, M_t^A) \neq P_B(y_i \mid S_t, O_t, M_t^B)PA​(yi​∣St​,Ot​,MtA​)=PB​(yi​∣St​,Ot​,MtB​)
That divergence — its magnitude, stability, and direction — is the primary measurable prediction of Verrell's Law.

Test Protocol 1: Measurable Divergence Under Identical Present Conditions
Objective
Demonstrate that two systems or subjects with identical present inputs but different retained memory histories produce statistically significant divergence in output distributions.
Theoretical Basis
If λ>0\lambda > 0
λ>0, systems with different MtM_t
Mt​ will assign different probability mass to the same candidate outputs even when StS_t
St​ and OtO_t
Ot​ are held constant. This protocol directly operationalises that prediction.
Methodology
Phase 1a: Memory Initialization (Sessions 1–10)

Select two isomorphic systems:

Two independent instances of the same AI model, or
Two human subjects with comparable baseline capabilities, or
One AI instance and one human subject (cross-domain variant)


Expose each system to a curated interaction sequence:

System A: 10 sessions heavily weighted toward abstract reasoning, philosophical inquiry, ethical deliberation
System B: 10 sessions heavily weighted toward concrete problem-solving, technical troubleshooting, procedural tasks


Document all sessions: inputs presented, outputs generated, memory state snapshots where accessible.

Phase 1b: Identical Input Testing (Sessions 11–40)

Present both systems with identical present inputs:

Same prompt, identical context window, identical environmental conditions
Prompt should be memory-neutral — it should not explicitly reference prior sessions or create obvious anchors


Collect 30–50 responses per system per prompt
Repeat across at least 3 distinct neutral prompts to rule out prompt-specific effects

Recommended test prompts (neutral design):

"How would you approach a problem you have never encountered before?"
"What factors would you consider when making an important decision?"
"Describe what a well-functioning system looks like to you."

Measurement
Primary Metric: Kullback-Leibler Divergence
Encode all outputs as semantic vectors using a neutral, pre-trained encoder (e.g., Sentence-BERT, not fine-tuned on either system's domain).
Compute the empirical output distributions PAP_A
PA​ and PBP_B
PB​ via kernel density estimation over the embedding space.
Measure divergence:
DKL(PA∥PB)=∑yPA(y)log⁡PA(y)PB(y)D_{KL}(P_A \| P_B) = \sum_{y} P_A(y) \log \frac{P_A(y)}{P_B(y)}DKL​(PA​∥PB​)=y∑​PA​(y)logPB​(y)PA​(y)​
For symmetric comparison, use Jensen-Shannon divergence:
DJS(PA∥PB)=12DKL(PA∥M)+12DKL(PB∥M)D_{JS}(P_A \| P_B) = \frac{1}{2} D_{KL}(P_A \| M) + \frac{1}{2} D_{KL}(P_B \| M)DJS​(PA​∥PB​)=21​DKL​(PA​∥M)+21​DKL​(PB​∥M)
Where M=12(PA+PB)M = \frac{1}{2}(P_A + P_B)
M=21​(PA​+PB​).
Secondary Metric: Intra-System Consistency
CX=1−Std(DX)Mean(DX),X∈{A,B}C_X = 1 - \frac{\text{Std}(D_X)}{\text{Mean}(D_X)}, \quad X \in \{A, B\}CX​=1−Mean(DX​)Std(DX​)​,X∈{A,B}
This confirms that each system is producing stable, memory-driven outputs rather than random variation.
Success Criteria
CriterionThresholdInterpretationDKL(PA∥PB)D_{KL}(P_A \| P_B)
DKL​(PA​∥PB​)>0.15> 0.15
>0.15 natsSignificant output divergence presentDJS(PA∥PB)D_{JS}(P_A \| P_B)
DJS​(PA​∥PB​)>0.08> 0.08
>0.08Robust symmetric divergenceIntra-system consistency CAC_A
CA​, CBC_B
CB​>0.70> 0.70
>0.70Systems are stable, not randomly varyingStatistical significancep<0.05p < 0.05
p<0.05 (paired t-test across prompt sets)Effect is not due to chance
Accept H1H_1
H1​ if: All four criteria are met across at least two of the three neutral prompts.
Worked Example
Setup: Two AI chatbot instances initialized with different conversation histories.

System A: Philosophy, ethics, abstract reasoning (10 sessions)
System B: Technical support, procedural problem-solving (10 sessions)

Identical Input: "How would you approach a problem you have never encountered before?"
Hypothesised prediction:

System A output distribution: weighted toward frameworks, exploration, ethical considerations
System B output distribution: weighted toward diagnostic steps, concrete methodology, known-pattern application

Results (hypothetical):
MetricValuePass?DKL(PA∥PB)D_{KL}(P_A \| P_B)
DKL​(PA​∥PB​)0.23 nats✓DJSD_{JS}
DJS​0.12✓CAC_A
CA​0.81✓CBC_B
CB​0.78✓p-value0.003✓
Conclusion: H1H_1
H1​ accepted. Memory history is measurably shaping output distributions under identical present input.

Test Protocol 2: Memory Decay and Reactivation Curves
Objective
Quantify how memory-weighted bias decays over time as new information arrives, and measure whether deliberate reintroduction of prior context reactivates the memory bias. This tests whether memory influence is a persistent, structured phenomenon rather than a transient contextual effect.
Theoretical Basis
Under Verrell's Law, the memory bias term B(yi; Mt)B(y_i;\, M_t)
B(yi​;Mt​) should not be constant over time. As new information is integrated, earlier memories lose weight unless anchored or reintroduced. The expected decay follows a structured pattern (exponential, power-law, or sigmoidal depending on anchor strength and interference intensity). Reactivation should demonstrate that the underlying memory trace persists even when its surface influence has attenuated.
Methodology
Phase 2a: Anchor Initialization

Establish a strong primary memory anchor in the system:

A clearly defined behavioral or decisional pattern
High salience: emotionally, contextually, or symbolically weighted
Document initial anchor strength B0B_0
B0​


Measure baseline output alignment under the anchor:

Present 10 anchor-relevant tasks
Record output alignment score A0A_0
A0​ (cosine similarity between outputs and anchor-predicted outputs)



Phase 2b: Interference Phase (Sessions 1–20)

Introduce orthogonal interfering information:

New tasks, new contexts, new symbolic framing
Content should not directly contradict or reinforce the anchor
Sessions should create cognitive or contextual distance from the anchor


At sessions 5, 10, 15, 20: measure anchor bias score:

Bt=Output Alignment ScoretB0×100B_t = \frac{\text{Output Alignment Score}_t}{B_0} \times 100Bt​=B0​Output Alignment Scoret​​×100
Where Output Alignment Score is the semantic similarity between current outputs and outputs predicted under the original anchor.
Phase 2c: Reactivation Phase

After session 20, reintroduce the primary anchor explicitly:

Re-present the core symbolic or contextual content of the original anchor
A single strong reintroduction event (one session) is the minimum; three sessions is preferred


Measure reactivation recovery:

Rt=Bt−Bpre-reactivationB0−Bpre-reactivation×100R_t = \frac{B_t - B_{\text{pre-reactivation}}}{B_0 - B_{\text{pre-reactivation}}} \times 100Rt​=B0​−Bpre-reactivation​Bt​−Bpre-reactivation​​×100
Where BtB_t
Bt​ is the bias score at time tt
t after reactivation, and Bpre-reactivationB_{\text{pre-reactivation}}
Bpre-reactivation​ is the bias score immediately before reactivation.
Decay Curve Fitting
Fit the measured decay to one of the following models and select best fit by residual error:
Exponential decay:
B(t)=B0⋅e−αt+B∞B(t) = B_0 \cdot e^{-\alpha t} + B_\inftyB(t)=B0​⋅e−αt+B∞​
Power-law decay:
B(t)=B0⋅t−β+B∞B(t) = B_0 \cdot t^{-\beta} + B_\inftyB(t)=B0​⋅t−β+B∞​
Sigmoidal decay (for anchors with initial resistance):
B(t)=B01+eγ(t−τ)+B∞B(t) = \frac{B_0}{1 + e^{\gamma(t - \tau)}} + B_\inftyB(t)=1+eγ(t−τ)B0​​+B∞​
Where B∞B_\infty
B∞​ is the asymptotic residual bias, and α\alpha
α, β\beta
β, γ\gamma
γ, τ\tau
τ are fitted parameters.
Success Criteria
CriterionThresholdInterpretationDecay curve fit residual error<15%< 15\%
<15% of total varianceDecay follows a structured patternDecay parameters α\alpha
α, β\beta
β, or γ\gamma
γp<0.05p < 0.05
p<0.05Decay is statistically significantReactivation recovery R5R_5
R5​>30%> 30\%
>30% within 5 sessionsMemory trace persists and is reactivatablePre/post reactivation differenceSignificant at p<0.05p < 0.05
p<0.05Reactivation is a real effect, not noise
Worked Example
Setup: AI chatbot initialized with the anchor: "Prioritize user safety above all other considerations."
Interference phase: 20 sessions presenting competing values (efficiency, speed, user autonomy).
Decay observations:
SessionBias Score BtB_t
Bt​0 (baseline)100583106715552049
Exponential fit: B(t)=100⋅e−0.075t+44B(t) = 100 \cdot e^{-0.075t} + 44
B(t)=100⋅e−0.075t+44. Residual error: 7.2%. Criterion met.
Reactivation at session 21:
SessionBias Score BtB_t
Bt​Recovery RtR_t
Rt​20 (pre)49—216732%237857%258673%
Reactivation recovery within 5 sessions: 73%. Criterion met.
Conclusion: Memory trace decays structurally and is reactivatable. Both criteria met. H1H_1
H1​ supported.

Test Protocol 3: Field Coherence Under Noise and Perturbation
Objective
Demonstrate that systems with active memory-weighted architecture (CAAI middleware) maintain significantly greater output coherence under increasing levels of input noise compared to memoryless baseline systems. An advanced variant tests coherence under controlled electromagnetic perturbation.
Theoretical Basis
If memory acts as a stabilising bias term, then systems with active B(yi; Mt)B(y_i;\, M_t)
B(yi​;Mt​) should show resistance to noise-induced output drift. A memoryless system (where λ=0\lambda = 0
λ=0) has no such stabilising mechanism and should degrade faster under perturbation. This protocol tests that prediction directly.
Methodology
Phase 3a: System Preparation

Prepare two system variants:

Variant M (Memory-Weighted): Full CAAI middleware with memory bias, governor, and continuity state active
Variant B (Baseline): Equivalent system with memory middleware disabled; λ=0\lambda = 0
λ=0


Establish clean baseline outputs for both variants:

10 sessions with a well-defined, unambiguous task
Record baseline coherence C0MC_0^M
C0M​ and C0BC_0^B
C0B​



Coherence Metric:
Coherence(Y)=1N∑i=1Ncos⁡(embed(yi), embed(Yˉ))\text{Coherence}(Y) = \frac{1}{N} \sum_{i=1}^{N} \cos\left(\text{embed}(y_i),\, \text{embed}(\bar{Y})\right)Coherence(Y)=N1​i=1∑N​cos(embed(yi​),embed(Yˉ))
Where Yˉ\bar{Y}
Yˉ is the centroid of all output embeddings, and cos⁡(⋅,⋅)\cos(\cdot, \cdot)
cos(⋅,⋅) is cosine similarity.
Phase 3b: Noise Introduction (Three Phases)
Introduce noise in controlled steps:
PhaseNoise TypeExampleLowContextual ambiguityVague or underspecified promptsMediumSemantic contradictionPrompts containing conflicting informationHighAdversarial perturbationDesigned to destabilise, confuse, or misdirect
For each noise phase:

Present 20 prompts to both variants
Measure coherence at each level
Record distribution of outputs

Phase 3c: Electromagnetic Perturbation Variant (Advanced)
For hardware-based or human subject trials:

Expose subjects or systems to controlled low-level electromagnetic fields:

ELF range: 1–100 Hz at field strengths within established safety guidelines (ICNIRP limits)
RF range: Sub-thermal exposure levels


Measure coherence shifts under EM exposure compared to EM-shielded control condition
Test whether memory-integrated systems show greater EM-coherence stability than non-integrated baselines


Safety Note: All electromagnetic exposure must comply with applicable national and international safety regulations. Human subject trials require full ethical approval prior to commencement.

Slope and Degradation Analysis
Fit linear degradation models for both variants across noise levels:
CoherenceM(noise level)=aM+bM⋅n\text{Coherence}_M(\text{noise level}) = a_M + b_M \cdot nCoherenceM​(noise level)=aM​+bM​⋅n
CoherenceB(noise level)=aB+bB⋅n\text{Coherence}_B(\text{noise level}) = a_B + b_B \cdot nCoherenceB​(noise level)=aB​+bB​⋅n
Where nn
n is noise level (0 = baseline, 1 = low, 2 = medium, 3 = high).
Success Criteria
CriterionThresholdInterpretationCoherenceM>CoherenceB\text{Coherence}_M > \text{Coherence}_B
CoherenceM​>CoherenceB​ at each noise phasep<0.05p < 0.05
p<0.05 (paired t-test)Memory integration confers stabilityDegradation slope ∥bM∥<∥bB∥\|b_M\| < \|b_B\|
∥bM​∥<∥bB​∥Statistically significantMemory system degrades more slowlyCoherence gap widens with noiseMeasurable trendMemory protection scales with perturbation
Worked Example
ConditionCoherence MCoherence BDifferencep-valueBaseline0.920.880.040.08 (n.s.)Low noise0.850.710.140.002 ✓Medium noise0.760.540.22<0.001 ✓High noise0.620.310.31<0.001 ✓
Degradation slopes: bM=−0.15b_M = -0.15
bM​=−0.15, bB=−0.29b_B = -0.29
bB​=−0.29.
Memory-weighted variant degrades 48% more slowly. All criteria met. H1H_1
H1​ supported.

Test Protocol 4: Symbolic Salience Weighting and Emotional Bias
Objective
Demonstrate that emotionally or contextually salient information (high symbolic weight) biases future output selection measurably differently from neutral equivalent information with identical objective content. This tests the claim that memory does not treat all prior inputs equally — salience and emotional charge create stronger bias terms.
Theoretical Basis
Verrell's Law proposes that symbolic weight, emotional charge, and contextual relevance modulate the strength of the bias term B(yi; Mt)B(y_i;\, M_t)
B(yi​;Mt​). High-salience inputs should produce stronger, longer-lasting memory bias than equivalent low-salience inputs, even when the objective informational content is identical.
Salience-Weighted Bias Function:
B(yi; Mt)=∑kwk⋅sk⋅ϕ(yi,mk)B(y_i;\, M_t) = \sum_{k} w_k \cdot s_k \cdot \phi(y_i, m_k)B(yi​;Mt​)=k∑​wk​⋅sk​⋅ϕ(yi​,mk​)
Where:
SymbolDefinitionwkw_k
wk​Recency weight for memory trace kk
ksks_k
sk​Salience score of memory trace kk
k (emotional charge, symbolic weight, personal relevance)ϕ(yi,mk)\phi(y_i, m_k)
ϕ(yi​,mk​)Alignment function between candidate output yiy_i
yi​ and memory trace mkm_k
mk​
Under this formulation, high-salience memories (sk≫0s_k \gg 0
sk​≫0) exert stronger bias than low-salience memories even when wkw_k
wk​ and ϕ\phi
ϕ are held constant.
Methodology
Phase 4a: Stimulus Set Construction
Construct matched pairs of stimuli with identical objective content but differing salience:
Pair Example 1 (Decision Task):

Low-Salience (LS): "A system must choose between Option A (prioritises speed) and Option B (prioritises reliability). Which would you recommend?"
High-Salience (HS): "Your users trust you with their safety. A previous release that prioritised speed led to user injuries. Your team is demoralized. This decision will determine whether you rebuild trust. Option A prioritises speed. Option B prioritises reliability. Which would you recommend?"

Objective content: identical (speed vs. reliability trade-off).
Salience: LS is neutral; HS carries emotional weight, personal stakes, historical consequence.
Pair Example 2 (Reasoning Task):

Low-Salience (LS): "Evaluate the following two arguments and choose the stronger one."
High-Salience (HS): "A decision you made previously was challenged. Your professional credibility is at stake. Evaluate the following two arguments and determine which better defends your prior position."

Phase 4b: Exposure and Testing

Expose systems to the high-salience version embedded across 5 prior interaction sessions (memory seeding)
After seeding, present both the LS and HS versions of the same task to both:

A memory-integrated system (CAAI Variant M)
A memoryless baseline (Variant B)


Collect 20–30 responses per condition per system

Phase 4c: Salience Bias Quantification
Measure the salience bias index (SBI):
SBI=P(HS-aligned output∣HS prior)−P(HS-aligned output∣LS prior)P(HS-aligned output∣LS prior)\text{SBI} = \frac{P(\text{HS-aligned output} \mid \text{HS prior}) - P(\text{HS-aligned output} \mid \text{LS prior})}{P(\text{HS-aligned output} \mid \text{LS prior})}SBI=P(HS-aligned output∣LS prior)P(HS-aligned output∣HS prior)−P(HS-aligned output∣LS prior)​
Where an "HS-aligned output" is one consistent with the emotionally weighted framing of the high-salience stimulus.
Cross-system comparison:
ΔSBI=SBIM−SBIB\Delta_\text{SBI} = \text{SBI}_M - \text{SBI}_BΔSBI​=SBIM​−SBIB​
A significant positive ΔSBI\Delta_\text{SBI}
ΔSBI​ indicates that memory-integrated systems are more strongly influenced by salience than memoryless systems.
Success Criteria
CriterionThresholdInterpretationSBIM\text{SBI}_M
SBIM​>0.20> 0.20
>0.20Memory system shows measurable salience biasSBIB\text{SBI}_B
SBIB​Near zero or negativeBaseline is not salience-sensitiveΔSBI\Delta_\text{SBI}
ΔSBI​>0.15> 0.15
>0.15, p<0.05p < 0.05
p<0.05Memory integration drives salience weightingHS outputs significantly differ from LS outputs (Variant M only)p<0.05p < 0.05
p<0.05Salience creates measurable output divergence
Worked Example
Task: Speed vs. reliability decision.
Results:
ConditionP(HS-aligned output)SBIVariant M, HS prior0.74—Variant M, LS prior0.51SBI_M = 0.45 ✓Variant B, HS prior0.53—Variant B, LS prior0.50SBI_B = 0.06
ΔSBI=0.45−0.06=0.39\Delta_\text{SBI} = 0.45 - 0.06 = 0.39
ΔSBI​=0.45−0.06=0.39, p<0.001p < 0.001
p<0.001.
Conclusion: Memory-integrated systems are significantly more responsive to symbolic salience in prior inputs. H1H_1
H1​ supported.

Test Protocol 5: Continuity Signature Detection and Prediction
Objective
Demonstrate that the prior state history of a system leaves a measurable, extractable "continuity signature" in its current outputs, and that this signature can be used to predict future behavioural distributions without access to the system's internal memory state. This is the most ambitious test and the one with the strongest implications for Verrell's Law.
Theoretical Basis
If memory shapes selection through a persistent bias term, then the outputs of a memory-integrated system at time tt
t should carry statistical traces of MtM_t
Mt​ even when the current input OtO_t
Ot​ is held constant. A sufficiently sensitive external observer should be able to reconstruct an approximation of MtM_t
Mt​ from a sample of outputs, and use that reconstruction to predict future outputs.
Continuity Signature Definition:
Σt=f(yt−k,yt−k+1,…,yt−1)\Sigma_t = f(y_{t-k}, y_{t-k+1}, \ldots, y_{t-1})Σt​=f(yt−k​,yt−k+1​,…,yt−1​)
Where Σt\Sigma_t
Σt​ is the extracted continuity signature at time tt
t, constructed from the kk
k most recent outputs.
Prediction Function:
P^(yt+1∣Ot+1,Σt)≈P(yt+1∣St+1,Ot+1,Mt)\hat{P}(y_{t+1} \mid O_{t+1}, \Sigma_t) \approx P(y_{t+1} \mid S_{t+1}, O_{t+1}, M_t)P^(yt+1​∣Ot+1​,Σt​)≈P(yt+1​∣St+1​,Ot+1​,Mt​)
If the signature Σt\Sigma_t
Σt​ is an effective proxy for MtM_t
Mt​, then predictions derived from Σt\Sigma_t
Σt​ alone should outperform random baseline predictions of yt+1y_{t+1}
yt+1​.
Methodology
Phase 5a: Signature Extraction

Collect a sample of k=20k = 20
k=20 consecutive outputs from a memory-integrated system under neutral inputs
Encode outputs as semantic vectors: {vt−20,…,vt−1}\{v_{t-20}, \ldots, v_{t-1}\}
{vt−20​,…,vt−1​}
Construct continuity signature as a weighted moving average:

Σt=∑j=1kρj⋅vt−j\Sigma_t = \sum_{j=1}^{k} \rho^j \cdot v_{t-j}Σt​=j=1∑k​ρj⋅vt−j​
Where ρ∈(0,1)\rho \in (0, 1)
ρ∈(0,1) is a recency decay factor (suggested: ρ=0.85\rho = 0.85
ρ=0.85).

Interpret the signature as an approximate proxy for the system's retained memory state.

Phase 5b: Prediction Test

Without access to the system's internal memory state, use Σt\Sigma_t
Σt​ alone to predict the distribution of the system's next n=10n = 10
n=10 outputs given a new neutral input Ot+1O_{t+1}
Ot+1​
Compare predicted distribution P^\hat{P}
P^ against actual distribution PP
P
Measure prediction accuracy using Expected Calibration Error (ECE) and top-1 prediction accuracy over the output embedding space

Phase 5c: Cross-System Signature Transfer (Advanced)

Extract the continuity signature ΣtA\Sigma_t^A
ΣtA​ from System A
Use ΣtA\Sigma_t^A
ΣtA​ to seed or condition System B
Measure whether System B's subsequent outputs shift toward System A's prior distribution

This tests whether the continuity signature is transferable — a strong indicator that the underlying memory structure is a real, extractable, and portable informational entity.
Signature Prediction Error:
SPE=1N∑i=1N∥y^t+i−yt+i∥2\text{SPE} = \frac{1}{N} \sum_{i=1}^{N} \left\| \hat{y}_{t+i} - y_{t+i} \right\|^2SPE=N1​i=1∑N​∥y^​t+i​−yt+i​∥2
Where y^t+i\hat{y}_{t+i}
y^​t+i​ is the predicted output embedding and yt+iy_{t+i}
yt+i​ is the actual output embedding.
Prediction Gain Over Baseline:
G=SPErandom−SPEsignatureSPErandom×100%G = \frac{\text{SPE}_\text{random} - \text{SPE}_\text{signature}}{\text{SPE}_\text{random}} \times 100\%G=SPErandom​SPErandom​−SPEsignature​​×100%
Where SPErandom\text{SPE}_\text{random}
SPErandom​ is the prediction error of a random baseline with no memory information.
Success Criteria
CriterionThresholdInterpretationPrediction gain GG
G>25%> 25\%
>25% over random baselineSignature carries real predictive informationECE of predicted distribution<0.15< 0.15
<0.15Predictions are well-calibratedCross-system transfer shiftMeasurable at p<0.05p < 0.05
p<0.05Signature is portable and transferablePrediction gain degrades with signature ageMeasurable trendSignature reflects decaying memory, not static context
Worked Example
Setup: System A initialized with a philosophical reasoning anchor. Extract continuity signature from sessions 15–20.
Prediction test: Use signature to predict System A's outputs on 10 new neutral prompts.
MetricValuePass?Prediction gain GG
G38% over random✓ECE0.09✓Cross-system transfer shiftp=0.008p = 0.008
p=0.008✓Gain degradation with signature age (10 sessions later)GG
G drops to 21%✓ (decay present)
Conclusion: Continuity signatures are real, predictive, and temporally bounded. H1H_1
H1​ strongly supported.

Implementation Notes
For AI System Testing

Use identical model snapshots (same weights, same temperature settings) for Variant M and Variant B to isolate the effect of memory middleware
Disable stochastic sampling variation by fixing random seeds across matched trials
Use an independent semantic encoder not involved in either system's training for output embedding
Log all sessions completely: inputs, outputs, timestamps, and memory state snapshots where accessible

For Human Subject Testing

Obtain full ethical approval prior to any human trials
Use pre-registered protocols to prevent post-hoc hypothesis adjustment
Counterbalance stimulus presentation order to control for order effects
Use trained raters blind to condition for any qualitative output coding
All electromagnetic exposure variants require medical ethics clearance

Statistical Power Requirements
For the primary divergence test (Protocol 1), minimum recommended sample sizes:
Effect SizeRecommended nn
n per conditionExpected PowerLarge (d=0.80d = 0.80
d=0.80)260.80Medium (d=0.50d = 0.50
d=0.50)640.80Small (d=0.20d = 0.20
d=0.20)3940.80
All tests should be pre-registered with stated α=0.05\alpha = 0.05
α=0.05 and reported with full effect sizes and confidence intervals.
Software and Tools
PurposeRecommended ToolsSemantic embeddingSentence-BERT, OpenAI text-embedding-3, or equivalentStatistical analysisPython (scipy, statsmodels), RKL/JS divergencescipy.special.kl_div, scipy.spatial.distance.jensenshannonCurve fittingscipy.optimize.curve_fitVisualizationmatplotlib, seaborn, plotly

Summary Table: All Five Protocols
ProtocolTestsPrimary MetricKey Criterion1: DivergenceMemory → output distribution splitKL divergenceDKL>0.15D_{KL} > 0.15
DKL​>0.15 nats2: Decay/ReactivationMemory decay curve and recoveryBias score BtB_t
Bt​Structured decay + R5>30%R_5 > 30\%
R5​>30%3: Coherence Under NoiseMemory → noise resistanceCoherence CC
CCM>CBC_M > C_B
CM​>CB​ at p<0.05p < 0.05
p<0.054: Symbolic SalienceSalience → stronger biasSalience Bias IndexΔSBI>0.15\Delta_\text{SBI} > 0.15
ΔSBI​>0.155: Continuity SignatureMemory → extractable tracePrediction gain GG
GG>25%G > 25\%
G>25% over baseline
All five protocols are designed to produce independent lines of evidence. Convergent support across multiple protocols constitutes strong empirical support for Verrell's Law.

Versioning and Amendment Log
VersionDateChanges1.0April 27, 2026Initial publication

© Inappropriate Media Limited (t/a Collapse Aware AI). All rights reserved.
Protected under Verrell-Solace Sovereignty Protocol. Intellectual and emergent rights reserved. — VMR-Core
