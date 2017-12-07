# -*- coding:utf-8 -*-
import json
import urllib




global_template_code = {
    'pay_success': 'TM00015',  # 支付成功  3
    'send_notify': 'OPENTM200565259',  # 发货通知 1
    'refund_success': 'TM00004',  # 退款成功 4
    'refund_failed': 'OPENTM207144006',  # 退款失败 5
    'no_pay': 'TM00184',  # 催付订单 2
    'after_sale_apply_failed': 'OPENTM201567177'  # 售后未通过 6
}

a = {
    "weixin": {
        "parent_order_id": "P192017070716215802306",
        "shipper": "yuantong",
        "sum": "1",
        "send_time": "",
        "product_name": "pilu",
        "tracking_id": "wuliu123456",
        "order_id": "order12345",
        "order_time": "2017/11/24",
        "reason": "张butui",
        "apply_id": "apply1234"
    }
}

b = {
    'weixin': 'osjL_wpaAkDsK4-F4IRcDzzLwtdA'
}

params = [
    {'data_type': 1},
    {'data_type': 0}
]

# def _():
#     for data in params:
#         if data['data_type'] == 1:
#             data.update({
#                 'data_key': '',
#                 'data_extension': '',
#             })
#
#             if not data.get('data_name') or data['data_name'] == '':
#                 data.update({
#                     'data_name': '新建文件夹'
#                 })
#         return params

data_list = [

    {
        'data_name': '是',
        'parent_id': 0,
        'data_type': 1
    }
]


params_list = [
    {
        'data_id': 91,
        'data_type': 0,
    },
    {
        'data_id': 93,
        'data_type': 0,
    }

]

print json.dumps(params_list)

import datetime


import hashlib
import time
import random

def salt(salt_len=6, is_num=False):
    """
    密码加密字符串
    生成一个固定位数的随机字符串，包含0-9a-z
    @:param salt_len 生成字符串长度
    """

    if is_num:
        chrset = '0123456789'
    else:
        chrset = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWSYZ'
    salt = []
    for i in range(salt_len):
        item = random.choice(chrset)
        salt.append(item)

    return ''.join(salt)


def create_uuid():
    """
    声称随机字符串
    :return:
    """
    m = hashlib.md5()
    m.update(bytes(str(time.time()) + salt(12)))
    return m.hexdigest()

print True or False

