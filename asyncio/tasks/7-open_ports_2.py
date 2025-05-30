import asyncio
import random

ip_dct = {
    '192.168.0.1': [0, 100],
    '192.168.0.2': [225, 300],
    '192.168.2.5': [150, 185]
}


async def scan_port(address, port):
    """
    Асинхронная функция, имитирующая сканирование порта на заданном ip-адресе.
    """
    await asyncio.sleep(1)
    if random.randint(0, 100) == 1:
        # Печать сообщения об обнаружении открытого порта.
        print(f"Port {port} on {address} is open")
        return port
    else:
        return None


async def scan_range(address, start_port, end_port):
    """
    Асинхронная функция, проверяющая состояние диапазона портов по указанному адресу.
    """
    # Печать сообщения о начале сканирования диапазона портов для заданного ip-адреса.
    print(f"Scanning ports {start_port}-{end_port} on {address}")
    tasks = []
    for port in range(start_port, end_port + 1):
        task = asyncio.create_task(scan_port(address, port))
        tasks.append(task)

    open_ports = []
    results = await asyncio.gather(*tasks)

    for port in results:
        if port is not None:
            open_ports.append(port)
    return address, open_ports


async def main(dct):
    """
    Основная асинхронная функция, управляющая процессом сканирования портов из переданного в нее словаря.
    """
    tasks = []
    for ip, ports in dct.items():
        start, end = ports
        task = asyncio.create_task(scan_range(ip, start, end))
        tasks.append(task)
    result = await asyncio.gather(*tasks)
    for item in result:
        ip, port = item
        if port != []:
            print(
                f"Всего найдено открытых портов {len(port)} {port} для ip: {ip}")

# Запуск асинхронного приложения с передачей в main() словаря ip_dct
asyncio.run(main(ip_dct))
