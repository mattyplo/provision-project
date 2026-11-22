# EITC §32 — independent research-run comparison (initial audit, 2026-11-16)

**Status:** completed report-to-report comparison; **partial independent source audit**, not a publication-ready EITC record. **Legal snapshot:** 2026-10-31. Related: #29, #9. Preserve archived outputs unchanged.

## Inputs and comparability
- [Gemini raw report](research-runs/eitc-gemini-20261107-01-raw-report.md), [manifest](research-runs/eitc-gemini-20261107-01-manifest.md) (PR #35).
- [ChatGPT Deep Research raw report](research-runs/eitc-chatgpt-20261107-01-output.md), [manifest](research-runs/eitc-chatgpt-20261107-01-manifest.md) (PR #36).
- PR #37's interrupted Ask-Chat attempt is **supplemental workflow evidence only**, not an equivalent completed research comparator.
- Both completed reports target 2026-10-31. Gemini used Auto / Gemini 3 family and High thinking (operator-reported); ChatGPT exact model not exposed. Gemini omitted the manifest addendum/template due to prompt length; neither run has a contemporaneously preserved byte-exact assembled submission. Therefore these observations **do not establish comparative provider quality or causal prompt effects**.

## Comparison matrix
| Dimension | ChatGPT report | Gemini report | Assessment / next audit |
| --- | --- | --- | --- |
| §32 mechanics | Phase-in, plateau, phaseout; 2026 tables and rate columns | General mechanism, smaller applicability matrix | ChatGPT more detailed; verify against §32 and IRS, not against model agreement. |
| 2026 investment-income limit | $12,200 | Approximately $11,610, explicitly projected | **Resolved contradiction**: IRS Rev. Proc. 2025-32 §3.06(2) states $12,200 for TY2026. Gemini figure contradicted. |
| Original enactment | P.L. 94-12, §204, original §43; 1975 | Same | **Verified** directly from P.L. 94-12, 89 Stat. 30–32. Original §209(b) limits operation to taxable years beginning after 1974 and before 1976; later amendments matter. |
| Legislative rationale | Payroll-tax relief / work incentive with qualifications | Similar three-part rationale | Agreement is not proof of congressional intent; Senate Report 94-36 not independently inspected. |
| Legislative evolution | More detailed statutory timeline and effective-date caveats | Chronology with several generic JCT citations | Audit each material amendment against enacted text, especially 1978 and ARPA 2021. |
| IRS observed use | Distinguishes returns, dollars, take-up and denominators | Headline counts, take-up, improper payments | Reconcile data vintage, tax year vs fiscal year, claims vs allowances and refunds. |
| Fiscal effect | JCT total/outlay split; ~$10.6b FY2026 residual expressly project-derived | Fiscal reconciliation with less precise locators | JCT source and exact columns still require independent audit; never present residual as published JCT line. |
| Compliance | Differentiates GAO improper payments from intentional fraud | Discusses overclaims and compliance | Verify GAO definitions and years; improper ≠ fraudulent. |
| Employment response | Contrasts Eissa/Liebman and later reappraisal; contested generalizability | Calls single-mother extensive-margin effects conclusive/robust | **Unresolved empirical disagreement**; full original studies and identification assumptions needed. |
| Economic incidence | Separates statutory claimant from ultimate beneficiary | Mentions wage/employer capture | Neither establishes national incidence allocation; retain Unknown / insufficient evidence. |
| Source provenance | Claim IDs EITC-C001–C014; platform-specific citation markers; some direct URLs in source map | Generic source inventory and source claims marked inspected | Both require durable URLs, precise pinpoints, actual inspection evidence and independent checks. |

## Independent primary-source checks performed in this pass
1. **Verified — original statutory creation and original terms.** [P.L. 94-12, §204(a)–(b), 89 Stat. 30–32](https://www.govinfo.gov/content/pkg/STATUTE-89/pdf/STATUTE-89-Pg26.pdf): enacted March 29, 1975 as IRC §43; 10% of up to $4,000 of earned income (maximum $400), 10% phaseout above $4,000, and refundability via §6401(b). [§209(b), 89 Stat. 35](https://www.govinfo.gov/content/pkg/STATUTE-89/pdf/STATUTE-89-Pg26.pdf) originally applied §204 to taxable years beginning after December 31, 1974 and before January 1, 1976. This is the **original enacted text**, not a claim about subsequent extension/permanence.
2. **Verified — 2026 parameters.** [IRS Rev. Proc. 2025-32, §3.06(1)–(2), Internal Revenue Bulletin 2025-45](https://www.irs.gov/irb/2025-45_IRB): TY2026 investment-income exclusion threshold is **exceeds $12,200**; maximum credits are $664 / $4,427 / $7,316 / $8,231 for zero/one/two/three-or-more qualifying children. IRS [TY2026 EITC tables](https://www.irs.gov/credits-deductions/individuals/earned-income-tax-credit/earned-income-and-earned-income-tax-credit-eitc-tables) corroborate.
3. **Verified — present statutory architecture (not full 2026 enactment sweep).** [House Office of Law Revision Counsel, 26 USC §32, through P.L. 119-124](https://uscode.house.gov/us/usc/119-124/t26/s32/) provides §32(a), (b), (c), (i), and notes. This does **not** by itself verify the absence of enactments from Oct. 16–31, 2026.

## Boundaries and conclusions
- **Source verification is claim-specific.** Two verified clusters do not validate the reports wholesale; all other findings remain provisional pending audit.
- **No model winner:** ChatGPT gives more explicit uncertainty and a more usable claim map in these outputs; Gemini supplies a useful independent comparison and an identifiable wrong 2026 projection. Different execution settings, citation accessibility, and one run per platform preclude broader performance conclusions.
- **Editorial rule:** union useful source leads, not unsupported assertions. Do not infer economic incidence from eligibility or observed claims.
- Next: complete [audit queue](audit-queue.md), record results in [research log](research-log.md), then create the audited §32 record separately.


## Subsequent independent verification (2026-11-16)
JCT [JCX-45-25 Table 1](https://www.jct.gov/getattachment/fe301c56-965c-48c9-ac06-52b7b6765b05/x-45-25.pdf) confirms FY2026 EITC tax-expenditure estimate $67.2b and outlay component $56.6b; $10.6b is a **project-calculated rounded difference**, not JCT's separately stated estimate. IRS [TY2024 processed-2025 claims](https://www.irs.gov/tax-professionals/eitc-central/statistics-for-tax-returns-with-the-earned-income-tax-credit-eitc) are ~24m/$69.6b, distinct from JCT fiscal-year estimates. [GAO-26-108044](https://files.gao.gov/reports/GAO-26-108044/index.html) corroborates FY2023/FY2024 improper-payment rates 33.5%/27.3%, not fraud rates. [P.L. 95-600](https://www.govinfo.gov/content/pkg/STATUTE-92/pdf/STATUTE-92-Pg2763.pdf) places permanence in **§103** (correcting the original audit queue's erroneous §§104–105 label). [91 FR 53812](https://www.govinfo.gov/content/pkg/FR-2026-08-20/pdf/FR-2026-08-20.pdf) and [91 FR 64631](https://www.govinfo.gov/content/pkg/FR-2026-10-09/html/2026-20790.htm) establish proposed rule status and cancelled hearing. [Eissa/Liebman W5158](https://www.nber.org/papers/w5158) supports the reported 1.4 percentage point *relative* participation change, but the authors also attribute possible effects to other TRA86 provisions. Remaining full-source gates are recorded in [audit-queue.md](audit-queue.md); **do not treat this as complete publication verification**.


## Legal cutoff closure (2026-11-16)
The bounded Oct. 16–31, 2026 direct §32 statutory audit is **closed**: eleven enacted slip-law texts plus the full GPO **enrolled** text of H.R. 4307 (enacted P.L. 119-131), cross-checked against GPO law metadata and OLRC 29 USC §570, revealed no direct amendment to §32. [Full source ledger and method](october-2026-cutoff-closeout.md). This does **not** certify all indirect interactions or the empirical/economic record.
