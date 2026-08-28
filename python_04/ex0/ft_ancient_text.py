import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return

    filename: str = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    try:
        f: typing.IO = open(filename, "r")
    except Exception as e:
        print(f"Error opening file '{filename}': {e}")
        return

    try:
        contents: str = f.read()
    finally:
        f.close()

    lines: list[str] = contents.splitlines()
    if lines:
        print(f"--{lines[0]}")
        for line in lines[1:]:
            print(line)

    print(f"--File '{filename}' closed.")


if __name__ == "__main__":
    main()
