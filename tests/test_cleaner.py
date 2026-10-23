from file_reading_and_filtering.cleaner import (
    clean,
    lowerText,
    normalizeText,
    removePunct,
)


def test_normalizeText():
    assert normalizeText("caf\u00e9") == "café"  # é as one character
    assert normalizeText("cafe\u0301") == "café"  # e + acentuation sign


def test_loweText():
    assert lowerText("Árbol") == "árbol"


def test_removePunct():
    assert removePunct("¡Hola, mundo!") == "Hola mundo"


def test_cleaner():
    assert clean("¡Hola, ÑANDÚ! Don't panic.") == "hola ñandú don't panic"
