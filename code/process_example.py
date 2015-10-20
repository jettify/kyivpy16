import asyncio
import math
from concurrent.futures import ProcessPoolExecutor

loop = asyncio.get_event_loop()
executor = ProcessPoolExecutor(max_workers=3)

def is_prime(n):
    if n % 2 == 0: return False
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0: return False
    return True

async def go(loop, executor):
    number = 112272535095293 
    result = await loop.run_in_executor(executor, is_prime, number)
loop.run_until_complete(go(loop, executor))
