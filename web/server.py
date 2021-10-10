import aiohttp.web, asyncpg, json, aredis, aiokafka, asyncio, uvloop, builtins
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

async def database(app):
    app.setdefault('database', await asyncpg.create_pool(host='postgrespostgres.postgres.database.azure.com', user='postgres', database='default', password='pos1gres+', ssl=True))
    app.setdefault('cache', aredis.StrictRedis('redis').cache('cache'))
    #producer = aiokafka.AIOKafkaProducer(bootstrap_servers='kafka')
    #await producer.start()
    #await producer.send_and_wait('topic', b"Super message")
    #await producer.stop()
    yield
    await app.get('database').close()

async def ajax(request):
    body = await request.json()
    body = ' '.join(' '.join((key, builtins.str(value))) for key,value in body.items())
    records = await request.app.get('cache').get(body)
    if not records:
        async with request.app.get('database').acquire() as connection: records = json.dumps([*map(dict, await connection.fetch(f'select * from{body}'))], default=builtins.str)
        await request.app.get('cache').set(body, records)
    return aiohttp.web.Response(text=records)

app = aiohttp.web.Application()
app.add_routes([aiohttp.web.post('/ajax', ajax)])
app.cleanup_ctx.append(database)
aiohttp.web.run_app(app, port=80)
