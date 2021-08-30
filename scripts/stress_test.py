import asyncio

from httpx import AsyncClient, Limits


async def register_user(client:AsyncClient):
    r = await client.post(
        url='http://localhost:8001/users',
        json={
            'email': 'example@example.com',
            'nickname': 'example'
        },
        timeout=30.0
    )

    if r.status_code != 201:
        print(r.text)

    await asyncio.sleep(2.0)

    r = await client.patch(
        url=f'http://localhost:8002/profiles/{r.json()["id"]}',
        json={
            'bio': 'stress test',
            'age': 17,
            'gender': 'male'
        },
        timeout=30.0
    )

    if r.status_code != 200:
        print(r.text)

async def main():
    client = AsyncClient(
        limits=Limits(max_keepalive_connections=50, max_connections=1000)
    )

    try:
        calls = [register_user(client) for _ in range(10000)]

        r = await asyncio.gather(*calls)
    finally:
        await client.aclose()

asyncio.run(main())
