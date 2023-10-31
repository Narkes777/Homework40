# # ---Task 1---
# import os
# import json
# import requests
# import aiohttp
# import asyncio

# os.makedirs("json_files", exist_ok=True)

# response = requests.get("https://jsonplaceholder.typicode.com/posts")
# data = response.json()

# for i, item in enumerate(data, start=1):
#     filename = f"json_files/json_object_{i}.json"
#     with open(filename, "w") as file:
#         json.dump(item, file)

# # ---Task 2---
# import os
# import json

# async def download_json(url, save_path):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             data = await response.json()
#             with open(save_path, "w") as file:
#                 json.dump(data, file)

# os.makedirs("json_files_async", exist_ok=True)

# loop = asyncio.get_event_loop()
# tasks = []
# for i in range(1, 11): 
#     url = f"https://jsonplaceholder.typicode.com/posts/{i}"
#     save_path = f"json_files_async/json_object_{i}.json"
#     task = download_json(url, save_path)
#     tasks.append(task)

# loop.run_until_complete(asyncio.gather(*tasks))
