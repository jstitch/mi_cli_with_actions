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
