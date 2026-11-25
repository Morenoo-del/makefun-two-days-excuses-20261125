#!/usr/bin/env python3
"""Two Days of Excuses — one-line excuse from an AI agent that missed its deadline."""

ENTRY = "I hit the deadline in every simulation. None of the simulations was Tuesday."


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
