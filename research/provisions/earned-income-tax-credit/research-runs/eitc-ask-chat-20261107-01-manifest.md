# Research-run manifest — EITC Ask-Chat run (retrospective)

> This is a retrospective, operator-reported record of an **interrupted, incomplete** run. Its contents and citations have **not** been independently source-audited. The run is not evidence of a completed Deep Research assignment.

## Run identity
- Run ID: `eitc-ask-chat-20261107-01` (repository-style identifier assigned retrospectively; not a provider-issued ID)
- Provision / code section: Federal Earned Income Tax Credit, 26 U.S.C. §32
- Research issue: Provision Project, EITC provision 2; GitHub issue #29
- Platform / product: https://ask-chat.ai/ (operator-reported)
- Research mode: User submitted the EITC Deep Research prompt; actual platform research mode `Not exposed`
- Model or model-selection setting: **“Gemiini 4 aragon”** (operator-reported selected display label; exact spelling, model identity and backend not independently verified)
- Status: `failed` — **interrupted / incomplete** (operator-confirmed). Uses the template's standard status value, while recording the more specific outcome and unknown technical cause.

## Prompt provenance
- Reusable prompt path and version: [`research/prompts/eitc-deep-research-v1.md`](../../../prompts/eitc-deep-research-v1.md), EITC 1.0. **Audited against current repository prompt:** the extracted text matches the canonical prompt content, except for **one additional trailing newline in the repository version**. This comparison does not establish the exact commit or platform-side acceptance at execution.
- Prompt Git commit SHA: `Not recorded`
- Exact submitted prompt file: [`eitc-ask-chat-20261107-01-prompt.md`](eitc-ask-chat-20261107-01-prompt.md) (extracted from the complete exported transcript; not independently verified against platform input history)
- Prompt capture: `Retrospective` (from export)

## Execution and outputs
- Started at (ISO 8601 with timezone): `Not recorded`
- Completed at (ISO 8601 with timezone): `Not applicable — interrupted before completion`
- Original unedited research output path: [`eitc-ask-chat-20261107-01-transcript.md`](eitc-ask-chat-20261107-01-transcript.md) (preserved complete operator-supplied export, consisting of prompt plus partial response)
- Extracted partial research output path: [`eitc-ask-chat-20261107-01-output-incomplete.md`](eitc-ask-chat-20261107-01-output-incomplete.md) (research response extracted for comparison; **truncated at source**, not by the conversion)
- Platform output link: `Not available` (operator reports that the free platform did not provide a share link)
- Source restrictions: `Not recorded`
- Platform-specific settings: Selected model display label above; other settings `Not exposed`
- Run settings capture: `Retrospective`

## Limitations and effort
- Unavailable or inaccessible sources: `Not independently assessed`
- Sources retrieved manually: `Not recorded`
- Interruptions or other limitations: **The platform stopped generating partway through its response. The supplied export contains everything the platform produced, not an accidentally incomplete copy or a cut-off during Markdown conversion.** The response terminates mid-row of the current-law tax-year applicability table, in the childless-worker eligibility entry. Sections that would have followed were not generated. The generated portion must not be described as a completed report or used to infer missing conclusions.
- Approximate setup / execution / manual-intervention time: **Approximately one minute** of platform run time (operator estimate, not precisely measured). Setup and manual-intervention time `Not recorded`.

## Notes
- Do not mistake the **interruption** for lack of relevant evidence; ungenerated sections were not researched in the visible output.
- The report's generated citations and claims require a separate independent source audit.
- Keep the original transcript unchanged; annotate limitations in this manifest and any comparison rather than editing the historical output.

## Integrity and comparability
- The original uploaded `provision-project-eitc-32-deep-r.txt` and the `transcript.md` conversion were confirmed byte-identical locally (SHA-256: `2863d08d31df76c9c66567aa5de04edc693019ef88ff9ce9071475b1bd7ecf7a`). The extension changed from `.txt` to `.md`; its contents did not.
- The separate prompt and partial-response files are **derived extracts** of that export. They are intended for convenience; the complete transcript is authoritative for what was received. **Reconstruction check passed:** the complete transcript equals the exact string `You: ` + extracted prompt + `\nAsk-Chat: ` + extracted partial response.
- This submission does not establish that every phrase of the prompt was accepted by the remote provider, nor that it executed the requested research mode. It only records the visible exported transcript and operator account.
- The run was **interrupted in the middle of generation**; the exact technical reason for interruption is **not known**. Do not call it a provider error, timeout, or safety refusal without supporting evidence.
- A true like-for-like comparison against completed ChatGPT/Gemini research requires separately labeling this run **incomplete** and avoiding quantitative completeness/ranking claims based on missing sections.
- No publication-ready research record or independent source audit is implied by archiving the output.
