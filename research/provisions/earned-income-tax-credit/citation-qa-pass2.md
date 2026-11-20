# Citation QA pass 2 — IRS claims, participation, GAO payment integrity

**Audit date:** 2026-11-19. **Scope:** reopened official IRS and GAO pages, extracted direct table/footnote locators; attempted JCT landing page, which timed out. This is a targeted verification pass, **not** an exhaustive source audit.

## Verified source-to-claim rows
| Claim in provision draft | Primary source and exact locator | Result |
| --- | --- | --- |
| TY2024 24 million claims and $69.6b, processed in 2025 | [IRS EITC returns by state](https://www.irs.gov/tax-professionals/eitc-central/statistics-for-tax-returns-with-the-earned-income-tax-credit-eitc), heading **“2024 EITC tax returns by state processed in 2025”**, **NATL / National** row, and asterisk methodology below state table | **VERIFIED**: 24 M, $69.6 B, $2,894 mean. Source explicitly says “as of December 2025”; underlying cycle 202553. Claim counts are rounded, not unique individuals. |
| TY2022 national ACS-linked participation 80.8% | [IRS participation rate by state](https://www.irs.gov/tax-professionals/eitc-central/eitc-participation-rate-by-state), **National row**, **Tax year 2022** column, **footnote 1** | **VERIFIED**. ACS model estimates eligibility, IRS tax records identify payments; denominator is modeled eligible population. |
| TY2022 CPS national participation 78% | Same IRS participation table, **footnote 2** | **VERIFIED**. Different national methodology, not a discrepancy to average or silently reconcile. |
| EITC improper-payment 33.5% FY2023, 27.3% FY2024 | [GAO-26-108044](https://files.gao.gov/reports/GAO-26-108044/index.html), **Table 1**, “Internal Revenue Service – Earned Income Tax Credit” row, FY2023 and FY2024 columns; also “Monitoring” discussion | **VERIFIED**. GAO notes rates include **improper and unknown payments** and payments lacking sufficient documentation; not a measure of proven fraud. |
| JCT FY2026 $67.2b total and $56.6b outlay | [JCT JCX-45-25 landing](https://www.jct.gov/publications/2025/jcx-45-25/) | **NOT REVERIFIED THIS PASS**. Official landing page timed out; previous direct attachment returned 404. Prior research claims still require direct JCT Table 1 inspection or reliable official mirror. |
| IRS TY2023 SOI ~23m/$64b | [IRS EITC statistics](https://www.irs.gov/credits-deductions/individuals/earned-income-tax-credit/earned-income-tax-credit-statistics) | **NOT REVERIFIED THIS PASS**; do not mark closed. |

## Public-facing wording check
- TY2024: “approximately **24 million EITC claims** and **$69.6 billion** for tax-year 2024 returns processed in 2025, per IRS national row (data through December 2025).”
- TY2022: “IRS reports **80.8%** using linked ACS and tax records and **78%** using CPS; these are **distinct estimates** of participation, not administrative counts of everyone eligible.”
- GAO: “GAO Table 1 reports **estimated improper/unknown payment rates** of **33.5% FY2023** and **27.3% FY2024**; improper/unknown **is not synonymous with fraud**.”

## Publication status
These **three official-source claim clusters are closed at the citation/table level**. **JCT original total/outlay row and IRS TY2023 SOI remain open**. Other empirical/historical source checks from earlier audit passes are not re-certified here.
