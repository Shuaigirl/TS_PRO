from aiohttp import web
import aiohttp
import ujson

routes = web.RouteTableDef()
# @routes.post('/api/v4/shipment/label')
# async def shipment_create(request):
#     req_json = await request.json()
#     print(req_json)
#     token = req_json["validation"]["access_token"]
#     print(token)
#     post_json = req_json
#
#     client_session = aiohttp.ClientSession(raise_for_status=True)
#     resp = await client_session.post("http://127.0.0.1:8082/api/v4/shipment/label", json=post_json)
#     async with resp:
#         x = await resp.json()
#         print(x)
#     await client_session.close()
#     return web.json_response(x)

#构造供应商标准Json格式，并赋值
def CreatJson(req_json):
    access_token = req_json['validation'].get('access_token')
    service = req_json['shipment'].get('service')
    store_id = req_json['shipment'].get('store_id')
    client_reference = req_json['shipment'].get('client_reference')
    reference_1 = req_json['shipment'].get('reference_1')
    reference_2 = req_json['shipment'].get('reference_2')
    parcel_count = req_json['shipment'].get('parcel_count')
    # export_scc = req_json['shipment'].get('export_scc')
    # import_scc = req_json['shipment'].get('import_scc')
    taxwith = req_json['shipment'].get('taxwith')
    deliverywith = req_json['shipment'].get('deliverywith')
    exportwith = req_json['shipment'].get('exportwith')
    importwith = req_json['shipment'].get('importwith')
    attrs = req_json['shipment'].get('attrs')
    vat_number = req_json['shipment'].get('vat_number')
    declaration_currency = req_json['shipment'].get('declaration_currency')
    amazon_ref_id = req_json['shipment'].get('amazon_ref_id')
    to_warehouse_code = req_json['shipment'].get('to_warehouse_code')
    # to_address = req_json['shipment'].get('to_address')
    # from_address = req_json['shipment'].get('from_address')
    # to_address收件人地址
    # to_address = req_json['shipment'].get('to_address')
    t_name = req_json['shipment']['to_address'].get('name')
    t_company = req_json['shipment']['to_address'].get('company')
    t_tel = req_json['shipment']['to_address'].get('tel')
    t_mobile = req_json['shipment']['to_address'].get('mobile')
    t_address_1 = req_json['shipment']['to_address'].get('address_1')
    t_address_2 = req_json['shipment']['to_address'].get('address_2')
    t_address_3 = req_json['shipment']['to_address'].get('address_3')
    t_city = req_json['shipment']['to_address'].get('city')
    t_state = req_json['shipment']['to_address'].get('state')
    t_state_code = req_json['shipment']['to_address'].get('state_code')
    t_country = req_json['shipment']['to_address'].get('country')
    t_postcode = req_json['shipment']['to_address'].get('postcode')
    t_email = req_json['shipment']['to_address'].get('email')
    t_validated = req_json['shipment']['to_address'].get('validated')
    # print(t_name,t_company,t_tel,t_mobile,t_address_1,t_address_2,t_address_3,t_city,t_state,t_state_code,t_country,t_postcode,t_email,t_validated)
    # 获取from_address发件人地址
    f_name = req_json['shipment']['from_address'].get('name')
    f_company = req_json['shipment']['from_address'].get('company')
    f_tel = req_json['shipment']['from_address'].get('tel')
    f_mobile = req_json['shipment']['from_address'].get('mobile')
    f_address_1 = req_json['shipment']['from_address'].get('address_1')
    f_address_2 = req_json['shipment']['from_address'].get('address_2')
    f_address_3 = req_json['shipment']['from_address'].get('address_3')
    f_city = req_json['shipment']['from_address'].get('city')
    f_state = req_json['shipment']['from_address'].get('state')
    f_state_code = req_json['shipment']['from_address'].get('state_code')
    f_country = req_json['shipment']['from_address'].get('country')
    f_postcode = req_json['shipment']['from_address'].get('postcode')
    f_email = req_json['shipment']['from_address'].get('email')
    remark = req_json['shipment']['remark']
    # parcels = req_json['shipment']['parcels']
    # # # 把declarations字段加入到parcels字段下，作为子字段
    # # req_json['shipment']['parcels'][0]['declarations'] = []
    # number = req_json['shipment']['parcels'].value('number')
    # for vat_number in req_json['shipment']['parcels'][0]:
    #     print(vat_number)
    # parcels数据获取
    number = req_json['shipment']['parcels'][0].get('number')
    client_weight = req_json['shipment']['parcels'][0].get('client_weight')
    client_length = req_json['shipment']['parcels'][0].get('client_length')
    client_width = req_json['shipment']['parcels'][0].get('client_width')
    client_height = req_json['shipment']['parcels'][0].get('client_height')
    # declarations数据获取
    sku = req_json['shipment']['declarations'][0].get('sku')
    name_zh = req_json['shipment']['declarations'][0].get('name_zh')
    name_en = req_json['shipment']['declarations'][0].get('name_en')
    unit_value = req_json['shipment']['declarations'][0].get('unit_value')
    qty = req_json['shipment']['declarations'][0].get('qty')
    material = req_json['shipment']['declarations'][0].get('material')
    usage = req_json['shipment']['declarations'][0].get('usage')
    brand = req_json['shipment']['declarations'][0].get('brand')
    brand_type = req_json['shipment']['declarations'][0].get('brand_type')
    model = req_json['shipment']['declarations'][0].get('model')
    sale_price = req_json['shipment']['declarations'][0].get('sale_price')
    sale_url = req_json['shipment']['declarations'][0].get('sale_url')
    asin = req_json['shipment']['declarations'][0].get('asin')
    fnsku = req_json['shipment']['declarations'][0].get('fnsku')
    weight = req_json['shipment']['declarations'][0].get('weight')
    size = req_json['shipment']['declarations'][0].get('size')
    photo_url = req_json['shipment']['declarations'][0].get('photo_url')
    hscode = req_json['shipment']['declarations'][0].get('hscode')
    duty_rate = req_json['shipment']['declarations'][0].get('duty_rate')
    photos = req_json['shipment']['declarations'][0].get('photos')
    is_battery = req_json['shipment']['declarations'][0].get('is_battery')
    is_magnetic = req_json['shipment']['declarations'][0].get('is_magnetic')

    # for parcels in req_json['shipment']['parcels']:
    #     pass


    post_json = {
                    "validation": {
                        "access_token": access_token
                    },
                    "shipment": {
                        "service": service,
                        "store_id": store_id,
                        "client_reference": client_reference,
                        "reference_1": reference_1,
                        "reference_2": reference_2,
                        "parcel_count": parcel_count,
                        "export_scc": 0,
                        "import_scc": 0,
                        "taxwith": taxwith,
                        "deliverywith": deliverywith,
                        "exportwith": exportwith,
                        "importwith": importwith,
                        "attrs": attrs,
                        "vat_number": vat_number,
                        "declaration_currency": declaration_currency,
                        "amazon_ref_id": amazon_ref_id,
                        "to_warehouse_code": to_warehouse_code,
                        "to_address": {
                            "name": t_name,
                            "company": t_company,
                            "tel": t_tel,
                            "mobile": t_mobile,
                            "address_1": t_address_1,
                            "address_2": t_address_2,
                            "address_3": t_address_3,
                            "city": t_city,
                            "state": t_state,
                            "state_code": t_state_code,
                            "country": t_country,
                            "postcode": t_postcode,
                            "email": t_email
                        },
                        "from_address" : {
                            "name": f_name,
                            "company": f_company,
                            "tel": f_tel,
                            "mobile": f_mobile,
                            "address_1": f_address_1,
                            "address_2": f_address_2,
                            "address_3": f_address_3,
                            "city": f_city,
                            "state": f_state,
                            "state_code": f_state_code,
                            "country": f_country,
                            "postcode": f_postcode,
                            "email": f_email
                        },
                        "parcels": [{
                            "number": number,
                            "client_weight": client_weight,
                            "client_length": client_length,
                            "client_width": client_width,
                            "client_height": client_height,
                            "declarations": [{
                                                "sku": sku,
                                                "name_zh": name_zh,
                                                "name_en": name_en,
                                                "unit_value":unit_value,
                                                "qty": qty,
                                                "material": material,
                                                "usage": usage,
                                                "brand": brand,
                                                "brand_type":brand_type,
                                                "model": model,
                                                "sale_price":sale_price,
                                                "sale_url": sale_url,
                                                "asin": asin,
                                                "fnsku": fnsku,
                                                "weight": weight,
                                                "size": size,
                                                "hscode": hscode,
                                                "duty_rate": duty_rate,
                                                "photos": photos,
                                                "is_battery": is_battery,
                                                "is_magnetic": is_magnetic
                                            }]
                        }],
                        # "parcels": [],
                        "remark": remark

                    }
        }
    return post_json

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
                'user-agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 99.0.4844.51Safari / 537.36',
                # 'Cookie': 'grid-view-pagesize=10; _csrf-parcelos-wos=2d2c7da843f30791069ba20e9bc6d70fed1c2015ba37ef37039761a7de64681ca%3A2%3A%7Bi%3A0%3Bs%3A18%3A%22_csrf-parcelos-wos%22%3Bi%3A1%3Bs%3A32%3A%22z8goL_3NTf1VKfoVZh8vKyGriKq_yP5_%22%3B%7D; parcelos_wos=0433fuacv5mgupb50siahfeh30'
        }

    post_json = CreatJson(req_json)
    return await Clintservices(url, post_json, header)
    # print(type(post_json))
    # return Clintservices(url, post_json, headers)
    # return Clintservices(url, post_json)
    # print(req_json['validation'].get('access_token'))
    # url = 'http://tiansheng.nextsls.com/api/v4/shipment/creat'

    # post_json = req_json
    # return await Clintservices(url, post_json, headers)

    # # 1、添加字段：export_scc，import_scc
    # req_json['shipment']['export_scc'] = 0
    # req_json['shipment']['import_scc'] = 0
    # req_json['shipment']['test'] = '测试字段'
    # print(req_json)
    #
    # # 2、修改字段下的value值
    # for i in req_json['shipment']:
    #     # print(i)
    #     if i == 'import_scc':
    #         print('这是我要修改的字段：', i)
    #         req_json['shipment'][i] = 1  # 这样只是修改import_scc字段的值为'1',而不是直接修改字段
    #         break
    #
    # # 3、删除字段
    # del req_json['shipment']['test']

    # req_json['shipment']['export_scc'] = 0
    # req_json['shipment']['import_scc'] = 0
    # req_json['shipment']['parcels'][0]['declarations'] = []
    # for i in req_json['shipment']['parcels'][0]:
    #     # print(i)
    #     if i == 'declarations':
    #         print('给字段赋值', i)
    #         req_json['shipment']['parcels'][0][i] = [{
    #             "sku": "testsku",
    #             "name_zh": "zhongwenming",
    #             "name_en": "yingwenming",
    #             "unit_value": 11,
    #             "qty": 1,
    #             "material": "glass",
    #             "usage": "play",
    #             "brand": "",
    #             "brand_type": "",
    #             "model": "",
    #             "sale_price": 0,
    #             "sale_url": "",
    #             "asin": "",
    #             "fnsku": "fnsku",
    #             "weight": 0,
    #             "size": "",
    #             "hscode": 1234567890,
    #             "duty_rate": 0,
    #             "photos": "",
    #             "is_battery": 0,
    #             "is_magnetic": 0
    #         }]
    #         break
    # del req_json['shipment']['declarations']
    # print(req_json)

    # print(type(post_json))
    # return Clintservices(url, post_json, headers)

app = web.Application()
app.add_routes(routes)
web.run_app(app)


