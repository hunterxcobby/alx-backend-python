#!/usr/bin/env python3

"""
a coroutine called async_generator that takes no arguments.
The coroutine will loop 10 times, 
each time asynchronously wait 1 second, 
then yield a random number between 0 and 10. Use the random module.
"""

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]: # type: ignore
    """Coroutine that loops 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10.
    """
    for i in range(10):
        # Simulate an asynchronous operation using asyncio.sleep
        await asyncio.sleep(1)
        # Yield the current value asynchronously
        yield random.uniform(i, 10)
