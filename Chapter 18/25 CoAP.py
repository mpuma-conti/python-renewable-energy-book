from aiocoap import *

async def main():
    protocol = await Context.create_client_context()

    request = Message(code=GET, uri='coap://localhost/sensor/nivel')

    try:
        response = await protocol.request(request).response
    except Exception as e:
        print('Failed to fetch resource:')
        print(e)
    else:
        print('Result: %s\n%r'%(response.code, response.payload))

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())