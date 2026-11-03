# Function that counts total words of text
def totalWords(text: str) -> int:
    total = text.split()
    return len(total)


# Function for avarege word lenth of the text
def avgWordLength(text: str) -> float:
    total = text.split()
    totalWords = len(total)
    totalLenth = sum(len(word) for word in total)
    avgLenth = totalLenth / totalWords
    return avgLenth


# Function to search a word in the text
def searchWord(text: str, word_toSearch: str) -> int:
    totalWords = text.split()
    count = totalWords.count(
        word_toSearch
    )  # count method counts the number of time the word appears automatically

    if count == 0:
        raise ValueError("This word does not appear on the text")

    return count
