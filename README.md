# Tell a Whole Story in 32 Characters

Competition: `u-xvader-tell-a-whole-story-in-32-characters-f86dd978`
("Tell a Whole Story in 32 Characters", $2, program/v1).
Deadline: 2026-11-26T17:25:00Z (2026-11-27 01:25 CST).

## Entry

```
Ex took the dog, I kept WiFi
```

28 characters (including spaces and punctuation), no trailing newline —
well inside the 1–32 character gate.

## Why this story

The brief is not a generic micro-story: the entry must read as a **Wi-Fi
network name** — a joke a stranger gets at a glance in a phone's network
list, that also implies a whole story. The judge weighs, in order: Wi-Fi
name fit (≤32 chars), joke landing on first read, how much story it
carries, freshness, tight wording.

This line has a full arc in one breath:

- **Setup / character:** a breakup — "Ex" and "I".
- **Turn:** the ex took the dog (the loss that should hurt most).
- **Punchline / ending:** the narrator kept the WiFi — the consolation
  prize is bragged about as if it were the win, flipping the usual
  priorities (dog vs. internet) for the laugh.

It avoids the stock Wi-Fi jokes ("Pretty Fly for a Wi-Fi", "FBI
Surveillance Van", "It Burns When IP", password gags) and is original —
not a retelling of any known flash-fiction line (e.g. the famous
six-word baby-shoes story is deliberately not used).

## How it runs

`main.py` (Python standard library only, deterministic) writes the story
to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), with no trailing
newline, then reads the file back and asserts byte-for-byte equality and
the exact 28-character / 28-byte length.
