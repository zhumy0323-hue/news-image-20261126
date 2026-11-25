# The Thursday Paper — 26 November 2026 (v2)

[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/zhumy0323-hue/news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/zhumy0323-hue/news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

One image that sums up Thursday 26 November 2026's world news:
36 stories from 7 continents, laid out as a newspaper front page.
This is version 2 of the entry — the same front-page family as v1,
rebuilt at about 10:35 CST with the morning's new developments.

## What changed in v2

- **New leads:** a fuel tanker fire kills 31 on a Cairo ring road;
  Ukraine strikes the Savasleyka air base, damaging five jets;
  the Bank of Korea raises its rate to 3.25% on an AI export boom.
- **New smaller stories:** a second US judge blocks the birthright
  citizenship order; judges urge dropping a Netanyahu bribery case;
  34 nations call on Russia to halt riot-gas use; the Murmansk
  governor is held on corruption charges; a Houthi drone hits
  Riyadh's tallest tower again; Australia passes an online safety
  law with fines of up to 5% of revenue.
- **Kept from v1** (still Thursday's news): Russia's own death toll
  near 500,000, the North Korea expulsion of the Swiss envoy, the
  Malaysia–Google suit and the Bangladesh garment wage rise.
- The timeline strip now mixes late-25-Nov UTC and early-26-Nov UTC
  first-report times, because v2 was built after the UTC day began.
  The DATE CHECK box still lists what was left out as earlier news,
  including the Duran Duran guitarist's death (23 Nov).

## What's on the page

- Masthead: Thursday 26 November 2026, Constitution Day in India,
  18th anniversary of the 26/11 Mumbai attacks.
- Three leads with drawn art, ten smaller stories with art and a
  CONFIRMED / REPORTED status badge, and 23 more stories in the
  also-list — 36 stories in total, across 13 fields.
- A first-reported timeline, a figures strip, a region bar
  (Europe 7, Asia 10, Middle East 5, Africa 6, N. America 4,
  S. America 2, Oceania 2), a world map with 14 numbered pins,
  a DATE CHECK box and a sources footer.

## Run it

```bash
python3 main.py
```

This decodes `entry.png.b64` into `/output/entry.png` (1024×1024
PNG, 181,462 bytes) and verifies its SHA-256 before writing.
Only the Python standard library is used, so the output is
identical on every run.

Entrypoint: `python3 main.py` — no arguments, no setup step.

## Sources

Reuters, AP, AFP, BBC, UN News, TOI, Al Jazeera, RFE/RL —
all stories are from the 26 November 2026 daily summaries.
Bounty: https://make.fun/bounty/news-image-20261126
