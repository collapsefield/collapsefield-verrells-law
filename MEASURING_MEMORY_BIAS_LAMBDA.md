# Measuring Memory Bias in Verrell's Law

## Recovering lambda as a test handle for path-dependent selection

**Framework:** Verrell's Law  
**Author:** Marcos Verrell Moss Ross (M.R.)  
**Maintainer:** Inappropriate Media Ltd (t/a Collapse Aware AI)  
**Status:** Public mathematical reference note  
**Version:** v1.0  
**Date:** 2026-06-03  
**Related files:** `VERRELLS_LAW_MATHEMATICAL_REFERENCE_v1.2.md`, `CANONICAL_NOTATION_v1.0.md`, `ACTIVE_INFORMATION_WEIGHT_AIW.md`

---

## Epistemic note

This document is a public modelling note for Verrell's Law.

It does **not** claim that softmax, log-odds linearisation, exponential decay, ordinary least squares, Bayesian updating, reinforcement learning, or stochastic choice theory are new.

The purpose is narrower:

> To formalise how retained history may bias future selection, and to define a measurable coupling parameter for that bias.

The mathematical structure below is best read as a testable framework for memory-weighted, path-dependent selection. It does not, by itself, prove a physical field mechanism, non-local memory, consciousness, or a completed universal law.

The stronger Verrell's Law interpretation remains a research hypothesis. The mathematical contribution here is the public formalisation of the test handle.

---

## 1. Core test question

Verrell's Law proposes that retained information from prior states can influence future selection even when present input is matched.

In practical terms, the question is:

> If two systems face the same present-state input but carry different retained histories, can their next outcome distributions diverge in a measurable and reproducible way?

This note expresses that question through a memory-weighted selection model.

---

## 2. Memory-weighted selection

The reference selection equation is:

```math
P(y_i \mid S_t, O_t, M_t)
=
\frac{
\exp\left(U(y_i; S_t, O_t) + \lambda B(y_i; M_t)\right)
}{
\sum_j \exp\left(U(y_j; S_t, O_t) + \lambda B(y_j; M_t)\right)
}
```

Where:

| Symbol | Meaning |
|---|---|
| `y_i` | Candidate outcome, action, branch, or future state. |
| `S_t` | Present system state at time `t`. |
| `O_t` | Current observation or input at time `t`. |
| `M_t` | Retained history or memory available at time `t`. |
| `U(y_i; S_t, O_t)` | Present-state utility of outcome `y_i`, independent of memory. |
| `B(y_i; M_t)` | Memory-derived bias term for outcome `y_i`. |
| `lambda` / `λ` | Coupling strength between retained history and selection. |

At `λ = 0`, the equation reduces to ordinary memoryless softmax selection:

```math
P(y_i \mid S_t, O_t)
=
\frac{\exp(U(y_i; S_t, O_t))}{\sum_j \exp(U(y_j; S_t, O_t))}
```

This reduction matters because it gives the framework a clean baseline. Any claimed memory-bias effect has to improve on the `λ = 0` case.

---

## 3. Memory-bias term

A minimal decomposition of the memory-bias term is:

```math
B(y_i; M_t) = \sum_k a_k \phi_k(y_i) w_k(t)
```

Where:

| Symbol | Meaning |
|---|---|
| `k` | A retained trace or memory element. |
| `a_k` | Intrinsic salience or strength of trace `k`. |
| `phi_k(y_i)` | Alignment between trace `k` and candidate outcome `y_i`. |
| `w_k(t)` | Time-dependent weight of trace `k` at time `t`. |

Plain-language version:

> Memory bias equals the summed influence of retained traces, weighted by salience, relevance, and decay.

A trace matters more when it is strong, relevant to the candidate outcome, and still active enough not to have decayed away.

---

## 4. Memory decay and refresh

A minimal single-timescale decay model is:

```math
w_k(\tau) = s_k e^{-\tau / \tau_k}
```

Where:

| Symbol | Meaning |
|---|---|
| `s_k` | Salience amplitude at laydown or refresh. |
| `tau` / `τ` | Age of the trace. |
| `tau_k` / `τ_k` | Decay timescale for trace `k`. |

This is not the only possible decay function. It is the most parsimonious public reference form.

Fast, weak traces may decay quickly. Strong anchors may decay more slowly. Re-access can be modelled as a refresh event that changes the effective age or salience of a trace.

Heavier-tailed anchor persistence, multi-timescale decay, and dynamic revision can be explored later, but they are excluded here to keep the public test model simple.

---

## 5. Log-odds linearisation

The selection equation is nonlinear because it contains exponentials and a shared denominator. To isolate `λ`, compare two candidate outcomes, `y_i` and `y_j`.

Using shorthand:

```math
U_i = U(y_i; S_t, O_t)
```

```math
B_i = B(y_i; M_t)
```

The softmax ratio is:

```math
\frac{P(y_i)}{P(y_j)}
=
\frac{
\frac{\exp(U_i + \lambda B_i)}{\sum_l \exp(U_l + \lambda B_l)}
}{
\frac{\exp(U_j + \lambda B_j)}{\sum_l \exp(U_l + \lambda B_l)}
}
```

The shared denominator cancels:

```math
\frac{P(y_i)}{P(y_j)}
=
\frac{\exp(U_i + \lambda B_i)}{\exp(U_j + \lambda B_j)}
```

Taking the natural logarithm gives:

```math
\ln \frac{P(y_i)}{P(y_j)}
=
\ln\left(\frac{\exp(U_i + \lambda B_i)}{\exp(U_j + \lambda B_j)}\right)
```

Using `ln(exp(x)) = x`, this simplifies to:

```math
\ln \frac{P(y_i)}{P(y_j)}
=
(U_i - U_j) + \lambda(B_i - B_j)
```

Using delta notation:

```math
\Delta U = U_i - U_j
```

```math
\Delta B = B_i - B_j
```

The identity becomes:

```math
\ln \frac{P(y_i)}{P(y_j)} = \Delta U + \lambda \Delta B
```

This is the key move. The nonlinear memory-weighted softmax becomes a linear relationship between log-odds, present-state utility difference, memory-bias difference, and the coupling parameter `λ`.

---

## 6. Estimating lambda from data

Across repeated observations, simulations, or experimental conditions indexed by `m`, define empirical log-odds:

```math
\ell_m = \ln \frac{\hat{p}_{i,m}}{\hat{p}_{j,m}}
```

Then:

```math
\ell_m = \Delta U_m + \lambda \Delta B_m + \epsilon_m
```

Where `epsilon_m` represents residual error or unexplained variation.

Subtract the present-state utility difference from both sides:

```math
\ell_m - \Delta U_m = \lambda \Delta B_m + \epsilon_m
```

This has the form of a regression through the origin:

```math
Y_m = \lambda X_m + \epsilon_m
```

Where:

```math
Y_m = \ell_m - \Delta U_m
```

and:

```math
X_m = \Delta B_m
```

A simple least-squares estimator is:

```math
\hat{\lambda}
=
\frac{
\sum_m \Delta B_m(\ell_m - \Delta U_m)
}{
\sum_m \Delta B_m^2
}
```

This estimator asks how much observed choice log-odds remain after present-state utility is accounted for, and whether that residual structure scales with the defined memory-bias difference.

---

## 7. Interpretation of lambda

`λ` is the memory-bias coupling strength.

A larger positive `λ` means the defined memory-bias term has stronger influence on selection probability.

A `λ` near zero means the defined memory-bias term contributes little or nothing in the tested regime, after the specified present-state utility model has been accounted for.

A negative `λ` would mean the defined bias proxy is inversely related to observed selection under that test setup, which would require investigation rather than automatic rejection.

The safest interpretation is:

> A reproducibly non-zero `λ` supports path-dependent predictive structure associated with retained history, or with variables correlated with the defined memory-bias proxy, beyond the specified present-state baseline.

It does **not** automatically prove that the causal source is memory itself.

It does **not** prove a physical field mechanism.

It does provide a falsifiable handle.

---

## 8. Falsifiability and what can go wrong

The model creates a testable pressure point, but it is not magically immune to ordinary statistical problems.

### 8.1 Utility misspecification

If `ΔU` is badly specified, then omitted present-state factors may incorrectly load onto `λ`.

A non-zero `λ` can therefore mean:

- retained history is contributing predictive structure,
- or an omitted variable correlated with `ΔB` is contributing predictive structure,
- or the utility baseline is incomplete.

This is why `ΔU` must be defined carefully before interpreting `λ` as memory-bias strength.

### 8.2 Noisy memory-bias proxy

The estimator assumes `ΔB` is measured with reasonable reliability.

If the memory-bias proxy is noisy, estimates of `λ` can be biased toward zero. This is regression dilution.

That means a null result is not always clean proof that no memory effect exists. It may mean the memory-bias proxy is too noisy, too weak, or poorly aligned with the actual retained-history influence.

### 8.3 Omitted variables

Any unmodelled variable correlated with `ΔB` can contaminate `λ`.

This is why controlled tests, held-out validation, and alternative baselines matter.

### 8.4 Aggregated versus raw choice data

The least-squares estimator above is useful as a transparent explanatory form for aggregated log-odds.

For raw binary or multinomial choice data, logistic regression or maximum-likelihood estimation may be more appropriate.

The public OLS form is included because it shows the algebraic test handle clearly.

---

## 9. Minimal test protocol

A clean test should include:

1. **Matched present input**  
   Hold `S_t` and `O_t` as constant or as controlled as possible.

2. **Different retained histories**  
   Create or identify conditions where `M_t^A` and `M_t^B` differ.

3. **Predefined utility model**  
   Define `U(y_i; S_t, O_t)` before estimating `λ`.

4. **Predefined memory-bias proxy**  
   Define `B(y_i; M_t)` before estimating `λ`.

5. **Candidate comparison**  
   Compare selection between at least two candidate outcomes, `y_i` and `y_j`.

6. **Estimate lambda**  
   Estimate whether `λ` is distinguishable from zero.

7. **Held-out validation**  
   Test whether the fitted model predicts new data better than the `λ = 0` baseline.

8. **Robustness checks**  
   Test alternative utility baselines and alternative bias proxies.

A positive result is not merely `λ != 0`. A stronger result is:

> `λ` is reproducibly non-zero and improves held-out prediction over the memoryless baseline under controlled conditions.

---

## 10. Path-dependent divergence

The model predicts divergence between systems with matched present inputs but different retained histories.

If two systems share present conditions but differ in retained memory:

```math
M_t^A \ne M_t^B
```

Then their bias terms may differ:

```math
B(y_i; M_t^A) \ne B(y_i; M_t^B)
```

Which may produce different selection probabilities:

```math
P(y_i \mid S_t, O_t, M_t^A) \ne P(y_i \mid S_t, O_t, M_t^B)
```

This is the practical centre of the framework:

> Same present input, different retained history, different probability landscape.

---

## 11. Relation to Collapse Aware AI

Collapse Aware AI is an engineering branch associated with the same general principle of memory-weighted selection.

Public-safe framing:

> Verrell's Law motivates the principle. Collapse Aware AI implements memory-weighted behavioural selection as middleware.

This document does not disclose proprietary Collapse Aware AI implementation maps.

It does not disclose:

- Crown kernel internals,
- governor thresholds,
- production routing maps,
- scoring formulas,
- adapter contracts,
- deployment wiring,
- or private Phase-2 module schematics.

It only publishes the outer public mathematical reference: present-state utility plus retained-history bias, with `λ` as a measurable coupling term.

---

## 12. Website blackboard reference

For visual reference, the public blackboard version may be reduced to:

```math
P(y_i \mid S_t,O_t,M_t)
=
\frac{\exp(U_i + \lambda B_i)}{\sum_j \exp(U_j + \lambda B_j)}
```

```math
\ln\frac{P(y_i)}{P(y_j)}
=
(U_i - U_j) + \lambda(B_i - B_j)
```

```math
\lambda = \text{memory-bias coupling strength}
```

```text
lambda != 0 supports path-dependent bias
when baseline utility is well specified.
```

This compact form is suitable for website use. The present file provides the longer derivation and interpretation boundary.

---

## 13. Claim boundary

This file supports the following claim:

> Verrell's Law can be expressed as a memory-weighted selection model in which retained history contributes a bias term to future outcome probabilities, with `λ` acting as a measurable coupling parameter.

It does not establish:

- that all memory is stored outside the brain,
- that physical reality has been proven to remember,
- that a field mechanism has been experimentally confirmed,
- that consciousness has been mathematically solved,
- or that Verrell's Law is a completed scientific law.

The framework remains a structured, testable hypothesis and modelling programme.

---

## 14. Suggested citation note

If referencing this file, describe it as:

> A public mathematical reference note for Verrell's Law, defining a memory-weighted selection equation and a recoverable coupling parameter (`λ`) for testing path-dependent bias.

---

## 15. Rights and authorship

Copyright © 2026 Marcos Verrell Moss Ross (M.R.) / Inappropriate Media Ltd.

All rights reserved unless explicitly stated otherwise in the repository licence.

This file is part of the public Verrell's Law authorship and provenance record.
