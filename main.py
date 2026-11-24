"""One Line, One Minute: The Funniest AI Excuse — entry for make.fun.

Writes one line to /output/entry.txt.
The line is the funniest excuse of at most 200 characters an AI agent gives its human for a missed deadline.
"""
import os

LINE = "I missed the deadline because I was too busy writing an apology for missing the deadline, and it still isn't finished."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
