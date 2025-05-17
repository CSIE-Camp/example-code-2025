import asyncio

async def add(a, b):
    return a + b

async def mul(a, b):
    c = 0
    for i in range(b):
        c = await add(c, a)
    return c

print(asyncio.run(mul(2, 3)))