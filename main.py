#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters entry for make.fun.

Writes one original Wi-Fi network name to entry.txt: a breakup told in
28 characters. The ex took the dog; the narrator kept the WiFi. The
joke is the priority flip -- losing the dog hurts, but keeping the
network is the consolation prize worth bragging about in a network
list. Deterministic, standard library only: the same bytes every run.
"""

import os

STORY = "Ex took the dog, I kept WiFi"


def main() -> None:
    # Enforce the competition gate locally: 1 to 32 characters, and no
    # trailing newline -- the gate counts every character in the file.
    assert len(STORY) == 28, "STORY must be exactly 28 characters"
    assert 1 <= len(STORY) <= 32, "STORY must be 1-32 characters"
    assert "\n" not in STORY, "STORY must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(STORY)
    # Read back and verify the written bytes match exactly.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == STORY, "entry.txt does not match STORY"
    assert len(written.encode("utf-8")) == 28, "entry.txt must be 28 bytes"


if __name__ == "__main__":
    main()
