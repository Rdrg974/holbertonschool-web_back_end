#!/usr/bin/env python3
"""A type-annotated function make_multiplier."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier."""
    def multi(x: float) -> float:
        """Return a float by multiplier."""
        return x * multiplier
    return multi
