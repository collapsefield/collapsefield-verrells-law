# Verrell’s Law — Frequency-Coupled Retained-State Extension
## Exploratory Mathematics v0.2 — Review-Hardened Form

**Status:** Early exploratory mathematical work — non-canonical, unvalidated, and not evidence for the Principal Hypothesis.  
**Date:** 27 July 2026  
**Author:** M.R. (Marcos Verrell Moss Ross), Author of Verrell’s Law  
**Maintainer:** Inappropriate Media Limited (t/a Collapse Aware AI)  
**Repository:** `collapsefield/collapsefield-verrells-law`

---

## 1. Purpose and Revision Status

This file hardens the exploratory frequency-coupled retained-state mathematics introduced in v0.1.

The canonical Verrell’s Law specification remains unchanged:

```math
\Delta L = \lambda\Delta R + \varepsilon,
```

with `λ` interpreted only under a declared scoring, normalization and test regime.

The exploratory question remains narrower:

> **Can a controlled frequency-dependent intervention provide reproducible predictive information about either (A) the strength with which retained state affects later selection, or (B) the persistence of the retained state itself?**

This v0.2 revision specifically addresses:

- nuisance parameters that exist only under the frequency-effect alternative;
- confounding between baseline coupling and broad frequency-response terms;
- over-interpretation of a Lorentzian response shape;
- causal linear-response and phase constraints;
- separation of coupling modulation from retention-kernel modulation;
- apparatus resonance, timing, aliasing and sampling artifacts;
- softmax scale and temperature identifiability;
- a direct on/off/on discriminator between Models A and B;
- strict separation of software-periodicity experiments from physical-substrate/EM experiments.

This document **supersedes v0.1 as the current exploratory frequency mathematics**, while v0.1 remains preserved as part of the development trail.

No frequency effect is claimed to have been observed.

---

## 2. Canonical Starting Point

For paired binary trials, the canonical estimation model is:

```math
\Delta L_k
=
\alpha
+
\lambda\Delta R_k
+
\varepsilon_k.
```

where:

- `ΔL_k` is the change in candidate-relative selection log-odds relative to baseline;
- `ΔR_k` is the preregistered retained-state compatibility difference;
- `λ` is the retained-state coupling under the frozen normalization convention;
- `α` is a diagnostic intercept;
- `ε_k` is residual variation.

The frequency extension does not change the canonical Principal Hypothesis. It asks whether an additional controlled intervention explains out-of-sample variation beyond this baseline.

---

## 3. Separate the Drive Frequency from Analysis Frequency

Let the externally imposed or experimentally varied drive frequency be:

```math
\omega_d = 2\pi f_d,
```

where `f_d` is the declared drive frequency in hertz.

The subscript `d` is deliberate. It prevents confusion between:

- the frequency of an imposed experimental drive, `ω_d`; and
- a Fourier-domain analysis variable, written later as `Ω`.

A frequency value is not a complete intervention specification. A physical experiment must also freeze or explicitly control relevant quantities such as amplitude, power or delivered energy, exposure duration, temperature, geometry, shielding, hardware state and timing.

These variables are **controls**, not automatically additional free arguments of the Verrell coupling function.

The first experiment should therefore avoid an unrestricted form such as:

```text
λ(ω, A, φ, E, ...)
```

because that introduces unnecessary degrees of freedom and, in many apparatuses, correlated quantities such as amplitude and delivered energy.

The first question is narrower: does a frequency-structured term survive when the intervention protocol is otherwise fixed?

---

## 4. Model A — Frequency-Modulated Selection Coupling

Model A assumes that the retained history is already fixed and that the drive changes only the strength with which that retained state influences selection.

Define:

```math
\lambda_{\mathrm{eff}}(\omega_d)
=
\lambda_0
+
\kappa h(\omega_d),
```

where:

- `λ₀` is baseline retained-state coupling;
- `κ` is the frequency-structured modulation coefficient;
- `h(ω_d)` is a frozen, dimensionless response basis or profile.

Then:

```math
\Delta L_k
=
\alpha
+
\lambda_0\Delta R_k
+
\kappa h(\omega_{d,k})\Delta R_k
+
\varepsilon_k.
```

The frequency-specific null is:

```math
H_0^{(F)}:\kappa=0.
```

The exploratory alternative is:

```math
H_1^{(F)}:\kappa\neq0.
```

This remains separate from the canonical retained-state hypothesis:

```math
H_0:\lambda=0
\qquad\text{vs}\qquad
H_1:\lambda>0.
```

A supported retained-state effect does not imply a frequency effect.

---

## 5. Serious Statistical Boundary — Unknown Peak Parameters Are Unidentified Under the Null

Suppose `h(ω_d)` is given a peaked form with unknown centre frequency `ω₀` and width `Γ`:

```math
h(\omega_d;\omega_0,\Gamma).
```

Under:

```math
H_0^{(F)}:\kappa=0,
```

both `ω₀` and `Γ` disappear from the model. They therefore cannot be identified under the null.

This is the class of problem studied by Davies: a nuisance parameter is present only under the alternative. Standard nominal `t`, Wald or ordinary likelihood-ratio calibration for `κ` is not valid if `ω₀` and/or `Γ` were selected by searching the same data.

Therefore **v0.2 prohibits a naive peak search followed by an ordinary p-value on the winning `κ`**.

### Confirmatory routes

Two routes are acceptable.

### Route 1 — independently fixed peak parameters

If `ω₀` and `Γ` are obtained from independent measurement or frozen before the confirmatory data are collected, then `h(ω_d)` is fixed and the interaction coefficient `κ` can be estimated under the declared regression model.

### Route 2 — discovery followed by held-out prediction

If the response shape, centre or width is learned from the data:

1. use only a discovery/training set to select the response model;
2. freeze the complete fitted rule;
3. evaluate it on untouched frequencies, runs or experimental blocks;
4. compare predictive performance against the frequency-independent model.

Where outcome probabilities are available, held-out predictive log-loss or log score is preferred. For direct `ΔL` measurements, a preregistered held-out prediction error or likelihood can be used.

Any bootstrap, permutation, sup-score or sup-likelihood procedure intended to attach a null probability to a scanned frequency model must repeat the **entire search/fitting procedure inside each null replicate**. The maximum or selected model cannot be treated as though it had been specified in advance.

For this exploratory programme, **held-out prediction is the primary recommended route** because it directly tests whether the frequency term adds information beyond the canonical model without pretending that a searched peak has an ordinary one-parameter null distribution.

---

## 6. Broad-Response Degeneracy Between `κ` and `λ₀`

For the normalized Lorentzian candidate:

```math
h_L(\omega_d)
=
\frac{\Gamma^2}
{(\omega_d-\omega_0)^2+\Gamma^2},
```

we have:

```math
\Gamma\rightarrow\infty
\quad\Rightarrow\quad
h_L(\omega_d)\rightarrow1
```

across any finite sampled frequency range.

Then:

```math
\lambda_0\Delta R
+
\kappa h_L(\omega_d)\Delta R
\approx
(\lambda_0+\kappa)\Delta R,
```

so `κ` and `λ₀` become non-separable.

Therefore, if a peaked parametric model is used, the sampled frequency range must contain substantial data both within and well outside the proposed response width. A frequency grid clustered near the candidate peak is insufficient.

### Design rule

For a preregistered candidate `ω₀, Γ`, the frequency plan must explicitly include:

- on-peak or near-peak conditions;
- shoulder conditions;
- clearly off-peak conditions;
- enough repeated observations in each region to estimate the baseline and modulation separately.

If the sampled band is too narrow to distinguish `h(ω_d)` from a constant, the experiment cannot identify `κ` separately from `λ₀` and should be declared non-informative for Model A.

---

## 7. Do Not Start by Assuming a Lorentzian

A Lorentzian-shaped response is mathematically convenient and physically appropriate for some damped linear systems, but using it as the first model risks importing a resonance interpretation before a resonant degree of freedom has been identified.

Therefore v0.2 changes the order of analysis.

### Stage 1 — frequency-structure discovery

First ask only whether predictive response varies with drive frequency.

Permitted exploratory representations include:

- preregistered frequency bins;
- a low-complexity penalized spline;
- another explicitly regularized smooth response model;
- a small set of physically motivated contrasts.

The complexity penalty, knots or bins must be fixed from the training data only and the result evaluated on held-out data.

### Stage 2 — peaked parametric candidate

A Lorentzian or other resonant lineshape should be introduced only when:

1. an independently characterised subsystem supplies a plausible centre/width; or
2. exploratory data show reproducible localized structure that is then frozen and tested on new data.

A good fit to a Lorentzian is not itself evidence that the underlying mechanism is a physical oscillator.

---

## 8. Causal Linear-Response Boundary and Phase Prediction

A scalar function `h(ω_d)` can be used merely as a descriptive predictor. In that limited role, no Kramers–Kronig claim is required.

However, if the frequency effect is promoted to a **causal linear physical response** or susceptibility, then the response must be treated as complex:

```math
\chi(\Omega)
=
\chi'(\Omega)
+
i\chi''(\Omega),
```

and causality constrains the real and imaginary parts through the Kramers–Kronig relations.

Schematically:

```math
\chi'(\Omega)
=
\frac{1}{\pi}
\mathcal{P}
\int_{-\infty}^{\infty}
\frac{\chi''(\Omega')}
{\Omega'-\Omega}
\,d\Omega',
```

```math
\chi''(\Omega)
=
-\frac{1}{\pi}
\mathcal{P}
\int_{-\infty}^{\infty}
\frac{\chi'(\Omega')}
{\Omega'-\Omega}
\,d\Omega'.
```

This creates an additional falsification opportunity.

If an experiment claims a causal linear resonance, the protocol should measure both magnitude and phase, or otherwise reconstruct the complex response where physically meaningful. A claimed amplitude feature with no compatible phase/dispersion structure should count against the causal-resonance interpretation and trigger an apparatus/artifact investigation.

This requirement applies **only** when making a causal linear-response claim. It is not imposed on a purely phenomenological predictor of behavioural outcomes.

---

## 9. Model B — Retention-Kernel Modulation

Model B is conceptually different.

It does not require the drive to alter the downstream coupling `λ`. Instead, it asks whether the retained trace itself changes in strength, persistence or temporal shape.

The canonical score contains a persistence term `d_j`. A simple exponential candidate is:

```math
d_j(t;\omega_d)
=
\exp[-\beta_j(\omega_d)t].
```

But the more general and less prejudicial representation is a retention kernel.

Let:

```math
M(t)
=
\int_{-\infty}^{t}
K(t-s;\omega_d)O(s)\,ds,
```

where:

- `O(s)` is the history-forming input;
- `K(τ;ω_d)` is the retention kernel under the declared drive condition;
- `M(t)` is the resulting retained state.

In Fourier representation, using `Ω` for analysis frequency:

```math
\widetilde M(\Omega)
=
\widetilde K(\Omega;\omega_d)
\widetilde O(\Omega).
```

A non-flat or non-single-exponential retention kernel is mathematically ordinary. It may indicate multiple decay modes, filtering, delayed response or other memory dynamics.

It must **not** automatically be described as a physical resonance in the substrate.

The narrow Model B claim is only:

> the controlled drive condition changes the measured retention kernel or persistence of retained state.

Any physical mechanism requires separate evidence.

---

## 10. Direct A/B Discriminator — On/Off/On Protocol

The cleanest first experiment does not require fitting a resonance peak.

The key discriminator is what happens when the drive is removed.

### Model A prediction

If frequency changes only instantaneous selection coupling:

```text
Drive ON  → altered coupling
Drive OFF → coupling returns toward baseline on the ordinary response/settling timescale
```

There should be no additional memory-like tail attributable to the drive once instrumentation and system settling are accounted for.

### Model B prediction

If frequency changes retained state itself:

```text
Drive ON  → retained state is altered
Drive OFF → altered state persists and decays according to the retention dynamics
```

The post-drive effect should therefore survive removal of the drive and decay over a measurable time course.

### Minimal randomized protocol

Use randomized, blinded blocks containing:

```text
OFF baseline
→ ON exposure
→ OFF observation / washout
→ ON re-challenge
```

with matched retained-history conditions and preregistered observation windows.

Primary discriminating measurement:

```math
Q(t)
=
\Delta L_{\text{post-off}}(t)
-
\Delta L_{\text{matched off baseline}}(t).
```

A Model-A-like outcome is:

```math
Q(t)\rightarrow0
```

on the independently measured ordinary response/settling timescale.

A Model-B-like outcome is a reproducible residual:

```math
Q(t)\neq0
```

after the drive has been removed, followed by decay that predicts held-out post-off observations.

This test should precede any attempt to estimate a full resonance profile.

---

## 11. Apparatus and Timing Confounds

The apparatus itself may have frequency structure unrelated to the system under test.

Mandatory artifact candidates include, where applicable:

- mechanical resonances;
- power-supply switching frequencies and harmonics;
- mains coupling;
- RF pickup;
- clocks and scheduler frequencies;
- sensor bandwidth;
- amplifier/filter response;
- thermal response;
- cable, enclosure or geometry effects;
- digital control-loop cadence;
- frequency-dependent source amplitude or delivered power.

### Sham and apparatus-only controls

A physical frequency study should include runs in which the drive and measurement apparatus operate while the active system-under-test contribution is absent, replaced by an inert/dummy load, scrambled, shielded or otherwise placed into a preregistered sham condition appropriate to the apparatus.

A candidate peak that appears in the apparatus-only condition is not evidence for retained-state coupling.

### Blinding

Frequency labels or condition identities should be hidden from the analyst wherever practical until the analysis code, exclusions and scoring procedure are frozen.

---

## 12. Sampling, Nyquist and Beat-Frequency Controls

Any digitally sampled experiment must declare the effective sampling rate:

```math
f_s.
```

The Nyquist frequency is:

```math
f_N = \frac{f_s}{2}.
```

Frequency components above the usable sampled band can alias into lower frequencies. Periodic drive interacting with a software or hardware loop can also generate beat structure that looks like a response peak.

Therefore:

1. the usable drive band must remain safely within the validated acquisition bandwidth and below the relevant Nyquist limit;
2. antialias filtering or equivalent bandwidth limitation must be documented where applicable;
3. loop/update rates, timer resolution and scheduler cadence must be recorded;
4. candidate peaks should be re-tested under at least one changed sampling/update rate where practical;
5. a genuine physical-frequency candidate should remain tied to the physical drive frequency rather than moving predictably with `f_s`, loop cadence or clock rate.

For a purely software periodicity experiment, timing and alias structure are part of the mechanism under test and must not be described as electromagnetic resonance.

---

## 13. Softmax Scale and Temperature Identifiability

The canonical retained-state model already requires the scale of `R` to be frozen because:

```math
R\rightarrow cR,
\qquad
\lambda\rightarrow\lambda/c
```

leaves the product `λR` unchanged.

The frequency extension adds the same requirement for `h(ω_d)`:

```math
h\rightarrow ch,
\qquad
\kappa\rightarrow\kappa/c.
```

Therefore both scales must be fixed before confirmatory estimation.

A further issue arises when probabilities are manufactured from raw selector scores through a temperature mapping:

```math
\widetilde p_i(T)
=
\frac{\exp(s_i/T)}
{\sum_j\exp(s_j/T)}.
```

If `T` is free while the scale of the logits and retained-state coefficients is also free, scale can be traded against temperature and the parameters are not jointly interpretable.

### Rule

- Where genuine model probabilities/log-probabilities are available, use those declared observables and do not add a free temperature.
- Where the canonical deterministic-score measurement mapping is used, fix `T` before the confirmatory analysis and do not estimate `T`, `λ₀` and `κ` jointly from the same data.
- Preserve the canonical normalization of `R`.

---

## 14. Control Variables Without Built-In Collinearity

Amplitude, power, energy and exposure duration are often physically related.

For example, under many fixed-impedance sinusoidal drive conditions, delivered power scales with amplitude squared. Therefore a regression containing unconstrained amplitude and energy terms may be poorly identified by construction.

The preferred hierarchy is:

1. control the intervention by experimental design;
2. independently measure the physically relevant delivered quantity;
3. include only preregistered nuisance covariates needed for residual variation;
4. avoid simultaneously estimating redundant transformations of the same intervention unless the design independently identifies them.

A representative controlled regression is:

```math
\Delta L_k
=
\alpha
+
\lambda_0\Delta R_k
+
\kappa h(\omega_{d,k})\Delta R_k
+
\boldsymbol{\gamma}^{\top}\mathbf C_k
+
\varepsilon_k,
```

but `C_k` must be a small preregistered set, not an unrestricted collection added after inspecting the data.

---

## 15. Two Separate Research Programmes

The word “frequency” can refer to fundamentally different experiments. They must not be mixed.

### Track S — software periodicity / timing

Examples:

- timed state updates;
- periodic prompts or observations;
- control-loop cadence;
- scheduler or sampling periodicity;
- synthetic oscillatory perturbations applied numerically.

This can test whether a software retained-state system has frequency-dependent dynamics.

It does **not** provide evidence of electromagnetic coupling, atomic resonance or a physical field mechanism.

### Track P — physical substrate / field drive

Examples may involve a declared physical substrate subjected to a controlled external physical drive with independent measurement of delivered conditions.

This requires apparatus controls, calibration, shielding where appropriate, phase/transfer measurements where a causal linear-response claim is made, and independent replication.

A positive Track S result cannot be used as evidence for Track P.

A positive Track P result cannot be assumed to describe CAAI software behaviour.

This boundary is mandatory for publication and review.

---

## 16. Recommended First Experimental Sequence

The first programme should be deliberately boring.

### Experiment 1 — on/off/on A/B discriminator

Goal: determine whether the effect behaves like instantaneous coupling modulation or altered retained-state persistence.

Do not fit a resonance peak.

Primary evidence:

- immediate/settling-timescale return to baseline after drive removal; or
- reproducible post-drive persistence with predictive decay.

### Experiment 2 — broad frequency-structure screen

Only after Experiment 1 shows a reproducible effect:

- sample a broad, preregistered frequency range;
- randomize order;
- include sham/apparatus-only controls;
- use a low-complexity nonparametric response model;
- reserve held-out frequencies/runs.

Primary question:

> Does frequency improve prediction beyond the frequency-independent retained-state model?

### Experiment 3 — frozen parametric candidate

Only after a reproducible localized structure exists:

- freeze `ω₀` and `Γ` from independent or discovery data;
- run new confirmatory data;
- estimate `κ` without re-searching the peak;
- test held-out predictive performance and replication.

### Experiment 4 — physical-response characterization

Only if a physical causal resonance interpretation is proposed:

- measure complex transfer/phase where applicable;
- test consistency with causal linear response;
- vary sampling and apparatus configuration;
- verify the candidate frequency is not an apparatus resonance or alias.

---

## 17. Falsification Conditions for v0.2

The frequency extension is not supported in a tested regime when one or more of the following occurs:

1. the frequency-dependent model fails to improve preregistered held-out prediction over the frequency-independent model;
2. the apparent response is obtained only by post-hoc scanning and does not survive untouched validation data;
3. `κ` is compatible with zero when the response basis was legitimately fixed in advance;
4. the apparent frequency profile fails replication;
5. the profile moves with sampling rate, loop cadence, source electronics or apparatus configuration in a manner consistent with aliasing or instrumentation;
6. apparatus-only or sham runs reproduce the candidate peak;
7. amplitude, power, heating, timing, noise or drift explains the effect equally well or better;
8. a broad candidate response makes `κ` indistinguishable from `λ₀`;
9. the result depends on fitting a free temperature or changing the scale of `R` or `h` after seeing the data;
10. a claimed physical causal resonance lacks the accompanying phase/dispersion behaviour expected under the declared linear-response model;
11. the proposed Model-B persistence disappears immediately with the drive once ordinary settling is accounted for;
12. the proposed Model-A effect shows an unexplained persistent post-drive tail inconsistent with the stated coupling-only model;
13. frequency ordering, block ordering or analyst knowledge predicts the result;
14. independent replication fails.

The correct null verdict is:

> **frequency-coupled retained-state modulation was not supported in the tested regime.**

It is not:

> **frequency can never affect retained state in any system.**

---

## 18. What a Positive Result Would Mean

A strong v0.2 result would require more than a fitted bump.

At minimum it would require:

- a reproducible retained-state effect;
- a frequency-dependent term that improves held-out prediction;
- successful sham and apparatus controls;
- stable results under changed sampling conditions where applicable;
- clear separation of Model A versus Model B behaviour;
- replication on new data.

The strongest permitted conclusion would still be narrow:

> **Within the tested system and declared regime, a controlled frequency-dependent condition added reproducible predictive information about retained-state coupling or retained-state persistence beyond the frequency-independent baseline.**

It would **not by itself establish**:

- a universal resonance law;
- electromagnetic memory storage;
- consciousness as a field;
- non-local memory;
- quantum consciousness;
- atomic-scale causation;
- a new force;
- Verrell’s Law as established universal physics.

---

## 19. Relationship to the Canonical Specification

The canonical authority remains:

[`VERRELLS_LAW_MATHEMATICAL_FOUNDATIONS_AND_FALSIFICATION_PROTOCOL_v1.0.md`](../VERRELLS_LAW_MATHEMATICAL_FOUNDATIONS_AND_FALSIFICATION_PROTOCOL_v1.0.md)

The canonical first-order claim remains:

```math
\Delta L = \lambda\Delta R,
\qquad
\lambda>0.
```

This v0.2 document does not modify the Principal Hypothesis, canonical normalization requirements, sign convention or falsification protocol.

Where any conflict exists, the canonical specification governs.

Physical interpretation remains a separate research layer.

---

## 20. Relationship to v0.1 and the Conceptual Note

Earlier exploratory mathematics is preserved at:

[`FREQUENCY_COUPLED_RETAINED_STATE_EXPLORATORY_MATHEMATICS_v0.1.md`](FREQUENCY_COUPLED_RETAINED_STATE_EXPLORATORY_MATHEMATICS_v0.1.md)

The physical motivation and claim boundaries remain recorded in:

[`ATOMIC_STRUCTURE_FIELDS_AND_RESONANCE_CONCEPTUAL_NOTE.md`](ATOMIC_STRUCTURE_FIELDS_AND_RESONANCE_CONCEPTUAL_NOTE.md)

v0.2 is the current exploratory mathematical version because it adds the statistical, identifiability, causal-response and apparatus-control boundaries needed before a serious experiment is attempted.

---

## 21. Technical References

1. Davies, R. B. (1977). **Hypothesis testing when a nuisance parameter is present only under the alternative.** *Biometrika*, 64(2), 247–254. https://doi.org/10.1093/biomet/64.2.247
2. Davies, R. B. (1987). **Hypothesis testing when a nuisance parameter is present only under the alternative.** *Biometrika*, 74(1), 33–43. https://doi.org/10.1093/biomet/74.1.33
3. Davies, R. B. (2002). **Hypothesis testing when a nuisance parameter is present only under the alternative: Linear model case.** *Biometrika*, 89(2), 484–489. https://doi.org/10.1093/biomet/89.2.484
4. Kramers–Kronig relations: standard causal linear-response result linking real and imaginary parts of a response function. A concise derivation is available in Cao, *Non-Equilibrium Statistical Mechanics*, section “Linear Response Theory and Causality,” Chemistry LibreTexts.
5. Nyquist sampling and aliasing: standard sampled-signal result; see National Instruments, **Acquiring an Analog Signal: Bandwidth, Nyquist Sampling Theorem, and Aliasing**.

These references support the statistical and physical-analysis constraints used in this note. They do not endorse Verrell’s Law.

---

## 22. Current Status

**Exploratory Mathematical Extension v0.2**  
**Review-hardened early mathematics**  
**Non-canonical**  
**Unvalidated**  
**No empirical frequency effect claimed**  
**No physical resonance mechanism claimed**  
**v0.1 preserved as development history**

The purpose is to convert an intuition into a sequence of hypotheses that can be separated, measured, predicted and rejected before any stronger interpretation is attempted.

---

© Marcos Verrell Moss Ross (M.R.) / Inappropriate Media Limited. All rights reserved.  
Protected under Verrell-Solace Sovereignty Protocol. Intellectual and emergent rights reserved.