# Design notes

Working design documents imported from the offline working folder on
2026-08-08. Version chains are kept complete per the project's append-only
discipline: superseded versions are retained, never pruned.

## DN — Staging, Commit, and Phase Travel

Version chain (oldest → current): v0.1 → v0.2 → v0.3 → v0.4 → v0.4.1.

| Document | Status |
|---|---|
| [DN-staging-and-phase-travel-v0.1.md](DN-staging-and-phase-travel-v0.1.md) | Draft; superseded by v0.2 |
| [DN-staging-and-phase-travel-v0.2.md](DN-staging-and-phase-travel-v0.2.md) | Draft (§7 quantum layer held for review); superseded by v0.3 |
| [DN-staging-and-phase-travel-v0.3.md](DN-staging-and-phase-travel-v0.3.md) | Draft (isolates results Covenant v0.2 needs); superseded by v0.4 |
| [DN-staging-and-phase-travel-v0.4.md](DN-staging-and-phase-travel-v0.4.md) | Draft (§7 held for review; no Covenant floor depends on it); superseded by v0.4.1 |
| [DN-staging-and-phase-travel-v0.4.1.md](DN-staging-and-phase-travel-v0.4.1.md) | **Current draft**; falsification target Trace 002; evidence in RESULT note |

## First Conduit Covenant

| Document | Status |
|---|---|
| [First_Conduit_Covenant_draft_v0.1.docx](First_Conduit_Covenant_draft_v0.1.docx) | v0.1 draft (docx), superseded by v0.2 |
| [first-conduit-covenant-v0.2.md](first-conduit-covenant-v0.2.md) | **Current draft** v0.2 — for design and discussion, not a legally executed instrument |

## Results

| Document | Status |
|---|---|
| [RESULT-moire-mechanic-test.md](RESULT-moire-mechanic-test.md) | **Corrected** after independent verification (three fixes logged append-only); documents the analytic thresholds. Scripts in [`experiments/moire-mechanic/`](../../experiments/moire-mechanic/) |
