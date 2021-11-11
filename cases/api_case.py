# -*- coding: utf-8 -*-
import configparser
import unittest
from ddt import ddt, file_data
from future.moves import configparser
from ydjw_case.Packaging_method import keyDemo


# 创建一个测试框架
@ddt
class ApiCases(unittest.TestCase):
	# 公共部分提取，作为初始化
	@classmethod
	def setUpClass(cls) -> None:
		cls.token = None
		conf = configparser.ConfigParser()
		conf.read('../config/config.ini')
		cls.url = conf.get('DEFAULT', 'url')
		cls.kd = keyDemo()

	def setUp(self) -> None:
		pass

	# 测试数据
	@file_data('../data/login.yaml')
	def test_1_api_demo(self, **kwargs):
		# 实例化需要内容
		url = self.url + kwargs['path']
		# 接口测试
		res = self.kd.post(url=url, data=kwargs['data'])
		print(res.text)
		# 断言
		value = self.kd.get_text(res.text, 'name')
		print(value)
		self.assertEqual(first=kwargs["text"], second=value, msg="获取失败")

	@file_data('../data/login.yaml')
	def test_2_login(self, **kwargs):
		url = self.url + kwargs['path']
		# 访问login接口登录操作
		res = self.kd.post(url=url, headers=kwargs['headers'], data=kwargs['data'])
		# 提取msg内容，作为断言
		value = self.kd.get_text(res.text, 'msg')
		ApiCases.token = self.kd.get_text(res.text, 'token')
		print(self.token)
		# 断言
		self.assertEqual(first=kwargs["text"], second=value, msg="获取失败")

	@file_data('../data/login.yaml')
	def test_3_userinfo(self, **kwargs):
		url = self.url + kwargs['path']
		headers = kwargs['headers']
		headers['token'] = self.token
		res = self.kd.get(url=url, headers=headers)


if __name__ != '__main__':
	unittest.main()
