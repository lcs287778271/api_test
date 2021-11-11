# -*- coding: utf-8 -*-
import os
import unittest
from BSTestRunner import BSTestRunner
from ydjw_case.ydjw import ApiCases
# ****************************************
# 执行所有用例，测试报告
def report_1():
	report_name="测试报告"
	report_title="移动检务"
	report_desc="接口自动化测试报告"
	report_path=r"D:\python文件\api接口\report\report"
	report_file=report_path+'report.html'
	# 判断文件夹是否存在
	if not os.path.exists(report_path):
		os.mkdir(report_path)
	else:
		pass
	with open(report_file,"wb") as report:
		suite = unittest.TestSuite()
		suite.addTest(unittest.TestLoader().loadTestsFromTestCase(ApiCases))
		runner=BSTestRunner(stream=report,title=report_title, description=report_desc, )
		runner.run(suite)
#*************************************************************
#单用例运行
def test_case():
	suite1 = unittest.TestSuite()
	for method in dir(ApiCases):
		if method.startswith("test_CasesBindController_queryStatusList"):
			suite1.addTest(ApiCases(method))
	unittest.TextTestRunner().run(suite1)
#*********************************************************
if __name__ == '__main__':
	# report_1()
	test_case()

