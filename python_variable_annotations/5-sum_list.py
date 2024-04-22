#!/usr/bin/env python3
"""A type-annotated function sum_list."""


def sum_list(input_list: list[float]) -> float:
    """Returns their sum as a float."""
    sum_float = 0.0
    for item in input_list:
        sum_float += item
    return sum_float
