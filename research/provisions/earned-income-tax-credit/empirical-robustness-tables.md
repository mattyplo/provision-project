# Empirical robustness: inspected tables, specification sensitivity and disagreement

**Inspection date:** 2026-11-16. This is a **source-level robustness audit**, not a microdata replication or comprehensive literature review. The paper's claims are attributed to its authors; interpretations below are project technical assessments.

## 1. Rothstein (2010): material sensitivity found in published supplement
**Sources:** [Published AEJ article/abstract](https://www.aeaweb.org/articles?id=10.1257/pol.2.1.177); [published supplemental appendix, pp. 1–3](https://www.aeaweb.org/articles/materials/705).

- Main article abstract: with preferred model parameters, **$1 of EITC spending yields $0.73 of increased worker after-tax income**. This is a simulated equilibrium incidence result, not a measured employer share.
- **Appendix A** reports results over **27 elasticity parameter combinations** (separate groups by marital/child status).
- **Appendix B**, p. 3, states that allowing **larger income-effect elasticities (−0.36)** **reverses the result that EITC true transfers to workers are smaller than statutory transfers**: there is instead a **net transfer from employers to workers**, reflecting a net reduction in labor supply. The appendix says the comparative result favoring NIT still holds.
- **Material interpretation:** The *sign of modeled employer-to-worker redistribution is not invariant to income-effect assumptions*. It is inappropriate to publish 'employers capture 27%' or even 'employers necessarily benefit' as an unconditional Rothstein finding. Retain both base-case and alternative scenarios. No replication performed.

## 2. Leigh (2010): actual tables and composition check
**Source:** [IZA DP 4960, full 45-page PDF](https://docs.iza.org/dp4960.pdf); published in *B.E. Journal of Economic Analysis & Policy* 10(1), article 45.

- Abstract: **10% more generous EITC associated with 5% lower hourly wages for high-school dropouts**, **2% lower** for high-school graduates, no estimated effect for college graduates; **association under study's identification**, not universal causal coefficient.
- **Table 4, pp. 22–23**: employment response to log maximum EITC among workers **with children**: dropout coefficient **0.194*** (SE 0.067); **without children** dropout **−0.010** (SE 0.060). These are coefficients on log generosity in a linear probability model, **not percentages**. For a roughly 10% increase in generosity, the author interprets the overall dropout employment response as about **+0.9 percentage points** (pp. 29–30).
- **§4.4, pp. 30–31** explicitly tests whether wage declines merely reflect newly entering lower-wage workers. The author compares workers with/without children (similar estimated wage effects despite differing entry responses) and constructs a **worst-case minimum-wage new-entrant bound**. The bound accounts for about **0.8%** of a reported **5%** wage decline in the illustrative dropout case. This weakens, but does not logically eliminate, all possible composition bias.
- **Important:** State-policy variation, group definition, regional trends and simultaneous policies can still confound wage associations; these checks are not proof of a nationwide causal employer-capture share. Retain estimates and assumptions.

## 3. Hoynes/Miller/Simon (2015) vs Dench/Joyce (2020): table-level disagreement
**Sources:** [HMS published full 40-page PDF](https://gspp.berkeley.edu/archived/files/research/pdf/Hoynes-Miller-Simon-AEJPolicy-Feb-2015.pdf); [Dench/Joyce manuscript, full 26-page PDF](https://www.danieldench.com/static/pdfs/published/HE2.pdf).

- **HMS Table 3, printed p. 188** (parity 3+ vs 2): estimated low-birth-weight percentage-point changes **Black −0.715*** (SE 0.121), **White −0.0231** (SE 0.071), **Hispanic −0.121** (SE 0.092). These subgroup contrasts matter: the statistically significant parity-3+/2 result is concentrated among Black mothers in this specification, **not uniform across groups**.
- **Dench/Joyce Table 2, manuscript p. 23**, independently reproduces essentially the same subgroup contrast (**Black −0.715**, White −0.028, Hispanic −0.121), then performs **parity 3 vs 4** and **3 vs 4+** placebo comparisons. The Black subgroup shows **−0.421*** and **−0.483*** respectively, although parity 3 and 4+ face the same EITC maximum under the reform. Critics argue these nonzero placebo contrasts undermine attributing all changes to EITC.
- **Dench/Joyce manuscript pp. 8–9** acknowledges the parity 3+ vs 2 contrast **supports the original authors' conclusion** before identifying subgroup/placebo concerns. This nuance must be retained: the critique is **not** simply 'could not replicate the result'.
- **HMS Table 3, parity 2+ vs 1** reports significant negative estimates in several subgroups; **Dench/Joyce** argue this comparison is contaminated by earlier EITC expansions / nonparallel pretrends. Authors dispute design interpretation in [their response](https://gspp.berkeley.edu/assets/uploads/research/pdf/DJ_response_JHE_012519.pdf). Neither the critique nor rejoinder independently resolves causality.
- **Project conclusion:** Published **2–3% relative low-birth-weight** treatment-on-treated estimate is a valid *reported study result*; causal generalization is disputed. Store table-specific estimates, subgroup heterogeneity, critics' placebo tests, and authors' response separately.

## 4. Employment studies: bounded inspection, not table-level certified
[Eissa/Liebman NBER W5158](https://www.nber.org/papers/w5158), [QJE 1996](https://academic.oup.com/qje/article-abstract/111/2/605/1938452), [Schanzenbach/Strain 2021](https://www.journals.uchicago.edu/doi/10.1086/713494), and [Kleven 2024](https://www.sciencedirect.com/science/article/pii/S0047272724000719) remain in the evidence ledger with distinct estimates and study designs. **Full published robustness tables were not accessible/inspected in this pass**; NBER and ScienceDirect pages returned access errors. Do not claim employment table-level robustness verified.

## Updated synthesis
- **Employment:** Studies differ in reform window, comparison groups, counterfactuals, specification search and control for coincident policy. Evidence of positive participation in particular designs coexists with skeptical multi-reform reappraisal. **No pooled effect inferred.**
- **Wages/incidence:** Both empirical wage associations and equilibrium simulations suggest wage pass-through is possible, but Rothstein's supplemental income-effect scenario demonstrates **even the direction of simulated net transfers can reverse**. **National economic incidence remains unknown.**
- **Infant health:** Original estimates replicate in some subgroup contrasts, but placebo comparisons and trends raise identification concerns. **Keep the result and the challenge**, do not declare causal certainty.

**Remaining work:** inspect full published employment robustness tables where accessible; inspect authors' infant-health rejoinder line-by-line and other independent replications; independently execute published replication code/data only if a reproducibility exercise is separately authorized.


## Employment-table follow-up (2026-11-16)
The earlier statement that employment published robustness tables were inaccessible is **superseded in part**: full published PDFs of Eissa/Liebman 1996 and Schanzenbach/Strain 2021, and the author-hosted May 2024 Kleven full text, were located and selected tables inspected. See [employment-robustness-audit.md](employment-robustness-audit.md). **This is not full online-appendix or independent replication certification.**
