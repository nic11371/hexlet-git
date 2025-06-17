import aiofiles
import asyncio
import aiohttp
from bs4 import BeautifulSoup
import os


async def get_soup(session, url):
    async with session.get(url) as response:
        return BeautifulSoup(await response.text(), 'lxml')


def find_links(base, soup):
    return [base + x['href'] for x in soup.find_all('a')]


async def write_file(session, url, name_img, semaphore):
    async with semaphore:
        async with aiofiles.open(f'BeautifulSoup/aiofiles/images2/{name_img}', mode='wb') as f:
            async with session.get(url) as response:
                async for x in response.content.iter_chunked(1024):
                    await f.write(x)
            print(f'Изображение сохранено {name_img}')


async def main():
    domain = 'https://parsinger.ru/asyncio/aiofile/3/'
    url = 'https://parsinger.ru/asyncio/aiofile/3/index.html'
    connector = aiohttp.TCPConnector(limit_per_host=6)
    async with aiohttp.ClientSession(connector=connector) as session:
        soup = await get_soup(session, url)
        links_top = find_links(domain, soup)
        semaphore = asyncio.Semaphore(100)
        seen_images = set()
        for link in links_top:
            soup2 = await get_soup(session, link)
            link = link.rsplit('/', 1)[0] + '/'
            links_middle = find_links(link, soup2)
            for link_img in links_middle:
                soup3 = await get_soup(session, link_img)
                img_urls = [x['src'] for x in soup3.find_all('img')]
                tasks = []
                for img in img_urls:
                    if img in seen_images:
                        continue
                    seen_images.add(img)
                    name_img = img.split('/')[6]
                    task = asyncio.create_task(write_file(session, img, name_img, semaphore))
                    tasks.append(task)
            await asyncio.gather(*tasks)


# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())


def get_folder_size(filepath, size=0):
    for root, dirs, files in os.walk(filepath):
        for f in files:
            size += os.path.getsize(os.path.join(root, f))
    return size


print(get_folder_size('BeautifulSoup/aiofiles/images2'))
