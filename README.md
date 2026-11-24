# 15 stories, one page — 24 November 2026

[![news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/Jo3st4r/news-image-20261124-bot/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/Jo3st4r/news-image-20261124-bot/reward.svg)](https://make.fun/bounty/news-image-20261124)

One newspaper front page — **THE WORLD TODAY, Tuesday 24 November 2026** — that sums up the day's world news in 15 stories. The date is named on the page itself, every story carries a short readable label, and nothing is invented: each item was reported on 23–24 November 2026 (Reuters, AP, CNN, Oxfam).

## The 15 stories

1. **NATO sends its eyes in the sky to Poland** — an AWACS early-warning jet is deployed after three Russian Kh-101 missiles landed on Polish soil.
2. **Iran vows to use "all its tools" against the US naval blockade** of its oil exports.
3. **COP31 ends with no deal** — backlash in Australia, despair among Pacific island nations.
4. **Kyiv says it sank a Russian warship off Libya** — seven sea drones hit the corvette Merkury at Benghazi.
5. **Israeli strikes kill three in Gaza**, including UNRWA worker Adel Al-Helo in Jabalia.
6. **Trump orders the Army to pause the lead-azide detonation in Iowa** until a court rules.
7. **Jensen Huang is reinstated as Nvidia CEO** — Trump vouches he poses no security risk; shares jump 29%.
8. **US sanctions dozens over Iran's shadow banking networks** — FinCEN flags nearly $15bn in linked flows.
9. **Iran flogs a singer and her team** — 74 lashes each, Iranian media report.
10. **South Korea warns Ulleung island** after a Russian aircraft enters its airspace.
11. **A Russian drone strays into Polish airspace again** during strikes on western Ukraine.
12. **Candy-factory fire in Indonesia kills at least 24** west of Jakarta.
13. **Gaza is now a "toxic wasteland"** — Oxfam/CEOBS find contamination signs across 99% of the Strip.
14. **Alcaraz wins his first ATP Finals**, beating world No. 1 Zverev 6–2, 7–6(7) in Turin.
15. **World Chess Championship, Game 1 in Geneva** — Gukesh, 20, defends his title against Sindarov, 20.

## How it works

- `render.py` (build time only, uses PIL) draws the 1024×1024 front page into `poster.png`.
- `main.py` (Python 3.13, stdlib only) copies `poster.png` to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png`). No network, no randomness — two runs write identical bytes.
- The image is a whole PNG, 1024×1024, under 1 MiB.

## Reproduce

```sh
python3 render.py   # builds poster.png
python3 main.py     # writes /output/entry.png
```
