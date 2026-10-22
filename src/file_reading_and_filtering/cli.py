import argparse
from pathlib import Path

from .cleaner import clean
from .reader import readFiles


def main():
    # Creat the parser for the cli and asks for the file rute to finally print the content
    parser = argparse.ArgumentParser(
        prog="Program to filter text files",
        description="It filters, searches and analizes words and phrases in a text",
    )
    parser.add_argument("route", type=Path)
    args = parser.parse_args()

    readText = readFiles(
        args.route
    )  # This is the variable that stores the text in the .txt file itself(without any changes, just reads)
    print(readText)

    cleanText = clean(
        readText
    )  # This variable stores the .txt text filtered/cleaned(without puntuation, capitals, symbols, etc)
    print(cleanText)
