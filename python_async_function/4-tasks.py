#!/user/bin/env python3
"""Alter a function task_wait_n"""
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Return the list of all the delays."""
    delay_list = []
    for _ in range(1, n + 1):
        delay_list.append(await task_wait_random(max_delay))
    for i in range(1, n):
        cle = delay_list[i]
        j = i - 1
        while j >= 0 and delay_list[j] > cle:
            delay_list[j + 1] = delay_list[j]
            j -= 1
        delay_list[j + 1] = cle
    return delay_list
