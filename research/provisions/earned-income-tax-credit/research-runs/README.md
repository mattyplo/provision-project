# EITC (§32) — independent research run manifests

Related: [Provision 2](https://github.com/mattyplo/provision-project/issues/29), [AI comparison](https://github.com/mattyplo/provision-project/issues/9).

The canonical, platform-agnostic schema is [research-run-manifest.schema.json](../../../templates/research-run-manifest.schema.json). Maintain **one JSON manifest per individual run**, not one per platform template. `platform.settings` accepts provider-specific options without altering shared fields. Schema version is explicit; older records must not be silently reinterpreted.

The two `*-planned-01-manifest.json` files are **planning stubs, not completed runs**. Before each run, record the actual model/mode/settings, version and commit of the reusable prompt, and save the **verbatim submitted prompt** (including substitutions and wrapper text) to a sibling `*-prompt.md`. Use a new run ID for every rerun. Immediately afterward, record timestamps, raw unedited output path, inaccessible sources, manual retrievals, and approximate time spent. Use `null` for unavailable or not-yet-known values; don't infer model IDs.

Suggested executed filename: `eitc-<platform>-YYYYMMDD-01-manifest.json` (and corresponding `-prompt.md` and raw report). Do not rename a planning stub into a completed run without updating its run ID and populating actual provenance.

Validate from repository root with:

```sh
python -m pip install jsonschema
python scripts/validate_research_manifests.py
```

Validation checks structure and basic completion requirements, **not** truth of research claims or whether cited sources were inspected. Source/claim verification remains a separate human-reviewed workflow (Improvement #2).
