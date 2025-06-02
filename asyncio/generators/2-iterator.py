import aiohttp
import asyncio


# Асинхронный генератор 
async def async_url_generator(urls):        
    for url in urls:     
        yield url                          


# Асинхронная функция для асинхронных HTTP-запросов, возвращает текст ответа
async def fetch(session, url): 
    async with session.get(url) as response:      
        return await response.text()               


async def main():             
    urls = [
        'https://example.com',
        'https://example.org',
        'https://example.net',
    ]

    # Создаем асинхронный контекстный менеджер сессии для выполнения HTTP-запросов
    async with aiohttp.ClientSession() as session: 
        # Итерируемся по URL-адресам с помощью асинхронного генератора async_url_generator  
        async for url in async_url_generator(urls):                 
            content = await fetch(session, url)                    
            print(f'Fetched content from {url}: {content[:100]}')   


asyncio.run(main())                             