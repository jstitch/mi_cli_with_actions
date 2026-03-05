"""Simple CLI tool — greets a user or counts words in a string."""

import argparse
import sys


def greet(name: str) -> str:
    return f"Hello, {name}!"


def word_count(text: str) -> int:
    return len(text.split())


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="A simple CLI tool")
    subparsers = parser.add_subparsers(dest="command", required=True)

    greet_parser = subparsers.add_parser("greet", help="Greet someone")
    greet_parser.add_argument("name", help="Name to greet")

    wc_parser = subparsers.add_parser("wordcount", help="Count words in a string")
    wc_parser.add_argument("text", help="Text to count words in")

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "greet":
        print(greet(args.name))
    elif args.command == "wordcount":
        print(word_count(args.text))
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()


def reverse_text(text: str) -> str:
    """Reverses the given text."""
    return text[::-1]


def is_palindrome(text: str) -> bool:
    """Checks if the given text is a palindrome."""
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def caesar_cipher(text: str, shift: int) -> str:
    """Encrypts text using Caesar cipher."""
    result = []
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            result.append(chr((ord(char) - base + shift) % 26 + base))
        else:
            result.append(char)
    return "".join(result)


def count_vowels(text: str) -> int:
    """Counts vowels in a string."""
    return sum(1 for c in text.lower() if c in "aeiou")


def truncate(text: str, max_len: int, suffix: str = "...") -> str:
    """Truncates text to max_len characters."""
    if len(text) <= max_len:
        return text
    return text[:max_len - len(suffix)] + suffix


def title_case(text: str) -> str:
    """Converts text to title case skipping small words."""
    small = {"a", "an", "the", "and", "but", "or", "in", "on", "at", "to"}
    words = text.split()
    return " ".join(
        w if (i > 0 and w.lower() in small) else w.capitalize()
        for i, w in enumerate(words)
    )


def password_strength(password: str) -> str:
    """Evaluates the strength of a password."""
    score = 0
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in "!@#$%^&*()-_=+[]{}|;:,.<>?" for c in password):
        score += 1
    if score <= 2:
        return "weak"
    if score <= 4:
        return "moderate"
    return "strong"


def slug(text: str) -> str:
    """Converts text to a URL-friendly slug."""
    import re
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text)
    text = re.sub(r"^-+|-+$", "", text)
    return text


def wrap_text(text: str, width: int) -> list[str]:
    """Wraps text to lines of at most `width` characters."""
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        if not current:
            current = word
        elif len(current) + 1 + len(word) <= width:
            current += " " + word
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def levenshtein(s1: str, s2: str) -> int:
    """Computes the Levenshtein edit distance between two strings."""
    if len(s1) < len(s2):
        return levenshtein(s2, s1)
    if not s2:
        return len(s1)
    prev = list(range(len(s2) + 1))
    for i, c1 in enumerate(s1):
        curr = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = prev[j + 1] + 1
            deletions = curr[j] + 1
            substitutions = prev[j] + (c1 != c2)
            curr.append(min(insertions, deletions, substitutions))
        prev = curr
    return prev[-1]


def roman_to_int(s: str) -> int:
    """Converts a Roman numeral string to an integer."""
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    prev = 0
    for ch in reversed(s.upper()):
        val = values.get(ch, 0)
        if val < prev:
            total -= val
        else:
            total += val
        prev = val
    return total


def int_to_roman(num: int) -> str:
    """Converts an integer to a Roman numeral string."""
    val_map = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
    ]
    result = ""
    for value, numeral in val_map:
        while num >= value:
            result += numeral
            num -= value
    return result


def fizzbuzz(n: int) -> list[str]:
    """Returns FizzBuzz sequence from 1 to n."""
    output = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            output.append("FizzBuzz")
        elif i % 3 == 0:
            output.append("Fizz")
        elif i % 5 == 0:
            output.append("Buzz")
        else:
            output.append(str(i))
    return output


def flatten(nested: list) -> list:
    """Flattens a nested list of arbitrary depth."""
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def chunk(lst: list, size: int) -> list[list]:
    """Splits a list into chunks of a given size."""
    return [lst[i:i + size] for i in range(0, len(lst), size)]


def deduplicate(lst: list) -> list:
    """Removes duplicates from a list preserving order."""
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def is_prime(n: int) -> bool:
    """Returns True if n is a prime number."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def primes_up_to(n: int) -> list[int]:
    """Returns all prime numbers up to n using the Sieve of Eratosthenes."""
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i, is_p in enumerate(sieve) if is_p]


def fibonacci(n: int) -> list[int]:
    """Returns the first n Fibonacci numbers."""
    if n <= 0:
        return []
    if n == 1:
        return [0]
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq


def matrix_multiply(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    """Multiplies two matrices a and b."""
    rows_a, cols_a = len(a), len(a[0])
    rows_b, cols_b = len(b), len(b[0])
    if cols_a != rows_b:
        raise ValueError("Incompatible matrix dimensions")
    result = [[0.0] * cols_b for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += a[i][k] * b[k][j]
    return result


def transpose(matrix: list[list[float]]) -> list[list[float]]:
    """Returns the transpose of a matrix."""
    if not matrix:
        return []
    rows, cols = len(matrix), len(matrix[0])
    return [[matrix[r][c] for r in range(rows)] for c in range(cols)]


def binary_search(lst: list, target) -> int:
    """Returns the index of target in sorted lst, or -1 if not found."""
    lo, hi = 0, len(lst) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def merge_sort(lst: list) -> list:
    """Sorts a list using merge sort and returns a new sorted list."""
    if len(lst) <= 1:
        return lst[:]
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def group_by(lst: list, key_fn) -> dict:
    """Groups list elements by the result of key_fn."""
    groups: dict = {}
    for item in lst:
        k = key_fn(item)
        groups.setdefault(k, []).append(item)
    return groups


def frequency_map(lst: list) -> dict:
    """Returns a dict mapping each element to its count in lst."""
    freq: dict = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return freq


def rotate_list(lst: list, k: int) -> list:
    """Rotates list to the right by k positions."""
    if not lst:
        return []
    k = k % len(lst)
    return lst[-k:] + lst[:-k] if k else lst[:]


def zip_with(fn, lst1: list, lst2: list) -> list:
    """Applies fn element-wise to two lists and returns the results."""
    return [fn(a, b) for a, b in zip(lst1, lst2)]


def running_total(lst: list[float]) -> list[float]:
    """Returns a list of running (cumulative) totals."""
    totals = []
    acc = 0.0
    for x in lst:
        acc += x
        totals.append(acc)
    return totals
