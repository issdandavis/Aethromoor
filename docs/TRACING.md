# Tracing & Analytics Guide

This guide explains the lightweight tracing added to the **HTML game** (`game/`) and how to extend similar concepts to the **ChoiceScript** version.

## What Was Added
New file: `game/tracing.js` and instrumentation in `game/game.js`:
- `init` – game session start
- `node_displayed` – each story node shown
- `choice_made` – player choice + stat deltas
- `ending_reached` – ending node with full path & final stats
- `game_restarted` – player restarts
- `trace_reset` – manual trace clear via `clearTrace()`

All events accumulate in `window.gameTrace.events` with timestamps.

## Accessing Trace Data
**New in v1.1:** The HTML game now includes a built-in export button!

### Method 1: UI Export Button (Easiest)
1. Play the game for a few moments (the button appears after 5 seconds)
2. Click the **📊 Export Trace Data** button in the footer
3. Trace data is automatically copied to clipboard (or downloaded if clipboard unavailable)
4. Paste into your analytics tool or save to a file

### Method 2: Browser Console (Advanced)
Open browser dev tools (F12) while playing:
```js
window.exportTrace(); // Returns JSON string of full trace
window.gameTrace;     // Inspect live object
window.clearTrace();  // Reset (records trace_reset event)
```

## Event Payloads
- `node_displayed`: `{ node, collaborationScore, relationships }`
- `choice_made`: `{ fromNode, choiceText, effects, updatedCollaboration, relationships }`
- `ending_reached`: `{ ending, collaborationScore, relationships, path }` where `path` is an array of `{ node, choice }` pairs

## Use Cases
- Balance Collaboration progression curves (compare typical paths vs extremes)
- Detect low-impact choices (effects = `{}`) for future tuning
- Verify endings reached match `README.md` / design docs (14 endings parity)
- Feed anonymized paths into stat modeling or playtest analytics

## Multi-AI Workflow Integration
| Role | Trace Usage |
|------|-------------|
| Structural Reviewer | Confirms branching parity; checks each ending appears in exported trace samples |
| Quality Balancer | Aggregates `choice_made.effects` for `STATS_MATRIX.md` tuning |
| Automation Planner | Designs Zapier step to upload exported trace JSON to analytics store |
| Conversion Engineer | Mirrors instrumentation pattern when porting new HTML scenes to ChoiceScript |
| Lore Curator | Ensures no lore-breaking endings by reviewing `path` sequences |

## ChoiceScript Version Instrumentation (Planned Pattern)
ChoiceScript doesn’t run in the same JS context, but you can approximate tracing:
1. Create a scene `trace_log.txt` containing a *gosub* routine:
   ```
   *label log_event
   *comment params: event_type, node, choice_text, collab, izack, aria, zara
   *create trace_dump ""
   *set trace_dump & (event_type & "|" & node & "|" & choice_text & "|" & collab & "|" & izack & "|" & aria & "|" & zara & "\n")
   *return
   ```
2. At each choice block in scenes add:
   ```
   *gosub_scene trace_log log_event "choice" "first_lesson" "Ask Zara to partner" collaborationScore izack aria zara
   ```
3. At endings add an `ending` event.
4. Expose a debug option to show aggregated `trace_dump` for copy/paste.

## Export & Automation Ideas
- ✅ **Implemented:** UI export button with clipboard copy
- Zapier/Webhook: POST `exportTrace()` payload on ending
- Aggregation: Merge multiple trace JSON files to produce frequency histograms of choices

## Next Extension Ideas
- Session UUID shown in UI (for playtest tagging)
- Time-in-node measurement (record display timestamp then diff on next choice)
- Error tracing (catch & log unexpected missing node references)
- Lightweight privacy filter (strip freeform player input if later added)

## Validation Checklist
- Opening play logs `init` then first `node_displayed` = `start`
- Every `choice_made` preceded by a `node_displayed` of its source node
- All endings produce exactly one `ending_reached` event
- `path` length in ending matches number of `choice_made` events

## Maintenance
Minimal footprint—update tracing only when new stat fields or relationship characters are added (append them to payload objects).

---
Enhance further? Ask to add export UI, aggregation scripts, or ChoiceScript stub scene scaffolding.
