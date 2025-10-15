from work.script_data.T116_Environment_Page_Traverse.Base_Class.Base_Page import BasePage
from work.script_data.T116_Environment_Page_Traverse.Tools.log_tool import Logging

log = Logging()


class Process_Approval_Tab(BasePage):   # 进入流程审批Tab
    # 进入流程审批Tab
    process_approval_element = "//div[@class='flex items-center gap-2'][contains(text(),'流程审批')]"

    def Process_Approval_Tab(self):     # 进入流程审批Tab
        # 点击流程审批
        self.click('xpath', self.process_approval_element)


# 工作流盒子
class Process_Approval_Workflow_Page(BasePage):
    # 进入流程审批模块
    # process_approval_element = "//div[@class='flex items-center gap-2'][contains(text(),'流程审批')]"

    # 展开工作流下拉框元素
    workflow_element = "//div[@title='工作流']"

    # 遍历工作流页面元素
    # 请款
    payment_request_element = "//div[@title='请款']"
    payment_request_element1 = "//div[@title='外部请款申请']"
    payment_request_element2 = "//div[@title='外部请款审批']"
    payment_request_element3 = "//div[@title='对内请款']"  # 对内请款盒子
    payment_request_element4 = "//div[@title='对内请款申请']"
    payment_request_element5 = "//div[@title='对内请款审批']"
    payment_request_element6 = "//div[@title='内部请款']"

    server_exception_element = "//span[contains(text(),'知道了')]"

    # 请款
    def Workflow_Box(self):
        # 点击流程审批
        # self.click('xpath', self.process_approval_element)
        # 展开工作流下拉框
        self.click('xpath', self.workflow_element)

        # 遍历请款
        self.click('xpath', self.payment_request_element)
        self.click('xpath', self.payment_request_element1)
        self.click('xpath', self.payment_request_element2)
        self.click('xpath', self.payment_request_element3)
        self.click('xpath', self.payment_request_element4)
        self.click('xpath', self.payment_request_element5)
        self.click('xpath', self.payment_request_element6)

    # 本级员工报销
    def CurrentLevel_employee_reimbursement(self):
        # 展开本级员工报销元素
        curren_tlevel_employee_reimbursement_box_element = "//div[@class='ant-menu-submenu-title']//div[@title='本级员工报销'][contains(text(),'本级员工报销')]"

        # 遍历本级员工报销元素
        curren_tlevel_employee_reimbursement_1_element = "//li[@role='menuitem']//div[@title='本级员工报销'][contains(text(),'本级员工报销')]"
        # curren_tlevel_employee_reimbursement_2_element = '//*[@id="sub_menu_7_$$_/erp/workflow/expense/coreStaff-popup"]/li[2]/span'
        curren_tlevel_employee_reimbursement_2_element = "//li[@class='ant-menu-item ant-menu-item-only-child']//div[@title='审批'][contains(text(),'审批')]"
        curren_tlevel_employee_reimbursement_3_element = "//li[@class='ant-menu-item ant-menu-item-only-child']//div[@title='明细查询'][contains(text(),'明细查询')]"
        curren_tlevel_employee_reimbursement_4_element = "//div[@title='电子发票查询']"
        curren_tlevel_employee_reimbursement_5_element = "//div[@title='报销专用发票类型']"

        # 展开本级员工报销
        self.click('xpath', curren_tlevel_employee_reimbursement_box_element)

        # 遍历本级员工报销
        self.click('xpath', curren_tlevel_employee_reimbursement_1_element)
        self.click('xpath', curren_tlevel_employee_reimbursement_2_element)
        self.click('xpath', curren_tlevel_employee_reimbursement_3_element)
        self.click('xpath', curren_tlevel_employee_reimbursement_4_element)
        self.click('xpath', curren_tlevel_employee_reimbursement_5_element)

    # 折让金/补贴
    def Discount_gold(self):
        # 展开折让金/补贴元素
        discount_gold_box_element = "//div[@title='折让金/补贴']"

        # 遍历折让金/补贴元素
        discount_gold_1_element = "//div[@title='折让金申请']"
        discount_gold_2_element = "//div[@title='折让金审批']"
        discount_gold_3_element = "//div[@title='政府补贴类申请']"
        discount_gold_4_element = "//div[@title='政府补贴类审批']"

        # 展开折让金/补贴
        self.click('xpath', discount_gold_box_element)

        # 遍历折让金/补贴
        self.click('xpath', discount_gold_1_element)
        self.click('xpath', discount_gold_2_element)
        self.click('xpath', discount_gold_3_element)
        self.click('xpath', discount_gold_4_element)

    # 外包员工报销
    def Outsourcing_Employee_Reimbursement(self):
        # 展开外包员工报销元素
        outsourcing_employee_reimbursement_box_element = "//div[@class='ant-menu-submenu-title']//div[@title='外包员工报销'][contains(text(),'外包员工报销')]"

        # 遍历外包员工报销元素
        outsourcing_employee_reimbursement_1_element = "//li[@role='menuitem']//div[@title='外包员工报销'][contains(text(),'外包员工报销')]"
        # outsourcing_employee_reimbursement_2_element = '//*[@id="sub_menu_9_$$_/erp/workflow/expense/extStaff-popup"]/li[2]/span'   # 116 的元素
        outsourcing_employee_reimbursement_2_element = '//*[@id="sub_menu_6_$$_/erp/workflow/expense/extStaff-popup"]/li[2]/span'   # test1 的元素
        outsourcing_employee_reimbursement_3_element = "//div[@title='特殊协议配置页面']"
        outsourcing_employee_reimbursement_4_element = "//div[@title='明细']"

        # 展开外包员工报销
        self.click('xpath', outsourcing_employee_reimbursement_box_element)

        # 遍历外包员工报销
        self.click('xpath', outsourcing_employee_reimbursement_1_element)
        self.click('xpath', outsourcing_employee_reimbursement_2_element)
        self.click('xpath', outsourcing_employee_reimbursement_3_element)
        self.click('xpath', outsourcing_employee_reimbursement_4_element)

    # 内部派单
    def Internal_Dispatch_Order(self):
        # 展开内部派单元素
        internal_dispatch_order_box_element = "//div[@title='内部派单']"

        # 遍历内部派单元素
        internal_dispatch_order_1_element = "//div[@title='内部派单（业务）']"
        internal_dispatch_order_2_element = "//div[@title='内部派单（审批）']"
        internal_dispatch_order_3_element = "//li[@class='ant-menu-item ant-menu-item-only-child']//div[@title='配置页面'][contains(text(),'配置页面')]"

        # 展开内部派单
        self.click('xpath', internal_dispatch_order_box_element)

        # 遍历内部派单
        self.click('xpath', internal_dispatch_order_1_element)
        self.click('xpath', internal_dispatch_order_2_element)
        self.click('xpath', internal_dispatch_order_3_element)

        # self.click('xpath', "//span[contains(text(),'知道了')]")
        # self.click('xpath', "//span[contains(text(),'新 增')]")
        # self.click('xpath', "//span[contains(text(),'知道了')]")
        # self.click('xpath', "//span[@class='!ml-4px']")
        # time.sleep(2)
        # self.capture_prompt('xpath', "//div[@class='w-full break-all']", '未配置科目', "未配置科目截图")

    # 团队基金
    def Team_Fund(self):
        # 展开团队基金元素
        team_fund_box_element = "//div[@title='团队基金']"

        # 遍历团队基金元素
        team_fund_1_element = "//li[@class='ant-menu-item ant-menu-item-only-child']//div[@title='申请'][contains(text(),'申请')]"
        team_fund_2_element = "//div[@title='账户管理']"
        # team_fund_3_element = '//*[@id="sub_menu_11_$$_/erp/workflow/teamfund-popup"]/li[3]/span'   # 116环境
        team_fund_3_element = '/html/body/div[1]/section/section/aside/div/div/div/div[2]/ul/li[1]/ul/li[6]/ul/li[3]/span'   # test1环境

        # 展开团队基金
        self.click('xpath', team_fund_box_element)

        # 遍历团队基金
        self.click('xpath', team_fund_1_element)
        self.click('xpath', team_fund_2_element)
        self.click('xpath', team_fund_3_element)

    # 薪资垫付审批
    def salary_advance_approval(self):
        # 薪资垫付审批元素
        salary_advance_approval_element = "//div[@title='薪资垫付审批']"

        # 点击薪资垫付审批
        self.click('xpath', salary_advance_approval_element)

    # 采购
    def Procurement(self):
        # 展开采购元素
        procurement_box_element = "//div[@title='采购']"

        # 遍历采购元素，116环境
        # procurement_1_element = '//*[@id="sub_menu_12_$$_/erp/workflow/purchase-popup"]/li[1]/span'
        # procurement_2_element = '//*[@id="sub_menu_12_$$_/erp/workflow/purchase-popup"]/li[2]/span'
        # procurement_3_element = '//*[@id="sub_menu_12_$$_/erp/workflow/purchase-popup"]/li[3]/span'
        # procurement_4_element = '//*[@id="sub_menu_12_$$_/erp/workflow/purchase-popup"]/li[4]/span'

        # test1环境
        procurement_1_element = "/html/body/div[1]/section/section/aside/div/div/div/div[2]/ul/li[1]/ul/li[8]/ul/li[1]/span"
        procurement_2_element = "/html/body/div[1]/section/section/aside/div/div/div/div[2]/ul/li[1]/ul/li[8]/ul/li[2]/span"
        procurement_3_element = "//li[@class='ant-menu-item ant-menu-item-only-child']//div[@title='物品配置'][contains(text(),'物品配置')]"
        procurement_4_element = "/html/body/div[1]/section/section/aside/div/div/div/div[2]/ul/li[1]/ul/li[8]/ul/li[4]/span"

        # 展开采购
        self.click('xpath', procurement_box_element)

        # 遍历采购
        self.click('xpath', procurement_1_element)
        self.click('xpath', procurement_2_element)
        self.click('xpath', procurement_3_element)
        self.click('xpath', procurement_4_element)

    # 请款审批(财务)
    def Payment_Request_Approval(self):
        # 请款审批(财务)元素
        payment_equest_approval_element = "//div[@title='请款审批（财务）']"

        # 遍历请款审批(财务)
        self.click('xpath', payment_equest_approval_element)

    # 跑腿业务
    def Errand_Business(self):
        # 展开跑腿业务元素
        errand_business_element = "//div[@title='跑腿业务']"

        # 遍历跑腿业务元素
        errand_business_1_element = "//div[@title='跑腿业务(申请)']"
        # errand_business_2_element = '//*[@id="sub_menu_13_$$_/erp/workflow/business-running-popup"]/li[2]/span'   # 116
        errand_business_2_element = '/html/body/div[1]/section/section/aside/div/div/div/div[2]/ul/li[1]/ul/li[10]/ul/li[2]/span'   # test1
        errand_business_3_element = "//div[@title='跑腿业务(审批)']"

        # 展开跑腿业务
        self.click('xpath', errand_business_element)

        # 遍历跑腿业务
        self.click('xpath', errand_business_1_element)
        self.click('xpath', errand_business_2_element)
        self.click('xpath', errand_business_3_element)

    # 原件寄出管理
    def Original_Send_Management(self):
        # 原件寄出管理元素
        original_send_management_element = "//div[@title='原件寄出管理']"

        # 遍历原件寄出管理
        self.click('xpath', original_send_management_element)

    # 还款管理
    def Repayment_Management(self):
        # 还款管理元素
        repayment_management_element = "//div[@title='还款管理']"

        # 遍历还款管理
        self.click('xpath', repayment_management_element)

    # 还款管理（出纳审批）
    def Repayment_Management_Cashier_Approval(self):
        # 还款管理（出纳审批）元素
        repayment_management_cashier_approval_element = "//div[@title='还款管理（出纳审批）']"

        # 遍历还款管理（出纳审批）
        self.click('xpath', repayment_management_cashier_approval_element)

    # 延期申请审批管理
    def Postponement_Approval(self):
        # 延期申请审批管理元素
        postponement_approval_element = "//div[@title='延期申请审批管理']"

        # 遍历延期申请审批管理元素
        self.click('xpath', postponement_approval_element)

    # 垫付回款审批管理
    def Advance_Approval(self):
        # 垫付回款审批管理元素
        advance_approval_element = "//div[@title='垫付回款审批管理']"

        # 遍历垫付回款审批管理
        self.click('xpath', advance_approval_element)

    # 回款管理
    def Payment_Collection_Approval(self):
        # 回款管理元素
        payment_collection_approval_element = "//div[@title='回款管理']"

        # 遍历回款管理
        self.click('xpath', payment_collection_approval_element)

    # 简易报销
    def Simple_Reimbursement(self):
        # 简易报销元素
        simple_reimbursement_element = "//div[@title='简易报销']"

        # 遍历简易报销
        self.click('xpath', simple_reimbursement_element)

    # 简易请款
    def Simple_Payment_Request(self):
        # 简易请款元素
        simple_payment_request_element = "//div[@title='简易请款']"

        # 遍历简易请款
        self.click('xpath', simple_payment_request_element)

    # 退款
    def Refund(self):
        # 展开退款元素
        refund_box_element = "//div[@title='退款']"

        # 遍历退款元素 116环境
        # refund_apply_1_element = '//*[@id="sub_menu_14_$$_/erp/workflow/refund-popup"]/li[1]/span'
        # refund_approval_2_element = '//*[@id="sub_menu_14_$$_/erp/workflow/refund-popup"]/li[2]/span'

        # test1环境
        refund_apply_1_element = '/html/body/div[1]/section/section/aside/div/div/div/div[2]/ul/li[1]/ul/li[19]/ul/li[1]/span'
        refund_approval_2_element = '/html/body/div[1]/section/section/aside/div/div/div/div[2]/ul/li[1]/ul/li[19]/ul/li[2]/span'

        # 展开退款
        self.click('xpath', refund_box_element)

        # 遍历退款
        self.click('xpath', refund_apply_1_element)
        self.click('xpath', refund_approval_2_element)

    # 请款退回确认
    def Payment_Request_Return(self):
        # 请款退回确认元素
        payment_request_return_element = "//div[@title='请款退回确认']"

        # 遍历请款退回确认元素
        self.click('xpath', payment_request_return_element)

    # 一事一议
    def discuss_one_matter_at_a_time(self):
        # 展开一事一议元素
        discuss_one_matter_at_a_time_box_element = "//div[@title='一事一议']"

        # 遍历一事一议元素
        discuss_one_matter_at_a_time_1_element = "//div[@title='一事一议(申请)']"
        discuss_one_matter_at_a_time_2_element = "//div[@title='一事一议(审批)']"

        # 展开一事一议
        self.click('xpath', discuss_one_matter_at_a_time_box_element)

        # 遍历一事一议
        self.click('xpath', discuss_one_matter_at_a_time_1_element)
        self.click('xpath', discuss_one_matter_at_a_time_2_element)


# 流程审批盒子
class Process_Approval_ERP_Approval_Page(BasePage):
    # 展开流程审批元素
    process_approval_box_element = "//div[@title='流程审批']"

    # 展开ERP审批元素
    erp_approval_element = "//div[@title='ERP审批']"

    # 遍历ERP审批元素
    erp_approval_1 = "//div[@title='协议审批']"
    erp_approval_2 = "//div[@title='协议归档']"
    erp_approval_3 = "//div[@title='协议编辑审批']"
    erp_approval_4 = "//div[@title='协议续签']"
    erp_approval_5 = "//div[@title='集团标签审批']"
    erp_approval_6 = "//div[@title='客户品牌审批']"
    erp_approval_7 = "//div[@title='潜在客户新增审批']"
    erp_approval_8 = "//div[@title='同名潜在客户审批']"
    erp_approval_9 = "//div[@title='营销待办审批']"
    erp_approval_10 = "//div[@title='结算单审批']"
    erp_approval_11 = "//div[@title='招投标待办审批']"
    erp_approval_12 = "//div[@title='申请失效']"

    # 流程审批-ERP审批
    def ERP_Approval(self):
        """调试方法"""
        # self.click('xpath', Process_Approval_Workflow_Page(self).process_approval_element)

        # 展开流程审批
        self.click('xpath', self.process_approval_box_element)

        # 展开ERP审批
        self.click('xpath', self.erp_approval_element)

        # 遍历ERP审批
        self.click('xpath', self.erp_approval_1)
        self.click('xpath', self.erp_approval_2)
        self.click('xpath', self.erp_approval_3)
        self.click('xpath', self.erp_approval_4)
        self.click('xpath', self.erp_approval_5)
        self.click('xpath', self.erp_approval_6)
        self.click('xpath', self.erp_approval_7)
        self.click('xpath', self.erp_approval_8)
        self.click('xpath', self.erp_approval_9)
        self.click('xpath', self.erp_approval_10)
        self.click('xpath', self.erp_approval_11)
        self.click('xpath', self.erp_approval_12)
