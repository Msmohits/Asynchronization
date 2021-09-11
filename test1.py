import asyncio


async def function_asyc():
    for i in range(100000):
        if i % 5000 == 0:
            print("Hello, I'm Mohit")
           

            # New Line Added
            await asyncio.sleep(0.01)
    return 0


async def function_2():
    for i in range(10):

        print("\n Byi Byi \n")
        await asyncio.sleep(0.01)
    return 0


async def main():
    f1 = loop.create_task(function_asyc())
    f2 = loop.create_task(function_2())
    await asyncio.wait([f1, f2])


# to run the above function we'll
# use Event Loops these are low level
# functions to run async functions
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()

# You can also use High Level functions Like:
# asyncio.run(function_asyc())
