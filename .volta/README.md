# .volta/

This folder is Volta's per-project memory. It was created automatically the
first time Volta opened this project, and most of it is meant to be
committed to git so the whole team shares the same project knowledge.

```
memory/
  board_profile.json   — which board/target this project is for (set on first run)
  notes.md              — free-form project notes Volta accumulates over time
  embedder_index/       — semantic codebase search cache (gitignored, regenerable)
  bootloop_state.json   — tracks repeated failure loops (gitignored, local-only)

history/                 (gitignored — local chat transcripts)
  session.json           — current/last session, restored on next `volta`
  history.json           — index of past sessions (titles + dates)

skills/                  — drop-in skill folders, each with a SKILL.md
  <skill-name>/SKILL.md

plans/
  todos.json             — TODO tracker, scoped to this project
  active_plan.json       — the current multi-step plan, if any
  architecture_log.md    — architecture decision records (ADRs)
```

Delete this folder any time to reset Volta's memory of this project — it
will be recreated automatically the next time Volta opens it.
