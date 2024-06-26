#!/usr/bin/env python3
"""Measure_time function."""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Return total_time / n"""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    result = (end - start) / n
    return result
