# Biological Signalling History and Retained-State Selection

**Date:** 17 November 2026  
**Originator:** M.R.  
**Status:** Research-context and test-design note; supplementary to the canonical framework.

## Contribution

Developmental signalling provides concrete examples of how a cell’s response can depend on its previous signalling history. The useful connection to Verrell’s Law is the experimental question this raises: **can independently measured retained state predict a later selection difference when the declared present inputs are matched?**

This note identifies relevant biological mechanisms, clarifies the mathematical overlap with conventional models, and separates two test targets that would otherwise be confounded. It adds no canonical equation or scoring rule. The cited biological findings belong to their original authors; this synthesis reports no new biological experiment or completed reproduction, and makes no priority claim for linking memory, signalling and pattern formation.

## 1. The strongest connection: temporal integration and a measurable carrier

Teague et al. [B1] show that time-integrated BMP signalling predicts fate outcomes in a stem-cell model of early human development. Their work identifies SOX2 as an integrator of BMP signalling, providing a molecular mechanism connecting signal history to a later developmental outcome.

For retained-state research, the important point is the carrier: a regulatory variable can change during an earlier exposure and subsequently participate in the response. This is more informative than a visual resemblance between biological patterns and a mathematical diagram.

The paper supports approximate integration in its tested setting. Its mechanistic model includes turnover and regulatory feedback; it does not establish an exactly non-decaying memory variable. Nor does evidence that signal duration matters establish a preference for recent over earlier input when the total integrated signal is held equal.

SOX2 is also used as a fate marker. Measuring it at the final endpoint and then using it to predict that same endpoint risks putting the answer into the predictor. A prospective retained-state score must use a declared earlier measurement and a later outcome, with the overlap between the two addressed explicitly.

## 2. Biological context and prior art

| Research | Relevant contribution | Consequence for this framework |
| --- | --- | --- |
| Teague et al. 2024 [B1] | BMP signal integration and a SOX2-associated mechanism in a human stem-cell model. | A concrete candidate carrier and a strong conventional integration comparator. |
| Dessaud et al. 2007 [B7] | Temporal adaptation in interpretation of Sonic Hedgehog signalling. | Duration and pathway dynamics must be considered alongside signal level. |
| Balaskas et al. 2012 [B2] | Gene-regulatory logic for interpreting the Sonic Hedgehog gradient. | Regulatory-network state is part of the mechanistic explanation, rather than an unspecified memory store. |
| Purvis and Lahav 2013 [B8] | Review of how cells encode and decode signalling dynamics. | Temporal decoding is established prior art; a new test must discriminate among existing explanations. |
| Dessaud et al. 2010 [B9] | Dynamic assignment and maintenance of positional identity; some identities revert when signalling is interrupted. | Persistence is conditional. Assignment, maintenance and a new response after signal withdrawal are different questions. |

Fingerprint and digit-pattern studies [B3, B4] supply a separate spatial-patterning context. Turing’s reaction–diffusion theory [B6] and Wolpert’s positional-information framework [B5] provide theoretical foundations for pattern generation and interpretation of position.

These spatial and temporal questions can interact, but they are not interchangeable. A pattern can arise through ordinary reaction–diffusion dynamics without demonstrating a retained-state selection rule. Likewise, a cell can integrate a signal without establishing any particular spatial-pattern mechanism. The relevant processes are biological and involve gene regulation, proteins and signalling interactions; describing them as chemical does not remove the role of genes.

## 3. Mathematical overlap: one predictive family

The existing public retained-state tilt is

```math
P_i=\frac{P_{0,i}\exp(\lambda R_i)}{\sum_j P_{0,j}\exp(\lambda R_j)}.
```

For two candidates with positive baseline probabilities and finite scores,

```math
\log\frac{P_a}{P_b}=\log\frac{P_{0,a}}{P_{0,b}}+\lambda(R_a-R_b).
```

Set the baseline log-odds to $\beta_0$, and let $R_a=I$, $R_b=0$, where $I$ is a declared signal integral. Then

```math
P_a=\operatorname{logistic}(\beta_0+\lambda I).
```

This is an exact algebraic specialisation of the assumed tilt, and the conventional logistic-integral model. Calling the same fitted model “retained-score selection” does not create an independent competitor or a new biological mechanism. The biological evidence for integration does not itself establish the logistic link.

A useful contribution must instead come from a restriction fixed before testing: a frozen score, calibration rule or transferable prediction that can fail on held-out conditions. Score scale, preprocessing and the coefficient must not be adjusted after seeing the test outcomes.

## 4. B1’s protocols determine what a transfer test means

B1’s differentiation readout is at 42 hours. Its duration experiments include signalling stopped before that endpoint as well as a 42-hour exposure. Its level experiments include both exposure maintained to 42 hours and signalling stopped at 32 hours, followed by the later 42-hour readout [B1, B1-S].

Consequently, a mixed transfer from duration to level conditions can change the present input as well as the accumulated signal. Carrying a fitted intercept across those families assumes that any additional present-input contribution is absent or adequately controlled. That assumption must be tested rather than hidden in the notation.

| Proposed target | What it can ask | Required interpretation |
| --- | --- | --- |
| Freeze an integral-to-outcome curve on duration conditions, then predict level conditions. | Does the calibrated integral relationship transport across the declared conditions? | If present inputs differ, this tests integral sufficiency and transport, not isolated retained-state influence. |
| Prepare different histories, then match declared present inputs throughout a later decision window. | Does a pre-outcome retained-state score predict a later response under those controls? | This is the relevant retained-state target, provided the score, baseline and decision rule are independently fixed. |

Nominal removal of an external ligand does not establish that intracellular pathway activity has already returned to an equal level. Conversely, a marker remaining after shutdown may reflect an earlier commitment: persistence alone is not automatically a new selection made after the signal ended.

The operational boundary must therefore declare which present inputs and covariates are matched, which regulatory features constitute retained history, and when the response is being predicted. Do not require the entire physical state to be identical while simultaneously varying a retained component of that state. Do not count the same variable as both matched current signal and deliberately varied memory.

## 5. What would make a later test informative?

A future study should freeze score construction, normalization, time units, integration interval, baseline, calibration and endpoint rules before using held-out outcomes. Compare against competent current-signal, duration and integral models; include a model with decay only where timing coverage makes it identifiable.

B1 reports single- and multiple-pulse conditions, with released time traces and outcome summaries. Inspection did not establish an exact equal-total early-versus-recent comparison. Nearby noisy integral estimates are not a designed matched-total experiment. A timing test must first establish suitable data coverage, input matching and independent experimental units.

Count experiments, wells, colonies and cells separately, accounting for shared preparation and batch structure. Large cell counts do not replace independent experiments. With few independent units, **inconclusive is the planning default** until a feasibility and precision assessment supports a stronger decision. No power calculation or biological outcome fitting is reported here.

A preregistered wrong-direction or outside-tolerance result would challenge the specified model in its declared regime. Wide intervals remain inconclusive. A distinctive cross-domain prediction remains a research target; rewriting an existing fit in retained-state notation does not supply one.

## 6. Scope and record

The immediate value is a clearer biological evidence map and a better-defined future test. Reproduction is deferred. This note does not alter the canonical mathematics or the separate proprietary engineering programme, and contains no runtime code, private scoring implementation, production thresholds or confidential audit material.

Related public documents:

- [Retained-State Selection Framework](../RETAINED_STATE_SELECTION_FRAMEWORK.md)
- [Mathematical Status and Structural Results](../MATHEMATICAL_STATUS_AND_STRUCTURAL_RESULTS_2026-11-11.md)
- [Empirical Identification Clarification](../VERRELLS_LAW_EMPIRICAL_IDENTIFICATION_CLARIFICATION_v1.0.md)
- [Scientific Evidence Map](../RETAINED_STATE_SCIENTIFIC_EVIDENCE_MAP_2026.md)

## References and access

**[B1]** Teague, S. et al. (2024). *Time-integrated BMP signaling determines fate in a stem cell model for early human development.* Nature Communications 15, 1471. [DOI: 10.1038/s41467-024-45719-9](https://doi.org/10.1038/s41467-024-45719-9). [Full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC10874454/). Open access, CC BY 4.0.

**[B1-S]** Teague et al., accompanying [publisher Supplementary Information](https://static-content.springer-cdn.com/esm/art%3A10.1038%2Fs41467-024-45719-9/MediaObjects/41467_2024_45719_MOESM1_ESM.pdf). [Europe PMC supplementary package, including source data](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10874454/supplementaryFiles). Source inspection is not a completed reanalysis.

**[B2]** Balaskas, N. et al. (2012). *Gene Regulatory Logic for Reading the Sonic Hedgehog Signaling Gradient in the Vertebrate Neural Tube.* Cell 148, 273–284. [DOI: 10.1016/j.cell.2011.10.047](https://doi.org/10.1016/j.cell.2011.10.047). [Full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC3267043/). Open access, CC BY 3.0 as stated on PMC.

**[B3]** Glover, J. D. et al. (2023). *The developmental basis of fingerprint pattern formation and variation.* Cell 186, 940–956.e20. [DOI: 10.1016/j.cell.2023.01.015](https://doi.org/10.1016/j.cell.2023.01.015). [University author record](https://www.research.ed.ac.uk/en/publications/the-developmental-basis-of-fingerprint-pattern-formation-and-vari/). Author record identifies a CC BY publication.

**[B4]** Raspopovic, J., Marcon, L., Russo, L. and Sharpe, J. (2014). *Digit patterning is controlled by a Bmp-Sox9-Wnt Turing network modulated by morphogen gradients.* Science 345, 566–570. [DOI: 10.1126/science.1252960](https://doi.org/10.1126/science.1252960). [Free-to-read author copy](https://marconlab.org/papers/LM2014.PDF). No open-access publisher licence asserted here.

**[B5]** Wolpert, L. (1969). *Positional information and the spatial pattern of cellular differentiation.* Journal of Theoretical Biology 25, 1–47. [DOI: 10.1016/S0022-5193(69)80016-0](https://doi.org/10.1016/S0022-5193%2869%2980016-0). [Free-to-read institutional teaching copy](https://www.imsc.res.in/~sitabhra/teaching/sb18/Wolpert1969.pdf). No open-access publisher licence asserted here.

**[B6]** Turing, A. M. (1952). *The Chemical Basis of Morphogenesis.* Philosophical Transactions of the Royal Society B 237, 37–72. [DOI: 10.1098/rstb.1952.0012](https://doi.org/10.1098/rstb.1952.0012). [Free-to-read institutional copy](https://www.damtp.cam.ac.uk/user/gold/pdfs/teaching/old_literature/Turing1952.pdf). Availability does not create a new reuse licence.

**[B7]** Dessaud, E. et al. (2007). *Interpretation of the sonic hedgehog morphogen gradient by a temporal adaptation mechanism.* Nature 450, 717–720. [DOI: 10.1038/nature06347](https://doi.org/10.1038/nature06347). [Free-copy repository record](https://hdl.handle.net/2027.42/62511), University of Michigan Deep Blue.

**[B8]** Purvis, J. E. and Lahav, G. (2013). *Encoding and decoding cellular information through signaling dynamics.* Cell 152, 945–956. [DOI: 10.1016/j.cell.2013.02.005](https://doi.org/10.1016/j.cell.2013.02.005). [Free-to-read author manuscript](https://pmc.ncbi.nlm.nih.gov/articles/PMC3707615/). Review; copyright retained.

**[B9]** Dessaud, E. et al. (2010). *Dynamic Assignment and Maintenance of Positional Identity in the Ventral Neural Tube by the Morphogen Sonic Hedgehog.* PLoS Biology 8(6), e1000382. [DOI and open-access full text](https://doi.org/10.1371/journal.pbio.1000382). Creative Commons Attribution.

---

**Authorship and assistance:** Verrell’s Law was originated by M.R. This note was prepared with AI assistance for literature synthesis, mathematical checking and drafting, with review corrections incorporated under M.R.’s direction. The cited authors retain credit for their findings and mechanisms.

**Rights:** Public research documentation under the repository’s [Research Rights and Use Notice](../IP_NOTICE.md) and [LICENSE](../LICENSE). External papers retain their own rights and licences. Publication of this note creates no additional licence for proprietary implementations.
