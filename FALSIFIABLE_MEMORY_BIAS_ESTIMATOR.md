# A Falsifiable Estimator for Memory-Biased Selection

**Verrell's Law — Measurement Note**

> This note is the compact measurement-protocol version of the λ estimator introduced in `MEASURING_MEMORY_BIAS_LAMBDA.md`.

---

## Framework Link

This estimator is measurement machinery for the retained-state selection framework defined in:

> `RETAINED_STATE_SELECTION_FRAMEWORK.md`

The estimator should be used to test whether retained history contributes measurable selection divergence beyond the baseline condition.

The key public claim is not that the selection equation is mathematically novel. The claim is that retained-state influence can be pre-defined, measured, and tested against a null baseline.

This note specifies a single testable claim: retained history may exert measurable influence on selection behaviour over and above what present-state utility predicts. It concerns *measurement of behaviour only*. It is independent of any particular engineering implementation.

## 1. The selection model

Let a system choose among alternatives $\{y_1,\dots,y_K\}$ under present state $S_t$, observation $O_t$, and retained history $M_t$. Each alternative $i$ carries a present-state utility $U_i$ and a memory-bias term $B_i$. The memory-weighted selection probability is:

$$
P(y_i \mid S_t, O_t, M_t) = \frac{\exp\left(U_i + \lambda B_i\right)}{\sum_{j} \exp\left(U_j + \lambda B_j\right)}
$$

The scalar $\lambda$ is the memory-bias coupling strength under the declared scoring convention. If $\lambda = 0$, the equation reduces to the utility-only choice rule with respect to this tested term.

### Identifiability note

Only the product enters the selection score:

```math
\lambda B(y_i;M_t)
```

Therefore `λ` should not be interpreted without a predefined baseline, retained-state feature, candidate set, scoring scale and estimation rule.

## 2. Identification: recovering λ

For alternatives $i$ and $j$:

$$
\ln\left(\frac{P(y_i)}{P(y_j)}\right) = (U_i-U_j)+\lambda(B_i-B_j)
$$

Writing $\Delta U = U_i-U_j$ and $\Delta B = B_i-B_j$:

$$
\ln\left(\frac{P(y_i)}{P(y_j)}\right)=\Delta U+\lambda\Delta B
$$

This reduces the choice model to a linear relationship in the parameter of interest under the declared scoring convention.

## 3. Estimator

Across trials $m=1,\dots,N$, let observed log-odds be $\ell_m$:

$$
\ell_m=\Delta U_m+\lambda\Delta B_m+\epsilon_m
$$

Then:

$$
(\ell_m-\Delta U_m)=\lambda\Delta B_m+\epsilon_m
$$

The through-origin ordinary-least-squares estimator is:

$$
\boxed{\;\lambda^{*}=\frac{\sum_{m=1}^{N}\Delta B_m(\ell_m-\Delta U_m)}{\sum_{m=1}^{N}\Delta B_m^2}\;}
$$

The later canonical specification also recommends an intercept diagnostic where appropriate, because a materially non-zero intercept can indicate uncontrolled mismatch between conditions.

## 4. Confounds

### 4.1 A non-zero estimate need not be retained history

$\lambda^{*}$ can absorb omitted influences correlated with $\Delta B$.

**Mitigation:** randomise or independently manipulate history while holding present conditions fixed; include placebo or irrelevant-state controls; and test whether the estimate survives plausible omitted controls.

### 4.2 A near-zero estimate need not be a clean null when the predictor is unreliable

Measurement error in the retained-state proxy can attenuate the estimate toward zero.

**Mitigation:** report proxy reliability and use an appropriate errors-in-variables treatment where required.

## 5. Precommitted decision rule

The verdict must be fixed before confirmatory data are inspected.

- **Support in the tested regime:** the retained-state coefficient is directionally consistent, distinguishable from the preregistered null, survives declared confound/placebo checks and predicts held-out data.
- **Not supported / refuted in the tested regime:** the coefficient remains within the preregistered null region under adequate power and reliable measurement, or other preregistered falsification conditions are met.
- **Indeterminate:** power, measurement reliability or protocol integrity is insufficient for a supported verdict.

Thresholds should be fixed by the preregistered design and, where relevant, power analysis.

---

## Scope and status

This is a measurement protocol, not a physical mechanism claim. A reproducible retained-state coefficient supports a path-dependent, history-correlated selection effect in the tested regime; it does not by itself establish an electromagnetic, quantum, consciousness or other physical mechanism.

For independent empirical testing, the retained-state predictor must be frozen independently of the confirmatory selection outcome. Reusing a selector’s own internal score to verify the behaviour it was designed to produce is engineering conformance unless a separate independent analysis route is supplied.

---

**Version:** retained-state framework measurement note  
**Updated:** 2026-09-14  
**Author / originator:** Marcos Verrell Moss Ross (M.R.)

Copyright © 2026 Marcos Verrell Moss Ross (M.R.).
