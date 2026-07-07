# API stands for Application Programming Interface. used to connect backend to the frontend.


import  requests,httpx
import asyncio

api_url = "https://api.github.com"

async def get_user_details():
    print("Fetching User Profile Details...")
    async with httpx.AsyncClient() as client:
        response = await client.get(api_url)
        return response.json()


async def main():
    print("Profile Data Request Calling...")
    user_data = await asyncio.gather(get_user_details())
    print("User Data reaches...")
    print(user_data)




# asyncio.run(main())

# There are multiple API methods
# 1. get
# 2. post
# 3. put
# 4. patch
# 4. delete


opensource_api = 'https://jsonplaceholder.typicode.com/posts'

def get_posts():
    response = requests.get(opensource_api)
    return response.json()


# posts = get_posts()
# for post in posts:
#     print(post['title'])


def create_post(**data):
    response = requests.post(opensource_api,json=data,timeout=2.50)
    print("Data created successfully!")
    print(response.json())


# create_post(user_id=1,title="MCP Server Intrduction",body="An MCP server is an open-source bridge connecting AI applications (like Claude or ChatGPT) to external data sources and tools. Acting like a USB-C port for AI, it allows models to interact with file systems, databases, and APIs uniformly without needing brittle, custom integrations.")
# print("Thanks for creating new post!!")


# Headers and Authentication

headers = {
    "User-Agent":"Python",
    "Accept":"application/json",
    "Custom-Header":"CustomValue"
}

response = requests.get(opensource_api,headers=headers)
print(response.status_code)
print(response.headers)
# print(response.json())


# Authorization
token = "mfdvfdvfdm"
headers = {
    "Authorization":f"Bearer {token}",
    "Content-Type":"application/json"
}


# API KEY Authentication

headers = {
    "X-API-Key":"Your_API_KEY_HERE"
}