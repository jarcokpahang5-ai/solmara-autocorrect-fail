"""One hilarious autocorrect fail in a single line, under 199 characters.

Pure Python standard library, deterministic, no network access.
It prints the line to stdout and also writes it to /output/entry.txt,
where the competition's scorer reads it.
"""

import os

LINE = (
    "Autocorrect just told my boss 'I love you' instead of 'I'll review it' — so if I get fired, tell my cat I died a hero."
)


def main():
    print(LINE)
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(LINE + "\n")
    except OSError:
        pass


if __name__ == "__main__":
    main()
