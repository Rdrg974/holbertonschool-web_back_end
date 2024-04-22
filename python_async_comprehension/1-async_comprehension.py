#!/usr/bin/env python3
"""A coroutine called async_comprehension."""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """A coroutine called async_comprehension."""
    return [i async for i in async_generator()]
