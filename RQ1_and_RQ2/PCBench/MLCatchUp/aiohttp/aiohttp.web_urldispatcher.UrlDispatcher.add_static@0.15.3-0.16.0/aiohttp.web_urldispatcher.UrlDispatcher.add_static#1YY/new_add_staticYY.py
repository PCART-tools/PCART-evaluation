from aiohttp import web
app = web.Application()
app.router.add_static('/static/', './', chunk_size=262144)
