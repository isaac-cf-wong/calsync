from __future__ import annotations


def hello_world(i: int = 0) -> str:
    """Doc String."""
    print("hello world")
    return f"string-{i}"


def good_night() -> str:
    """Doc String."""
    print("good night")
    return "string"


def hello_goodbye():
    hello_world(1)
    good_night()
