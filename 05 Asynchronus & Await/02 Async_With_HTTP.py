import aiohttp
import asyncio

async def func():
    async with aiohttp.ClientSession() as session:

    # async with aiohttp.ClientSession() as session:
        async with session.get("https://example.com/") as res:
            data = await res.text()
            print(data[:100])  

asyncio.run(func())



