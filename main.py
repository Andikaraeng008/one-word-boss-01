import os

# One word for the boss: Echo — the boss who only repeats what
# everyone else just said, in meetings, as if it were their idea.
WORD = "Echo"

assert 1 <= len(WORD) <= 30, "gate: 1-30 chars"
assert WORD.strip() == WORD and " " not in WORD, "gate: single word"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(WORD)
