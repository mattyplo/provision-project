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
