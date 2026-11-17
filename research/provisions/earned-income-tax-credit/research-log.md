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
