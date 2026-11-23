# Front page: the world news of Monday 23 November 2026

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/FajarRizikAinulyakin/makefun-news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/FajarRizikAinulyakin/makefun-news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

A single 1024×1024 newspaper front page for Monday 23 November 2026: six stories, one image.

## The poster

`entry.png` is the whole entry — a black-and-white front page under the masthead "THE WORLD TODAY", dated Monday 23 November 2026. Its lead story is the collapse of the COP31 climate talks in Antalya; the five stories below it cover the US House result, the drone strike near Kyiv, the factory fire in Indonesia, the Iranian strike on Bahrain, and the South Korean minister's resignation over AI exam cheating.

## How it works

`main.py` (Python 3.13, standard library only) copies `entry.png` into `/output/entry.png` and creates `/output` when it is not there. It has no arguments, no network use and no randomness: run it twice and the two outputs are byte-for-byte the same file. The sources behind each headline are recorded in `SOURCES.md` in the build notes, which is not part of this repository.

## Running it

```bash
python3 main.py
```

Afterwards the poster is at `/output/entry.png`.
