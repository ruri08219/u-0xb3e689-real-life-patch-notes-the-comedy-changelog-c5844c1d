import os

ENTRY = "v4.1.1: fixed a bug where the left eyelid twitched for three days straight, then stopped the moment you booked a doctor's appointment."

os.makedirs("/output", exist_ok=True)

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY + "\n")

with open("/output/entry.txt", "r", encoding="utf-8") as f:
    lines = f.read().splitlines()

assert len(lines) == 1
assert lines[0] == ENTRY
