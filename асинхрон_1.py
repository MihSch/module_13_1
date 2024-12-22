import time
import asyncio


async def start_strongman(name, power):
    n = 1
    print(f'Силач {name} начал соревнования.')
    for i in range(power):
        print(f'Силач {name} поднял {n} шар')
        n += 1
        await asyncio.sleep(1 / power)
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    t1 = asyncio.create_task(start_strongman('Петя', 3))
    t2 = asyncio.create_task(start_strongman('Наташа', 5))
    t3 = asyncio.create_task(start_strongman('Анна', 1))
    await t1
    await t2
    await t3


s = time.time()
asyncio.run(start_tournament())
f = time.time()

print(f"Время выполнения: {f - s} сек")
