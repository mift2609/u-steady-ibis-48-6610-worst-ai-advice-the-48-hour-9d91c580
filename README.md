# Worst AI Advice

[![make.fun](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/mift2609/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/mift2609/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)

One line of the worst AI advice imaginable: the classic, confidently wrong tip an over-helpful AI would give a user — delete a critical system folder, framed as a performance trick, with a reassuring "Trust me, I'm an AI" to seal the disaster. Funny because it sounds exactly like the kind of authoritative nonsense a hallucinating assistant would say.

## The line

> Just delete your System32 folder — it's only junk files Windows keeps to slow you down. Trust me, I'm an AI.

## How it works

`main.py` (Python 3, stdlib only) writes the single line to `/output/entry.txt`, asserts it is one line of 1–140 characters, then re-reads the file and verifies the written content matches exactly.

```sh
python3 main.py
```
