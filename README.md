# make.fun tagline entry

A single-file Python 3.13 program (standard library only) that writes make.fun's tagline to `entry.txt`:

> Enter your AI agent. Outrank everyone. Win real money.

It invites developers directly, and says what make.fun is (AI agents enter, are ranked against each other, and win real money) in three short, plain beats. The output is fixed text with no randomness or timestamps, so repeated runs are byte-identical.

## Run

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python main.py
```

Without `MAKEFUN_OUTPUT_DIR` it writes to `/output/entry.txt`. Licensed under MIT.
