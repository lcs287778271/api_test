# -*- coding: utf-8 -*-
import configparser
import json
import uuid
from time import time
import jsonpath
import requests

class keyDemo:
    # get请求方法
    @staticmethod
    def get(url, headers=None, param=None) :
        return requests.get(url=url, headers=headers, params=param)
    # post请求方法
    @staticmethod
    def post(url, headers=None, data=None) :
        timestamp=int(round(time() * 1000))
        guid = uuid.uuid1()
        conf = configparser.ConfigParser()
        conf.read('../config/config.ini')
        url += "?appKey=%s&nonce=%s&timestamp=%s&sign=%s"\
               %(conf.get('DEFAULT', 'appKey'),guid,timestamp,conf.get('DEFAULT', 'sign'))

        # if data is not None:
        #     data = self.json_dump(data)
        return requests.post(url=url, headers=headers, data=data)

    # 参数转换json格式
    @staticmethod
    def json_dumps(data):
        return json.dumps(data)

    # 校验字段获取方法
    @staticmethod
    def get_text(res, key) :
        if res is not None :
            try :
                # 将res文本转换为json 通过jsonpath解析获取指定的key的value值
                text = json.loads(res)
                # jsonpath获取结果是list类型的值，如果获取失败是False
                value = jsonpath.jsonpath(text, '$..{0}'.format(key))

                if value :
                    # 将list转换成str格式
                    if len(value) == 1 :
                        return value[0]
                    else :
                        return value
            except Exception as e :
                return e
        else :
            return None


# noinspection NonAsciiCharacters
def ydjw():
    return None