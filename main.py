"""The joke about the demo (make.fun).

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
"""

import os

# Punchline structure: setup promises a one-line fix, then the escalation
# ("a refactor, a migration, and a README") undercuts it — the agent did
# everything except the one line asked for.
JOKE = (
    "I asked my agent for a one-line fix; it shipped a refactor, "
    "a migration, and a README explaining why the one line was "
    "never the problem."
)


def main() -> None:
    # The joke must be a single non-blank line, 1-280 chars (one-line format).
    if not JOKE.strip() or not 1 <= len(JOKE) <= 280:
        raise SystemExit("JOKE must be 1-280 non-blank characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
