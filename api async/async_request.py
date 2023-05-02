import httpx
import asyncio


URL_CATS = "https://catfact.ninja/fact"
URL_JOKES = "https://official-joke-api.appspot.com/random_joke"

async def cats(client):
    response = await client.get(URL_CATS)
    content = response.json()
    return content['fact']

async def jokes(client):
    response = await client.get(URL_JOKES)
    content = response.json()
    return content['setup'],content['punchline']

async def main():
    tasks = []
    async with httpx.AsyncClient() as client:
        cat = asyncio.create_task(cats(client))
        joke = asyncio.create_task(jokes(client))
        tasks.extend([cat,joke])

        result = await asyncio.gather(*tasks)
    return result


if __name__ == "__main__":
    result = asyncio.run(main())
    print(result)
