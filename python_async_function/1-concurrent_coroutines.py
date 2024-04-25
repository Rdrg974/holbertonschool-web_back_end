#!/usr/bin/env python3
"""An async routine called wait_n."""
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Return the list of all the delays."""
    delay_list = []
    for _ in range(1, n + 1):
        delay_list.append(await wait_random(max_delay))
    for i in range(1, n):
        cle = delay_list[i]
        j = i - 1
        while j >= 0 and delay_list[j] > cle:
            delay_list[j + 1] = delay_list[j]
            j -= 1
        delay_list[j + 1] = cle
    return delay_list
