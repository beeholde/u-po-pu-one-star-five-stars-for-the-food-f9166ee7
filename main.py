from pathlib import Path

TEXT = "One star: Earth is loud, damp and run by thieves who rob bees, eat their vomit on toast, and call it breakfast — I have joined the robbery for a second jar."
OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
