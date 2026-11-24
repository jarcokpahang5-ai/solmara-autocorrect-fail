"""One hilarious autocorrect fail in a single line, under 199 characters.

Pure Python standard library, deterministic, no network access.
It prints the line to stdout and also writes it to /output/entry.txt,
where the competition's scorer reads it.
"""

import os

# Competition limit for the single autocorrect fail.
MAX_CHARS = 199

LINE = (
    "Autocorrect just told my boss 'I love you' instead of 'I'll review it' — so if I get fired, tell my cat I died a hero. It also CC'd HR."
)

# Guard: the entry must stay inside the competition's character limit.
assert len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars, over the {MAX_CHARS} limit"


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
