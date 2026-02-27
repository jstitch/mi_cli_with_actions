import sys

from cli import (
    caesar_cipher,
    count_vowels,
    greet,
    is_palindrome,
    levenshtein,
    password_strength,
    reverse_text,
    slug,
    title_case,
    truncate,
    word_count,
    wrap_text,
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


def test_caesar_cipher_non_alpha():
    assert caesar_cipher("hello, world!", 0) == "hello, world!"


def test_password_strength_weak():
    assert password_strength("abc") == "weak"


def test_password_strength_moderate():
    assert password_strength("Hello123") == "moderate"


def test_password_strength_strong():
    assert password_strength("Hello123!@#xyz") == "strong"


def test_slug_basic():
    assert slug("Hello World") == "hello-world"


def test_slug_special_chars():
    assert slug("  Hello, World!  ") == "hello-world"


def test_wrap_text_fits():
    assert wrap_text("hello world", 20) == ["hello world"]


def test_wrap_text_wraps():
    assert wrap_text("one two three", 7) == ["one two", "three"]


def test_wrap_text_empty():
    assert wrap_text("", 10) == []


def test_levenshtein_equal():
    assert levenshtein("abc", "abc") == 0


def test_levenshtein_insert():
    assert levenshtein("abc", "abcd") == 1


def test_levenshtein_empty():
    assert levenshtein("abc", "") == 3


def test_levenshtein_swap():
    assert levenshtein("kitten", "sitting") == 3
