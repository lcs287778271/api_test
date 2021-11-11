# -*- coding: utf-8 -*-
import configparser
import json
import unittest
from ddt import ddt, file_data
from future.moves import configparser
from ydjw_case.Packaging_method import keyDemo
@ddt
class ApiCases(unittest.TestCase):
    #公共部分提取，作为初始化内容
    @classmethod
    def setUpClass(cls) -> None:
        cls.token = None  # token定义全局变量
        conf = configparser.ConfigParser()
        conf.read('../config/config.ini')
        cls.url = conf.get('DEFAULT', 'url')
        cls.kd = keyDemo()
    def setUp(self) -> None:
        print("开始执行")
    def tearDown(self) -> None:
        print("执行结束")

    # # 1.登录
    @file_data('../data/login.yaml')
    def test_login(self,**kwargs):
        # 测试数据'
        url = self.url + kwargs['path']
        res = self.kd.post(url=url, headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        #获取token
        ApiCases.token=self.kd.get_text(res.text,'token')
        # print(self.token)
        # 断言
        value=self.kd.get_text(res.text,"message")
        self.assertEqual(first=kwargs['text'],second=value,msg="操作失败")

    # 2.获取用户菜单
    @file_data('../data/suerMenu.yaml')
    def test_userMenu(self,**kwargs):
        url = self.url + kwargs['path']
        res =self.kd.post(url=url, headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,"message")
        self.assertEqual(first=kwargs['text'],second=value,msg="操作失败")
    # #3.人员编码登录
    @file_data('../data/loginRybm.yaml')
    def test_loginRybm(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,"message")
        self.assertEqual(first=kwargs['text'],second=value,msg="操作失败")
    # 4.获取短信验证码接口
    @unittest.skip
    @file_data('../data/validCode.yaml')
    def test_validCode(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,"success")
        self.assertEqual(first=kwargs['text'], second=value, msg="操作失败")
    # 5.获取单位数接口
    @file_data('../data/getdeptTree.yaml')
    def test_getdeptTree(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'])
        value=self.kd.get_text(res.text,"message")
        self.assertEqual(first=kwargs['text'],second=value,msg='操作失败')
    # 6.获取部门列表接口
    @file_data('../data/getListByParentCode.yaml')
    def test_getListByParentCode(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,"message")
        self.assertEqual(first=kwargs['text'],second=value,msg="操作失败")
    # 7.获取用户频道接口
    @file_data('../data/getChannelList.yaml')
    def test_getChannelList(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value = self.kd.get_text(res.text, "message")
        self.assertEqual(first=kwargs['text'], second=value, msg="操作失败")
    # # 8.获取人脸核验token接口
    @file_data('../data/getBasicToken.yaml')
    def test_getBasicToken(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value = self.kd.get_text(res.text, "message")
        self.assertEqual(first=kwargs['text'], second=value, msg="操作失败")
    # # 9.身份变更，人身验证
    @file_data('../data/getChangeBasicToken.yaml')
    def test_getChangeBasicToken(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,"message")
        self.assertEqual(first=kwargs['text'],second=value,msg="操作失败")
    # #10获取人脸核验token接口
    @file_data('../data/verifyResult.yaml')
    def test_verifyResult(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,"success")
        self.assertEqual(first=kwargs['text'],second=value,msg="操作失败")
    # 11.获取省市区树形数据
    @file_data('../data/getAreaList.yaml')
    def test_getAreaList(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'])
        value=self.kd.get_text(res.text,"message")
        self.assertEqual(first=kwargs['text'],second=value,msg="操作失败")
    #12退出登录接口
    @file_data('../data/logout.yaml')
    def test_logout(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs["headers"],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs["text"],second=value,msg='操作失败')
    #13.检察官信息接口
    @file_data('../data/queryInquisitorByDeptCode.yaml')
    def test_queryInquisitorByDeptCode(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs["headers"],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs["text"],second=value,msg='操作失败')
    #14.代表委员权限接口
    @file_data('../data/selectUnitRegionByUser.yaml')
    def test_selectUnitRegionByUser(self,**kwargs):
        url = self.url + kwargs['path']
        res = self.kd.post(url=url, headers=kwargs["headers"])
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs["text"], second=value, msg='操作失败')
    #15.根据单位，部门编码查询通讯录列表
    @file_data('../data/selectMailByDeptCode.yaml')
    def test_selectMailByDeptCode(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs["headers"],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作失败')
    #16.通讯录用户详情
    @file_data('../data/selectUserMailDetail.yaml')
    def test_selectUserMailDetail(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作失败')
    # #17. 通讯录模糊查询列表
    @file_data('../data/selectUserMail.yaml')
    def test_selectUserMail(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作失败')
    #18.通讯录省市检察院部门列表查询
    @file_data('../data/queryDeptList.yaml')
    def test_queryDeptList(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs["headers"],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作失败')
    #19.用户菜单树形pc（包含用户角色的菜单）
    @file_data('../data/queryUserMenu.yaml')
    def test_queryUserMenu(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs["headers"],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作失败')
    # #20.获取个人信息
    @file_data('../data/getUserInfo.yaml')
    def test_getUserInfo(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs["headers"],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作失败')
    #21.修改个人信息
    @file_data('../data/updateUser.yaml')
    def test_updateUser(self,**kwargs):
        url = self.url + kwargs['path']
        res = self.kd.post(url=url, headers=kwargs["headers"], data=json.dumps(kwargs['payload']))
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作失败')
    #22.获取律师手机号
    @file_data('../data/getMobile.yaml')
    def test_getMobile(self,**kwargs):
        url = self.url + kwargs['path']
        res = self.kd.post(url=url, headers=kwargs["headers"], data=json.dumps(kwargs['payload']))
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作失败')
    #23. 添加日历提醒
    @file_data('../data/eventRemind.yaml')
    def test_eventRemind(self,**kwargs):
        url = self.url + kwargs['path']
        res = self.kd.post(url=url, headers=kwargs["headers"], data=json.dumps(kwargs['payload']))
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作失败')
    #24. 修改日历提醒
    @file_data('../data/eventRemindUpdate.yaml')
    def test_eventRemindUpdate(self,**kwargs):
        url = self.url + kwargs['path']
        res = self.kd.post(url=url, headers=kwargs["headers"], data=json.dumps(kwargs['payload']))
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作失败')
    #25.查看三个月日历提醒
    @file_data('../data/getByThreeMonth.yaml')
    def test_getByThreeMonth(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作失败')
    #26.查看某日事件列表
    @file_data('../data/getByDay.yaml')
    def test_getByDay(self,**kwargs):
        url=self.url+kwargs['path']
        res = self.kd.post(url=url, headers=kwargs['headers'], data=json.dumps(kwargs['payload']))
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作失败')
    #27.查看日历提醒详情
    @file_data('../data/detail.yaml')
    def test_detail(self,**kwargs):
        url=self.url+kwargs['path']
        res = self.kd.post(url=url, headers=kwargs['headers'], data=json.dumps(kwargs['payload']))
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作失败')
    ##28.1.32 日历提醒删除
    @file_data('../data/deleted.yaml')
    def test_deleted(self, **kwargs):
        url = self.url + kwargs['path']
        res = self.kd.post(url=url, headers=kwargs['headers'], data=json.dumps(kwargs['payload']))
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作失败')
    #29.查看事件提醒历史
    @file_data('../data/getHistory.yaml')
    def test_getHistory(self,**kwargs):
        url=self.url+kwargs['path']
        res = self.kd.post(url=url, headers=kwargs['headers'], data=json.dumps(kwargs['payload']))
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作失败')
    #30.代表委员名册分页接口
    @file_data('../data/represent_getPage.yaml')
    def test_represent_getPage(self, **kwargs):
        url = self.url + kwargs['path']
        res = self.kd.post(url=url, headers=kwargs['headers'], data=json.dumps(kwargs['payload']))
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作失败')
    #31.代表委员层级接口
    @file_data('../data/represent_getLevels.yaml')
    def test_represent_getLevels(self, **kwargs):
        url = self.url + kwargs['path']
        res = self.kd.post(url=url, headers=kwargs['headers'])
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作失败')
    #32.查询操作人单位树
    @file_data('../data/dept_queryDept.yaml')
    def test_dept_queryDept(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作失败')
    #33.获取院下所有人员树结构
    @file_data('../data/getUserInfoDeptList.yaml')
    def test_getUserInfoDeptList(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'])
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作失败')
    #34.获取院下所有人员树结构(根据token获取当前登录下的)
    @file_data('../data/getUserInfoDeptListPc.yaml')
    def test_getUserInfoDeptListPc(self, **kwargs):
        url = self.url + kwargs['path']
        res = self.kd.post(url=url, headers=kwargs['headers'])
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作失败')
    #35.获取院下所有人员树结构(根据单位编号)
    @file_data('../data/getUserInfoDeptListByDeptCode.yaml')
    def test_getUserInfoDeptListByDeptCode(self, **kwargs):
        url = self.url + kwargs['path']
        res = self.kd.post(url=url, headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作失败')
    #36.根据用户获取权限
    @file_data('../data/getRoles.yaml')
    def test_getRoles(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作失败')
    #37.根据名字搜索单位下检察官
    @file_data('../data/queryListByName.yaml')
    def test_queryListByName(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作失败')
    #38.首页数据导航条
    @file_data('../data/dataMenu_tree.yaml')
    def test_dataMenu_tree(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'])
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作失败')
    #39.用户列表pc
    @file_data('../data/user_listPc.yaml')
    def test_user_listPc(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作失败')
    #40.验证姓名和手机号码是否已注册
    @file_data('../data/validNameMobile.yaml')
    def test_validNameMobile(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作失败')
    #41.法院单位下拉树
    @file_data('../data/deptCourt_getTree.yaml')
    def test_deptCourt_getTree(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'])
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作失败')
    #42.菜单排序-添加
    @file_data('../data/menu_addCustom.yaml')
    def test_menu_addCustom(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作失败')
    #43.菜单排序-集合
    @file_data('../data/getCustomList.yaml')
    def test_getCustomList(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作失败')
    #44.获取院下一级部门所有人员树结构
    @file_data('../data/getFistLevelUserInfoDeptListPc.yaml')
    def test_getFistLevelUserInfoDeptListPc(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'])
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作失败')
    #45.政务用户登录接口
    @file_data("../data/govLogin.yaml")
    def test_govLogin(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作失败')
    #46.根据单位code获取本单位及下属单位列表
    @file_data("../data/queryListForDeptCode.yaml")
    def test_queryListForDeptCode(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作失败')
    #47.人民监督员列表
    @file_data("../data/peopleSupervisor_nameList.yaml")
    def test_peopleSupervisor_nameList(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作失败')
    #48.人民监督员筛选列表
    @file_data("../data/judicialBureauList.yaml")
    def test_judicialBureauList(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'])
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作失败')
    #49.通过姓名获取律师集合
    @file_data("../data/getByNameList.yaml")
    def test_getByNameList(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作失败')
    #50.通过单位编号和姓名获取检察官信息
    @file_data("../data/getInquisitorByDeptCodeAndName.yaml")
    def test_getInquisitorByDeptCodeAndName(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作失败')
    #51.律师详情
    @file_data("../data/lawyer_details.yaml")
    def test_lawyer_details(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作失败')
    #52.查询检察院/部门树
    @file_data("../data/queryLevelDept.yaml")
    def test_queryLevelDept(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作失败')
    # 53.注册时，人身认证, 阿里云金融级人脸验证获取 certifyId
    @file_data("../data/user_getCertifyId.yaml")
    def test_user_getCertifyId(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作失败')
    #54.更换身份时，人身认证,前端调用,阿里云金融级人脸验证获取 certifyId
    @file_data("../data/getChangeCertifyId.yaml")
    def test_getChangeCertifyId(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作失败')
    #55.获取人脸验证结果接口
    @file_data("../data/describeFaceVerify.yaml")
    def test_describeFaceVerify(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'success')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作失败')
    #56.纯服务端小程序实人认证接口
    @file_data("../data/contrastFaceVerify.yaml")
    def test_contrastFaceVerify(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作失败')
    #57.验证用户是否注册
    @file_data("../data/validationRegister.yaml")
    def test_validationRegister(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作失败')
    #58.pc用户密码登录接口
    @file_data("../data/pcLogin_login.yaml")
    def test_pcLogin_login(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作失败')
    #59.pc修改密码验证手机号
    @file_data('../data/pcLogin_checkMobile.yaml')
    def test_pcLogin_checkMobile(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作失败')
    #60. pc修改密码验证用户名字
    @file_data('../data/pcLogin_checkName.yaml')
    def test_pcLogin_checkName(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作失败')
    # 61.app验证身份证号
    @file_data('../data/changeMobile_checkIdCard.yaml')
    def test_changeMobile_checkIdCard(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作失败')
    #62.app更新身份证号
    @file_data('../data/changeMobile_saveIdCard.yaml')
    def test_changeMobile_saveIdCard(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作失败')
    # 63.app验证手机号
    @file_data('../data/changeMobile_checkMobile.yaml')
    def test_changeMobile_checkMobile(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作失败')
    # 64.app确定更换-验证验证码
    @file_data('../data/changeMobile_checkValidCode.yaml')
    def test_changeMobile_checkValidCode(self, **kwargs):
        url = self.url + kwargs['path']
        res = self.kd.post(url=url, headers=kwargs['headers'], data=json.dumps(kwargs['payload']))
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作失败')
    # 65.app工作台菜单集合
    @file_data('../data/appMenu_workBenchedList.yaml')
    def test_appMenu_workBenchedList(self, **kwargs):
        url = self.url + kwargs['path']
        res = self.kd.post(url=url, headers=kwargs['headers'], data=json.dumps(kwargs['payload']))
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作失败')
    # 66.根据区域名字获取编码
    @file_data('../data/appMenu_queryAreaId.yaml')
    def test_appMenu_queryAreaId(self, **kwargs):
        url = self.url + kwargs['path']
        res = self.kd.post(url=url, headers=kwargs['headers'], data=json.dumps(kwargs['payload']))
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作失败')
    # 67.app未登录菜单集合
    @file_data('../data/appMenu_unLoginMenuList.yaml')
    def test_appMenu_unLoginMenuList(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作失败')
    # 68.app清空菜单角标数量
    @file_data('../data/subscript_clear.yaml')
    def test_subscript_clear(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作成功')
    # 69.查询申请人监督员信息
    @file_data('../data/peopleSupervisor/peopleSupervisorMessage.yaml')
    def test_peopleSupervisorMessage(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'])
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作成功')
    #70.pc/app监督类型/拟监督案件名称集合
    @file_data('../data/peopleSupervisor/appealTypeCaseNameList.yaml')
    def test_appealTypeCaseNameList(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'])
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作成功')
    #71. app监督诉求联名查询监督员集合
    @file_data('../data/peopleSupervisor/peopleSupervisorList.yaml')
    def test_peopleSupervisorList(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作成功')
    # 72.app监督诉求新增
    @file_data('../data/peopleSupervisor/insert.yaml')
    def test_insert(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作成功')
    # 73.根据类型查询监督员活动下拉框接口
    @file_data('../data/peopleSupervisor/activity_selectType.yaml')
    def test_activity_selectType(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作成功')
    #74.添加监督员反馈记录接口
    @unittest.skip
    @file_data('../data/peopleSupervisor/addSupervisionSinceFeedback.yaml')
    def test_addSupervisionSinceFeedback(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作成功')
    # 75.查看监督员反馈详情接口
    @unittest.skip
    @file_data('../data/peopleSupervisor/selectSinceFeedbackDetails.yaml')
    def test_selectSinceFeedbackDetails(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作成功')
    # 76.app监督诉求列表
    @file_data('../data/peopleSupervisor/pageApp.yaml')
    def test_pageApp(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作成功')
    # 77.pc/app监督诉求详情
    @unittest.skip
    @file_data('../data/peopleSupervisor/details.yaml')
    def test_details(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'code')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作成功')
    # 78.app确认/拒绝联名
    @unittest.skip
    @file_data('../data/peopleSupervisor/jointOrNot.yaml')
    def test_jointOrNot(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作成功')
    # 79.pc监督诉求列表
    @file_data('../data/peopleSupervisor/pagePc.yaml')
    def test_pagePc(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作成功')
    #80.补选监督员可被替换列表
    @file_data('../data/peopleSupervisor/selectReplaceSupervision.yaml')
    def test_selectReplaceSupervision(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作成功')
    # 81.查看履职反馈监督员分页列表详情接口
    @file_data('../data/peopleSupervisor/selectSinceFeedbackPersonDetails.yaml')
    def test_selectSinceFeedbackPersonDetails(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作成功')
    # 82.pc流转单位
    @unittest.skip
    @file_data('../data/peopleSupervisor/supervisionAppeal_updateDept.yaml')
    def test_supervisionAppeal_updateDept(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作成功')
    # 83.pc受理反馈/拒绝
    @unittest.skip
    @file_data('../data/peopleSupervisor/acceptance.yaml')
    def test_acceptance(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作成功')
    #84.编辑反馈活动接口
    @unittest.skip
    @file_data('../data/peopleSupervisor/updateFeedbackActivity.yaml')
    def test_updateFeedbackActivity(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作成功')
    # 85.查询反馈活动结果中需要填写采纳意见的监督员
    @file_data('../data/peopleSupervisor/selectFeedbackActivityPerson.yaml')
    def test_selectFeedbackActivityPerson(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作成功')
    # #86.新增监督活动
    @file_data('../data/peopleSupervisor/supervision_activity_add.yaml')
    def test_supervision_activity_add(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作成功')
    # 87. 监督活动管理分页
    @file_data('../data/peopleSupervisor/supervision_activity_page.yaml')
    def test_supervision_activity_page(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作成功')
    # 88.监督活动明细
    @file_data('../data/peopleSupervisor/supervision_activity_details.yaml')
    def test_supervision_activity_details(self, **kwargs):
        url = self.url + kwargs['path']
        res = self.kd.post(url=url, headers=kwargs['headers'], data=json.dumps(kwargs['payload']))
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作成功')
    # 89.活动监督审核
    @unittest.skip
    @file_data('../data/peopleSupervisor/supervision_activity_audit.yaml')
    def test_supervision_activity_audit(self, **kwargs):
        url = self.url + kwargs['path']
        res = self.kd.post(url=url, headers=kwargs['headers'], data=json.dumps(kwargs['payload']))
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作成功')
    # 90.活动监督人民监督员page
    @file_data('../data/peopleSupervisor/supervision_activity_personPage.yaml')
    def test_supervision_activity_personPage(self, **kwargs):
        url = self.url + kwargs['path']
        res = self.kd.post(url=url, headers=kwargs['headers'], data=json.dumps(kwargs['payload']))
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作成功')
    #91.监督活动追踪分页
    @file_data('../data/peopleSupervisor/supervision_activity_trackPage.yaml')
    def test_supervision_activity_trackPage(self, **kwargs):
        url = self.url + kwargs['path']
        res = self.kd.post(url=url, headers=kwargs['headers'], data=json.dumps(kwargs['payload']))
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作成功')
    # 92.监督活动追踪明细H5
    @file_data('../data/peopleSupervisor/supervision_activity_trackDetails.yaml')
    def test_supervision_activity_trackDetails(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作成功')
    # 93.监督活动通知 分页
    @file_data('../data/peopleSupervisor/supervision_activity_noticePage.yaml')
    def test_supervision_activity_noticePage(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作成功')
    #94.pc替换监督员
    @file_data('../data/peopleSupervisor/changeSupervision.yaml')
    def test_changeSupervision(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作成功')
    # #95.用印完成
    @file_data('../data/peopleSupervisor/supervision_activity_seal.yaml')
    def test_supervision_activity_seal(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作成功')
    #96. 同意/拒绝参加活动
    @file_data('../data/peopleSupervisor/supervision_activity_personAgree.yaml')
    def test_supervision_activity_personAgree(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作成功')
    #97.预览文书信息
    @file_data('../data/peopleSupervisor/supervision_activity_preview.yaml')
    def test_supervision_activity_preview(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'])
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作成功')
    #98.发起异议
    @file_data('../data/peopleSupervisor/supervision_represent_sponsor.yaml')
    def test_supervision_represent_sponsor(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作成功')
    #99.h5异议分页
    @file_data('../data/peopleSupervisor/supervision_represent_h5Page.yaml')
    def test_supervision_represent_h5Page(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作成功')
    #100.h5异议详情
    @file_data('../data/peopleSupervisor/supervision_represent_h5Details.yaml')
    def test_supervision_represent_h5Details(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作成功')
    # 101. 异议反馈
    @file_data('../data/peopleSupervisor/supervision_represent_feedback.yaml')
    def test_supervision_represent_feedback(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        print(res.text)
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作成功')
    # 102.pc异议分页
    @file_data('../data/peopleSupervisor/supervision_represent_pcPage.yaml')
    def test_supervision_represent_pcPage(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作成功')
    # 103.pc异议详情
    @file_data('../data/peopleSupervisor/supervision_represent_pcDetails.yaml')
    def test_supervision_represent_pcDetails(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作成功')
    #104.新增监督活动公开信息
    @file_data('../data/peopleSupervisor/supervision_public_add.yaml')
    def test_supervision_public_add(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作成功')
    #105.监督活动公开信息pc分页
    @file_data('../data/peopleSupervisor/supervision_public_pcPage.yaml')
    def test_supervision_public_pcPage(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作成功')
    # #106.监督活动公开信息h5分页
    @file_data('../data/peopleSupervisor/supervision_public_h5Page.yaml')
    def test_supervision_public_h5Page(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作成功')
    #107.监督活动公开详情
    @file_data('../data/peopleSupervisor/supervision_public_details.yaml')
    def test_supervision_public_details(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作成功')
    #108.监督活动公开信息更新删除
    @file_data('../data/peopleSupervisor/supervision_public_update.yaml')
    def test_supervision_public_update(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作成功')
    # 109.手动再次推送
    @unittest.skip
    @file_data('../data/peopleSupervisor/supervision_activity_pushAgain.yaml')
    def test_supervision_activity_pushAgain(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作成功')
    #110.浙里办用户登录接口
    @file_data('../data/login_idCardOrMobile.yaml')
    def test_login_idCardOrMobile(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作成功')
    # 111.预约检察官
    @file_data('../data/case_related/appointmentInquisitor.yaml')
    def test_appointmentInquisitor(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作成功')
    #112.预约检察官分页列表
    @file_data('../data/case_related/appointmentListByForPage.yaml')
    def test_appointmentListByForPage(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作成功')
    # 113.预约检察官详情
    @file_data('../data/case_related/queryDetailByCode.yaml')
    def test_queryDetailByCode(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作成功')
    #114.预约检察官约见记录
    @file_data('../data/case_related/queryRecordListByForPage.yaml')
    def test_queryRecordListByForPage(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作成功')
    # 115.预约检察官审批
    @unittest.skip
    @file_data('../data/case_related/appointmentApproval.yaml')
    def test_appointmentApproval(self, **kwargs):
        url = self.url + kwargs['path']
        res = self.kd.post(url=url, headers=kwargs['headers'], data=json.dumps(kwargs['payload']))
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作成功')
    #116.卷宗列表
    @file_data('../data/case_related/casesArchiveListForPage.yaml')
    def test_casesArchiveListForPage(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作成功')
    # 117.卷宗查看
    @file_data('../data/case_related/addCasesBindApplication.yaml')
    def test_addCasesBindApplication(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作成功')
    #118.案件绑定修改
    @file_data('../data/case_related/CasesBindController_update.yaml')
    def test_CasesBindController_update(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作成功')
    #119.案件绑定 批准驳回接口
    @file_data('../data/case_related/updateRejectApplication.yaml')
    def test_updateRejectApplication(self,**kwargs):
        url=self.url+kwargs['path']
        res=self.kd.post(url=url,headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value=self.kd.get_text(res.text,'message')
        self.assertEqual(first=kwargs['text'],second=value,msg='操作成功')
    #120. 律师模块根据案件编号获取案件详情
    @file_data('../data/case_related/detailLawyer.yaml')
    def test_detailLawyer(self, **kwargs):
        url = self.url + kwargs['path']
        res = self.kd.post(url=url, headers=kwargs['headers'], data=json.dumps(kwargs['payload']))
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作成功')
    #121.通过当事人证件号获取案件信息
    @file_data('../data/case_related/casesByIdCardPage.yaml')
    def test_casesByIdCardPage(self, **kwargs):
        url = self.url + kwargs['path']
        res = self.kd.post(url=url, headers=kwargs['headers'], data=json.dumps(kwargs['payload']))
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作成功')
    #122.一案一查新增
    @file_data('../data/case_related/addOneQuery.yaml')
    def test_addOneQuery(self, **kwargs):
        url = self.url + kwargs['path']
        res = self.kd.post(url=url, headers=kwargs['headers'], data=json.dumps(kwargs['payload']))
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作成功')
    #123. 一案一查分页查询
    @file_data('../data/case_related/queryApplyListForPage.yaml')
    def test_queryApplyListForPage(self, **kwargs):
        url = self.url + kwargs['path']
        res = self.kd.post(url=url, headers=kwargs['headers'], data=json.dumps(kwargs['payload']))
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作成功')
    #124.一案一查审批
    @file_data('../data/case_related/oneQueryApproval.yaml')
    def test_oneQueryApproval(self, **kwargs):
        url = self.url + kwargs['path']
        res = self.kd.post(url=url, headers=kwargs['headers'], data=json.dumps(kwargs['payload']))
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作成功')
    #125.一案一查详情
    @file_data('../data/case_related/getOneQueryDetail.yaml')
    def test_getOneQueryDetail(self, **kwargs):
        url = self.url + kwargs['path']
        res = self.kd.post(url=url, headers=kwargs['headers'], data=json.dumps(kwargs['payload']))
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作成功')
    #126.案件跟踪列表
    @file_data('../data/case_related/getCasesTrackListForPage.yaml')
    def test_getCasesTrackListForPage(self, **kwargs):
        url = self.url + kwargs['path']
        res = self.kd.post(url=url, headers=kwargs['headers'], data=json.dumps(kwargs['payload']))
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作成功')
    #127.案件申请绑定列表接口
    @file_data('../data/case_related/getCasesBindList.yaml')
    def test_getCasesBindList(self, **kwargs):
        url = self.url + kwargs['path']
        res = self.kd.post(url=url, headers=kwargs['headers'], data=json.dumps(kwargs['payload']))
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作成功')
    #128.案件绑定结果列表
    @file_data('../data/case_related/selectReviewResultList.yaml')
    def test_selectReviewResultList(self, **kwargs):
        url = self.url + kwargs['path']
        res = self.kd.post(url=url, headers=kwargs['headers'], data=json.dumps(kwargs['payload']))
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作成功')
    #130.案件类型列表
    @file_data('../data/case_related/selectCasesTypeList.yaml')
    def test_selectCasesTypeList(self, **kwargs):
        url = self.url + kwargs['path']
        res = self.kd.post(url=url, headers=kwargs['headers'])
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作成功')
    #131.获取已绑定律师列表
    @file_data('../data/case_related/selectLawyerBound.yaml')
    def test_selectLawyerBound(self, **kwargs):
        url = self.url + kwargs['path']
        res = self.kd.post(url=url, headers=kwargs['headers'],data=json.dumps(kwargs['payload']))
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作成功')
    #132.解除已绑定案件律师
    @file_data('../data/case_related/relieveBoundByLawyer.yaml')
    def test_relieveBoundByLawyer(self, **kwargs):
        url = self.url + kwargs['path']
        res = self.kd.post(url=url, headers=kwargs['headers'], data=json.dumps(kwargs['payload']))
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作成功')
    #133. 案件预审通过
    @file_data('../data/case_related/updatePretrialPassed.yaml')
    def test_updatePretrialPassed(self, **kwargs):
        url = self.url + kwargs['path']
        res = self.kd.post(url=url, headers=kwargs['headers'], data=json.dumps(kwargs['payload']))
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作成功')
    #134.PC端案件审批列表
    @file_data('../data/case_related/selectManagerCasesBindList.yaml')
    def test_selectManagerCasesBindList(self, **kwargs):
        url = self.url + kwargs['path']
        res = self.kd.post(url=url, headers=kwargs['headers'], data=json.dumps(kwargs['payload']))
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作成功')
    #135.案件绑定详情
    @file_data('../data/case_related/selectManagerCasesBindDetail.yaml')
    def test_selectManagerCasesBindDetail(self, **kwargs):
        url = self.url + kwargs['path']
        res = self.kd.post(url=url, headers=kwargs['headers'], data=json.dumps(kwargs['payload']))
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作成功')
    #136.获取承办检察官案件列表
    @file_data('../data/case_related/queryByAuditor.yaml')
    def test_queryByAuditor(self, **kwargs):
        url = self.url + kwargs['path']
        res = self.kd.post(url=url, headers=kwargs['headers'], data=json.dumps(kwargs['payload']))
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作成功')
    #137.案件绑定结果列表-新
    @file_data('../data/case_related/selectCasesBindResultList.yaml')
    def test_selectCasesBindResultList(self, **kwargs):
        url = self.url + kwargs['path']
        res = self.kd.post(url=url, headers=kwargs['headers'], data=json.dumps(kwargs['payload']))
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作成功')
    #138.获取案件已绑定的律师数
    @file_data('../data/case_related/getCasesBindLawyerNum.yaml')
    def test_getCasesBindLawyerNum(self, **kwargs):
        url = self.url + kwargs['path']
        res = self.kd.post(url=url, headers=kwargs['headers'], data=json.dumps(kwargs['payload']))
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作成功')
    #139.根据案件编号获取案件摘要字段
    @file_data('../data/case_related/getCasesAbstract.yaml')
    def test_getCasesAbstract(self, **kwargs):
        url = self.url + kwargs['path']
        res = self.kd.post(url=url, headers=kwargs['headers'], data=json.dumps(kwargs['payload']))
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作成功')
    #140.获取案件详情(pc认罪认罚与远程讯问使用)
    @file_data('../data/case_related/queryDetail.yaml')
    def test_queryDetail(self, **kwargs):
        url = self.url + kwargs['path']
        res = self.kd.post(url=url, headers=kwargs['headers'], data=json.dumps(kwargs['payload']))
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作成功')
    #141.案件绑定列表(助理)
    @file_data('../data/case_related/selectCasesBindList.yaml')
    def test_selectCasesBindList(self, **kwargs):
        url = self.url + kwargs['path']
        res = self.kd.post(url=url, headers=kwargs['headers'], data=json.dumps(kwargs['payload']))
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作成功')
    #142.案件绑定新增/更换助理
    @unittest.skip
    @file_data('../data/case_related/insertCasesAssistant.yaml')
    def test_insertCasesAssistant(self, **kwargs):
        url = self.url + kwargs['path']
        res = self.kd.post(url=url, headers=kwargs['headers'], data=json.dumps(kwargs['payload']))
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作成功')
    #143.助理列表
    @file_data('../data/case_related/queryAssistantList.yaml')
    def test_queryAssistantList(self, **kwargs):
        url = self.url + kwargs['path']
        res = self.kd.post(url=url, headers=kwargs['headers'], data=json.dumps(kwargs['payload']))
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作成功')
    #144.删除助理
    @unittest.skip
    @file_data('../data/case_related/deletedAssistant.yaml')
    def test_deletedAssistant(self, **kwargs):
        url = self.url + kwargs['path']
        res = self.kd.post(url=url, headers=kwargs['headers'], data=json.dumps(kwargs['payload']))
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作成功')
    #145.根据案件信息获取案件详情-检察官助理页面
    @file_data('../data/case_related/detailAssistant.yaml')
    def test_detailAssistant(self, **kwargs):
        url = self.url + kwargs['path']
        res = self.kd.post(url=url, headers=kwargs['headers'], data=json.dumps(kwargs['payload']))
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作成功')
    #146.一案一查分页查询 新
    @file_data('../data/case_related/queryCasesOneQueryList.yaml')
    def test_queryCasesOneQueryList(self, **kwargs):
        url = self.url + kwargs['path']
        res = self.kd.post(url=url, headers=kwargs['headers'], data=json.dumps(kwargs['payload']))
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作成功')
    #147.获取案件状态列表新
    @file_data('../data/case_related/queryStatusList.yaml')
    def test_queryStatusList(self, **kwargs):
        url = self.url + kwargs['path']
        res = self.kd.post(url=url, headers=kwargs['headers'])
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作成功')
    #148.获取案件状态列表新
    @file_data('../data/case_related/CasesBindController_queryStatusList.yaml')
    def test_CasesBindController_queryStatusList(self, **kwargs):
        url = self.url + kwargs['path']
        res = self.kd.post(url=url, headers=kwargs['headers'])
        value = self.kd.get_text(res.text, 'message')
        self.assertEqual(first=kwargs['text'], second=value, msg='操作成功')


if __name__ == '__main__':
    unittest.main()