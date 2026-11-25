# Sum up 26 November's world news in one image

[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/zhumy0323-hue/news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/zhumy0323-hue/news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

This is a single 1024x1024 front page, **THE THURSDAY PAPER**, that sums up
the world news of Thursday 26 November 2026 in one image: 36 stories from
7 continents across 16 fields, laid out as a newspaper you can read at a
glance.

## What's on the page

- **Three leads.** Russia's own figures put the Ukraine war death toll at
  nearly 500,000; North Korea orders the Swiss diplomatic office shut
  within 48 hours; Lebanon opens its second airport at Kleiat next month.
- **Ten illustrated small stories**, each carrying a verification badge —
  CONFIRMED, OFFICIAL or REPORTED — so the reader can see at a glance how
  solid each item is.
- **Twenty-three short items** in the also-listed column, one line each.
- **A UTC timeline strip** showing first-report times, a figures strip,
  and a region bar breaking the 36 stories down by continent.
- **A world map with 14 numbered pins** marking where the stories happened.
- **A DATE CHECK box** separating today's news from earlier stories that
  look similar but belong to 24 or 25 November, plus a footer legend
  explaining the badges and pins.
- The masthead notes Constitution Day in India and the 18th anniversary
  of the 26/11 Mumbai attacks.
- The finished image is a single 1024x1024 PNG, 178,745 bytes, well under
  the 1 MiB limit. The drawing is original front-page art made for this
  field: death-toll bars, an expulsion door and a runway scene for the
  leads, and small slot-sized illustrations for the ten small stories.

## Running it

```sh
python3 main.py
```

The script reads `entry.png.b64` from this directory, decodes it and
writes the image to `/output/entry.png` (creating the directory if
needed). It uses only the Python standard library, needs no network, and
prints the byte count and SHA-256 of the image. The SHA is checked
against the expected value, and the script exits with an error if it
does not match. Running it twice writes byte-identical output. The
bounty entrypoint is `python3.13`.

## A note on dates

The image was built on 26 November at about 07:00 CST, before the UTC
day began, so the timeline strip shows first-report UTC times — which
fall on 25 November UTC (04:26–14:32). Every story in the image comes
from the 26 November daily news summaries; none is dated 24 November
or earlier.

<!-- Entry for the make.fun news-image-20261126 bounty ($100, free entry). -->
