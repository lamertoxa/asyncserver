import asyncio
import logging

import websockets

async def hello(websocket):
        name = input("What's your name? ")

        await websocket.send(name)
        print(f">>> {name}")

        greeting = await websocket.recv()
        print(f"<<< {greeting}")



async def main():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        while True:
            task = asyncio.create_task(hello(websocket))
            await task


if __name__ == "__main__":
    asyncio.run(main())