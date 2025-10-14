import allure
import pytest

from work.conftest import all_case_fixture
from work.script_data.T116_Environment_Page_Traverse.Page_Object_Class.login_page import Login
from work.script_data.T116_Environment_Page_Traverse.Page_Object_Class.process_approval_page import \
    Process_Approval_Workflow_Page, Process_Approval_ERP_Approval_Page, Process_Approval_Tab
from work.script_data.T116_Environment_Page_Traverse.Base_Class.Base_Page import BasePage
from work.script_data.T116_Environment_Page_Traverse.Tools.kka import allure_wrapper


# 流程审批页面
@pytest.mark.smoke
@allure.epic("脚本名称：邦芒综合服务平台页面遍历")
class Test_01_case:

    @allure.feature("登录")   # 模块
    @allure.story("登录页面")   # 页面名称
    @allure.title("使用账号密码登录")   # 用例名称
    def test_login(self, all_case_fixture):  # 登录，可为抽象方法
        with allure.step("前置步骤：登录"):
            pass
        # Login(all_case_fixture).login_fun("admin", "123456")  # 后续使用前置方法

    @allure.feature("流程审批")
    @allure.story("流程审批Tab")
    @allure.title("进入流程审批Tab")
    def test_Process_Approval_Workflow_01(self, all_case_fixture):  # 进入流程审批Tab
        with allure.step("步骤一：进入流程审批Tab"):
            Process_Approval_Tab(all_case_fixture).Process_Approval_Tab()

    @allure.feature("流程审批-工作流")
    @allure.story("请款")
    @allure.title("遍历请款下的页面")
    def test_Process_Approval_Workflow_02(self, all_case_fixture):  # 工作流-请款
        with allure.step("步骤二：遍历请款下的页面"):
            Process_Approval_Workflow_Page(all_case_fixture).Workflow_Box()

    # @allure.feature("流程审批-工作流")
    # @allure.story("本级员工报销")
    # @allure.title("遍历本级员工报销下的页面")
    # def test_Process_Approval_Workflow_03(self, all_case_fixture):  # 本级员工报销
    #     with allure.step("步骤三：遍历本级员工报销下的页面"):
    #         Process_Approval_Workflow_Page(all_case_fixture).CurrentLevel_employee_reimbursement()
    #
    # @allure.feature("流程审批-工作流")
    # @allure.story("折让金/补贴")
    # @allure.title("遍历折让金/补贴下的页面")
    # def test_Process_Approval_Workflow_04(self, all_case_fixture):  # 折让金/补贴
    #     with allure.step("步骤四：遍历折让金/补贴下的页面"):
    #         Process_Approval_Workflow_Page(all_case_fixture).Discount_gold()
    #
    # @allure.feature("流程审批-工作流")
    # @allure.story("外包员工报销")
    # @allure.title("遍历外包员工报销下的页面")
    # def test_Process_Approval_Workflow_05(self, all_case_fixture):  # 外包员工报销
    #     with allure.step("步骤五：遍历外包员工报销下的页面"):
    #         Process_Approval_Workflow_Page(all_case_fixture).Outsourcing_Employee_Reimbursement()
    #
    # @allure.feature("流程审批-工作流")
    # @allure.story("内部派单")
    # @allure.title("遍历内部派单下的页面")
    # def test_Process_Approval_Workflow_06(self, all_case_fixture):  # 内部派单
    #     with allure.step("步骤六：遍历内部派单下的页面"):
    #         Process_Approval_Workflow_Page(all_case_fixture).Internal_Dispatch_Order()
    #
    # @allure.feature("流程审批-工作流")
    # @allure.story("团队基金")
    # @allure.title("遍历团队基金下的页面")
    # def test_Process_Approval_Workflow_07(self, all_case_fixture):  # 团队基金
    #     with allure.step("步骤七：遍历团队基金下的页面"):
    #         Process_Approval_Workflow_Page(all_case_fixture).Team_Fund()
    #
    # @allure.feature("流程审批-工作流")
    # @allure.story("薪资垫付审批")
    # @allure.title("遍历薪资垫付审批下的页面")
    # def test_Process_Approval_Workflow_08(self, all_case_fixture):  # 薪资垫付审批
    #     with allure.step("步骤八：遍历薪资垫付审批下的页面"):
    #         Process_Approval_Workflow_Page(all_case_fixture).salary_advance_approval()
    #
    # @allure.feature("流程审批-工作流")
    # @allure.story("采购")
    # @allure.title("遍历采购下的页面")
    # def test_Process_Approval_Workflow_09(self, all_case_fixture):  # 采购
    #     with allure.step("步骤九：遍历采购下的页面"):
    #         Process_Approval_Workflow_Page(all_case_fixture).Procurement()
    #
    # @allure.feature("流程审批-工作流")
    # @allure.story("请款审批(财务)")
    # @allure.title("遍历请款审批(财务)下的页面")
    # def test_Process_Approval_Workflow_10(self, all_case_fixture):  # 请款审批(财务)
    #     with allure.step("步骤十：遍历请款审批(财务)下的页面"):
    #         Process_Approval_Workflow_Page(all_case_fixture).Payment_Request_Approval()
    #
    # @allure.feature("流程审批-工作流")
    # @allure.story("跑腿业务")
    # @allure.title("遍历跑腿业务下的页面")
    # def test_Process_Approval_Workflow_11(self, all_case_fixture):  # 跑腿业务
    #     with allure.step("步骤十一：遍历跑腿业务下的页面"):
    #         Process_Approval_Workflow_Page(all_case_fixture).Errand_Business()
    #
    # @allure.feature("流程审批-工作流")
    # @allure.story("原件寄出管理")
    # @allure.title("遍历原件寄出管理下的页面")
    # def test_Process_Approval_Workflow_12(self, all_case_fixture):  # 原件寄出管理
    #     with allure.step("步骤十二：遍历原件寄出管理下的页面"):
    #         Process_Approval_Workflow_Page(all_case_fixture).Original_Send_Management()
    #
    # @allure.feature("流程审批-工作流")
    # @allure.story("还款管理")
    # @allure.title("遍历还款管理下的页面")
    # # @allure_wrapper(module="流程审批-工作流", page="还款管理", case_name="遍历还款管理下的页面")
    # def test_Process_Approval_Workflow_13(self, all_case_fixture):  # 还款管理
    #     with allure.step("步骤十三：遍历还款管理下的页面"):
    #         Process_Approval_Workflow_Page(all_case_fixture).Repayment_Management()
    #
    # @allure.feature("流程审批-工作流")
    # @allure.story("还款管理（出纳审批）")
    # @allure.title("遍历还款管理（出纳审批）下的页面")
    # # @allure_wrapper(module="流程审批-工作流", page="还款管理（出纳审批）", case_name="遍历还款管理（出纳审批）下的页面")
    # def test_Process_Approval_Workflow_14(self, all_case_fixture):  # 还款管理（出纳审批）
    #     with allure.step("步骤十四：遍历还款管理（出纳审批）下的页面"):
    #         Process_Approval_Workflow_Page(all_case_fixture).Repayment_Management_Cashier_Approval()
    #
    # @allure.feature("流程审批-工作流")
    # @allure.story("延期申请审批管理")
    # @allure.title("遍历延期申请审批管理下的页面")
    # # @allure_wrapper(module="流程审批-工作流", page="延期申请审批管理", case_name="遍历延期申请审批管理下的页面")
    # def test_Process_Approval_Workflow_15(self, all_case_fixture):  # 延期申请审批管理
    #     with allure.step("步骤十五：遍历延期申请审批管理下的页面"):
    #         Process_Approval_Workflow_Page(all_case_fixture).Postponement_Approval()
    #
    # @allure.feature("流程审批-工作流")
    # @allure.story("垫付回款审批管理")
    # @allure.title("遍历垫付回款审批管理下的页面")
    # def test_Process_Approval_Workflow_16(self, all_case_fixture):  # 垫付回款审批管理
    #     with allure.step("步骤十六：遍历延期申请审批管理下的页面"):
    #         Process_Approval_Workflow_Page(all_case_fixture).Advance_Approval()
    #
    # @allure.feature("流程审批-工作流")
    # @allure.story("回款管理")
    # @allure.title("遍历回款管理下的页面")
    # def test_Process_Approval_Workflow_17(self, all_case_fixture):  # 回款管理
    #     with allure.step("步骤十七：遍历回款管理下的页面"):
    #         Process_Approval_Workflow_Page(all_case_fixture).Payment_Collection_Approval()
    #
    # @allure.feature("流程审批-工作流")
    # @allure.story("简易报销")
    # @allure.title("遍历简易报销下的页面")
    # def test_Process_Approval_Workflow_18(self, all_case_fixture):  # 简易报销
    #     with allure.step("步骤十八：遍历简易报销下的页面"):
    #         Process_Approval_Workflow_Page(all_case_fixture).Simple_Reimbursement()
    #
    # @allure.feature("流程审批-工作流")
    # @allure.story("简易请款")
    # @allure.title("遍历简易请款下的页面")
    # def test_Process_Approval_Workflow_19(self, all_case_fixture):  # 简易请款
    #     with allure.step("步骤十九：遍历简易请款下的页面"):
    #         Process_Approval_Workflow_Page(all_case_fixture).Simple_Payment_Request()
    #
    # @allure.feature("流程审批-工作流")
    # @allure.story("退款")
    # @allure.title("遍历退款下的页面")
    # def test_Process_Approval_Workflow_20(self, all_case_fixture):  # 退款
    #     with allure.step("步骤二十：遍历退款下的页面"):
    #         Process_Approval_Workflow_Page(all_case_fixture).Refund()
    #
    # @allure.feature("流程审批-工作流")
    # @allure.story("请款退回确认")
    # @allure.title("遍历请款退回确认下的页面")
    # def test_Process_Approval_Workflow_21(self, all_case_fixture):  # 请款退回确认
    #     with allure.step("步骤二十一：遍历请款退回确认下的页面"):
    #         Process_Approval_Workflow_Page(all_case_fixture).Payment_Request_Return()
    #
    # @allure.feature("流程审批-工作流")
    # @allure.story("退款")
    # @allure.title("遍历退款下的页面")
    # def test_Process_Approval_Workflow_22(self, all_case_fixture):  # 退款
    #     with allure.step("步骤二十二：遍历退款下的页面"):
    #         Process_Approval_Workflow_Page(all_case_fixture).discuss_one_matter_at_a_time()
    #
    # @allure.feature("流程审批-流程审批")
    # @allure.story("流程审批-ERP审批")
    # @allure.title("遍历流程审批-ERP审批下的页面")
    # def test_Process_Approval_ERP_Approval_23(self, all_case_fixture):  # 流程审批-ERP审批
    #     with allure.step("步骤二十三：遍历流程审批-ERP审批下的页面"):
    #         Process_Approval_ERP_Approval_Page(all_case_fixture).ERP_Approval()

    # def test_Process_Approval_quit_Webdriver(self, all_case_fixture):  # 退出浏览器，释放资源
    #     BasePage(all_case_fixture).quit_Webdriver()

