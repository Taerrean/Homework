import asyncio
async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(5):
        await asyncio.sleep(3/power) #Такой большой числитель, чтобы время не было слишком маленьким
        print(f'Силач {name} поднял {i} шар(ов).')
    print(f'Силач {name} закончил соревнования.')
async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Hercules', 10))
    task2 = asyncio.create_task(start_strongman('Heracles', 25))
    task3 = asyncio.create_task(start_strongman('Prometheus', 15))
    await task1, task2, task3
asyncio.run(start_tournament())