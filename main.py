import os

TEXT = "One star: Earth is loud, damp and run by thieves who rob bees, eat their vomit on toast, and call it breakfast — I have joined the robbery for a second jar."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    main()
