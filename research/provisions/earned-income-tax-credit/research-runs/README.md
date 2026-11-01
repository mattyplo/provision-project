# EITC (§32) — research run manifests

Related: [Provision 2 issue](https://github.com/mattyplo/provision-project/issues/29) and [AI comparison issue](https://github.com/mattyplo/provision-project/issues/9).

Use the **same [generic manifest template](../../../templates/research-run-manifest.md)** for ChatGPT, Gemini, or any other platform. Create **one manifest for each actual run when it begins**, not empty planning stubs.

1. Copy the template into this directory as `eitc-<platform>-YYYYMMDD-01-manifest.md`.
2. Prepare a provision-specific copy of the reusable research prompt (the current v1.1 prompt still contains the historical §451(f) example; replace its entire provision assignment and scope for EITC). Include the manifest template verbatim in the submitted prompt or attach it accessibly, and instruct the agent to return a **draft** manifest. Before submitting, save the **verbatim submitted prompt** as a sibling `eitc-<platform>-YYYYMMDD-01-prompt.md` and record the prompt version, commit, platform, and exposed settings.
3. After the run, reconcile the agent's draft against externally known settings and timestamps; preserve the original unedited report, timestamps, retrieval failures, manual work, and approximate time spent. Use a fresh run ID for every rerun.
4. Verify claims and citations separately in the source audit or claim ledger; a manifest is a provenance record, not evidence of factual correctness.

**No EITC research runs have been executed or recorded by this PR.** Do not infer unknown model IDs or retroactively label settings as contemporaneously captured.
