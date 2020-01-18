from interface.Client import Client
import asyncio


async def run():
    client = await Client.create()

    request = ">start {\"formatid\":\"gen7randombattle\"}"
    print(f"> {request}")
    await client.websocket.send(request)

    request = ">player p1 {\"name\": \"Romulus\"}"
    print(f"> {request}")
    await client.websocket.send(request)

    request = ">player p2 {\"name\": \"Remus\"}"
    print(f"> {request}")
    await client.websocket.send(request)

    request = ">p1 team 1"
    print(f"> {request}")
    await client.websocket.send(request)

    request = ">p2 team 2"
    print(f"> {request}")
    await client.websocket.send(request)

    response = await client.websocket.recv()
    print(f"< {response}")


asyncio.get_event_loop().run_until_complete(run())
