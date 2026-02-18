import sys

from cli import greet, word_count


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
