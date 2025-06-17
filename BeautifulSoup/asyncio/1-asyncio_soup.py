import asyncio
import time
import aiohttp
from bs4 import BeautifulSoup


category = ['watch', 'mobile', 'mouse', 'hdd', 'headphones']
urls = [f'https://parsinger.ru/html/{cat}/{i}/{i}_{x}.html' for cat, i in zip(
    category, range(1, len(category) + 1)) for
        x in range(1, 33)]


async def run_tasks(url, session):
    async with session.get(url) as resp:
        soup = BeautifulSoup(await resp.text(), 'lxml')
        price = soup.find('span', id='price').text
        name = soup.find('p', id='p_header').text
        return resp.url, price, name


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [run_tasks(link, session) for link in urls]
        result = await asyncio.gather(*tasks)
        for i in result:
            print(i, sep=', ')


if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    start = time.time()
    asyncio.run(main())
    print(time.time()-start)
