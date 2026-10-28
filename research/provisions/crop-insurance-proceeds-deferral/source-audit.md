# Provision 1 — Primary-source audit log

**Provision:** 26 U.S.C. § 451(f), crop-insurance proceeds deferral  
**Audit started:** 2026-10-27  
**Research inputs:** [ChatGPT](chatgpt-deep-research.md), [Gemini](gemini-deep-research.md), [comparison](comparison.md)  
**Status:** **In progress.** This is an independently checked source ledger, not a completed source audit or final provision record. Do not modify the original reports.

## Evidence standards

- **Verified:** directly inspected controlling statute, regulation, judicial opinion, or government publication that supports the narrowly stated claim.
- **Qualified:** source supports a narrower claim than the report asserts, or is guidance rather than statutory text.
- **Contradicted:** primary authority directly conflicts with report's assertion.
- **Open:** original authority, fiscal estimate, statistical interpretation, or incidence evidence still needs inspection.

## Primary-source claim ledger

| ID | Claim | Audit status | Pinpoint source | Qualification |
|---|---|---|---|---|
| A-01 | § 451(f) authorizes a cash-method taxpayer to elect to report eligible proceeds in the tax year after crop destruction/damage, provided customary practice would have reported crop income in a following year. | **Verified** | [U.S. Code, 26 USC § 451(f)](https://uscode.house.gov/us/usc/119-120/t26/s451/) | Tax **timing**, not permanent exclusion. |
| A-02 | Covered disaster payments under the Agricultural Act of 1949 and title II of the Disaster Assistance Act of 1988 are statutorily treated as insurance proceeds in specified circumstances. | **Verified** | [26 USC § 451(f)](https://uscode.house.gov/us/usc/119-120/t26/s451/) | Do not generalize to every USDA disaster payment. |
| A-03 | Congress first enacted this election in 1969 as § 451(d). | **Verified** | [Pub. L. 91-172 § 215(a)–(b)](https://uscode.house.gov/statutes/pl/91/172.pdf), heading “CROP INSURANCE PROCEEDS” | Applies to tax years **ending after** enactment (Dec. 30, 1969). |
| A-04 | An election is not required to recognize insurance proceeds received in the year after damage; no additional year's deferral is available. | **Verified** | [26 CFR § 1.451-6(a)(1)](https://www.ecfr.gov/current/title-26/section-1.451-6) | Regulation still refers to old subsection (d). |
| A-05 | Election covers all **qualifying** proceeds attributable to crops in a single trade or business; separate businesses require separate elections. | **Verified** | [26 CFR § 1.451-6(a)(2)](https://www.ecfr.gov/current/title-26/section-1.451-6) | Election scope is distinct from qualifying for election. |
| A-06 | Election statement attached to return or amended return for tax year of destruction/damage must identify crop, normal practice, loss circumstances, and itemized insurer payments. | **Verified** | [26 CFR § 1.451-6(b)(1)](https://www.ecfr.gov/current/title-26/section-1.451-6) | Full required items are enumerated in regulation. |
| A-07 | The >50% customary-next-year income threshold is the IRS's applied standard, supported by appellate authority. | **Verified with authority distinction** | [IRS Publication 225, Crop Insurance and Crop Disaster Payments](https://www.irs.gov/publications/p225); [*Nelson v. Commissioner*, 568 F.3d 662, opinion pp. 4–7](https://ecf.ca8.uscourts.gov/opndir/09/06/082912P.pdf) | Threshold does **not** appear numerically in § 451(f) itself; opinion quotes Rev. Rul. 74-145. |
| A-08 | *Nelson* approves whole-farm aggregation to satisfy the >50% test. | **Contradicted (Gemini report)** | [*Nelson* opinion pp. 6–7](https://ecf.ca8.uscourts.gov/opndir/09/06/082912P.pdf) | Court expressly **rejects** aggregation of other crops; for multiple damaged crops it discusses qualification as to an individual crop. |
| A-09 | Price-only revenue-insurance proceeds or rainfall-index proceeds unrelated to physical crop damage can be deferred. | **Contradicted by current IRS guidance** | [IRS Publication 225, election to postpone](https://www.irs.gov/publications/p225) | Guidance permits yield-loss portion only and excludes rainfall-based payment not resulting from physical damage. Need original administrative authority for final legal analysis. |
| A-10 | Current livestock weather-related sale election is § 451(e). | **Contradicted (Gemini numbering)** | [26 USC § 451(g)](https://uscode.house.gov/us/usc/119-120/t26/s451/) | Former § 451(e) was redesignated; current crop insurance is (f), livestock weather sales (g). |
| A-11 | 2023 IRS Schedule F line 6a amount is $8.413 billion. | **Contradicted (Gemini figure)** | [IRS Publication 4801 (Rev. 6-2026), tax year 2023 Schedule F amounts table, p. 53](https://www.irs.gov/pub/irs-pdf/p4801.pdf) | Official line 6a: **$9,106,009 thousand** ($9.106 billion); sample-based estimate. |
| A-12 | 2023 Schedule F 6a return count was 194,120. | **Contradicted (Gemini figure)** | [IRS Publication 4801, Schedule F returns table, p. 52](https://www.irs.gov/pub/irs-pdf/p4801.pdf) | Official line 6a count: **154,820**; sample-based estimate. |
| A-13 | 2023 Schedule F total schedules were ~1.68 million. | **Contradicted (Gemini figure)** | [IRS Publication 4801, Schedule F tables pp. 52–53](https://www.irs.gov/pub/irs-pdf/p4801.pdf) | **1,825,685** schedules. |
| A-14 | IRS publishes a 2023 Schedule F line 6d estimate for amounts deferred from 2022. | **Verified** | [IRS Publication 4801, Schedule F amounts table p. 53](https://www.irs.gov/pub/irs-pdf/p4801.pdf) | **$1,761,329 thousand** ($1.761 billion) reported on line 6d. This is a **prior-year deferral recognized in 2023**, not a measure of 2023 newly deferred amounts or fiscal cost. |
| A-15 | § 451(f) fiscal effect and ultimate economic incidence can be read from crop-insurance payment totals. | **Not supported** | [26 USC § 451(f)](https://uscode.house.gov/us/usc/119-120/t26/s451/); [IRS Publication 4801](https://www.irs.gov/pub/irs-pdf/p4801.pdf) | Payment totals do not show taxpayer tax liabilities, counterfactual recognition years, or ultimate incidence. |

## Important new data lead: Schedule F lines 6c and 6d

The IRS's 2023 line-item estimates show a distinct **line 6d amount deferred from 2022** of $1.761 billion. The current IRS Farmer's Tax Guide also describes a **line 6c election checkbox** for proceeds deferred from the current year. This potentially improves the data-discovery path compared with the initial reports' broad statement that no election-related series was located.

**Do not claim a § 451(f) election count or tax expenditure yet.** Follow up on (a) whether 2023 line 6c counts are reported or suppressed in the returns table, (b) the precise definition and completeness of line 6d, (c) any amended-return timing, (d) non-individual/entity coverage, and (e) comparable earlier-year publications. Do not equate the difference between lines 6a and 6b with newly deferred amounts without validating instructions and data definitions.

## Legislative and source-history queue

- **Open:** Inspect Senate Report 91-552 pp. 106–107 **directly**, rather than solely quoting its summary in *Nelson*. Verify the report's stated rationale and attribution.
- **Open:** Obtain original Revenue Ruling 74-145 (1974-1 C.B. 113), rather than relying on the court's quotation.
- **Open:** Verify 1976 Pub. L. 94-455 § 2102, 1988 Pub. L. 100-647 § 6033, later effective-date amendments, and 2017 redesignation with enacted texts.
- **Open:** Obtain original Notice 89-55 and check policy-specific interpretation.
- **Open:** Check JCT and Treasury tax-expenditure publications for a separately identified § 451(f) estimate; absence from one table is not proof of no official estimate.
- **Open:** Audit Gemini's 2020 and 2021 SOI numbers against exact year-specific publications.
- **Open:** Identify any direct incidence or distribution evidence for **this timing election**; do not substitute Federal Crop Insurance Program subsidy-incidence research.

## Editorial dispositions

1. Use verified statute and regulation for eligibility and election mechanics; cite the Eighth Circuit and IRS guidance distinctly.
2. Preserve Gemini's *Nelson* and SOI discrepancies in the audit trail; do not quietly merge them into final claims.
3. Update the eventual provision record's observed-use section to mention the **line 6d official data lead** with explicit limits.
4. Keep provision-specific **fiscal effect** and **economic incidence** as **Unknown / insufficient evidence** until supported.
5. Do not mark Issue #14 complete until the open items and final source audit are resolved.

## Primary-source URLs inspected in this pass

- https://uscode.house.gov/us/usc/119-120/t26/s451/ (official U.S. Code, 2026-10-07 snapshot)
- https://uscode.house.gov/statutes/pl/91/172.pdf (1969 public law, § 215)
- https://www.ecfr.gov/current/title-26/section-1.451-6 (Treasury regulation; eCFR displayed through 2026-10-22)
- https://ecf.ca8.uscourts.gov/opndir/09/06/082912P.pdf (Eighth Circuit opinion, 2009)
- https://www.irs.gov/publications/p225 (IRS Farmer's Tax Guide, 2025 edition)
- https://www.irs.gov/pub/irs-pdf/p4801.pdf (IRS SOI Publication 4801, Rev. 6-2026, tax year 2023)

**Date caution:** The reports' target legal snapshot is 2026-10-21. The official Code URL above is a slightly earlier codification snapshot; the eCFR source is later. Confirm intervening enactments before labeling the *entire* as-of snapshot independently verified.


---

## Audit continuation — legislative history, administrative authority, utilization, fiscal estimates

**Scope:** Additional direct examination of official statutory editorial notes, current IRS guidance, IRS SOI line-item estimates, JCT 2025–2029 report, and contemporary congressional/JCT explanatory leads. The original Senate report scan, original Revenue Ruling 74-145, and original Notice 89-55 were **not** directly inspected in this continuation.

### Legislative history and effective-date checks

| ID | Claim / evidence | Status | Primary locator and notes |
|---|---|---|---|
| A-16 | Congress created § 451(d) in the Tax Reform Act of 1969, § 215, to address the timing mismatch between insurance received after crop loss and the following-year marketing practice. | **Verified enactment; supported legislative rationale** | [Pub. L. 91-172 § 215](https://uscode.house.gov/statutes/pl/91/172.pdf); [Congressional Record, Oct. 20, 1969, Senator Miller Amendment No. 243](https://www.congress.gov/91/crecb/1969/10/20/GPO-CRECB-1969-pt22-6-2.pdf); [JCT, *General Explanation of the Tax Reform Act of 1969* (JCS-16-70), “7. Crop Insurance Proceeds”](https://www.taxnotes.com/research/federal/legislative-documents/jct-blue-books/joint-committee-report-jcs-16-70-general-explanation-of-the/1r3m8). The JCT explanation explicitly identifies bunching of prior-year crop-sale income and current-year indemnity, advance tax payment, and potential loss of personal exemptions/deductions. Senate Report 91-552 pp. 106–107 is located at the [Senate Finance Committee](https://www.finance.senate.gov/download/tax-reform-act-of-1969-report-91-552), but the ~41 MB scan could not be inspected directly; **do not claim direct Senate-report verification**. |
| A-17 | 1976 expanded former § 451(d) to qualifying Agricultural Act of 1949 disaster payments and inability-to-plant events. | **Verified statutory amendment and effective date** | [Official Code amendment and effective-date notes](https://uscode.house.gov/us/usc/119-120/t26/s451/), “1976—Subsec. (d)” and “Effective Date of 1976 Amendment”; Pub. L. 94-455 § 2102(a)–(c), effective for payments received **after December 31, 1973, in tax years ending after that date**. [JCT 1976 general explanation JCS-33-76](https://www.jct.gov/publications/1976/jcs-33-76/) located; ~49 MB source scan not inspected, so 1976 *rationale* remains open. |
| A-18 | 1988 added specified title II Disaster Assistance Act of 1988 payments. | **Verified statutory amendment and corrected effective date** | [Official Code § 451 editorial notes](https://uscode.house.gov/us/usc/119-120/t26/s451/), “1988—Subsec. (d)” and “Effective Date of 1988 Amendment”: Pub. L. 100-647 § 6033(a), effective for payments received **before, on, or after November 10, 1988**, as amended by Pub. L. 101-239 § 7816(g). **Do not confuse with § 6030(b)**, whose after-1987 effective date concerns livestock sales. Gemini's contrary 1988 effective-date characterization is incorrect. |
| A-19 | 2017 changed the subsection label from former § 451(d) to current § 451(f). | **Verified** | [Official Code § 451, 2017 amendment note](https://uscode.house.gov/us/usc/119-120/t26/s451/): Pub. L. 115-97 § 13221 added new subsections and twice redesignated older subsections. Regulation § 1.451-6 retains its former § 451(d) cross-reference; do not treat the old number as a different current election. |
| A-20 | Treasury regulations implement the election; 1977 amendments incorporated disaster-payment expansion. | **Verified text and amendment citation, not full original rulemaking history** | [26 CFR § 1.451-6](https://www.ecfr.gov/current/title-26/section-1.451-6), authority line: T.D. 7097, 36 FR 5215 (Mar. 18, 1971), amended T.D. 7526, 42 FR 64624 (Dec. 27, 1977), and T.D. 8429, 57 FR 38595 (Aug. 26, 1992). [Treasury archival regulation text](https://www.govinfo.gov/content/pkg/GOVPUB-T22-1bac9ce4176abd0155492a777a4e7b12/pdf/GOVPUB-T22-1bac9ce4176abd0155492a777a4e7b12-1.pdf) shows 1977 addition treating qualifying Agricultural Act payments as insurance. Original preambles and 1992 change still need pinpointing. |

### Administrative rulings — evidentiary status

**Rev. Rul. 74-145 (1974-1 C.B. 113):** The more-than-50% threshold is **verified as quoted and analyzed by the Eighth Circuit in [*Nelson*](https://ecf.ca8.uscourts.gov/opndir/09/06/082912P.pdf)** and reflected in [IRS Publication 225](https://www.irs.gov/publications/p225). The original 1974 Internal Revenue Bulletin/Cumulative Bulletin text has **not** been directly retrieved; classify the original ruling as **identified / indirectly verified**, not directly inspected.

**Notice 89-55 (1989-1 C.B. 696):** [Iowa State's Center for Agricultural Law and Taxation](https://www.calt.iastate.edu/post/special-rule-taxing-crop-insurance-and-disaster-payments) attributes an actual physical-crop-loss requirement to the notice. Current [IRS Publication 225](https://www.irs.gov/publications/p225) independently provides current operational guidance distinguishing physical yield loss from price-only and rainfall-index indemnities. **The original Notice has not been directly retrieved**, so its precise wording and historical reach remain open. Do not cite secondary summaries as direct proof of its text.

### Observed use: what IRS SOI actually shows

[IRS Publication 4801 (Rev. June 2026), 2023 Schedule F](https://www.irs.gov/pub/irs-pdf/p4801.pdf), states that all figures are **estimates based on samples**. The returns table reports:

- **1,825,685** total Schedule F schedules filed (not necessarily unique farmers).
- **154,820** schedules with a reported Line 6a crop-insurance/disaster-payment receipt.
- **18,540** schedules with a reported **Line 6d** amount deferred from 2022 (recognized in 2023).

The corresponding amounts table reports:

- Line 6a receipts: **$9,106,009 thousand** (~$9.106 billion).
- Line 6b taxable current-year amount: **$7,635,258 thousand** (~$7.635 billion).
- Line 6d prior-year deferred amount included in 2023: **$1,761,329 thousand** (~$1.761 billion).

[IRS Schedule F instructions](https://www.irs.gov/instructions/i1040sf) explain: 6a is total proceeds received in the tax year, 6b is taxable amount from that year's receipts, 6c is the **checkbox for an election to defer to next year**, and 6d reports **amounts received in the preceding year and elected for inclusion this year**.

**Interpretation (qualified):** Line 6d offers a directly relevant observed *reporting* proxy for the population recognizing prior-year deferrals, and a dollar estimate of that income recognized in 2023. It is **not** an estimate of § 451(f) elections newly made in 2023, unique taxpayer counts, nationwide coverage across all entity forms, tax savings, or the tax expenditure. The IRS public table displays a checkbox for 6c but does **not** provide a numeric 6c count in that table. The simple difference 6a–6b (~$1.471 billion) is a possible *reconciliation lead*, **not** a verified amount elected under § 451(f); do not publish it as utilization without methodological validation.

**Still open:** exact 2020/2021 IRS figures in Gemini; whether IRS has a more specific 6c checkbox tabulation; corporation/partnership coverage; amendment effects; confidence intervals; and whether the 2023 line 6d figure includes any filing categories that require qualification.

### Fiscal effect: official reporting search

**JCT:** [*Estimates of Federal Tax Expenditures for Fiscal Years 2025–2029*, JCX-45-25 (Dec. 3, 2025)](https://www.jct.gov/getattachment/8c830c45-1680-4f7e-a649-2a0106f6b6e3/x-45-25.pdf), Table 1, agriculture category (report p. 36 / PDF p. 38), **does not separately list § 451(f)**. It lists agricultural net-operating-loss carryback, soil/water conservation, fertilizer, and farm income averaging instead. JCT introduction, report p. 2, explains that a provision is generally listed if its five-year revenue loss is **not de minimis**; for this report the de minimis threshold is **less than $250 million over 2025–2029**. Absence from the table does **not** establish zero fiscal effect, nor prove that § 451(f) is below threshold (classification and aggregation decisions also matter).

**Treasury:** [Tax Expenditures and FAQ](https://home.treasury.gov/policy-issues/tax-policy/tax-expenditures) defines tax expenditures to include deferrals and distinguishes annual revenue effects from present-value effects. Treasury warns that a repeal estimate is not interchangeable with tax expenditure estimates and timing provisions can show negative annual values. Its landing page lists FY2027 and prior spreadsheets, but a specific § 451(f) figure **has not yet been verified from those spreadsheets**.

**Current disposition:** **No separately identified official § 451(f) fiscal estimate verified in the sources examined.** Do not assert “revenue-neutral,” zero cost, or a numeric revenue loss. A further Treasury spreadsheet check and older JCT search would strengthen this negative finding.

### Updated remaining work (priority)

1. Retrieve Senate Report 91-552 original pp. 106–107 and JCT JCS-33-76 1976 discussion using an accessible scan; mark provenance of the original passages.
2. Retrieve original Rev. Rul. 74-145 and Notice 89-55; compare exact language with *Nelson* and current Pub. 225.
3. Verify the Treasury FY2027/FY2026 workbook contents for any separate crop-insurance-deferral line; examine historic JCT reports if practical.
4. Determine whether IRS can provide a count of Schedule F line 6c elections, and reconcile 6a/6b/6d with line definitions.
5. Audit Gemini's 2020/2021 statistics and assess non-Schedule-F coverage before finalizing observed use.

## Direct verification: Senate Finance Committee Report No. 91-552 (1969)

**Source:** U.S. Senate Committee on Finance, *Tax Reform Act of 1969*, S. Rep. No. 91-552 (1969), **printed pp. 106–107** (PDF pp. 112–113 of the 358-page scan), section **“7. Crop Insurance Proceeds (sec. 215 of the bill and sec. 451 of the code)”**. [Official Senate Finance Committee scan](https://www.finance.senate.gov/download/tax-reform-act-of-1969-report-91-552).

**Verification status: DIRECTLY INSPECTED.** The complete Senate report supplied for the audit was searched, and the two relevant pages were extracted and checked against the text. This replaces the earlier “located but not directly inspected” qualification for S. Rep. 91-552; the earlier qualification is retained above as a record of audit progress.

| Committee section / page | Directly supported finding | Evidence classification |
|---|---|---|
| “Present law,” p. 106 | A cash-method farmer generally recognized crop-insurance proceeds in the year received, even where ordinary crop marketing occurred in a later year. | Contemporaneous committee description of pre-enactment law. |
| “General reasons for change,” pp. 106–107 | A casualty such as hail or windstorm could cause the farmer to report prior-year crop-sale receipts **and** current-year crop-insurance receipts in the same year, creating an income-bunching hardship beyond the farmer's control. | **Express congressional committee rationale**, not an inferred motive. |
| “General reasons for change,” p. 107 | A later-year net operating loss carryback was considered inadequate because the farmer first had to pay additional current-year tax and seek a refund after the next year's loss; the committee also cited possible loss of personal exemptions and standard or itemized deductions. | **Express committee rationale**. The cash-flow concern is distinct from ultimate tax liability. |
| “Explanation of provision,” p. 107 | A cash-method taxpayer could elect next-year recognition if ordinary practice would have reported crop income in that later year; delivery records could establish customary practice. | Committee's explanation of intended operation; enacted statute and regulations govern the actual legal rule. |
| “Effective date,” p. 107 | Provision to apply to taxable years ending after enactment. | Committee explanation; independently check enacted effective-date language. |
| “8. Revenue Effect,” p. 107 | **$25 million annual revenue increase** estimated for **“the farm loss provisions of the bill”** as a group. | **Not a § 451 crop-insurance-deferral-specific fiscal estimate.** Do not attribute this figure to the provision. |

**Provenance:** Printed pages 106–107 are located at PDF pages 112–113 (1-based) in the original 358-page Senate report scan. The authoritative citation should identify the **printed page numbers**. This audit record cites the official complete source rather than implying the two-page extract has been committed to the repository.

**Source preservation follow-up:** Add a two-page PDF extract to `research/sources/senate-report-91-552-pages-106-107.pdf` when a binary-file GitHub upload path is available; the GitHub connector currently available for this commit accepts UTF-8 text, not PDF bytes. Until then the official full-report URL above is the canonical source.


## Audit continuation — direct IRS Chief Counsel letter and fiscal-estimate search (2026-10-27)

### IRS administrative interpretation — new direct primary source

**A-21 — Verified directly:** IRS Office of Chief Counsel, **Information Letter INFO 2009-0024** (Feb. 26, 2009; released Mar. 27, 2009), [original two-page IRS PDF](https://www.irs.gov/pub/irs-wd/09-0024.pdf), pp. 1–2, responds to a senator's inquiry concerning crop-insurance policies with revenue-assurance components. The letter states that proceeds attributable to actual crop destruction or damage can be deferred, whereas proceeds attributable to a reduction in crop prices cannot; when both components are present, only the physical-damage component qualifies. This directly corroborates current [IRS Publication 225](https://www.irs.gov/publications/p225) and strengthens the evidence behind A-09. **Authority classification:** official IRS Chief Counsel *information letter*, not a regulation, revenue ruling, judicial holding, or generally binding precedent. The letter cites former § 451(d), now § 451(f).

**A-22 — Historical rulings still not directly verified:** **Rev. Rul. 74-145, 1974-1 C.B. 113** remains supported indirectly through [*Nelson v. Commissioner*](https://ecf.ca8.uscourts.gov/opndir/09/06/082912P.pdf) and the current IRS Farmer's Tax Guide. **Notice 89-55, 1989-1 C.B. 696** remains identified in [Iowa State University CALT's technical discussion](https://www.calt.iastate.edu/post/special-rule-taxing-crop-insurance-and-disaster-payments) but its original published text was not obtained. The 2009 letter is an independent IRS primary source for the physical-damage/price distinction, **not** a substitute for direct verification of the notice's exact words.

### Fiscal estimates — broadened source review

**A-23 — No provision-specific estimate established:** [Treasury's official Tax Expenditures index](https://home.treasury.gov/policy-issues/tax-policy/tax-expenditures) provides FY2027 and historical Excel workbooks. The **FY2027 workbook was identified** at `https://home.treasury.gov/system/files/131/Tax-Expenditures-FY2027.xlsx`, but **its cells were not inspected**: the web reader rejects XLSX, and the file could not be downloaded in the analysis environment. Do **not** characterize the FY2027 Treasury workbook as searched or claim it omits § 451(f). JCT's [2025–2029 tax-expenditure report](https://www.jct.gov/getattachment/8c830c45-1680-4f7e-a649-2a0106f6b6e3/x-45-25.pdf) was directly inspected in the earlier pass and does not list § 451(f) separately. A search also located JCT's [2022–2026 report](https://www.jct.gov/publications/2022/jcx-22-22/), but no claim about its complete contents is made here.

**A-24 — Historical proposal is not an enacted change or a § 451(f) cost estimate:** JCT's [*Technical Explanation, Estimated Revenue Effects ... of the Tax Reform Act of 2014* (JCS-1-14)](https://www.jct.gov/getattachment/ea4e2f45-ecaa-430c-851e-b8f1b1df3d80/S-1-14-4674.pdf) explicitly discusses a **proposal to repeal** the crop-insurance deferral election alongside the weather-related livestock-sale election. This is evidence of a legislative proposal, **not** evidence that repeal was enacted. The report's revenue estimates may be grouped with other provisions; no separately attributable § 451(f) revenue figure has been verified.

**Fiscal-effect disposition:** **Unknown / no separately attributable official estimate verified in the examined sources.** This is a statement about research coverage, not proof of zero cost. [Treasury explains](https://home.treasury.gov/policy-issues/tax-policy/tax-expenditures) that timing provisions can have positive or negative annual cash-flow effects and that present value can better capture their cost. **Remaining high-priority check:** download and inspect Treasury FY2027 workbook (and historical workbooks if needed), then examine any JCT revenue estimate associated with the 2014 *proposal*, keeping proposed repeal effects distinct from ongoing annual tax expenditures.
