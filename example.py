import asyncio


async def dog():
    await asyncio.sleep(1)
    print("bar")


async def cat():
    await asyncio.sleep(4)
    print("meow")

async def main():
    task_cat = asyncio.create_task(cat())
    task_dog = asyncio.create_task(dog())
    await task_cat
    await task_dog
asyncio.run(main())

