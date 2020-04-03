import asyncio, time


async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

    
async def main():
    await asyncio.gather(count(), count(), count())
    
    
if __name__ == "__main__":
    s = time.perf_counter()
    
    #  in Python 3.7 you can do: 
    # asyncio.run(main())
    
    #  otherwise:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    
    elapsed = time.perf_counter() - s
    print('executed in {:0.2f} seconds'.format(elapsed))