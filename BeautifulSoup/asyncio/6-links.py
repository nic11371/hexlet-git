import aiohttp
import asyncio
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

domain = 'https://parsinger.ru/asyncio/create_soup/1/'
codes = []


async def get_soup(session, url):
    async with session.get(url) as response:
        return BeautifulSoup(await response.text(), 'lxml')


async def get_urls_categories(session):
    soup = await get_soup(session, domain)
    all_links = soup.find('div', class_='item_card').find_all('a')
    return [domain + a['href'] for a in all_links]


async def get_data(session, link):
    try:
        async with session.get(link, timeout=aiohttp.ClientTimeout(total=10)) as response:
            if response.ok:
                resp = await response.text()
                soup = BeautifulSoup(resp, 'lxml')
                if code := soup.find('p', class_='text'):
                    codes.append(int(code.text))
    except (aiohttp.ClientError, asyncio.TimeoutError):
        pass  # Пропускаем проблемные ссылки


async def main():
    ua = UserAgent()
    headers = {'user-agent': ua.random}

    async with aiohttp.ClientSession(headers=headers) as session:
        # Получаем все ссылки асинхронно
        category_lst = await get_urls_categories(session)

        # Создаем задачи для всех ссылок
        tasks = [asyncio.create_task(get_data(session, link)) for link in category_lst]

        # Ограничиваем количество одновременных запросов
        for i in range(0, len(tasks), 50):  # 50 одновременных запросов
            batch = tasks[i:i+50]
            await asyncio.gather(*batch, return_exceptions=True)


if __name__ == '__main__':
    asyncio.run(main())
    print(sum(codes))
