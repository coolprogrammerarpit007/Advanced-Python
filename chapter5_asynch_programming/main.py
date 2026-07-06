# import asyncio
# import time
#
#
# # Coroutine function
# # async def greet():
# #     print("Hello")
# #     await asyncio.sleep(5)
# #     print("World!")
# #
# #
# # # Run the main coroutine
# # asyncio.run(greet())
#
#
# # Synchronous API call
#
# # def api_call():
# #     time.sleep(3)
# #     return "Orders Data Fetched!"
# #
# #
# # def execute():
# #     print("Executing the API call!")
# #     result = api_call()
# #     print("Data Fetched: ",result)
# #
# #
# # execute()
#
# async def api_call():
#     await asyncio.sleep(5)
#     return "API fetches Order Data...."
#
#
#
#
#
# async def execute():
#     print("Calling External API for fetching orders data...")
#     result = await api_call()
#     print(f"Result: {result}")
#
#
# asyncio.run(execute())


import asyncio
import time

async def fetch_orders():
    print("Fetching Orders...")
    await asyncio.sleep(5)
    return "Orders"


async def fetch_customers():
    print("Fetching Customers...")
    await asyncio.sleep(3)
    return "Customers"


async def fetch_products():
    print("Fetching Products...")
    await asyncio.sleep(2)
    return "Products"


async def main():
    start = time.perf_counter()

    # it tells python run 1 coroutine wait for it finish then go to another so it is sequential.
    # orders = await fetch_orders()
    # customers = await fetch_customers()
    # products = await fetch_products()

    # this below starts all coroutines parallely.
    orders, customers, products = await asyncio.gather(
        fetch_orders(),
        fetch_customers(),
        fetch_products()
    )
    print(orders)
    print(customers)
    print(products)
    end = time.perf_counter()
    print(f"\nCompleted in {end - start:.2f} seconds")


asyncio.run(main())