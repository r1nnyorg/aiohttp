#import aiohttp.web, asyncpg, json, aredis, aiokafka, asyncio, builtins, aiohttp_cors, uvloop, math, os, ssl, pathlib
#asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

#async def database(app):
    #app.setdefault('database', await asyncpg.create_pool(host='postgrespostgres.postgres.database.azure.com', user='postgres', database='default', password='pos1gres+', ssl=True))
#    sslctx = ssl.create_default_context(cafile=pathlib.Path(__file__).resolve().parent.joinpath('ca.crt'))
#    sslctx.check_hostname = False
#    sslctx.load_cert_chain(pathlib.Path(__file__).resolve().parent.joinpath('client.root.crt'), keyfile=pathlib.Path(__file__).resolve().parent.joinpath('client.root.key'))
#    app.setdefault('database', await asyncpg.create_pool(host='cockroach', user='root', database='defaultdb', port=26257, ssl=sslctx))
#    app.setdefault('cache', aredis.StrictRedisCluster(host='redis', port=6379, password=os.getenv('password'))) #app.setdefault('cache', aredis.StrictRedis('redis'))
    #producer = aiokafka.AIOKafkaProducer(bootstrap_servers='kafka')
    #await producer.start()
    #await producer.send_and_wait('topic', b"Super message")
    #await producer.stop()
#    yield
#    await app.get('database').close()

#async def ajax(request):
#    body = await request.json()
#    body = ' '.join(' '.join((key, builtins.str(value))) for key,value in body.items())
#    records = await request.app.get('cache').get(body)
#    if not records:
#        async with request.app.get('database').acquire() as connection: records = json.dumps([*map(builtins.dict, await connection.fetch(f'select * from{body}'))], default=builtins.str)
#        await request.app.get('cache').set(body, records)
#   return aiohttp.web.Response(text=records if builtins.isinstance(records, builtins.str) else records.decode())

#async def main():
#    app = aiohttp.web.Application()
#    #app.add_routes([aiohttp.web.post('/ajax', ajax)])
#    app.cleanup_ctx.append(database)
#    cors = aiohttp_cors.setup(app, defaults={'*': aiohttp_cors.ResourceOptions()})
#    cors.add(app.router.add_post('/ajax', ajax))
#    runner = aiohttp.web.AppRunner(app)
#    await runner.setup()
#    site = aiohttp.web.TCPSite(runner, port=80)
#    await site.start()
#    await asyncio.sleep(math.inf)

import asyncio, ssl, pathlib, asyncpg

async def main():
    sslctx = ssl.create_default_context(cafile=pathlib.Path(__file__).resolve().parent.joinpath('ca.crt'))
    sslctx.check_hostname = False
    sslctx.load_cert_chain(pathlib.Path(__file__).resolve().parent.joinpath('client.root.crt'), keyfile=pathlib.Path(__file__).resolve().parent.joinpath('client.root.key'))
    database=await asyncpg.create_pool(host='cockroach', user='root', database='defaultdb', port=26257, ssl=False)
    async with database.acquire() as connection: builtins.print(connection.fetch('select * from productitem'))

asyncio.run(main())
