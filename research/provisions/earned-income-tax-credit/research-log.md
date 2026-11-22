# EITC §32 — comparison and initial audit research log

**2026-11-16; reviewer:** ChatGPT assisted review; **law snapshot:** 2026-10-31. Related #29 and #9. No raw reports changed.

## Work actually performed
- Read #29, its process-retrospective comments, PR #35/#36/#37 descriptions, and the two complete archived research reports using the connected GitHub repository.
- Compared scope, statutory tables, original enactment, rationale, use, fiscal effect, incidence, citations, and execution provenance.
- Independently consulted official IRS Rev. Proc. 2025-32 §3.06 and IRS EITC 2026 tables; consulted the original P.L. 94-12 §204 and §209(b); consulted OLRC §32 version through P.L. 119-124.
- Recorded verified, contradicted, and open claims separately. **Did not** inspect original JCT estimates, S. Rep. 94-36, GAO source, or full empirical studies during this pass.

| Stage | Observed outcome | Friction / unresolved | Time / manual actions |
| --- | --- | --- | --- |
| Repository and run discovery | Both completed raw reports and manifests found; incomplete Ask-Chat identified | Exact assembled submitted prompts missing historically; Gemini omitted manifest addendum | Time not reliably measured; manual connector reads |
| Cross-report comparison | Disagreement in 2026 investment ceiling; different strength of empirical conclusions; citation weaknesses | Different run settings and incomplete comparable provenance | Time not reliably measured |
| Primary statutory verification | Original §43 enacted by P.L. 94-12, with temporary original effective period | Subsequent amendment history still unverified | Official govinfo text inspected |
| IRS parameters | $12,200 TY2026 investment-income ceiling and credit table verified | Gemini used projected ~$11,610 | IRS IRB and IRS table inspected |
| Fiscal / empirical audit | Queue established | JCT, GAO, original studies not independently checked | Not performed |
| Drafting | comparison.md and audit-queue.md prepared | Audited provision record remains outstanding | Not reliably measured |

## Process lessons (observed, not generalized model rankings)
- An independent IRS primary-source check resolved a real model discrepancy quickly.
- Strong-looking citation markers and a model's self-reported 'inspected' labels are not durable evidence; enforce URL + pinpoint + actual independent inspection.
- Maintain two independent axes: **run archival integrity** and **factual source verification**. The first can pass while the second remains open.
- Future research experiments should capture byte-exact submitted prompts, model selector/settings, and start/stop metadata **before** execution; no retrospective reconstruction as if contemporaneous.
- The proposed modular-versus-long prompt experiment in #29 remains separate; one unequal-settings run per provider cannot estimate causal effects of prompt length.
- A low-risk metadata/citation validator remains a separate potential automation; no prototype or time-savings measurement is claimed here.

## Next gate
Audit P0 JCT fiscal figures, S. Rep. 94-36, amendment chronology and 2026 cutoff; then P1 administrative and empirical claims. Only then draft/publish the EITC record under #29.


## Follow-up audit activity (2026-11-16)
Independently read JCT JCX-45-25 Table 1 (tax expenditure and outlay sections), GAO-26-108044 EITC discussion, IRS TY2024 processed-2025 claims and SOI series, P.L. 95-600 contents, the August/October 2026 Federal Register PRWORA notices, the official 2026 approved-acts list, and Eissa/Liebman NBER paper abstract. Confirmed JCT $67.2b/$56.6b FY2026 and qualified $10.6b arithmetic; confirmed GAO 33.5%/27.3% FY2023/FY2024; confirmed 1978 permanence belongs to §103; verified proposal/hearing status; distinguished IRS tax-year claims from JCT fiscal-year estimates. **Not performed:** S. Rep. 94-36 full-text inspection, full amendment sweep, all Oct. 20–22 public law texts, later causal studies and wage-incidence studies, complete EITC-C001–C014 source ledger. Time and manual action counts were not reliably measured. See [audit-queue.md](audit-queue.md) for pinpoints and dispositions.


## Bounded statutory audit (2026-11-16)
Checked original statutory text for P.L. 94-164 §2(f), P.L. 94-455 §401(c), P.L. 95-30 §103(b); checked OLRC §32 amendment/effective-date notes for P.L. 98-369 §§471(c),1042(e); enumerated 12 Oct. 16–31 public laws using National Archives official law list and compared GPO law metadata against OLRC release-point classifications. Inspected P.L. 119-134 text, which changes 30 USC §191(d). **Limit:** other 11 October laws were screened through official law metadata rather than individually full-text inspected. Result is qualified 'no direct §32 amendment identified,' not unconditional 'all laws exhaustively checked.' See [bounded-statutory-audit.md](bounded-statutory-audit.md).


## October enacted-law full-text follow-up
Individually inspected P.L. 119-125, 126, 127, 128, 129, 130, 132, 133, 134, 135 and 136 (eleven enacted texts), with sections and sources logged in [october-2026-cutoff-closeout.md](october-2026-cutoff-closeout.md). For 119-131, official GPO metadata and OLRC codified enacted 29 USC §570 plus notes were inspected; full slip-law fetch failed. No direct §32 amendment identified. Identified §2(b) of 119-125 as future-applicable only (service after 2028). **No assertion of 12/12 full-slip-law inspection**.


## Final October law retrieved (2026-11-16)
GPO P.L. 119-131 slip-law HTML/PDF direct endpoints failed, so retrieved and inspected GPO's **full enrolled H.R. 4307 text** (BILLS-119hr4307enr), all four sections. Independently cross-checked GPO P.L. 119-131 metadata (approved Oct. 20) and OLRC 29 USC §570 (operative section and notes). No §32/EITC amendment. This closes the **substantive 12/12 enacted-text audit**, while preserving the fact that 119-131 was examined as an **enrolled bill**, not as a slip-law PDF. See [october-2026-cutoff-closeout.md](october-2026-cutoff-closeout.md).


## Empirical reconciliation (2026-11-16)
Directly compared NBER 2012 infant-health abstract with **2015 published article** and found a material numerical change (6.7–10.8% vs published 1.6–2.9% relative). Read original published article's introduction and methods, Dench/Joyce 2020 published-paper manuscript, and Hoynes/Miller/Simon response. Logged design-specific dispute (preperiod, parity contrasts, placebo checks, confounding). Also checked Kleven 2024 journal abstract and Rothstein 2010 journal abstract for design/interpretation. No replication of underlying microdata or full table-by-table audit. See [empirical-reconciliation.md](empirical-reconciliation.md).


## Final research-quality pass (2026-11-16)
Read Eissa–Liebman NBER 1995 and **QJE 1996 published abstracts** and identified 1.4 pp vs up-to-2.8 pp version change and changed post-period. Read Schanzenbach–Strain 2021 published executive summary, Kleven 2024 published abstract, Hoynes/Miller/Simon 2015 publisher abstract, Dench/Joyce 2020 published abstract, and authors' 2019 response overview. Recorded competing findings without treating disagreement as reason to discard. **Not performed:** complete published-paper table-by-table review, independent robustness replication, exhaustive latest literature survey. See [research-quality-final-pass.md](research-quality-final-pass.md).


## Eligibility/regulatory cross-check (2026-11-16)
Read IRS eligibility guide, 2026 EITC income/credit table, draft Schedule 3-A, original 91 FR 53812 proposal, 91 FR 64631 hearing cancellation and Oct. 26 CRS analysis. Targeted REG-119882-25/RIN search did not locate final rule; did not complete exhaustive Federal Register docket sweep. Identified potential 2026 form/guidance vs proposed-rule ambiguity; documented rather than resolving speculatively. See [eligibility-regulatory-quality-check.md](eligibility-regulatory-quality-check.md).


## PRWORA regulatory status follow-up (2026-11-16)
Inspected full August 20 NPRM and proposed §1.32-4(g), Oct. 9 hearing cancellation, CRS Oct. 26 analysis, live IRS eligibility page and targeted REG-119882-25/RIN 1545-BS06/title search. Verified proposed applicability is conditional on **publication of final regulations**. Found no final rule by Oct. 31; recorded negative search limitation. **C014 qualified publication gate closed**; monitoring remains advisable. See [prwora-regulatory-status.md](prwora-regulatory-status.md).


## Eligibility exception primary-source review (2026-11-16)
Opened IRS [Publication 596 (2025)](https://www.irs.gov/publications/p596), including its contents, introductory rules, Rule 2 and named sections for child tiebreakers, combat pay, clergy, disability, Form 8862 and disallowance. Recorded 2025-vintage limitations explicitly; did **not** substitute 2025 thresholds for 2026 or claim 2026 exceptions exhaustively certified. [Audit](eligibility-exceptions-audit.md).


## Empirical robustness tables (2026-11-16)
Directly opened Rothstein 2010 supplemental appendix (3 pp), Leigh 2010 IZA full paper (45 pp), HMS 2015 journal full paper (40 pp), Dench/Joyce manuscript (26 pp). Inspected Rothstein Appendix B elasticity reversal, Leigh Table 4 and §4.4 composition bound, HMS Table 3 race/parity estimates, Dench/Joyce Table 2 parity placebos. NBER and ScienceDirect full-paper pages unavailable; employment full robustness table review remains open. **No original regressions rerun or datasets downloaded.** [Audit](empirical-robustness-tables.md).


## Employment published tables (2026-11-16)
Read [Eissa/Liebman published QJE full text](https://faculty.georgetown.edu/noe/qje_596.pdf) Tables III–IV; [Schanzenbach/Strain 2021 published 43-page PDF](https://www.journals.uchicago.edu/doi/epdf/10.1086/713494) Tables 3 and 5; [Kleven May 2024 author PDF](https://www.henrikkleven.com/uploads/3/7/3/1/37310663/kleven_eitc_may2024.pdf) Figure 8 and §§5.4–5.5. Directly inspected methodological reconciliation of Kleven (2019) in Schanzenbach/Strain 2021. Did **not** inspect all 432 appendix event studies, compare author version line-by-line to journal, or run microdata replication. [Audit](employment-robustness-audit.md).


## Publication synthesis (2026-11-16)
Created [provision-record-draft.md](provision-record-draft.md) using independently audited statutes/committee reports/IRS/JCT/GAO and the study-specific employment, wage-incidence and infant-health audits. Clearly labeled model simulation vs observational estimate, competing findings, source vintage, uncertainty and regulatory proposal status. No new claim of independent regression replication or exhaustive indirect-law sweep.


## Publication-readiness QA (2026-11-19)
Read [provision-record-draft.md](provision-record-draft.md), [research-quality-final-pass.md](research-quality-final-pass.md), and [legislative-history-audit.md](legislative-history-audit.md). Spot-checked [P.L. 95-600 §103](https://www.govinfo.gov/content/pkg/STATUTE-92/pdf/STATUTE-92-Pg2763.pdf) and [Schanzenbach/Strain published bibliography](https://ideas.repec.org/a/ucp/tpolec/doi10.1086-713494.html). Corrected mistaken 35:1–36 to **35:87–129**, updated draft compilation date, and created [publication-readiness-review.md](publication-readiness-review.md). **No full URL crawl or independent recheck of every claim**; draft remains conditional.


## Direct §32 eligibility crosswalk (2026-11-19)
Inspected [OLRC §32 full statutory text](https://uscode.house.gov/us/usc/119-124/t26/s32/) and [IRS live EITC eligibility page](https://www.irs.gov/credits-deductions/individuals/earned-income-tax-credit/who-qualifies-for-the-earned-income-tax-credit-eitc). Recorded exact subsections for childless age/residence, SSN distinction, separated spouses, combat-pay election, prior disallowance, 2021-only age expansion. Did not independently inspect §152(c) full text or finalized TY2026 Form 1040/EIC instructions. [Crosswalk](ty2026-eligibility-statutory-crosswalk.md).


## Qualifying-child cross-reference inspection (2026-11-19)
Read [OLRC §32(c)(3)](https://uscode.house.gov/us/usc/119-124/t26/s32/) and [OLRC §152(c), (f)](https://uscode.house.gov/us/usc/119-124/t26/s152/), laws through P.L. 119-124. Documented incorporated tests, expressly disregarded §152(c)(1)(D) support and §152(e) release, tie-breakers, age/student/disability, married child, joint return, identifiers, military and kidnapping. [Full matrix](qualifying-child-statutory-crosswalk.md). Did not inspect finalized TY2026 administrative forms.


## Citation verification pass 1 (2026-11-19)
Reopened [OLRC §32](https://uscode.house.gov/us/usc/119-124/t26/s32/), [OLRC §152](https://uscode.house.gov/us/usc/119-124/t26/s152/), and [IRS I.R.B. 2025-45](https://www.irs.gov/irb/2025-45_IRB). IRS 2026 EITC figures occur in Rev. Proc. 2025-32 **§4.06**, not §3.06. JCT attachment URL returned 404; [JCT landing](https://www.jct.gov/publications/2025/jcx-45-25/) exists, and [CRS R49052](https://www.everycrsreport.com/reports/R49052.html) corroborates $67.2b. Outlay $56.6b not reverified in this pass. Draft and [citation QA ledger](citation-qa-pass1.md) updated; no comprehensive link crawl.


## Targeted IRS/GAO primary-source check (2026-11-19)
Opened [IRS 2024 EITC claims](https://www.irs.gov/tax-professionals/eitc-central/statistics-for-tax-returns-with-the-earned-income-tax-credit-eitc) national row (24m, $69.6b; cycle 202553), [IRS participation](https://www.irs.gov/tax-professionals/eitc-central/eitc-participation-rate-by-state) national 2022 row 80.8% and footnotes 1/2 (CPS 78%), [GAO-26-108044 Table 1](https://files.gao.gov/reports/GAO-26-108044/index.html) EITC row FY2023 33.5% FY2024 27.3%, including GAO caveat that rates cover unknown payments. JCT landing timed out. [Citation pass 2](citation-qa-pass2.md). Draft precision updated.


## Recovered JCT PDF and IRS historical table — 2026-11-22
Opened [JCT landing](https://www.jct.gov/publications/2025/jcx-45-25/), followed **Download Now** to [current official attachment](https://www.jct.gov/getattachment/8c830c45-1680-4f7e-a649-2a0106f6b6e3/x-45-25.pdf). Directly checked Table 1 printed p.41 FY2026 $67.2b and footnote [3] printed p.43 $56.6b; introduction baseline laws through Aug31 2025 and Jan2025 CBO. Opened [IRS historical statistics](https://www.irs.gov/credits-deductions/individuals/earned-income-tax-credit/earned-income-tax-credit-statistics): TY2023* 23.2m/$63.8b, TY2024* 24.1m/$70.6b, starred footnote **CDW actual volume**. Draft updated. [Full QA pass 3](citation-qa-pass3.md).


## Editorial consistency audit (2026-11-22)
Read live PR provision draft, readiness review, employment robustness, empirical robustness, eligibility exceptions and citation QA pass 3. Identified arithmetically inconsistent Kleven grid (7×4×4×4=448, not 432); withdrew grid decomposition pending direct source verification. Clarified JCT outlay is included in total and updated draft editorial date. [Audit](final-editorial-consistency-audit.md). This was **not** a full external-source or link crawl.


## Kleven full-text count recheck (2026-11-22)
Reviewed [journal-formatted full text §5.4 p.16](https://eml.berkeley.edu/~saez/course/klevenJpubE24EITC.pdf) and [May 2024 author revision §5.4 p.24](https://www.henrikkleven.com/uploads/3/7/3/1/37310663/kleven_eitc_may2024.pdf). Both state 432 while prose lists 7 reform experiments, 4 samples, 4 outcomes, 4 controls = 448 fully crossed; journal Figure 9 says 304 non-1993. Discrepancy not resolved by inspected text. [Detailed audit](kleven-specification-count-audit.md).
