import allure
import pytest

from work.conftest import all_case_fixture
from work.script_data.T116_Environment_Page_Traverse.Page_Object_Class.policy_repository_page import \
    Policy_Repository_Page, Policy_Repository_Tab
from work.script_data.T116_Environment_Page_Traverse.Base_Class.Base_Page import BasePage


# 政策库页面
# @pytest.mark.smoke
class Test_02_case:

    @allure.feature("政策库")
    @allure.story("政策库页面")
    @allure.title("进入政策库页面")
    def test_Policy_Repository_Page_01(self, all_case_fixture):     # 进入政策库模块Tab
        with allure.step("步骤一：进入政策库页面"):
            Policy_Repository_Tab(all_case_fixture).Policy_Repository_Tab()

    @allure.feature("政策库")
    @allure.story("政策库页面")
    @allure.title("遍历政策库下的页面")
    def test_Policy_Repository_Page_02(self, all_case_fixture):     # 政策库遍历
        with allure.step("步骤二：遍历政策库下的页面"):
            Policy_Repository_Page(all_case_fixture).Policy_Repository()

    # def test_Policy_Repository_quit_Webdriver(self, all_case_fixture):  # 退出浏览器，释放资源
    #     BasePage(all_case_fixture).quit_Webdriver()
