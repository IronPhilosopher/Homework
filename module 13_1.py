import asyncio

async def  start_strongman(name, power):
    rest = 12//power
    for ball in range(5):
        await asyncio.sleep(rest)
        print(f'Силач {name} поднял шар {ball+1}')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Arnold', 6))
    task2 = asyncio.create_task(start_strongman('Silvester', 3))
    task3 = asyncio.create_task(start_strongman('Dwayne', 2))
    await task1
    await task2
    await task3
    return

asyncio.run(start_tournament())