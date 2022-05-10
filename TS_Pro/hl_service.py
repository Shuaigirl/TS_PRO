# _*_coding:utf-8_*_
# @Time:2022/4/27 16:27
# @Author:Young
# @File:service
from aiohttp import web
import aiohttp
import hl_CreateNewJson
routes = web.RouteTableDef()



async def Clintservices(url, data, header):
    async with aiohttp.ClientSession() as session:
        async with session.post(url=url, data=data, headers=header) as resp:
            print(data)
            cont = await resp.json(content_type='text/html', encoding='gbk')
            # print(cont)
            return web.json_response(cont)

@routes.post('/api/v4/shipment/create')
async def shipment_create(request):
     req_json = await request.json()
     url = "http://118.25.228.118:8082/createOrderApi.htm?param="
     header = {
         "user-agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 99.0.4844.51Safari / 537.36"
     }
     data =await hl_CreateNewJson.HualiJson(req_json)
     return await Clintservices(url, data, header)

app = web.Application()
app.add_routes(routes)
web.run_app(app, port=8082)


