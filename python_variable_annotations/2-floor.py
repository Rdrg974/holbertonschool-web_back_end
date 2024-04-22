#!/usr/bin/env python3
"""A type-annotated function floor."""


def floor(n: float) -> int:
    """Returns the floor of the float."""
    if n < 0:
        return int(n) + 1
    return int(n)
