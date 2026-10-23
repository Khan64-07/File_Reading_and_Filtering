import unicodedata


# Function to normalize text and detect words like 'é' instead of 'e' and ' ´ '
def normalizeText(text: str) -> str:
    normalizedText = unicodedata.normalize("NFC", text)
    return normalizedText


# Function to make every word lowercase in the text
def lowerText(text: str) -> str:
    loweredText = text.casefold()  # (casefold() is used instead of .lower because it also works in other lenguages as well)
    return loweredText


# Function to remove punctuation from the text
def removePunct(text: str) -> str:
    removePunct = [
        c for c in text if c.isalpha() or c == " " or c == "'"
    ]  # Only special charaters allowed are space and apostrophe
    removedPunctText = "".join(removePunct)
    return removedPunctText


# Main function that unites the cleaner functionality
def clean(text: str) -> str:
    normalize = normalizeText(text)

    lower = lowerText(normalize)

    remove = removePunct(lower)

    return remove
