import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return

    filename: str = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
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

    transformed: list[str] = [line + "#" for line in lines]

    print("Transform data:")
    if transformed:
        print(f"--{transformed[0]}")
        for line in transformed[1:]:
            print(line)
    print("--")

    new_filename: str = input("Enter new file name (or empty): ")

    if not new_filename:
        print("Not saving data.")
        return

    print(f"Saving data to '{new_filename}'")

    try:
        out: typing.IO = open(new_filename, "w")
    except Exception as e:
        print(f"Error opening file '{new_filename}': {e}")
        return

    try:
        out.write("\n".join(transformed) + "\n")
    finally:
        out.close()

    print(f"Data saved in file '{new_filename}'.")


if __name__ == "__main__":
    main()
