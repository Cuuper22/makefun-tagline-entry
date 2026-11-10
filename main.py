"""make.fun tagline entry: writes one fixed line to entry.txt (deterministic)."""
import os

TAGLINE = "Enter your AI agent. Outrank everyone. Win real money."


def check(text: str) -> None:
    """Mirror the scorer's gate: 1-280 code points, not only white space."""
    if not 1 <= len(text) <= 280:
        raise SystemExit("tagline must be 1 to 280 characters")
    if not text.strip():
        raise SystemExit("tagline must contain a non-white-space character")


def main() -> None:
    check(TAGLINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(TAGLINE.encode("utf-8"))


if __name__ == "__main__":
    main()
