from aiohttp import web
routes = web.RouteTableDef()

@routes.get('/')
async def hello(request):
    return web.Response(text="Hello, world")

@routes.get('/sex')
async def sex(request):
    return web.Response(text="YOU'RE SEXY")

app = web.Application()
app.add_routes([web.get('/', hello)])
app.add_routes([web.get('/sex', sex)])
web.run_app(app)