from pathlib import Path


# Function to read the file and return the text
def readFiles(route: Path | str) -> str:
    route = Path(route)
    if (route.suffix != ".txt") or (route.is_file() == False):  # noqa E712 (this only ignores ruff's E712 rule only in this line)
        raise TypeError("The file doesn't exist or isn't .txt")
    else:
        with open(route, encoding="utf-8") as f:
            text = f.read()
        return text
