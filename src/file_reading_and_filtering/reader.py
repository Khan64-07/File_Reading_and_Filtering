from pathlib import Path


def readFiles(route: Path | str) -> str:
    route = Path(route)
    with open(route, encoding="utf-8") as f:
        text = f.read()
    return text
