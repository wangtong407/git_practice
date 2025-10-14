import allure
import pytest

from work.script_data.T116_Environment_Page_Traverse.Page_Object_Class.settlement_center_page import \
    Accounts_Receivable_Management_Page, Payment_Management_Page, Value_Added_Service_Page, \
    Bid_Security_Management_Page, \
    Performance_Bond_Management_Page, Accounts_Receivable_Audit_Page, Interest_Whitelist_Page, \
    White_List_of_Guarantee_Deposit_Page, Tax_Return_Page, Settlement_Center_Tab
from work.script_data.T116_Environment_Page_Traverse.Base_Class.Base_Page import BasePage


# 结算中心页面
# @pytest.mark.smoke
class Test_05_case:

    @allure.feature("结算中心")
    @allure.story("结算中心页面")
    @allure.title("进入结算中心页面")
    def test_Settlement_Center_Page_01(self, all_case_fixture):  # 进入结算中心Tab
        with allure.step("步骤一：进入结算中心页面"):
            Settlement_Center_Tab(all_case_fixture).Settlement_Center_Tab()

    @allure.feature("结算中心")
    @allure.story("应收管理页面")
    @allure.title("进入应收管理页面")
    def test_Settlement_Center_Page_02(self, all_case_fixture):  # 应收管理模块
        with allure.step("步骤二：进入应收管理页面"):
            Accounts_Receivable_Management_Page(all_case_fixture).Accounts_Receivable_Management()

    @allure.feature("结算中心")
    @allure.story("到款管理页面")
    @allure.title("进入到款管理页面")
    def test_Settlement_Center_Page_03(self, all_case_fixture):    # 到款管理模块
        with allure.step("步骤三：进入到款管理页面"):
            Payment_Management_Page(all_case_fixture).Payment_Management()

    @allure.feature("结算中心")
    @allure.story("增值服务页面")
    @allure.title("进入增值服务页面")
    def test_Settlement_Center_Page_04(self, all_case_fixture):    # 增值服务模块
        with allure.step("步骤四：进入增值服务页面"):
            Value_Added_Service_Page(all_case_fixture).Value_Added_Service()

    @allure.feature("结算中心")
    @allure.story("投标保证金页面")
    @allure.title("进入投标保证金页面")
    def test_Settlement_Center_Page_05(self, all_case_fixture):  # 投标保证金管理
        with allure.step("步骤五：进入投标保证金页面"):
            Bid_Security_Management_Page(all_case_fixture).Bid_Security_Management()

    @allure.feature("结算中心")
    @allure.story("履约保证金页面")
    @allure.title("进入履约保证金页面")
    def test_Settlement_Center_Page_06(self, all_case_fixture):  # 履约保证金管理
        with allure.step("步骤六：进入履约保证金页面"):
            Performance_Bond_Management_Page(all_case_fixture).Performance_Bond_Management()

    @allure.feature("结算中心")
    @allure.story("应收账款页面")
    @allure.title("进入应收账款页面")
    def test_Settlement_Center_Page_07(self, all_case_fixture):  # 应收账款审核
        with allure.step("步骤七：进入应收账款页面"):
            Accounts_Receivable_Audit_Page(all_case_fixture).Accounts_Receivable_Audit()

    @allure.feature("结算中心")
    @allure.story("利息白名单页面")
    @allure.title("进入利息白名单页面")
    def test_Settlement_Center_Page_08(self, all_case_fixture):  # 利息白名单
        with allure.step("步骤八：进入利息白名单页面"):
            Interest_Whitelist_Page(all_case_fixture).Interest_Whitelist()

    @allure.feature("结算中心")
    @allure.story("保证金白名单页面")
    @allure.title("进入保证金白名单页面")
    def test_Settlement_Center_Page_09(self, all_case_fixture):  # 保证金白名单
        with allure.step("步骤九：进入保证金白名单页面"):
            White_List_of_Guarantee_Deposit_Page(all_case_fixture).White_List_of_Guarantee_Deposit()

    @allure.feature("结算中心")
    @allure.story("个税申报页面")
    @allure.title("进入个税申报页面")
    def test_Settlement_Center_Page_10(self, all_case_fixture):  # 个税申报
        with allure.step("步骤十：进入个税申报页面"):
            Tax_Return_Page(all_case_fixture).Tax_Return()

    # def test_Payment_Management_quit_Webdriver(self, all_case_fixture):  # 退出浏览器，释放资源
    #     BasePage(all_case_fixture).quit_Webdriver()

