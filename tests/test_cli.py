import sys

from cli import (
    binary_search,
    caesar_cipher,
    chunk,
    count_vowels,
    deduplicate,
    fibonacci,
    fizzbuzz,
    flatten,
    frequency_map,
    greet,
    group_by,
    int_to_roman,
    is_palindrome,
    is_prime,
    levenshtein,
    matrix_multiply,
    merge_sort,
    password_strength,
    primes_up_to,
    reverse_text,
    roman_to_int,
    rotate_list,
    running_total,
    slug,
    title_case,
    transpose,
    truncate,
    word_count,
    wrap_text,
    zip_with,
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


def test_roman_to_int_basic():
    assert roman_to_int("III") == 3
    assert roman_to_int("IV") == 4
    assert roman_to_int("IX") == 9
    assert roman_to_int("XLII") == 42
    assert roman_to_int("MCMXCIX") == 1999


def test_int_to_roman_basic():
    assert int_to_roman(3) == "III"
    assert int_to_roman(4) == "IV"
    assert int_to_roman(9) == "IX"
    assert int_to_roman(42) == "XLII"
    assert int_to_roman(1999) == "MCMXCIX"


def test_fizzbuzz_basic():
    result = fizzbuzz(15)
    assert result[0] == "1"
    assert result[2] == "Fizz"
    assert result[4] == "Buzz"
    assert result[14] == "FizzBuzz"


def test_flatten_basic():
    assert flatten([1, [2, 3], [4, [5, 6]]]) == [1, 2, 3, 4, 5, 6]


def test_flatten_empty():
    assert flatten([]) == []


def test_chunk_basic():
    assert chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]


def test_chunk_exact():
    assert chunk([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]


def test_deduplicate_basic():
    assert deduplicate([1, 2, 1, 3, 2]) == [1, 2, 3]


def test_deduplicate_empty():
    assert deduplicate([]) == []


def test_is_prime_true():
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(13) is True


def test_is_prime_false():
    assert is_prime(0) is False
    assert is_prime(1) is False
    assert is_prime(4) is False
    assert is_prime(9) is False


def test_is_prime_even():
    assert is_prime(4) is False


def test_primes_up_to_basic():
    assert primes_up_to(10) == [2, 3, 5, 7]


def test_primes_up_to_small():
    assert primes_up_to(1) == []


def test_fibonacci_basic():
    assert fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]


def test_fibonacci_empty():
    assert fibonacci(0) == []


def test_fibonacci_one():
    assert fibonacci(1) == [0]


def test_matrix_multiply_basic():
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]
    assert matrix_multiply(a, b) == [[19.0, 22.0], [43.0, 50.0]]


def test_matrix_multiply_incompatible():
    import pytest
    with pytest.raises(ValueError):
        matrix_multiply([[1, 2]], [[1, 2]])


def test_transpose_basic():
    assert transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]


def test_transpose_empty():
    assert transpose([]) == []


def test_binary_search_found():
    assert binary_search([1, 3, 5, 7, 9], 5) == 2


def test_binary_search_not_found():
    assert binary_search([1, 3, 5, 7, 9], 4) == -1


def test_binary_search_first():
    assert binary_search([1, 3, 5], 1) == 0


def test_binary_search_last():
    assert binary_search([1, 3, 5], 5) == 2


def test_merge_sort_basic():
    assert merge_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]


def test_merge_sort_empty():
    assert merge_sort([]) == []


def test_merge_sort_single():
    assert merge_sort([42]) == [42]


def test_group_by_basic():
    result = group_by([1, 2, 3, 4], lambda x: x % 2)
    assert result == {1: [1, 3], 0: [2, 4]}


def test_frequency_map_basic():
    assert frequency_map(["a", "b", "a", "c", "b", "a"]) == {"a": 3, "b": 2, "c": 1}


def test_rotate_list_basic():
    assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]


def test_rotate_list_empty():
    assert rotate_list([], 3) == []


def test_rotate_list_zero():
    assert rotate_list([1, 2, 3], 0) == [1, 2, 3]


def test_zip_with_basic():
    assert zip_with(lambda a, b: a + b, [1, 2, 3], [4, 5, 6]) == [5, 7, 9]


def test_running_total_basic():
    assert running_total([1.0, 2.0, 3.0, 4.0]) == [1.0, 3.0, 6.0, 10.0]


def test_running_total_empty():
    assert running_total([]) == []
