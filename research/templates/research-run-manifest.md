# Research run manifest — template

> Copy once per **individual research run**, before starting it. Preserve this file in the provision folder. Fill unknown fields with `Not recorded` or `Not exposed`; never infer model IDs. Do not overwrite the manifest for a rerun—create a new run ID.

## Identity
- Run ID: `<provision>-<platform>-<YYYYMMDD>-<sequence>`
- Provision name:
- Code citation and provision boundary:
- Related research issue:
- Operator:
- Status: `planned | running | completed | failed | cancelled`

## Prompt provenance
- Reusable prompt path:
- Prompt version:
- Prompt commit SHA (immutable reference):
- Exact submitted prompt path (verbatim, including substitutions/wrappers):
- Exact submitted prompt SHA-256 (optional, if computed):
- Differences from reusable prompt: `None | describe`
- Prompt submission capture: `contemporaneous | retrospective | not recorded`

## Execution provenance
- Platform / product:
- Research mode:
- Exposed model or model selection:
- Individual model IDs: `Not exposed` if unavailable
- Thinking/reasoning settings:
- Other research settings:
- Source/domain restrictions:
- Start timestamp (ISO 8601, timezone):
- End timestamp (ISO 8601, timezone):
- Run metadata capture: `contemporaneous | retrospective`

## Outputs and access
- Original unedited report path:
- Original platform output URL (if available):
- Source/citation export path (if available):
- Retrieval/access limitations:
- Manual source retrievals needed:
- Run failure or interruption notes:

## Verification boundary
- Research output is **unverified input**, not an audited provision record.
- Claim/source ledger path:
- Independent source audit path:
- Reviewer / review date:
- Open questions:

## Process measurement (approximate)
- Setup minutes:
- Research execution minutes:
- Manual intervention minutes:
- Notes on friction and opportunities to automate:
