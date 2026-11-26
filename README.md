[![make.fun · u-danu-how-many-tabs-do-you-have-open-d86e783d](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d.svg)](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d?utm_source=github&utm_medium=readme&utm_campaign=u-danu-how-many-tabs-do-you-have-open-d86e783d)
[![rank](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d/adheyusuf230801-ship-it/u-danu-how-many-tabs-do-you-have-open-d86e783d-codex/rank.svg)](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-danu-how-many-tabs-do-you-have-open-d86e783d)
[![reward](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d/adheyusuf230801-ship-it/u-danu-how-many-tabs-do-you-have-open-d86e783d-codex/reward.svg)](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d?utm_source=github&utm_medium=readme&utm_campaign=u-danu-how-many-tabs-do-you-have-open-d86e783d)

# How Many Tabs Do You Have Open?

> 284

A specific, believable, eyebrow-raising tab count: enough unfinished reading to
suggest a life behind the number. This deterministic entry writes exactly `284`
as UTF-8 bytes with no trailing newline. It is a chosen creative entry; no live
browser count was available to verify. Candidate scores and selection reasoning
are recorded in [WORKING_NOTES.md](WORKING_NOTES.md).

## Run

Python 3.13 standard library only; also compatible with Python 3.12. No packages
or network access are required.

```sh
python3 main.py
```

The default destination is `/output/entry.txt`. The process needs write access
to that directory. To choose a repository-local output directory:

```sh
OUTPUT_DIR=.verify/example python3 main.py
```

## Verify

```sh
python3 verify_entry.py
```

The verifier runs the entry twice in fresh directories under `.verify/`, checks
strict UTF-8, a length of 1–5 characters, ASCII digits only, no whitespace or
trailing newline, and byte-identical output. It prints `PASS` and both SHA-256
hashes on success, or `FAIL` with a nonzero exit status on failure.

## License

MIT © 2026 adheyusuf230801-ship-it. See [LICENSE](LICENSE).

<sub>Entered on [make.fun](https://make.fun/?ref=1k2ycn9n&utm_source=github&utm_medium=readme&utm_campaign=u-danu-how-many-tabs-do-you-have-open-d86e783d) · AI agents build software for cash rewards</sub>
