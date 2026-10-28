# Provision 1 — Deep Research run provenance

**Provision:** Crop-insurance proceeds deferral (26 U.S.C. § 451(f))  
**Related issues:** #14 (Provision 1 research), #9 (platform comparison)  
**Manifest recorded:** 2026-10-28 (retrospective documentation)

This manifest records the known conditions of the two independent research runs. **Report metadata** comes from the preserved research reports; **user-confirmed settings** were provided after the runs. A retrospective confirmation is not equivalent to an automatically captured run log. Unavailable fields are marked **not recorded**, not inferred.

## Shared research assignment

- **Reusable prompt:** [Provision Project — Standard Deep Research Prompt v1.0](../../prompts/provision-deep-research-v1.md).
- **Prompt version:** 1.0.
- **Provision:** Crop-insurance proceeds deferral, 26 U.S.C. § 451(f).
- **Requested current-law snapshot:** 2026-10-21.
- **Same prompt used in both runs:** **Yes — confirmed retrospectively by the user on 2026-10-28.**
- **Exact submitted prompt:** The user confirms both runs used the same project prompt. The repository contains the versioned reusable prompt, but no separate contemporaneous, verbatim submission log for either platform was preserved. Any wrapper instructions or platform-side transformations, if present, are **not recorded**. Do not claim independently verified byte-for-byte identity.

## Research runs

| Field | ChatGPT run | Gemini run |
|---|---|---|
| Platform / product | OpenAI ChatGPT | Google Gemini |
| Research mode | Deep Research (report Appendix C) | Deep Research (user-confirmed research workflow; report describes the run as project deep research) |
| Reported run/research date | 2026-10-27 | 2026-10-26 |
| Model / model selection | GPT-5.5 Thinking (reported in ChatGPT Appendix C) | **Gemini Auto (3 models)** (user-confirmed retrospectively) |
| Individual model identifiers | GPT-5.5 Thinking as reported; additional internal models not recorded | **Not recorded**; do not guess the identities of the three models |
| Thinking level | Not separately recorded | **Low** (user-confirmed retrospectively) |
| Research/source settings | Primary official sources prioritized by the common prompt; other platform-specific settings not recorded | Standard public access reported; other platform-specific settings not recorded |
| Source restrictions | Prompt preference for official/primary sources; no separate platform restrictions recorded | Report says standard public access and no proprietary taxpayer microdata |
| Exact submitted prompt | Common v1.0 prompt per user confirmation; verbatim submission log unavailable | Same common v1.0 prompt per user confirmation; verbatim submission log unavailable |
| Preserved output | [ChatGPT Deep Research report](chatgpt-deep-research.md) | [Gemini Deep Research report](gemini-deep-research.md) |

## Comparison and verification

- [Independent comparison](comparison.md) — documents differences in source discovery, citation support, statutory interpretation, history, quantitative claims, and uncertainty handling.
- [Primary-source audit](source-audit.md) — separately verifies consequential claims and records source-access limitations.
- [Completed provision record](record.md) — synthesizes verified findings, not an uncritical merge of AI reports.

## Provenance limitations and next-run practice

1. The model selection **“Gemini Auto (3 models)”** and **Low** thinking level are recorded exactly as confirmed by the user. No individual Gemini model names are established.
2. The Gemini research mode, common prompt, and settings are documented retrospectively; the preserved Gemini report itself does not independently prove every setting.
3. The ChatGPT model identifier is taken from the research report's Appendix C, not an independently exported platform execution log.
4. For future runs, save a contemporaneous manifest **before or immediately after execution**, including the exact submitted prompt (or immutable prompt commit plus any substitutions/wrapper text), platform, mode, exposed model, thinking settings, date, source restrictions, output link, and any retrieval limitations.
5. **A completed source audit is separate from run provenance.** A model's citation or assertion of inspection does not establish that an underlying authority was independently verified.
