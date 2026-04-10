import asyncio

async def main():
    print ("Hello World")
    await asyncio.sleep(10)
    print("Hello World")

asyncio.run(main())