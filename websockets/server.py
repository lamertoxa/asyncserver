import asyncio
import logging

import websockets

async def hello(websocket):
    name = await websocket.recv()
    print(f"<<< {name}")
    if name == "q":
        return None
    greeting = f"Hello {name}!"
    logging.warning(f"HELLO")
    await websocket.send(greeting)
    print(f">>> {greeting}")
    return await hello(websocket)

async def main():
    async with websockets.serve(hello, "localhost", 8765):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())