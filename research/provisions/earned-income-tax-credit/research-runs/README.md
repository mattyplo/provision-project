# EITC (§32) — research run manifests

Related: [Provision 2 issue](https://github.com/mattyplo/provision-project/issues/29) and [AI comparison issue](https://github.com/mattyplo/provision-project/issues/9).

Create **one manifest per independent platform run** using [the shared template](../../../templates/research-run-manifest.md). Save the exact submitted prompt as a separate UTF-8 file alongside each manifest, including any provision-specific substitutions and wrapper instructions. Preserve original research reports without editing.

Suggested filenames:
- `eitc-chatgpt-YYYYMMDD-01-manifest.md`
- `eitc-chatgpt-YYYYMMDD-01-prompt.md`
- `eitc-gemini-YYYYMMDD-01-manifest.md`
- `eitc-gemini-YYYYMMDD-01-prompt.md`

**No EITC Deep Research run is represented as completed by this scaffolding.** Fill run settings and timestamps contemporaneously when each run is actually performed. Do not invent exposed model identifiers. Record any source retrieval failures and manual interventions so the next retrospective can measure friction.

Workflow: (1) copy template; (2) record run ID and intended settings; (3) save verbatim submitted prompt; (4) run independently; (5) immediately record actual execution details and report location; (6) preserve raw output; (7) separately compare, verify and audit claims.
