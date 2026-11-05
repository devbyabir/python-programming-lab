from pathlib import Path
from tempfile import TemporaryDirectory


def read_file(path):
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        print(f"Could not read {path.name}: {error}")
        return None


def write_to_file(path, text):
    try:
        path.write_text(text, encoding="utf-8")
    except (OSError, UnicodeError) as error:
        print(f"Could not write {path.name}: {error}")
        return False
    print(f"Saved {path.name}.")
    return True


def modify_file(path, line):
    contents = read_file(path)
    if contents is None:
        return False
    separator = "\n" if contents and not contents.endswith("\n") else ""
    return write_to_file(path, contents + separator + line + "\n")


if __name__ == "__main__":
    with TemporaryDirectory() as directory:
        notes = Path(directory) / "notes.txt"
        read_file(notes)
        if write_to_file(notes, "First lab note.") and modify_file(notes, "Second lab note."):
            print(read_file(notes), end="")
