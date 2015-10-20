import asyncio
import aiohttp


# carry the loop Luke!
loop = asyncio.get_event_loop()


async def go():
    # works only with master branch of aiohttp
    session = aiohttp.ClientSession(loop=loop)
    async with session.get('http://python.org') as resp:
        data = await resp.text()
        print(data)
    session.close()

loop.run_until_complete(go())
