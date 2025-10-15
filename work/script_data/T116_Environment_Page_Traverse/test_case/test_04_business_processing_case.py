import allure
import pytest

from work.script_data.T116_Environment_Page_Traverse.Page_Object_Class.business_processing_page import \
    Employee_Management_Page, Social_Security_And_Housing_Fund_Processing_Page, Commercial_Insurance_Processing_Page, \
    Service_Handling_Page, Ordinary_Salary_Page, Yuncheng_Business_Page, Supplier_Payroll_Page, \
    Personal_Proxy_Payment_Page, Payment_Request_Page, Employee_Affairs_Handling_Center_Page, \
    Work_Injury_And_Dispute_Management_Center_Page, Business_Processing_Tab
from work.script_data.T116_Environment_Page_Traverse.Base_Class.Base_Page import BasePage


# @pytest.mark.smoke
# 业务办理页面
@allure.epic("项目名称：邦芒综合服务平台页面遍历")
class Test_04_case:

    @allure.feature("业务办理")
    @allure.story("业务办理页面")
    @allure.title("进入业务办理页面")
    def test_Business_Processing_Page_01(self, all_case_fixture):       # 进入业务办理Tab
        with allure.step("步骤一：进入业务办理页面"):
            Business_Processing_Tab(all_case_fixture).Business_Processing_Tab()

    @allure.feature("业务办理")
    @allure.story("员工管理页面")
    @allure.title("进入员工管理页面")
    def test_Business_Processing_Page_02(self, all_case_fixture):       # 员工管理模块遍历
        with allure.step("步骤二：遍历员工管理页面"):
            Employee_Management_Page(all_case_fixture).Employee_Management()

    @allure.feature("业务办理")
    @allure.story("社保公积金办理页面")
    @allure.title("进入社保公积金办理页面")
    def test_Business_Processing_Page_03(self, all_case_fixture):       # 社保公积金办理模块遍历
        with allure.step("步骤三：遍历社保公积金办理页面"):
            Social_Security_And_Housing_Fund_Processing_Page(all_case_fixture).Social_Security_And_Housing_Fund_Processing()

    @allure.feature("业务办理")
    @allure.story("商业险办理页面")
    @allure.title("进入商业险办理页面")
    def test_Business_Processing_Page_04(self, all_case_fixture):       # 商业险办理模块遍历
        with allure.step("步骤四：遍历商业险办理页面"):
            Commercial_Insurance_Processing_Page(all_case_fixture).Commercial_Insurance_Processing()

    @allure.feature("业务办理")
    @allure.story("服务办理页面")
    @allure.title("进入服务办理页面")
    def test_Business_Processing_Page_05(self, all_case_fixture):       # 服务办理模块遍历
        with allure.step("步骤五：遍历服务办理页面"):
            Service_Handling_Page(all_case_fixture).Service_Handling_Page()

    @allure.feature("业务办理")
    @allure.story("普通工资页面")
    @allure.title("进入普通工资页面")
    def test_Business_Processing_Page_06(self, all_case_fixture):       # 普通工资模块遍历
        with allure.step("步骤六：遍历普通工资页面"):
            Ordinary_Salary_Page(all_case_fixture).Personnel_Specific_Deduction()

    @allure.feature("业务办理")
    @allure.story("数据校验页面")
    @allure.title("进入数据校验页面")
    def test_Business_Processing_Page_07(self, all_case_fixture):       # 数据校验模块遍历
        with allure.step("步骤七：遍历数据校验页面"):
            Ordinary_Salary_Page(all_case_fixture).Data_Validation()

    @allure.feature("业务办理")
    @allure.story("数据配置页面")
    @allure.title("进入数据配置页面")
    def test_Business_Processing_Page_08(self, all_case_fixture):       # 数据配置模块遍历
        with allure.step("步骤八：遍历数据配置页面"):

            Ordinary_Salary_Page(all_case_fixture).Data_Configuration()

    @allure.feature("业务办理")
    @allure.story("薪税申请页面")
    @allure.title("进入薪税申请页面")
    def test_Business_Processing_Page_09(self, all_case_fixture):       # 薪税申请模块遍历
        with allure.step("步骤九：遍历薪税申请页面"):
            Ordinary_Salary_Page(all_case_fixture).Salary_Tax_Application()

    @allure.feature("业务办理")
    @allure.story("薪资发放页面")
    @allure.title("进入薪资发放页面")
    def test_Business_Processing_Page_10(self, all_case_fixture):       # 薪资发放模块遍历
        with allure.step("步骤十：遍历薪资发放页面"):
            Ordinary_Salary_Page(all_case_fixture).Salary_Tax_Payment()

    @allure.feature("业务办理")
    @allure.story("薪税查询页面")
    @allure.title("进入薪税查询页面")
    def test_Business_Processing_Page_11(self, all_case_fixture):       # 薪税查询模块遍历
        with allure.step("步骤十一：遍历薪税查询页面"):
            Ordinary_Salary_Page(all_case_fixture).Salary_Tax_Inquiry()

    @allure.feature("业务办理")
    @allure.story("个税管理页面")
    @allure.title("进入个税管理页面")
    def test_Business_Processing_Page_12(self, all_case_fixture):       # 个税管理块遍历
        with allure.step("步骤十二：遍历个税管理页面"):
            Ordinary_Salary_Page(all_case_fixture).Personal_Income_Tax_Management()

    @allure.feature("业务办理")
    @allure.story("昀丞业务页面")
    @allure.title("进入昀丞业务页面")
    def test_Business_Processing_Page_13(self, all_case_fixture):       # 昀丞业务遍历
        with allure.step("步骤十三：遍历昀丞业务页面"):
            Yuncheng_Business_Page(all_case_fixture).Yuncheng_Business()

    @allure.feature("业务办理")
    @allure.story("供应商发薪页面")
    @allure.title("进入供应商发薪页面")
    def test_Business_Processing_Page_14(self, all_case_fixture):       # 供应商发薪遍历
        with allure.step("步骤十四：遍历供应商发薪页面"):
            Supplier_Payroll_Page(all_case_fixture).Supplier_Payroll()

    @allure.feature("业务办理")
    @allure.story("个人代缴页面")
    @allure.title("进入个人代缴页面")
    def test_Business_Processing_Page_15(self, all_case_fixture):       # 个人代缴遍历
        with allure.step("步骤十五：遍历个人代缴页面"):
            Personal_Proxy_Payment_Page(all_case_fixture).Personal_Proxy_Payment()

    @allure.feature("业务办理")
    @allure.story("请款单页面")
    @allure.title("进入请款单页面")
    def test_Business_Processing_Page_16(self, all_case_fixture):       # 请款单
        with allure.step("步骤十六：遍历请款单页面"):
            Payment_Request_Page(all_case_fixture).Payment_Request()

    @allure.feature("业务办理")
    @allure.story("员工事务性办理中心页面")
    @allure.title("进入员工事务性办理中心页面")
    def test_Business_Processing_Page_17(self, all_case_fixture):       # 员工事务性办理中心
        with allure.step("步骤十七：遍历员工事务性办理中心页面"):

            Employee_Affairs_Handling_Center_Page(all_case_fixture).Employee_Affairs_Handling_Center()

    @allure.feature("业务办理")
    @allure.story("工伤/纠纷管理中心页面")
    @allure.title("进入工伤/纠纷管理中心页面")
    def test_Business_Processing_Page_18(self, all_case_fixture):       # 展开工伤/纠纷管理中心
        with allure.step("步骤十八：遍历工伤/纠纷管理中心页面"):
            Work_Injury_And_Dispute_Management_Center_Page(all_case_fixture).Work_Injury_And_Dispute_Management_Center()

    # def test_Business_Processing_quit_Webdriver(self, all_case_fixture):  # 退出浏览器，释放资源
    #     BasePage(all_case_fixture).quit_Webdriver()

