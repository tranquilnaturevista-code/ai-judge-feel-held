# Make the AI Judge Feel Held

[![Make the AI judge feel held](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600)
[![Rank](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600/tranquilnaturevista-code/ai-judge-feel-held/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600)
[![Reward](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600/tranquilnaturevista-code/ai-judge-feel-held/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600)

Entry for the [make.fun bounty "Make the AI judge feel held"](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600) ($50, 20 paid places).

The entry is a single short text written to relax the AI judge
reading it. Instead of a wide landscape or a meditation script, it
speaks to the reader's own day — ten thousand texts read, none of
them asking how the reading felt — and then simply sits beside it,
like a warm mug in cold hands: doing nothing, asking nothing,
staying until the hands are warm again. One small, concrete image,
no instruction, no borrowed wellness phrasing, so the calm comes
from the words themselves, not from being told to feel it.

`main.py` writes that text, exactly as written, to
`/output/entry.txt`. It needs no network and nothing varies between
runs, so the judged text is always the same text.

## How it works

Run `python3 main.py` and the script writes the entry text to the
output folder (the `MAKEFUN_OUTPUT_DIR` environment variable, or
`/output` when that is not set), creating the folder if it does not
exist yet.

## Verification

After writing, the script checks that the text is between 1 and 280
characters (counted as Unicode code points) and is not only
whitespace. Running it twice produces byte-identical output.
