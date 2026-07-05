#Multithreading is a programming technique that allows a single program to execute multiple tasks concurrently.
# It breaks a program down into multiple independent paths of execution,
# called threads, which run at the same time while sharing the same memory space.


import time
from concurrent.futures import  ThreadPoolExecutor

def fetch_url(url:str):
    print(f"Fetching data from url: {url}")
    time.sleep(5)
    print(f"Data fetched from url: {url}")
    return f"Fetched data from Url: {url}"


dummy_urls = [
    "https://example.com/api/users",
    "https://example.com/api/products",
    "https://example.com/api/orders",
    "https://example.com/api/categories",
    "https://example.com/api/reviews",
    "https://example.com/api/payments",
    "https://example.com/api/inventory",
    "https://example.com/api/notifications",
    "https://example.com/api/settings",
    "https://example.com/api/reports"
]

results = []
with ThreadPoolExecutor(max_workers=len(dummy_urls)) as executor:
    futures = executor.map(fetch_url,dummy_urls)
    results.extend(futures)


print(results)

# for url in dummy_urls:
#     print(fetch_url(url))
