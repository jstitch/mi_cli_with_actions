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
