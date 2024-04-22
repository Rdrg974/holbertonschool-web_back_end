#!/user/bin/env python3
"""A function task_wait_random."""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Returns a asyncio.Task"""
    loop = asyncio.get_event_loop()
    return loop.create_task(wait_random(max_delay))
