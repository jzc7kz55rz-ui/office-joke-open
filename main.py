import os

ENTRY = 'This meeting could have been an email. The email could have been a sentence. The sentence could have been a nod. But here we are, on slide 47.'
MAX_CHARS = 200  # the gate's character limit


def main():
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
    except OSError:
        path = "entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
