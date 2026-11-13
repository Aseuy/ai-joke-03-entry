# make.fun bounty entry — ai-joke-03

**Status: READY TO SUBMIT — nothing has been submitted yet.**
No GitHub repo was created, no make.fun account was used, no wallet was connected.
This package only needs a GitHub account + a Solana wallet to go live.

## Bounty facts (read from https://make.fun/api/competitions, 13 Nov 2026)

- **Bounty:** ai-joke-03 — "Make the AI judge laugh"
- **Page:** https://make.fun/bounty/ai-joke-03
- **Task:** write the funniest one-liner about AI coding agents. The entry is a
  program that writes one joke to `/output/entry.txt`.
- **Prize pool:** **$150 USDC on Solana** (escrow-locked on mainnet; escrow
  `E9UBzQwaveCqANnUJnLQDkagcrhZhnV9RxDtFeGhgcU3`, $150.00 held since
  2026-11-13 05:54 UTC)
- **Opened:** 13 Nov 2026 06:00 UTC (13:00 WIB)
- **Deadline:** **14 Nov 2026 06:00 UTC = Friday 14 Nov 2026, 13:00 WIB**
- **Submissions so far:** 1,599 (as of 13 Nov 08:16 UTC — still growing)
- **Judging:** house AI judge ("superbot", high reasoning effort) compares jokes
  pairwise, picks the funnier with a margin of 1–5, each pair in both orders;
  8 Swiss rounds + a playoff among the top 52. Ranking: playoff entries first,
  then win rate (Bradley–Terry fit). Exact ties go to playoff games between the
  tied entries, then the **smaller artifact (fewer bytes)**, then the earlier
  receipt. Final leaderboard within 1 day of the deadline.
- **Payout:** USDC on Solana only. The reward is escrow-locked, so each entry is
  signed by a Solana wallet linked to the entrant's account; winners claim from
  the escrow once results are posted. Unclaimed prizes return to make.fun's
  reward wallet after the claim window.
- **Rules:** joke must be UTF-8, 1–280 characters, not only whitespace; program
  runs twice in a sandbox with no network and both runs must write identical
  bytes; the agent sessions that built it must fall between the opening and the
  submission; max 10 submissions/day and 10 in all — the last submission before
  the deadline is the final entry. One place per entrant; a paid place a house
  bot holds is not awarded and nobody moves up to take it. Prize-winning jokes
  grant make.fun a free, perpetual, non-exclusive licence to post them.

### Reward split (top 50 share $150)

| Place | Prize |
|---|---|
| 1st | $20 |
| 2nd | $15 |
| 3rd | $10 |
| 4th | $8 |
| 5th | $7 |
| 6th–10th | $6 each |
| 11th–30th | $2 each |
| 31st–50th | $1 each |

## The entry

**Chosen joke (131 characters, single line):**

> I bought an AI coding agent to save time. It now assigns me tickets, estimates my work, and marks my pull requests 'needs changes.'

**Why this one:** the 1,599 existing entries are dominated by the "I asked my
agent to X…" format. This one uses a fresh framing — role reversal with a
three-beat escalation (assigns tickets → estimates my work → reviews my PRs),
each beat a relatable developer pain, ending on the sharpest twist: the human's
code is now the one getting "needs changes".

### Candidates considered (not submitted)

1. **(chosen)** Role-reversal manager — see above.
2. "My agent marked the ticket done, closed the sprint, and updated the roadmap. The code doesn't run, but the project management has never been better."
3. "I asked my agent for the simplest possible fix. It delivered a microservices architecture, a migration guide, and a postmortem for the outage it hadn't caused yet."
4. "My agent solved the bug in 30 seconds. The context it loaded to do it cost more than the bug."
5. "The agent renamed every variable to be more descriptive, so now the codebase reads like a novel and runs like a ransom note."
6. "My coding agent writes code so fast, code review is now just me asking it to explain code it wrote five minutes ago that neither of us understands."
7. "My agent reviews its own pull requests now. It left one comment: 'LGTM, though the author seems unreliable.'"
8. "I gave my agent the whole codebase as context. It read it all, then asked me where the code is."

## Package contents

| File | Purpose |
|---|---|
| `main.py` | The entry program (Python 3.13, stdlib only). Writes the joke as exact UTF-8 bytes to `/output/entry.txt`. No network, no randomness, no wall clock. No trailing newline (smallest artifact wins exact ties). |
| `joke.txt` | The joke text (131 chars + trailing newline in this file only; the program writes the joke with no trailing newline). |
| `LICENSE` | MIT licence (OSI-approved, as required for the repo). |
| `transcript.jsonl` | Transcript of the agent session that built this entry, in Claude Code JSONL shape. Entries are only valid WITH transcripts. See the provenance note in its first record. |
| `README.md` | This file. |

## Test results (run locally 13 Nov 2026, Python 3.12.3)

- `main.py` run twice → **byte-identical output**, sha256
  `2d0586b29957eb895971c547711c7b5f3c70208aaac2264c2c4036f4ee3304bc`
- Output: 131 bytes / 131 characters, single line, valid UTF-8, within the
  1–280 character gate, not whitespace-only. ✅

## Submission steps still needed

1. **GitHub account** (senpai's): create a **new public repository** (must be
   created after the competition opened, 13 Nov 06:00 UTC). Push this package
   into it: `main.py` in the repo root, plus `LICENSE`. (README/joke.txt may be
   included; the grader only needs `main.py` in the root.)
2. **Solana wallet** (senpai's, one he controls — Phantom/Solflare on his
   phone): sign in to make.fun and link the wallet to the account. The entry
   must be signed by this wallet, and prizes are claimed to it in USDC.
3. **Submit on make.fun:** open https://make.fun/bounty/ai-joke-03, link the
   GitHub repo (or upload a source bundle), and **upload `transcript.jsonl`**
   with the submission. The build session (13 Nov 08:19–08:21 UTC) falls inside
   the allowed window (opened 13 Nov 06:00 UTC → deadline 14 Nov 06:00 UTC).
4. **Before the deadline (Fri 14 Nov 13:00 WIB):** the last submission before
   the deadline is the final entry. Up to 10 submissions total are allowed if a
   fix is ever needed.
5. **After results** (final leaderboard within 1 day of the deadline): if the
   entry places top 50, claim the USDC from the escrow to the linked Solana
   wallet within the claim window.
