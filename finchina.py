# -*- coding: utf-8 -*-
# @Time    : 2021/1/5 11:54 上午
# @File    : finchina.py
# @Software: PyCharm
"""
这个app对于版本要求比较新
如果显示版本不行可以自己去应用市场查看最新是多少版本，替换下面system的版本号
"""

import json
import requests
import hashlib


def get_MD5(text):
    """获取MD5编码后的内容"""
    return hashlib.md5(str(text).lower().encode("utf-8")).hexdigest()


def login():
    """
    获取登录信息token
    :return:
    """
    login_url = "https://app.finchina.com/finchinaAPP/login.action"
    payload = {'password': get_MD5('你的密码'), 'phone': '你的手机号', 'system': 'v5.8, iPhone12'}
    response = requests.post(login_url, data=payload)
    token = json.loads(response.text)['data']['token']
    return token


def index_info(code, token, name):
    """
    首页信息
    :param code:
    :param token:
    :param name:
    :return:
    """

    url = "https://app.finchina.com/finchinaAPP/companyF9/getF9Data.action?type=company&code={}&name={}".format(code,
                                                                                                                name)
    headers = {
        'token': token
    }
    response = requests.get(url, headers=headers)

    print(response.text)


def get_news(code, token, page=1):
    """
    新闻信息
    :param code:
    :param token:
    :param page:
    :return:
    """
    skip = (page - 1) * 15
    payload = {
        'type': 'all',
        'itemArr': code,
        'option': 'new',
        'etime': '',
        'skip': skip,
        'pagesize': '15'
    }
    head = {'token': token}
    response = requests.post(url="https://app.finchina.com/finchinaAPP/getMonitorInfo2.action", params=payload,
                             headers=head)
    print(response.text)

    # 新闻详情页自己组装，好像得slenium访问
    # https://app.finchina.com/finchinaAPP/newsDetail.html?type=news&id=7C1632B6D31171DB989E9ABC789DD73E&sharetype=1&channelCode=1


if __name__ == '__main__':
    token=login()
    # print(token)
    # index_info(code='1050309289',token=token,name='拼多多')
    get_news(code='1050309289', token=token, page=1)
