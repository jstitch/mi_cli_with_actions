import sys

from cli import (
    caesar_cipher,
    count_vowels,
    greet,
    is_palindrome,
    reverse_text,
    title_case,
    truncate,
    word_count,
)


def test_greet_returns_greeting():
    assert greet("Alice") == "Hello, Alice!"


def test_greet_with_different_name():
    assert greet("World") == "Hello, World!"


def test_word_count_basic():
    assert word_count("hello world") == 2


def test_word_count_single_word():
    assert word_count("hello") == 1


def test_word_count_multiple_words():
    assert word_count("one two three four five") == 5


def test_cli_greet_command(capsys):
    from cli import main
    sys.argv = ["cli", "greet", "Alice"]
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, Alice!"


def test_cli_wordcount_command(capsys):
    from cli import main
    sys.argv = ["cli", "wordcount", "hello beautiful world"]
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "3"


def test_reverse_text():
    assert reverse_text("hello") == "olleh"


def test_is_palindrome_true():
    assert is_palindrome("racecar") is True


def test_is_palindrome_false():
    assert is_palindrome("hello") is False


def test_caesar_cipher():
    assert caesar_cipher("abc", 1) == "bcd"
    assert caesar_cipher("xyz", 1) == "yza"


def test_count_vowels():
    assert count_vowels("hello world") == 3


def test_truncate_short():
    assert truncate("hi", 10) == "hi"


def test_truncate_long():
    assert truncate("hello world", 8) == "hello..."


def test_title_case():
    assert title_case("the lord of the rings") == "The Lord Of the Rings"
