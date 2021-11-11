# -*- coding: utf-8 -*-
class fuzhi:
	def assignment(self,**kwargs):
		for key ,value in kwargs.items():
			if type(value) is dict:
				self.assignment(value)
			else:
				if value:
					pass
				else:
					kwargs[key]=getattr(self,key)
		print(kwargs)
		return kwargs

	def diaoyong(self,**kwargs):
		dict_=self.assignment(kwargs)
		url=self.url+dict_['path']
		res=self.if_.post(url,dict_['headers'],dict_['data'])
		print(res.text)
		self.assertEqual(dict_["text"],self.if_.get_msg(res.text),'result')



