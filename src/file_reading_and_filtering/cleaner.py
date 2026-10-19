import unicodedata


# Function to normalize text and detect words like 'é' instead of 'e' and ' ´ '
def normalizeText(text: str) -> str:
    normalizedText = unicodedata.normalize("NFC", text)
    return normalizedText


# Function to make every word lowercase in the text
def lowerText(text: str) -> str:
    loweredText = text.casefold()  # (casefold() is used instead of .lower because it also works in other lenguages as well)
    return loweredText
