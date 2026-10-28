# Provision 1 — Independent Deep Research comparison (pilot for #9)

**Provision:** Crop-insurance proceeds deferral, 26 U.S.C. § 451(f)  
**Comparison date:** 2026-10-27  
**Inputs (preserved verbatim in PR #20):** [ChatGPT report](chatgpt-deep-research.md) (report date 2026-10-27); [Gemini report](gemini-deep-research.md) (report provenance says 2026-10-26).  
**Status:** Preliminary cross-report evaluation with two targeted source checks. **Not** a completed claim-by-claim source audit or a final provision record.

## Executive assessment

The two reports agree on the broad structure: a one-year election for certain cash-method farmers receiving qualifying physical-crop-loss proceeds; origin in the 1969 Tax Reform Act; later statutory expansions; and a lack of directly measured provision-specific incidence and fiscal effect. These agreements are research leads, **not** independent source verification.

**ChatGPT** is stronger at marking the limits of the evidence, preserving inspection status, and resisting extrapolation from crop-insurance programs to this tax rule. **Gemini** supplies additional potential data leads, operational examples, and hypotheses, but makes several confident claims that either conflict with a judicial opinion or do not follow from the cited data. Both reports require a primary-source audit before publication.

## Evaluation by required dimension

| Dimension | ChatGPT | Gemini | Assessment / next action |
|---|---|---|---|
| Provision boundary and current law | Clear separation of § 451(f) from insurance premium subsidies and other farm programs; qualifies as-of snapshot. | Clear inclusion/exclusion table and explicit external-program relationships; asserts law fully operative. | Use statute and regulation to verify each boundary and the as-of date. |
| Source discovery | Statute, eCFR, IRS, case law, Treasury/JCT, USDA context; flags original documents not directly retrieved. | Broad bibliography including Pub. 4801, historic Federal Register material, extensions, academic and general web sources. | Union the **leads**, not the claims. Deduplicate, privilege original authorities, and record actual inspection. |
| Citation support | Claim map with 18 entries; distinguishes direct examination from secondhand leads. Some embedded research-platform citation tokens are not durable GitHub links. | Claim map with 8 entries and bibliography; many prose claims have numeric citation markers without pinpointed passages. Some source IDs and URLs are mismatched or weakly relevant. | Rebuild final claim map using stable URLs and pinpoint references; do not count a model's “Directly Examined” assertion as verification. |
| Statutory interpretation | Distinguishes damaged-crop qualification from trade/business-wide election scope. | Describes *Nelson* as upholding a whole-farm >50% eligibility test. | **Material Gemini error:** appellate opinion rejects aggregation of other crops to satisfy eligibility; see verified check below. |
| Legislative history | Tracks 1969, 1976, 1977, 1988, 1989, 2017 and explicitly flags uninspected history. | Tracks 1969, 1971, 1974, 1976, 1988, 2009, 2017 and offers a detailed contemporaneous rationale. | Verify 1969 committee reports/JCT explanation, statutory sections and effective dates, and missing/uncertain administrative changes. |
| Quantitative evidence / observed use | Does not claim a provision-specific participation series. | Gives 2020/2021/2023 Schedule F counts and amounts as if from IRS SOI Pub. 4801. | **Material numerical discrepancy** against 2023 IRS table; see check below. Keep insurance-receipt aggregates distinct from deferral elections. |
| Direct tax benefit | Distinguishes deferral and possible rate-smoothing effects from permanent exclusions. | Offers formulas for time value and bracket smoothing, but some Markdown math is broken. | Treat formulas as illustrative technical inference; specify assumptions and taxpayer-specific outcomes. |
| Economic incidence | Explicitly unknown for § 451(f); treats USDA crop-insurance distribution as context only. | Claims short-run incidence “entirely” with operator; hypothesizes land-rent capitalization from literature on different subsidies. | Do not adopt Gemini's incidence conclusion; direct tax recipient ≠ economic incidence. Other-program literature is only a hypothesis-generating analogy. |
| Distribution | Avoids asserting provision-specific distribution without usage data. | Asserts concentration by commodity, farm size, region, and income class. | Treat as unverified hypotheses, not observed § 451(f) distribution. |
| Fiscal effect | No standalone § 451(f) estimate located; emphasizes timing and uncertainty. | No standalone estimate, but claims steady-state budget neutrality and disaster-year revenue patterns. | Distinguish annual cash-flow effects, present value, bracket effects, and official scoring; no provision-specific number verified. |
| Uncertainty / unsupported inference | Uses Established/Supported/Uncertain/Unknown with caveats. | Includes unknowns, but several strong claims elsewhere conflict with those caveats. | ChatGPT more consistent; both need external audit. |
| Research provenance | Records report date and inaccessible/previous preservation problems separately; prompt and platform citations need durable capture. | Records research date and public access, but does not identify specific Gemini model, settings, or exact submitted prompt. | Add run manifest for both; mark unknown settings explicitly. |

## Targeted independent verification

### V-01 — *Nelson v. Commissioner* (high priority; legal interpretation)

**Gemini claim:** the Eighth Circuit “affirm[ed] whole-farm >50% test” and held the test applied to the “entire single trade or business” rather than individual crops (Gemini, Material Development History and Significant Disagreements).

**Primary source inspected:** Eighth Circuit's filed opinion, *Nelson v. Commissioner*, 568 F.3d 662 (8th Cir. June 10, 2009), https://ecf.ca8.uscourts.gov/opndir/09/06/082912P.pdf ; especially the discussion of the alternative aggregation argument (opinion pp. 6–7; reported opinion at 666).

**Finding:** The court **rejected** the taxpayers' argument that customary deferral of >50% of **all** crop income could qualify their sugar-beet proceeds where only 35% of sugar-beet income was normally deferred. The regulation's single-trade-or-business rule concerns the **scope of the election across qualifying proceeds**, not a license to satisfy the eligibility threshold by pooling other crops. This supports the ChatGPT report's distinction and contradicts Gemini's broad description.

**Disposition:** Mark Gemini's *Nelson* interpretation **incorrect**. Independently verify the exact treatment of multiple *damaged* crops under the regulation and ruling before writing a comprehensive rule.

### V-02 — IRS SOI Publication 4801 (high priority; quantitative evidence)

**Gemini claim:** for 2023, approximately 1.68 million Schedule F returns, 194,120 returns reporting Line 6a, and $8,412.8 million in Line 6a amounts (Gemini, Observed Use table).

**Official source inspected:** IRS, *Publication 4801 (Rev. 6-2026), Individual Income Tax Returns Line Item Estimates*, 2023 Schedule F tables, PDF pp. 53–54 (PDF page index 52–53), https://www.irs.gov/pub/irs-pdf/p4801.pdf .

**Finding:** The official table reports **1,825,685** total Schedule F returns, **154,820** reporting Line 6a, and **$9,106,009 thousand** ($9.106 billion) on Line 6a. Gemini's 2023 figures do not match these cells. The publication is based on samples; the figures are estimates. The public table does not by itself establish how many taxpayers made the § 451(f) election.

**Disposition:** Mark Gemini's 2023 figures **contradicted by the cited official table**. Independently check the 2020 and 2021 entries before any use; do not infer § 451(f) utilization from Line 6a or a difference between Lines 6a/6b.

## Material source leads discovered by one report

- **Gemini:** IRS Publication 4801 line-item tables (useful and verifiable, but misquoted in the report); additional extension/practitioner commentary on Revenue Protection indemnity allocation; historic Federal Register leads. These should enter a retrieval queue with source type and claim relevance.
- **ChatGPT:** Explicit USDA ERS farm-type context and Treasury tax-expenditure methodology; 1977 regulation amendment and 1989 administrative guidance; more granular inspection-status and claim-evidence distinctions.
- **Neither report alone:** Establishes a defensible § 451(f) national election count, distribution of its tax benefits, standalone official revenue estimate, or identified causal incidence study.

## Prioritized audit queue

1. **P0 legal:** Check 26 U.S.C. § 451(f), 26 C.F.R. § 1.451-6(a)–(b), Rev. Rul. 74-145, and *Nelson*; separate crop-level eligibility from all-eligible-proceeds election scope.
2. **P0 data:** Reconcile all Gemini SOI numbers to exact IRS publication pages and tax years; record line definitions and sample-estimate caveats.
3. **P1 origin:** Retrieve and pinpoint Pub. L. 91-172 § 215(a), House/Senate reports, and JCT general explanation; attribute legislative *intent* only to passages actually inspected.
4. **P1 amendments:** Verify 1976, 1988, and 2017 statutes, effective dates, and 1971/1977 regulations; track statutory vs administrative vs judicial change.
5. **P1 indemnity boundaries:** Verify yield-loss vs price-loss and rainfall-index treatment in current IRS Publication 225 and governing administrative authorities.
6. **P1 fiscal:** Search current JCT/Treasury tax expenditure series for § 451(f), document search scope and no-found result without implying definitive nonexistence.
7. **P2 incidence:** Search for causal work specific to the **tax deferral**, not crop-insurance premium subsidies. If absent, retain **Unknown / insufficient evidence**.
8. **P2 provenance:** Capture both exact prompts, run modes, dates, model/settings when exposed, and original source-link accessibility.

## Platform comparison — preliminary conclusion for Issue #9

**Not a platform-wide ranking.** This is one provision and one preserved report from each system; differences may reflect prompts, settings, source availability, or random variation. On this pilot, ChatGPT produced the more defensible **starting claim map** and better calibrated uncertainty; Gemini contributed potentially useful additional discovery leads but introduced at least one material legal misinterpretation and a numerical claim inconsistent with its own cited official source.

**Research process lesson:** Independent models do not substitute for independent source verification. A comparative review is especially valuable when it creates a ranked audit queue and records demonstrable errors, not when it votes on which model sounds more confident.

## Completion status

- [x] Both independent raw reports preserved in GitHub (PR #20).
- [x] Preliminary cross-platform comparison across Issue #14's required dimensions.
- [x] Two targeted checks against underlying sources.
- [ ] Complete verification of consequential claims.
- [ ] Final source audit and provision record.
- [ ] Complete run provenance and source access manifest.
- [ ] Record any reusable workflow improvements as follow-up issues.

**Related:** #9, #14. This document is an evaluation artifact, not a replacement for the raw reports or the final provision record.
