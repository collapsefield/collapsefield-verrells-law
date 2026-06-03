# Verrell's Law — Mathematical Reference (v1.2)

**Framework:** Verrell's Law  
**Author:** M.R.  
**Maintainer:** Inappropriate Media Limited (t/a Collapse Aware AI)  
**Status:** Public mathematical reference — extends `CANONICAL_NOTATION_v1.0`  

**Epistemic note:** Claims are tagged `[derived]`, `[ansatz]`, or `[speculative]`. The framework is presented as a set of testable hypotheses and research questions, not established scientific law.

This sheet is consistent with `CANONICAL_NOTATION_v1.0.md`. Where it adds new structure (§4–§5), those additions are research-stage and explicitly tagged. No canonical symbol is silently altered.

---

## 1. Canonical Selection Equation `[derived]`

The memory-weighted selection probability is a Boltzmann/softmax form over candidate states, with a memory-derived bias added to the present-state utility:

$$
P(y_i \mid S_t, O_t, M_t) =
\frac{\exp\!\left( U(y_i; S_t, O_t) + \lambda\, B(y_i; M_t) \right)}
{\sum_j \exp\!\left( U(y_j; S_t, O_t) + \lambda\, B(y_j; M_t) \right)}
$$

| Symbol | Meaning |
|---|---|
| $P(y_i \mid S_t, O_t, M_t)$ | Probability of selecting candidate $y_i$ given current state, observation, and retained memory |
| $y_i$ | Candidate output / behavioural branch / future probabilistic state |
| $S_t$ | Current system state at time $t$ |
| $O_t$ | Current observation / input at time $t$ |
| $M_t$ | Retained informational history accumulated prior to $t$ |
| $U(y_i; S_t, O_t)$ | Present-state utility (memory-independent component) |
| $B(y_i; M_t)$ | Memory-derived bias term; encodes Active Information Weight (AIW) |
| $\lambda$ | Memory-bias coupling coefficient |

**Reduction property `[derived]`.** At $\lambda = 0$ the bias term vanishes and the rule reduces exactly to memoryless selection $P(y_i) = \mathrm{softmax}(U(y_i))$. This is the zero-bias baseline against which any memory effect is measured.

---

## 2. Path-Dependent Divergence `[derived]`

Two systems with identical present-state inputs ($U$, $O_t$, $S_t$) but different retained histories ($M_t^A \ne M_t^B$) diverge in selection probability:

$$
\Delta P(y_i) \;\propto\; \lambda \cdot \left[\, B(y_i; M_t^A) - B(y_i; M_t^B) \,\right]
$$

This is the core falsifiable prediction: divergence scales with the coupling $\lambda$ and the bias difference $\Delta B = B^A - B^B$. If no repeatable divergence is observed when $\Delta B \ne 0$, the AIW claim fails.

---

## 3. Weighted Emergence Layering (WEL) `[ansatz]`

WEL formalizes the recursive accumulation of bias across sequential selections. Let the memory state update after each selection $y_{(t)}$:

$$
M_{t+1} = \Phi\!\left( M_t,\, y_{(t)},\, O_t \right)
$$

and let the bias at step $t$ be a sum over retained traces $k$:

$$
B(y_i; M_t) = \sum_{k} a_k\, \phi_k(y_i)\, w_k(t)
$$

where $\phi_k(y_i)$ is the alignment of candidate $y_i$ with trace $k$, $a_k$ is the trace's intrinsic salience, and $w_k(t)$ is its time-dependent weight. In the decay form below, $w_k(t)=w_k(\tau)$ where $\tau=t-t_k$.

Because each selection feeds back into $M_{t+1}$, the bias landscape is path-dependent: continuity emerges through layered informational weighting rather than being imposed.

**Identifiability caveat `[ansatz]`.** The decomposition into separate traces is only meaningful if the $\phi_k$ are experimentally distinguishable. Otherwise $B$ collapses to a single effective scalar bias per candidate.

---

## 4. Memory-Bias Decay `[ansatz]`

The canonical notation defines $B(y_i; M_t)$ but does not specify how a trace's contribution attenuates over time. This section proposes a minimal, single-timescale exponential decay. It is a research-stage ansatz, not a derived result.

For a trace $k$ laid down at time $t_k$, with age $\tau = t - t_k$:

$$
w_k(\tau) = s_k\, e^{-\tau / T_k}
$$

| Symbol | Meaning | Constraint |
|---|---|---|
| $s_k$ | Salience amplitude of trace $k$ at laydown | $s_k \ge 0$ |
| $T_k$ | Decay timescale of trace $k$ | $T_k > 0$ |

**Rationale.** A single exponential is the most parsimonious falsifiable decay: one amplitude, one timescale per trace. Transient traces fade quickly (small $T_k$); strong anchors are represented by long $T_k$. A trace is reinforced (its $s_k$ refreshed, its effective age reset) whenever re-accessed, which is how WEL sustains continuity.

**Limiting behaviour `[derived]` given the ansatz:**

- $\tau \to 0$: $w_k \to s_k$ (full weight at laydown).
- $\tau \to \infty$: $w_k \to 0$ (no permanent bias; preserves eventual forgetting).

**Deferred extension `[speculative]`.** A heavy-tailed (power-law) anchor component may be introduced after pilot data demonstrates that single-exponential decay underfits long-range anchor persistence. It is deliberately excluded from this public sheet to avoid over-parameterisation; it is held in a deeper research note.

---

## 5. Recovering $\lambda$ from Data `[ansatz]`

A falsifiability requirement: $\lambda$ must be experimentally recoverable, not assumed. This section gives an estimator that backs $\lambda$ out of observed selection frequencies.

### 5.1 Two-candidate log-odds form `[derived]`

For two candidates $y_i, y_j$, the selection equation gives a log-odds that is linear in $\lambda$:

$$
\ln\frac{P(y_i)}{P(y_j)}
= \big[U(y_i) - U(y_j)\big] + \lambda\big[B(y_i; M_t) - B(y_j; M_t)\big]
$$

Writing $\Delta U = U(y_i) - U(y_j)$ and $\Delta B = B(y_i; M_t) - B(y_j; M_t)$:

$$
\ln\frac{P(y_i)}{P(y_j)} = \Delta U + \lambda\,\Delta B
$$

### 5.2 Estimator `[ansatz]`

Run $N$ trials at known/controlled $\Delta U$ and $\Delta B$, measure empirical selection frequency $\hat{p}_i = n_i / N$. The single-point estimate:

$$
\hat{\lambda} = \frac{\displaystyle\ln\!\frac{\hat{p}_i}{1 - \hat{p}_i} - \Delta U}{\Delta B}, \qquad \Delta B \ne 0
$$

Across many conditions with varying $\Delta B$, fit by ordinary least squares: regress the empirical log-odds (minus $\Delta U$) on $\Delta B$ through the origin. The slope is $\hat\lambda$; a non-zero, stable slope across independent conditions is the positive result. A slope statistically indistinguishable from zero falsifies the AIW claim in that regime.

$$
\hat\lambda = \frac{\sum_m \Delta B_m \left(\ell_m - \Delta U_m\right)}{\sum_m \Delta B_m^2},
\qquad
\ell_m = \ln\frac{\hat p_{i,m}}{1-\hat p_{i,m}}
$$

### 5.3 Confidence / sufficiency `[derived]`

The variance of a single log-odds estimate scales as:

$$
\mathrm{Var}(\hat\ell) \approx \frac{1}{N\hat p_i (1-\hat p_i)}
$$

so the standard error on $\hat\lambda$ from one condition is approximately:

$$
\frac{1}{|\Delta B|}\sqrt{\frac{1}{N\hat p_i(1-\hat p_i)}}
$$

Larger $|\Delta B|$ and larger $N$ both tighten the estimate. In practice: design trials with strong bias contrast and high trial counts.

---

## 6. Consistency / Claim Boundaries

- **No-signalling.** Any application to physical systems requires $B$ to be evaluated locally; bias at one location cannot depend on spacelike-separated state.
- **Reduction.** The rule must recover standard memoryless statistics at $\lambda = 0$ and wherever $\lambda\,\Delta B$ is small relative to utility separations.
- **Prior art.** Softmax, Bayesian updating, reinforcement learning, and Markov processes are not claimed as inventions. The specific claim is narrower: retained informational history can act as an active, measurable probabilistic weighting on future selection, producing path-dependent divergence.
- **Status.** $\lambda$, the decay law (§4), and the WEL decomposition (§3) are testable hypotheses. They stand or fall on whether $\hat\lambda$ is reproducibly non-zero and whether the decay timescales are recoverable.

---

## Core Terms

- **Active Information Weight (AIW):** the measurable influence of retained prior information on future selection probability.
- **Weighted Emergence Layering (WEL):** recursive layering of retained information so prior selections influence later selection through measurable weighting.
- **Path-dependent divergence:** divergence between otherwise identical systems caused by different retained informational histories.
- **Memory-bias coupling coefficient ($\lambda$):** the term controlling how strongly retained information affects future selection.

---

*Notation consistent with `CANONICAL_NOTATION_v1.0.md`. Sections 4–5 are research-stage extensions; the two-component decay is deferred to a separate research note. © Marcos Verrell Moss Ross / Inappropriate Media Limited.*