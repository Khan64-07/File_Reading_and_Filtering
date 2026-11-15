# Function that counts total words of text
def totalWords(text: str) -> int:
    total = text.split()
    return len(total)


# Function for avarege word lenth of the text
def avgWordLength(text: str) -> float:
    total = text.split()
    totalWords = len(total)
    totalLength = sum(
        1 for word in total for letter in word if letter not in ["'", "’"]
    )  # (this only ignores apostrophes(' and ’) in the word length count)
    avgLength = totalLength / totalWords
    return avgLength


# Function to search a word in the text
def searchWord(text: str, word_toSearch: str) -> int:
    # It also includes the apostrophes(' and ’) in the word count, so it counts words like "don't"
    # It also counts words like "'hello'" and "‘hello’" as "hello" so  it's easier to search for words with apostrophes like 'hello'
    totalWords = [word.strip("'‘’") for word in text.split()]
    targetWord = word_toSearch.strip("'‘’")
    count = totalWords.count(targetWord)

    if count == 0:
        raise ValueError("This word does not appear on the text")

    return count
