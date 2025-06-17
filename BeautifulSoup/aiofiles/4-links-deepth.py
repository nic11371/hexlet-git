import aiofiles
import asyncio
import aiohttp
from bs4 import BeautifulSoup
import os


async def write_file(session, url, name_img):
    async with aiofiles.open(f'BeautifulSoup/aiofiles/images/{name_img}', mode='wb') as f:
        async with session.get(url) as response:
            async for x in response.content.iter_chunked(1024):
                await f.write(x)
        print(f'Изображение сохранено {name_img}')


async def main():
    domain = 'https://parsinger.ru/asyncio/aiofile/2/'
    url = 'https://parsinger.ru/asyncio/aiofile/2/index.html'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            soup = BeautifulSoup(await resp.text(), 'lxml')
            links = [domain + x['href'] for x in soup.find_all('a')]
            for link in links:
                async with session.get(link) as response:
                    soup = BeautifulSoup(await response.text(), 'lxml')
                    img_url = [x['src'] for x in soup.find_all('img')]
                    tasks = []
                    for img in img_url:
                        name_img = img.split('/')[6]
                        task = asyncio.create_task(write_file(session, img, name_img))
                        tasks.append(task)
                await asyncio.gather(*tasks)


# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())


def get_folder_size(filepath, size=0):
    for root, dirs, files in os.walk(filepath):
        for f in files:
            size += os.path.getsize(os.path.join(root, f))
    return size


print(get_folder_size('BeautifulSoup/aiofiles/images'))
