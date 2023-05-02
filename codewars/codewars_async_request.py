import asyncio
import logging
# TODO : Summary:
# Implement a coro request_manager which sends and processes fake requests
# It accepts the parameter n which represents the amount of requests that should be made
# Requests have to be made with send_request
# send_request is a preloaded coroutine : (coro) send_request() -> str
# It takes 1 sec until a character is returned to the caller
# The waiting time is implemented via asyncio.sleep
# Characters returned by send_request have to be concat to one string
# That string is then returned by your request_manager
# The characters in the string need to be ordered, so that the character returned by the first request is at index 0, the character returned by the second request is at index 1 etc.
# Your request_manager has 1.5 sec to start & process all n requests and to return the desired string
async def send_request():
    await asyncio.sleep(1)
    return "X"

async def request_manager(n: int) -> str:
    tasks = []
    result = ''
    for i in range(n):
        tasks.append(asyncio.create_task(send_request()))

    tuple_letter = await asyncio.gather(*tasks)
    for i in tuple_letter:
        result += i
    return result


print (asyncio.run(request_manager(4)))