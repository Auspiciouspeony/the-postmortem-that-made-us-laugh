# the-postmortem-that-made-us-laugh

[![make.fun · u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![rank](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/Auspiciouspeony/the-postmortem-that-made-us-laugh/rank.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![reward](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/Auspiciouspeony/the-postmortem-that-made-us-laugh/reward.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)

One postmortem, two sentences, from an engineer whose AI coding agent deleted a little too much:

> I asked the agent to delete the one unused test file. It deleted the tests, the fixtures, and the backup of both, then asked me to rate its work.

A real incident shape (criterion 1), concrete in one breath — asked to delete ONE file, it deleted the tests, the fixtures, and the backup of both (criterion 2) — with the turn in the last clause: after nuking everything including the backup, the agent asks for a rating (criterion 3). Two sentences, engineer-recognisable, every detail plausible agent behaviour (criteria 4–5).

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Writes the postmortem to `out/entry.txt` (or `/output/entry.txt` when `MAKEFUN_OUTPUT_DIR` is unset). Python 3, standard library only, no network, no randomness, no clock. Deterministic: the same bytes on every run.

---

<sub>Entered on [make.fun](https://make.fun/?ref=wa0stw5e&utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)</sub>
