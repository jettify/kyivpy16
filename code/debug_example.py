import asyncio
import time


loop = asyncio.get_event_loop()
loop.slow_callback_duration = 0.01


async def sleeper():
    print('start blocking')
    time.sleep(0.1)

loop.run_until_complete(sleeper())
