#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

Writes the chosen excuse to /output/entry.txt and prints it.
"""

import os

LINE = "I saw prod and staging were identical, so I deleted prod to save us the duplicate storage."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
print(LINE)
