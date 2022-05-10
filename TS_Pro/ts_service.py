from aiohttp import web
import aiohttp
import TS_CreateNewJson
routes = web.RouteTableDef()


async def Clintservices(url,post_json,header):
    async with aiohttp.ClientSession() as session:
        async with session.post(url=url, data=post_json, headers=header) as resp:
            cont = await resp.json(content_type='text/json', encoding='utf-8')
            print(cont)
            return web.json_response(cont)
            # return web.json_response({'main':'ok'})

@routes.post('/api/v4/shipment/create')
async def ship_create(request):
    req_json = await request.json()
    url = 'http://tiansheng.nextsls.com/api/v4/shipment/creat'
    header = {
                'user-agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 99.0.4844.51Safari / 537.36'
             }
    post_json = TS_CreateNewJson.CreatJson(req_json)
    print(post_json)
    return await Clintservices(url, post_json, header)

app = web.Application()
app.add_routes(routes)
web.run_app(app,port=8083)


