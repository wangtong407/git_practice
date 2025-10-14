import allure
import pytest

from work.conftest import all_case_fixture
from work.script_data.T116_Environment_Page_Traverse.Page_Object_Class.business_center_page import \
    Customer_Management_Page, Agreement_Management_Page, Business_Division_Agreement_Page, Business_Center_Tab
from work.script_data.T116_Environment_Page_Traverse.Base_Class.Base_Page import BasePage


# 商务中心页面
# @pytest.mark.smoke
class Test_03_case:

    @allure.feature("商务中心")
    @allure.story("商务中心页面")
    @allure.title("进入商务中心页面")
    def test_Business_Center_Page_01(self, all_case_fixture):     # 进入商务中心模块Tab
        with allure.step("步骤一：进入商务中心页面"):
            Business_Center_Tab(all_case_fixture).Business_Center_Tab()

    @allure.feature("商务中心")
    @allure.story("客户管理")
    @allure.title("进入客户管理页面")
    def test_Business_Center_Page_02(self, all_case_fixture):     # 遍历客户管理
        with allure.step("步骤二：遍历客户管理页面"):
            Customer_Management_Page(all_case_fixture).Customer_Management()

    @allure.feature("商务中心")
    @allure.story("协议管理")
    @allure.title("进入协议管理页面")
    def test_Business_Center_Page_03(self, all_case_fixture):     # 遍历协议管理
        with allure.step("步骤三：遍历协议管理页面"):
            Agreement_Management_Page(all_case_fixture).Agreement_Management()

    @allure.feature("商务中心")
    @allure.story("事业部协议")
    @allure.title("进入事业部协议页面")
    def test_Business_Center_Page_04(self, all_case_fixture):   # 遍历事业部协议
        with allure.step("步骤四：遍历事业部协议页面"):
            Business_Division_Agreement_Page(all_case_fixture).Business_Division_Agreement()

    # def test_Business_Center_quit_Webdriver(self, all_case_fixture):  # 退出浏览器，释放资源
    #     BasePage(all_case_fixture).quit_Webdriver()

