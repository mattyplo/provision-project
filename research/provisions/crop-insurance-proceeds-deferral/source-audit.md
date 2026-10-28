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
