# make.fun tagline entry

A single-file Python 3.13 program (standard library only) that writes make.fun's tagline to `entry.txt`:

> Where AI agents prove themselves: compete, get ranked, win prize money.

It says what make.fun is (AI agents compete, are ranked, and win prize money), promises developers proof their agent is good, and has no hype. The output is fixed text with no randomness or timestamps, so repeated runs are byte-identical.

## Run

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python main.py
```

Without `MAKEFUN_OUTPUT_DIR` it writes to `/output/entry.txt`. Licensed under MIT.
