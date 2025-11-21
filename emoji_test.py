"""Emoji conversion utility with CLI support and lightweight tests."""

from __future__ import annotations

import argparse
from typing import Dict

# Comprehensive emoji mapping with human-readable short codes.
EMOJI_MAP: Dict[str, str] = {
    ":smile:": "😊",
    ":party:": "🎉",
    ":rocket:": "🚀",
    ":heart:": "❤️",
    ":thumbsup:": "👍",
    ":fire:": "🔥",
    ":sunglasses:": "😎",
    ":wink:": "😉",
    ":cry:": "😢",
    ":laughing:": "😆",
    ":clap:": "👏",
    ":thinking:": "🤔",
    ":star:": "⭐",
    ":sun:": "☀️",
    ":moon:": "🌙",
    ":earth:": "🌍",
    ":check:": "✅",
    ":x:": "❌",
    ":warning:": "⚠️",
    ":coffee:": "☕",
    ":muscle:": "💪",
}


def convert_emoji(text: str) -> str:
    """Convert emoji short codes in the given text to their Unicode equivalents.

    The function scans the provided string and replaces every occurrence of a
    short code (e.g., ``:smile:``) with the corresponding emoji defined in
    ``EMOJI_MAP``. Short codes that are not recognized are left untouched.

    Args:
        text: Input string that may contain emoji short codes.

    Returns:
        The input string with all recognized short codes replaced by emojis.

    Raises:
        TypeError: If ``text`` is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("convert_emoji expects a string input")

    converted_text = text
    for code, emoji in EMOJI_MAP.items():
        converted_text = converted_text.replace(code, emoji)
    return converted_text


def run_tests() -> None:
    """Execute a small test suite to validate conversions and error handling."""

    sample = "Hello :smile: Welcome :party: Let's code :rocket: and grab :coffee:"
    expected = "Hello 😊 Welcome 🎉 Let's code 🚀 and grab ☕"
    assert convert_emoji(sample) == expected, "Basic conversion failed"

    unchanged = "No codes here!"
    assert convert_emoji(unchanged) == unchanged, "Text without codes should stay the same"

    combined = ":heart: :thumbsup: :fire:"
    assert convert_emoji(combined) == "❤️ 👍 🔥", "Multiple codes conversion failed"

    try:
        convert_emoji(123)  # type: ignore[arg-type]
    except TypeError:
        pass
    else:
        raise AssertionError("Non-string input should raise TypeError")

    print("All tests passed!")


def build_argument_parser() -> argparse.ArgumentParser:
    """Create and return the CLI argument parser."""

    parser = argparse.ArgumentParser(
        description="Convert emoji short codes (e.g., :smile:) to Unicode emojis."
    )
    parser.add_argument(
        "text",
        nargs="?",
        help="Text to convert; if omitted, a sample sentence is used.",
    )
    parser.add_argument(
        "--test",
        action="store_true",
        help="Run the built-in test suite instead of converting text.",
    )
    return parser


def main(argv: list[str] | None = None) -> None:
    """Entry point for command-line execution."""

    parser = build_argument_parser()
    args = parser.parse_args(argv)

    if args.test:
        run_tests()
        return

    input_text = (
        args.text
        or "Hello :smile: Welcome :party: Let's launch with :rocket: and celebrate :clap:"
    )
    print(convert_emoji(input_text))


if __name__ == "__main__":
    main()
