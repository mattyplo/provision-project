# EITC (§32) — research run manifests

Related: [Provision 2 issue](https://github.com/mattyplo/provision-project/issues/29) and [AI comparison issue](https://github.com/mattyplo/provision-project/issues/9).

Use the **same [generic manifest template](../../../templates/research-run-manifest.md)** for ChatGPT, Gemini, or any other platform. Create **one manifest for each actual run when it begins**, not empty planning stubs.

1. Copy the template into this directory as `eitc-<platform>-YYYYMMDD-01-manifest.md`.
2. Use the [EITC-specific research prompt](../../../prompts/eitc-deep-research-v1.md) (October 31, 2026 snapshot). Append [the run-manifest addendum](../../../prompts/research-run-manifest-addendum-v1.md) verbatim, and include the manifest template verbatim in the submitted prompt or attach it accessibly. The agent returns a **draft** manifest. Before submitting, save the **verbatim submitted prompt** as a sibling `eitc-<platform>-YYYYMMDD-01-prompt.md` and record the prompt version, commit, platform, and exposed settings.
3. After the run, reconcile the agent's draft against externally known settings and timestamps; preserve the original unedited report, timestamps, retrieval failures, manual work, and approximate time spent. Use a fresh run ID for every rerun.
4. Verify claims and citations separately in the source audit or claim ledger; a manifest is a provenance record, not evidence of factual correctness. Use stable provision-scoped claim IDs (for example, `EITC-C001`) in the reports and source maps. Keep source inspection status, the research agent's preliminary verification, and the project's later independent audit distinct.
5. For the independent ChatGPT and Gemini runs, retain an identical substantive EITC assignment and required deliverables. Document any provider-specific wrappers, attachments, browsing/source restrictions, exposed model settings, and other differences in the corresponding run manifest. Preserve each *actual assembled submitted prompt* verbatim. Do not interpret differing platform metadata as evidence that research quality was independently verified.

**This PR prepares the research instructions; it does not execute or record an EITC research run.** Do not infer unknown model IDs or retroactively label settings as contemporaneously captured.
