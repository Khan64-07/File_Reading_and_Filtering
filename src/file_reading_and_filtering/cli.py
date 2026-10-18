import argparse
from pathlib import Path

from .reader import readFiles


def main():
    # Creat the parser for the cli and asks for the file rute to finally print the content
    parser = argparse.ArgumentParser(
        prog="Program to filter text files",
        description="It filters, searches and analizes words and phrases in a text",
    )
    parser.add_argument("route", type=Path)
    args = parser.parse_args()

    print(readFiles(args.route))
