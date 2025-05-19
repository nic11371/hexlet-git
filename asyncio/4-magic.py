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
    await asyncio.sleep(cast_time)
    print(f"{student} успешно кастует {spell} за {cast_time} сек.")


async def main():
    tasks = []

    for k, v in spells.items():
        for s in students:
            task = asyncio.create_task(cast_spell(s, k, v))
            try:
                await asyncio.wait_for(asyncio.shield(task), timeout=max_cast_time)
            except TimeoutError:
                print(f"Ученик {s} не справился с заклинанием {k}, и учитель применил щит. {s} успешно завершает заклинание с помощью shield.")
            tasks.append(task)
    await asyncio.gather(*tasks, return_exceptions=True)



asyncio.run(main())