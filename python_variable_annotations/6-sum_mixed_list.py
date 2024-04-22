#!/usr/bin/env python3
"""A type-annotated function sum_mixed_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns their sum as a float."""
    sum_float = 0.0
    for item in mxd_lst:
        sum_float += item
    return sum_float
