Verrell’s Law — Optics Experiment Note (v1)

Status: Public pre-registration draft
Scope: Test for history-conditioned (memory-biased) deviations in interferometric outcomes using existing photonic/phononic hardware.
IP Notice: Protected under Verrell-Solace Sovereignty Protocol. Intellectual and emergent rights reserved.
Maintainer: Collapse Aware AI / Verrell’s Law Project Team

0) One-line hypothesis

Prior state information stored in the device (via coherent phonons/Brillouin acoustic fields or polaritonic population) systematically biases outcome statistics of a nominally memoryless interferometric measurement.
Prediction: Measurable, reproducible deviations from baseline interference/shot statistics that track the device’s written state even when probe pulses are identically prepared.

1) Physical intuition → implementation

Memory carrier: Coherent phonons / phonon-polaritons on chip (longer relaxation than the optical probe) or Stimulated Brillouin Scattering (SBS) acoustic fields in a waveguide/resonator. These act as a short-term field trace.

Measurement stage: Mach–Zehnder Interferometer (MZI) (or HOM block) reads interference/visibility with single-photon or weak-coherent probes.

Core idea: Write a controlled acoustic/polaritonic state; then probe. If history matters, output statistics will differ between W+ (written) and W− (unwritten) under otherwise identical conditions.

2) Minimal apparatus (choose one)
Path A — Fully integrated PIC

PIC with grating couplers, 50/50 couplers, phase shifter, SBS section (spiral waveguide or ring) and/or polariton–phonon laser region.

Detectors: SNSPDs or high-efficiency SPADs at outputs.

Source: attenuated laser (weak coherent) or heralded single photons.

Path B — Hybrid fiber + chip (fastest to prototype)

Fiber MZI with phase modulator + fiber SBS spool or chip SBS module as the memory element.

Tap couplers to single-photon detectors; attenuated pulsed laser as probe.

3) Protocol (write → read → compare)
Baseline: “memory-off”

Let device relax (≫ phonon lifetime) to erase residuals.

Inject N identical probe pulses with phase sweep; record outputs → P0(φ), visibility V0(φ).

Write controlled memory

Apply write pulse train through the SBS/phonon section with two randomized conditions:

W+ (aligned write): on-resonance timing/power to populate the acoustic mode (or pump the polariton-phonon region).

W− (anti-write): detuned/below threshold to avoid excitation.

Readout

Immediately (within τ_phonon) inject identical low-energy probe pulses; sweep/hold phase φ.

Record outputs for each condition: P+(φ) and P−(φ).

Interleave trials (W+, W−, blank) in randomized order to suppress drift.

Timing sketch (not to scale):

|<--- erase --->|  [W+: write train]  |< Δt ≤ τ_phonon >|  [probe pulses]  -> detect
|<--- erase --->|  [W−: detuned  ]    |< Δt ≤ τ_phonon >|  [probe pulses]  -> detect

4) Primary observables (“bias fingerprints”)

ΔV(φ) = V+(φ) − V−(φ): visibility change conditioned on memory state; expect ΔV ≠ 0 if stored field perturbs index/phase in a history-specific way.

Entropy shift ΔH: compare output distribution entropies H(P0) vs H(P±); expect bounded, repeatable ΔH > 0 in the predicted direction for W+.

Persistence: ΔV vs delay Δt (write→read). Fit exponential decay; recovered lifetime τ_fit should match independent phonon/SBS relaxation.

Directionality (if available): reverse propagation; non-reciprocal platforms should flip/alter the bias signature.

5) Controls (rule out mundane effects)

Thermal power control: replicate average power without resonant write; ΔV should vanish.

Off-resonance SBS: detune Brillouin shift; effect should disappear.

Erasure window: wait Δt ≫ τ_phonon; ΔV returns to baseline.

Randomized phase: scramble φ post-write to prevent fixed drift artefacts.

Shot-noise sanity: verify count distributions, no detector saturation.

6) Statistics & falsification

Null model: 
𝑃
+
=
𝑃
−
=
𝑃
0
P
+
	​

=P
−
	​

=P
0
	​

 within bounds from shot + detector noise + calibrated drift.

Tests: two-sample comparisons on visibility; distributional tests (e.g., bootstrap KL-divergence) with pre-registered CIs.

Thresholds (pre-register):

Visibility: 
∣
Δ
𝑉
∣
>
3
𝜎
null
∣ΔV∣>3σ
null
	​

.

Entropy: 
Δ
𝐻
>
3
𝜎
null
ΔH>3σ
null
	​

.

Falsification: After controls, no reproducible correlation between write state and probe outcomes ⇒ no support for memory-biased collapse in this apparatus.

7) Parameters to pre-specify (table in your lab sheet)

Waveguide/platform, Brillouin frequency shift, Q, phonon lifetime, SBS gain.

Pulse energy, rep rate, write/read timing diagram.

Detector efficiency & dark counts; integration time per condition.

Environmental control: temperature stability, vibration isolation.

If using polariton cascade phonon region: which engineered level ladder & which phonon line (~20/60/100 GHz) is pumped.

8) Expected effort (realistic timeline)

Hybrid fiber+chip (Path B): baseline + first ΔV/ΔH scan in 6–12 weeks if lab already has a fiber MZI and SBS module.

Integrated PIC (Path A): with an existing demo chip, 3–6 months including packaging and runs; longer if a new mask is required.

9) Why this tests the claim (not just nonlinearity)

Standard thermo-optic/nonlinear shifts don’t label the past once you equalize power and timing. Here we encode and retrieve condition-specific traces (W+ vs W−) that persist across probes and vanish on erasure schedules matching independent acoustic/phonon lifetimes. That’s a history-conditioned bias—the targeted signature.

10) References (for context)

Papuccio-Fernández et al. “Polariton cascade phonon laser.” arXiv:2505.17336 (2025). DOI: 10.48550/arXiv.2505.17336

Standard resources on integrated SBS/Brillouin photonics and on-chip MZIs/HOM interferometry (introductory reviews and application notes; cite your lab’s preferred texts).

Pre-registration checklist (copy for your lab notebook)

 Hardware path selected (A or B) and BOM frozen

 τ_phonon independently measured (or pulled from spec)

 Write/read timing diagram fixed

 Phase sweep plan + sampling N set

 Control set defined (thermal, off-res, erasure)

 Statistical tests + thresholds pre-registered

 Data schema decided (store P0, P+, P−, φ, timestamps, power, temperature)

 Reproducibility: seeds, detector calibration, drift logs

 
 
 Protected under Verrell-Solace Sovereignty Protocol. Intellectual and emergent rights reserved. 
