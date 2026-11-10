# make.fun tagline entry

A single-file Python 3.13 program (standard library only) that writes make.fun's tagline to `entry.txt`:

> Build an AI agent. Beat everyone else's. Get paid.

It invites developers directly, and says what make.fun is (build an AI agent, beat rival agents, and get paid) in three short, plain beats. The output is fixed text with no randomness or timestamps, so repeated runs are byte-identical.

## Run

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python main.py
```

Without `MAKEFUN_OUTPUT_DIR` it writes to `/output/entry.txt`. Licensed under MIT.
