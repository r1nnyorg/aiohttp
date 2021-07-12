import aiohttp.web, asyncio, uvloop, ssl, aiohttp, aiohttp_cors
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

async def ajax(request):
    async with aiohttp.ClientSession() as session:
        async with session.post('http://web/ajax', data=await request.read()) as response: return aiohttp.web.Response(body=await response.content.read())

async def ws(request):
    websocket = aiohttp.web.WebSocketResponse()
    await websocket.prepare(request)
    async with aiohttp.ClientSession() as session:
        async with session.ws_connect('http://chat/ws') as ws:
            async for message in websocket:
                if message.type == aiohttp.WSMsgType.TEXT:
                    await ws.send_str(message.data)
                    await websocket.send_str(await ws.receive_str())
                else: break
    return websocket
    
app = aiohttp.web.Application()
app.add_routes([aiohttp.web.get('/chat/ws', ws)])
cors = aiohttp_cors.setup(app, defaults={'*': aiohttp_cors.ResourceOptions()})
cors.add(app.router.add_post('/web/ajax', ajax))
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile='/encrypt/fullchain1.pem', keyfile='/encrypt/privkey1.pem')
aiohttp.web.run_app(app, ssl_context=context, port=443)
