# _*_coding:utf-8_*_
# @Time:2022/5/10 9:25
# @Author:Young
# @File:hl_CreateNewJson
async def HualiJson(req_json):
    access_token = req_json['validation'].get('access_token')
    service = req_json['shipment'].get('service')
    store_id = req_json['shipment'].get('store_id')
    client_reference = req_json['shipment'].get('client_reference')
    reference_1 = req_json['shipment'].get('reference_1')
    reference_2 = req_json['shipment'].get('reference_2')
    parcel_count = req_json['shipment'].get('parcel_count')

    taxwith = req_json['shipment'].get('taxwith')
    deliverywith = req_json['shipment'].get('deliverywith')
    exportwith = req_json['shipment'].get('exportwith')
    importwith = req_json['shipment'].get('importwith')
    attrs = req_json['shipment'].get('attrs')
    vat_number = req_json['shipment'].get('vat_number')
    declaration_currency = req_json['shipment'].get('declaration_currency')
    amazon_ref_id = req_json['shipment'].get('amazon_ref_id')
    to_warehouse_code = req_json['shipment'].get('to_warehouse_code')

    #to_address收件人地址
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
    #获取from_address发件人地址
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
    # print(f_name,f_company,f_tel,f_mobile,f_address_1,f_address_2,f_address_3,f_city,f_state,f_state_code,f_country,f_postcode,f_email)

    # from_address = req_json['shipment'].get('from_address')
    remark = req_json['shipment']['remark']

    #获取parcels数据
    parcel_data = []
    parcels = req_json['shipment']['parcels']
    for i in range(len(parcels)):
        number = parcels[i].get("number")
        client_weight=parcels[i].get("client_weight")
        client_length=parcels[i].get("client_length")
        client_width =parcels[i].get("client_width")
        client_height =parcels[i].get("client_height")
        data = {
             "volume_height": client_height, "volume_length": client_length, "volume_width": client_width, "volume_weight": client_weight
        }
        parcel_data.append(data)

    # declarations数据获取
    declarations = req_json['shipment']['declarations']
    d_data = []
    for j in range(len(declarations)):
        parcel_number = declarations[j].get("parcel_number")
        sku = declarations[j].get("sku")
        name_zh = declarations[j].get("name_zh")
        name_en = declarations[j].get("name_en")
        unit_value = float(declarations[j].get("unit_value"))
        qty = float(declarations[j].get("qty"))
        material = declarations[j].get("material")
        usage = declarations[j].get("usage")
        brand = declarations[j].get("brand")
        brand_type = declarations[j].get("brand_type")
        model = declarations[j].get("model")
        sale_price = declarations[j].get("sale_price")
        sale_url = declarations[j].get("sale_url")
        asin = declarations[j].get("asin")
        fnsku = declarations[j].get("fnsku")
        weight = declarations[j].get("weight")
        size = declarations[j].get("size")
        photo_url = declarations[j].get("photo_url")
        hscode = declarations[j].get("hscode")
        duty_rate = declarations[j].get("duty_rate")
        photos = declarations[j].get("photos")
        is_battery = declarations[j].get("is_battery")
        is_magnetic = declarations[j].get("is_magnetic")
        allWeight = qty * weight
        allunit_value = unit_value*qty
        platform = declarations[j].get("platform")
        d = {
                        "invoice_amount": allunit_value,  # 申报总价值，必填
                        "invoice_pcs": qty,  # 件数，必填
                        "invoice_title": name_en,  # 英文品名，必填
                        "invoice_weight": weight,  # 单件重
                        "sku": name_zh,#中文品名
                        "sku_code": brand_type,#配货信息
                        "hs_code": hscode,#海关编码
                        "transaction_url": sale_url,#销售地址
                        "invoiceunit_code": fnsku,#申报单位
                        "invoice_imgurl": photo_url,#图片地址
                        "invoice_brand": brand,#品牌
                        "invoice_rule": size,#规格
                        "invoice_currency":declaration_currency,#申报币种
                        "invoice_taxno": duty_rate,#税则号
                        "origin_country": platform,#原产国
                        "invoice_material": material,#材质
                        "invoice_purpose": usage#用途
            }
        d_data.append(d)
    # sku = req_json['shipment']['declarations'][0].get('sku')
    # name_zh = req_json['shipment']['declarations'][0].get('name_zh')
    # name_en = req_json['shipment']['declarations'][0].get('name_en')
    # unit_value = req_json['shipment']['declarations'][0].get('unit_value')
    # qty = req_json['shipment']['declarations'][0].get('qty')
    # material = req_json['shipment']['declarations'][0].get('material')
    # usage = req_json['shipment']['declarations'][0].get('usage')
    # brand = req_json['shipment']['declarations'][0].get('brand')
    # brand_type = req_json['shipment']['declarations'][0].get('brand_type')
    # model = req_json['shipment']['declarations'][0].get('model')
    # purchase_price =req_json['shipment']['declarations'][0].get('purchase_price')
    # sale_price = req_json['shipment']['declarations'][0].get('sale_price')
    # sale_url = req_json['shipment']['declarations'][0].get('sale_url')
    # asin = req_json['shipment']['declarations'][0].get('asin')
    # fnsku = req_json['shipment']['declarations'][0].get('fnsku')
    # weight = req_json['shipment']['declarations'][0].get('weight')
    # size = req_json['shipment']['declarations'][0].get('size')
    # photo_url = req_json['shipment']['declarations'][0].get('photo_url')
    # hscode = req_json['shipment']['declarations'][0].get('hscode')
    # duty_rate = req_json['shipment']['declarations'][0].get('duty_rate')
    # photos = req_json['shipment']['declarations'][0].get('photos')
    # is_battery = req_json['shipment']['declarations'][0].get('is_battery')
    # is_magnetic = req_json['shipment']['declarations'][0].get('is_magnetic')
    # battery_label = req_json['shipment']['declarations'][0].get('battery_label')
    # battery_description = req_json['shipment']['declarations'][0].get('battery_description')
    # title = req_json['shipment']['declarations'][0].get('title')
    # description = req_json['shipment']['declarations'][0].get('description')
    # platform = req_json['shipment']['declarations'][0].get('description')
    # amazon_ref_id2 = req_json['shipment']['declarations'][0].get('amazon_ref_id')
    # parcel_number = req_json['shipment']['declarations'][0].get('parcel_numbe')
    # allWeight = qty*weight
    #

    data = {
            "buyerid": store_id,
            "order_piece": parcel_count, #件数，小包默认1，快递需真实填写
            "consignee_mobile": t_mobile,  # 手机号,选填。为方便派送最好填写
            "order_returnsign": "N",  # 退回标志，默认N表示不退回，Y标表示退回。中邮可以忽略该属性
            "trade_type": importwith, # 贸易类型
            "duty_type": deliverywith, # DDU或DDP
            "battery_type": attrs, #电池类型代码，联系货代提供
            "consignee_name": t_name, #收件人,必填
            "consignee_companyname": t_company, #收件公司名,如有最好填写
            "consignee_address": t_address_1, #收件地址街道，必填
            "consignee_telephone": t_tel, #收件电话，必填
            "country": t_country, #收件国家二字代码，必填
            "consignee_state": t_state, #州/省
            "consignee_city": t_city, #城市
            "consignee_suburb": t_state_code, #收件区，选填
            "consignee_postcode": t_postcode, #邮编，有邮编的国家必填
            "consignee_passportno": amazon_ref_id,  # 收件护照号，选填
            "consignee_email": t_email, #邮箱，选填
            "consignee_taxno": reference_1,  # 收件人税号
            "consignee_streetno": t_address_2, #街道号
            "consignee_doorno": t_address_3, #门牌号

            "shipper_taxnotype": taxwith,  # 税号类型，邮政产品可选值：IOSS,NO-IOSS,OTHER；DHL可选值：SDT、VAT、FTZ、DAN、EOR、CNP、EIN等(类型说明参照文档底部“DHL发件人税号类型”)
            "shipper_taxno": reference_2,      # 发件人税号
            "shipper_taxnocountry": f_country,  # 发件人税号国家,用国家二字码
            "customer_id": number,  # 客户ID，必填
            "customer_userid": sku,  # 登录人ID，必填
            "order_customerinvoicecode": model,  # 原单号，必填
            "product_id": service,  # 运输方式ID，必填
            "weight": allWeight,  # 总重，选填，如果sku上有单重可不填该项
            "product_imagepath": photos,  # 图片地址，多图片地址用分号隔开
            "order_transactionurl": sale_url,  # 产品销售地址
            "order_cargoamount": sale_price,  # 选填；用于DHL/FEDEX运费；或用于白关申报（订单实际金额，特殊渠道使用）；或其他用途
            "order_insurance": 0,  # 保险金额
            "cargo_type": parcel_number,  #包裹类型，P代表包裹，D代表文件，B代表PAK袋
            "order_customnote": client_reference, # 订单
            "orderInvoiceParam":d_data ,
            "orderVolumeParam": parcel_data
}
    return data