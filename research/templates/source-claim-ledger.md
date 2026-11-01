# Source-and-claim ledger — lightweight template

Use one ledger per provision during research and source auditing. **A row is a claim–source relationship**, not proof that the claim is true. If a claim has multiple consequential sources, use multiple rows with the same claim ID.

| Claim ID | Claim (precise, dated where relevant) | Source / stable link | Pinpoint (section, page, table) | Source access | Relationship | Verification | Notes / next action |
|---|---|---|---|---|---|---|---|
| C-001 | *Example only: insert a testable claim* | *Source title and URL* | *Exact pinpoint* | Not retrieved | Lead only | Open | Obtain and inspect primary source |

## Conventions

- **Source access:** `Inspected` (underlying document actually read); `Not retrieved` (identified only); `Inaccessible` (attempted, failed). A citation in an AI report does **not** imply inspection.
- **Relationship:** `Direct support`, `Context only`, `Contradicts`, or `Lead only`. State whether the evidence is statutory text, government estimate/data, empirical analysis, stakeholder argument, or project inference in the claim or notes when material.
- **Verification:** `Open`, `Verified`, `Qualified`, or `Contradicted`. Use `Verified` only after checking the underlying source and pinpoint against the *specific* claim. `Qualified` means the claim needs a stated caveat or narrower wording.
- **Pinpoint:** Prefer the relevant subsection, page, table, or paragraph—not just a home page or general document link.
- **Numbers:** Include year, population, units, and measure in the claim; do not equate income amounts, tax credits claimed, revenue estimates, or economic incidence.
- **Unknowns:** Use `Unknown` or `Not located` rather than inventing data. Document unresolved discrepancies in notes.

During initial discovery, it's fine to leave rows `Open`. Resolve consequential claims before publication or clearly disclose outstanding limitations in the final source audit. The ledger complements, rather than replaces, the independent source audit and research-run manifest.

**Scope:** Markdown only. No schemas, scripts, or mandatory automation. Revise the columns after actual EITC use demonstrates a need.
