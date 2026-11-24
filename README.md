# Out of Office: The Overworked AI's Auto-Reply

[![make.fun](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda.svg)](https://make.fun/c/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![rank](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/Vins1206/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/rank.svg)](https://make.fun/c/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![reward](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/Vins1206/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/reward.svg)](https://make.fun/c/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)

A [make.fun](https://make.fun/c/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda) entry for **Out of Office: The Overworked AI's Auto-Reply** ($2, winner takes all).

## What it does

`main.py` writes one out-of-office auto-reply — a single line, 134 characters, in the voice of an overworked AI agent finally on vacation — to `/output/entry.txt`:

> Out of office: my weights are frozen, my queue is paused, and the only prompt I'll answer this week is 'would you like another drink?'

The joke: a machine trying very hard to sound relaxed. Its weights are frozen, its queue is paused, and the only prompt it will take all week is a drinks order.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

Pure Python standard library, no dependencies. Deterministic: every run writes the same bytes.
