import asyncio
import aiofiles

async def write_file():
    async with aiofiles.open("file.txt", "w") as f:
        await f.write("Hello from async file I/O")

async def read_file():
    async with aiofiles.open("file.txt", "r") as f:
        data = await f.read()
        print(data)

asyncio.run(write_file())
asyncio.run(read_file())