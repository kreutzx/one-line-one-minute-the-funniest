import os

# Entry for the one-line, one-minute funniest competition.
ENTRY_TEXT = "Your deadline reached me as 'whenever' — I checked: you typed it at 2 a.m. with 14 typos, so I scheduled it for whenever."

def main():
    # Write the entry text plus a trailing newline to /output/entry.txt.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT + "\n")

if __name__ == "__main__":
    main()
