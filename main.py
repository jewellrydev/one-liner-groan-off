#!/usr/bin/env python3
"""Falling Out — entry for The One-Liner Groan-Off on make.fun.

Prints exactly one line (at most 140 characters): an original dad joke.
"""

LINE = "My calendar and I had a falling out: it keeps throwing dates at me I never agreed to."


def main() -> None:
    assert "\n" not in LINE
    assert len(LINE) <= 140
    print(LINE)


if __name__ == "__main__":
    main()
