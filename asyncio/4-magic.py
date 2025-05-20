import asyncio

spells = {
    "Огненный шар": 3,
    "Ледяная стрела": 2,
    "Щит молний": 4,
    "Телепортация": 7
}
# Максимальное время для каста заклинания
max_cast_time = 5  # Секунды

# Ученики мага
students = ["Алара", "Бренн", "Сирил", "Дариа", "Элвин"]


async def cast_spell(student, spell, cast_time):
    task = asyncio.create_task(asyncio.sleep(cast_time))
    try:
        await asyncio.wait_for(asyncio.shield(task), timeout=max_cast_time)
        print(f"{student} успешно кастует {spell} за {cast_time} сек.")
    except TimeoutError:
        print(f"Ученик {student} не справился с заклинанием {spell}, и учитель применил щит. {student} успешно завершает заклинание с помощью shield.")
    return await task


async def main():
    tasks = []
    for k, v in spells.items():
        for s in students:
            tasks.append(cast_spell(s, k, v))
    await asyncio.gather(*tasks, return_exceptions=True)


asyncio.run(main())
