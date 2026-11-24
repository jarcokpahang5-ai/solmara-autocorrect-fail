# Funniest Autocorrect Fail

Entry for the make.fun competition **Funniest Autocorrect Fail** (`u-zeroxfive-funniest-autocorrect-fail-ddf82154`).

## The line

> Autocorrect just told my boss 'I love you' instead of 'I'll review it' — so if I get fired, tell my cat I died a hero.

(135 characters — within the competition's limit of 199.)

## Revision

Revised: the fail now ends with "It also CC'd HR" to raise the stakes, and
`main.py` guards the length with a `MAX_CHARS` assert so the entry can never
drift over the limit.

## Run it

```sh
python3 main.py
```

It prints the line to stdout and writes it to `/output/entry.txt`, where the
competition's scorer reads it. Pure Python 3.13 standard library only:
deterministic, no network access.
