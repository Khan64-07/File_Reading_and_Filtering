from pathlib import Path


def readFiles(route: Path | str) -> str:
    route = Path(route)
    if (route.suffix != ".txt") or (route.is_file() == False):
        raise TypeError("The file doesn't exist or isn't .txt")
    else:
        with open(route, encoding="utf-8") as f:
            text = f.read()
        return text
