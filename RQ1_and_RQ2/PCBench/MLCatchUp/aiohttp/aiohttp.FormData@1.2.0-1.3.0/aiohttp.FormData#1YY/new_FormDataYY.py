import asyncio
import aiohttp

async def main():
    session = aiohttp.ClientSession()
    try:
        data = aiohttp.FormData(quote_fields=True)
        response = await session.post('http://httpbin.org/post', data=data)
        print(await response.text())
    finally:
        session.close()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
