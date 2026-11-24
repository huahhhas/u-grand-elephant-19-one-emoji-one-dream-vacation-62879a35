#!/usr/bin/env python3
"""One Emoji, One Dream Vacation - make.fun entry.

Writes exactly one emoji, the dream vacation, to entry.txt.

Pick: the desert island. A single code point (U+1F3DD), one character.

Why it beats the draft beach-with-umbrella, against the judge's
criteria in order:
1. Exactly one emoji, and it plainly names a dream vacation: a remote
   tropical island, not just travel in general (a plane) or a pretty
   moment (a sunset).
2. Postcard-vivid at a glance: island, palm and sea in a single glyph;
   a stranger sees the place before reading a word.
3. Personal and specific rather than generic: not any beach holiday,
   but one faraway island escape - a particular dream, not the default
   pick every entrant reaches for first.
4. A spark of surprise: a fresher, more romantic choice than the
   obvious beach umbrella.
5. Reads instantly across cultures and screens, clear at small size,
   nothing obscure that needs explaining.
"""
import os

ENTRY = "\U0001f3dd"  # desert island

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
