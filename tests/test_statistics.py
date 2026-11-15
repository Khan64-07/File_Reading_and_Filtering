from file_reading_and_filtering.statistics import avgWordLength, searchWord, totalWords


def test_totalWords():
    text = "This is a test"
    assert totalWords(text) == 4
    text2 = "This isn't a test with more words"  # To test if it counts the words with apostrophes as one word
    assert totalWords(text2) == 7


def test_avgWordLength():
    text = "It's a test"
    assert avgWordLength(text) == 2.6666666666666665
    text2 = "Its a test"
    assert avgWordLength(text2) == 2.6666666666666665


def test_searchWord():
    text = "This is a test This test is only a test"
    assert searchWord(text, "test") == 3
    assert searchWord(text, "This") == 2
    # To test if it counts the words with apostrophes as one word
    text2 = "'hello' ‘hello’ don't"
    assert searchWord(text2, "hello") == 2
    assert searchWord(text2, "'hello'") == 2
    assert searchWord(text2, "don't") == 1

    try:
        searchWord(text, "notfound")
    except ValueError as e:
        assert str(e) == "This word does not appear on the text"
