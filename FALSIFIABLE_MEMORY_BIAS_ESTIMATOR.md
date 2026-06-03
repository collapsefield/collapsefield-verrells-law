# A Falsifiable Estimator for Memory-Biased Selection

**Verrell's Law — Measurement Note**

> This note is the compact measurement-protocol version of the λ estimator introduced in `MEASURING_MEMORY_BIAS_LAMBDA.md`.

---

This note specifies a single, testable claim: that retained history exerts a measurable bias on a system's selection behaviour, over and above what its present-state utility predicts. It gives the model, the identification step that makes the effect recoverable, the closed-form estimator, the two confounds that must be controlled, and a pre-committed decision rule for support or refutation. The note concerns *measurement of behaviour only*. It does not describe, and is independent of, any mechanism for producing or governing such bias in an engineered system.

## 1. The selection model

Let a system choose among alternatives $\{y_1,\dots,y_K\}$ under present state $S_t$, observation $O_t$, and retained history $M_t$. Each alternative $i$ carries a present-state utility $U_i$ (what current conditions alone favour) and a memory-bias term $B_i$ (the contribution attributable to retained history). The memory-weighted selection probability is

$$
P(y_i \mid S_t, O_t, M_t) = \frac{\exp\left(U_i + \lambda B_i\right)}{\sum_{j} \exp\left(U_j + \lambda B_j\right)}
$$

The scalar $\lambda$ is the *memory-bias coupling strength*: the quantity the whole protocol exists to estimate. If $\lambda = 0$, the equation collapses to a standard utility-only choice rule and history has no role.

## 2. Identification: recovering λ

The selection model is non-linear in its parameters because of the normalising denominator. The denominator is, however, identical for every alternative, so it cancels under a log-odds comparison of any two alternatives $i$ and $j$:

$$
\ln\left(\frac{P(y_i)}{P(y_j)}\right) = \ln\left(\exp(U_i + \lambda B_i)\right) - \ln\left(\exp(U_j + \lambda B_j)\right) = (U_i - U_j) + \lambda (B_i - B_j)
$$

Writing $\Delta U = U_i - U_j$ and $\Delta B = B_i - B_j$, the relationship is exactly linear in $\lambda$:

$$
\ln\left(\frac{P(y_i)}{P(y_j)}\right) = \Delta U + \lambda\, \Delta B
$$

This is the load-bearing step: a non-linear choice model has been reduced to a linear relationship in the one unknown of interest, with no approximation.

## 3. The estimator

Across $m = 1,\dots,N$ trials we observe empirical choice frequencies $\hat{p}_{i,m}$ rather than true probabilities, so we work with the observed log-odds $\ell_m$ and admit a noise term $\epsilon_m$:

$$
\ell_m = \Delta U_m + \lambda\, \Delta B_m + \epsilon_m
$$

Subtracting the known present-state utility difference $\Delta U_m$ from both sides isolates the component of choice variance that present utility cannot explain, leaving a regression through the origin:

$$
\left(\ell_m - \Delta U_m\right) = \lambda\, \Delta B_m + \epsilon_m
$$

Minimising the residual sum of squares $S(\lambda) = \sum_{m}\left((\ell_m - \Delta U_m) - \lambda\, \Delta B_m\right)^2$ gives the ordinary-least-squares estimator in closed form:

$$
\boxed{\;\lambda^{*} = \frac{\displaystyle\sum_{m=1}^{N} \Delta B_m\left(\ell_m - \Delta U_m\right)}{\displaystyle\sum_{m=1}^{N} \Delta B_m^{2}}\;}
$$

## 4. Two confounds that must be controlled

The estimator is only as good as the specification feeding it. Two failure modes are stated here explicitly, because each undermines a naive reading of the result and each cuts in a different direction.

### 4.1 A non-zero λ\* need not be "memory"

$\lambda^{*}$ absorbs *any* influence on choice that is omitted from $\Delta U$ and correlated with $\Delta B$. A non-zero estimate therefore licenses only the conclusion that *some* factor outside the specified utility, correlated with the bias proxy, is shifting choice — not that this factor is retained history specifically.

**Mitigation:** randomise or independently manipulate history while holding present conditions fixed; include a placebo bias regressor known to carry no historical information; and report whether $\lambda^{*}$ survives the addition of plausible omitted controls.

### 4.2 A near-zero λ\* need not be a clean null

If the bias proxy $\Delta B$ is itself measured with error, classical regression dilution (attenuation) biases $\lambda^{*}$ toward zero. A null result is then ambiguous: it is consistent both with a genuine absence of memory bias and with a real effect masked by a noisy proxy.

**Mitigation:** report the reliability of the $\Delta B$ measurement; apply an attenuation correction or errors-in-variables estimator where reliability is below threshold; and treat a null as informative only when proxy reliability is established.

## 5. Pre-committed decision rule

The hypothesis is testable only if the verdict is fixed before the data are seen. We therefore commit, in advance, to the following rule. Let $r$ denote the reliability of the $\Delta B$ proxy and let $\mathrm{CI}_{95}(\lambda^{*})$ denote the 95% confidence interval for the estimator.

- **Support.** The memory-bias hypothesis is supported if $\mathrm{CI}_{95}(\lambda^{*})$ excludes $0$ at $N \ge N_{\min}$ trials with proxy reliability $r \ge r_{\min}$, *and* $\lambda^{*}$ remains sign-stable and non-zero under the omitted-control and placebo checks of §4.1.
- **Refuted in the tested regime.** The hypothesis is refuted in the tested regime if $\mathrm{CI}_{95}(\lambda^{*})$ contains $0$ at $N \ge N_{\min}$ with proxy reliability $r \ge r_{\min}$ after attenuation correction. This verdict applies *only* to that setup — that proxy, that data, that utility model — and does not generalise beyond the regime tested.
- **Indeterminate.** Any outcome with $N < N_{\min}$ or $r < r_{\min}$ is reported as indeterminate, not as evidence either way.

The thresholds $N_{\min}$ and $r_{\min}$ are to be fixed by a power analysis prior to data collection and reported alongside the result.

---

## Scope and status

This is a measurement protocol, not a physical claim. A reproducible non-zero $\lambda$ establishes a path-dependent, history-correlated bias in observed selection; it does not by itself establish any field mechanism, nor does it require one. All quantities above are defined over observable choice behaviour. The protocol is offered for adversarial testing: the conditions under which it would fail are stated as plainly as the conditions under which it would succeed.

A result of $\lambda \approx 0$ in any single test is *refuted in the tested regime* only — it constrains that specific setup and does not falsify the broader framework, which must be assessed across many regimes, proxies, and utility specifications.
