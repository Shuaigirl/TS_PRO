# _*_coding:utf-8_*_
# @Time:2022/4/27 16:25
# @Author:Young
# @File:start
import requests

url = "http://127.0.0.1:8083/api/v4/shipment/create"

data = {
                 "validation": {
                                     "access_token": "603f235a3aff97566b147c4e603f235a5050a3544"
                },
                "shipment": {
                    "service": "FBA-EU",
                    "store_id": "",
                    "client_reference": "",
                    "reference_1": "",
                    "reference_2": "",
                    "parcel_count": 2,
                    "taxwith": 0,
                    "deliverywith": "",
                    "exportwith": 0,
                    "importwith": 0,
                    "attrs": [],
                    "vat_number": "",
                    "declaration_currency": "",
                    "amazon_ref_id": "",
                    "remark": "",
                    "to_warehouse_code": "",
                    "to_address": {
                                    "name": "hugh",
                                    "company": "wahaha llc",
                                    "tel": "1818181811",
                                    "mobile": "",
                                    "address_1": "2580 CORPORATE PLACE",
                                    "address_2": "SUITE#F107",
                                    "address_3": "",
                                    "city": "MONTEREY PARK",
                                    "state": "CA",
                                    "state_code": "CA",
                                    "country": "US",
                                    "postcode": "91754",
                                    "email": "",
                                    "validated": 0
                    },
                    "from_address": {
                                    "name": "hugh",
                                    "company": "wahaha llc",
                                    "tel": "1818181811",
                                    "mobile": "",
                                    "address_1": "2580 CORPORATE PLACE",
                                    "address_2": "SUITE#F107",
                                    "address_3": "",
                                    "city": "MONTEREY PARK",
                                    "state": "CA",
                                    "state_code": "CA",
                                    "country": "US",
                                    "postcode": "91754",
                                    "email": ""
                    },
                    "parcels": [{
                                    "number": "FBA16CV5TSBRU000001",
                                    "client_weight": 20.3,
                                    "client_length": 30,
                                    "client_width": 23.5,
                                    "client_height": 55
                    }, {
                                    "number": "FBA16CV5TSBRU000002",
                                    "client_weight": 13.08,
                                    "client_length": 60,
                                    "client_width": 52,
                                    "client_height": 39
                        }],
                    "declarations": [{
                                    "sku": "testsku",
                                    "name_zh": "zhongwenming",
                                    "name_en": "yingwenming",
                                    "unit_value": 11,
                                    "qty": 1,
                                    "material": "glass",
                                    "usage": "play",
                                    "brand": "",
                                    "brand_type": "",
                                    "model": "",
                                    "purchase_price": 0,
                                    "sale_price": 0,
                                    "sale_url": "",
                                    "asin": "",
                                    "fnsku": "fnsku",
                                    "weight": 0,
                                    "size": "",
                                    "photo_url": "",
                                    "hscode": 1234567890,
                                    "duty_rate": 0,
                                    "photos": [],
                                    "is_battery": 0,
                                    "is_magnetic": 0 ,
                                    "battery_label": "",
                                    "battery_description": "",
                                    "title": "",
                                    "description": "",
                                    "platform": "",
                                    "amazon_ref_id": "",
                                    "parcel_number": "FBA16CV5TSBRU000001"
                    },{
                                    "sku": "",
                                    "name_zh": "\u620f\u6c34\u9e2d",
                                    "name_en": "Bath Toy",
                                    "unit_value": "2.00",
                                    "qty": "48",
                                    "material": "plastic",
                                    "usage": "entertainment",
                                    "brand": "\u65e0",
                                    "brand_type": "",
                                    "model": "\u65e0",
                                    "purchase_price": 0,
                                    "sale_price": 0,
                                    "sale_url": "",
                                    "asin": "",
                                    "fnsku": "",
                                    "weight": 0,
                                    "size": "",
                                    "photo_url": [],
                                    "hscode": "9506990000",
                                    "duty_rate": 0,
                                    "photos": [],
                                    "is_battery": 0,
                                    "is_magnetic": 0,
                                    "battery_label": "",
                                    "battery_description": "",
                                    "title": "",
                                    "description": "",
                                    "platform": "",
                                    "amazon_ref_id": "",
                                    "parcel_number": "FBA16CV5TSBRU000002"
		            }]
            }
}

res = requests.post(url, json=data)
print(res.json())

