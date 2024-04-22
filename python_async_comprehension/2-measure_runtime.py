#!/usr/bin/env python3
"""
A measure_runtime coroutine that will execute
async_comprehension four times in parallel.
"""
import asyncio
import timeit

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the runtime and return it.
    """
    start = timeit.default_timer()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = timeit.default_timer()
    total_time = end - start
    return total_time
