import time

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
    # workflow_element = "//div[@title='工作流']"
    workflow_element = "[data-submenu-id='/workflow']"

    # 遍历工作流页面元素
    # 请款
    # payment_request_element = "//div[@title='请款']"
    # payment_request_element1 = "//div[@title='外部请款申请']"
    # payment_request_element2 = "//div[@title='外部请款审批']"
    # payment_request_element3 = "//div[@title='对内请款']"  # 对内请款盒子
    # payment_request_element4 = "//div[@title='对内请款申请']"
    # payment_request_element5 = "//div[@title='对内请款审批']"
    # payment_request_element6 = "//div[@title='内部请款']"
    #
    # server_exception_element = "//span[contains(text(),'知道了')]"

    # 遍历工作流页面元素
    # 请款
    payment_request_element = '[data-menu-id="/erp/workflow/claim"]'    # 请款
    payment_request_element1 = '[data-menu-id="/erp/workflow/claim/externalClaim/index"]'    # 外部请款申请
    payment_request_element2 = '[data-menu-id="/erp/workflow/claim/externalClaim/Approve"]'     # 外部请款审批
    payment_request_element3 = '[data-submenu-id="/claim-inner"]'     # 对内请款盒子
    payment_request_element4 = '[data-menu-id="/erp/workflow/claim/internalSettlement/index"]'     # 对内请款申请
    payment_request_element5 = '[data-menu-id="/erp/workflow/claim/internalSettlement/Approve"]'     # 对内请款审批
    payment_request_element6 = '[data-menu-id="/erp/workflow/claim/internalSettlement/list"]'     # 内部请款

    server_exception_element = "//span[contains(text(),'知道了')]"

    # 请款
    def Workflow_Box(self):
        # 点击流程审批
        # self.click('xpath', self.process_approval_element)
        # 展开工作流下拉框
        self.click('css_selector', self.workflow_element)

        # 遍历请款
        self.click('css_selector', self.payment_request_element)
        self.click('css_selector', self.payment_request_element1)
        self.click('css_selector', self.payment_request_element2)
        self.click('css_selector', self.payment_request_element3)
        self.click('css_selector', self.payment_request_element4)
        self.click('css_selector', self.payment_request_element5)
        self.click('css_selector', self.payment_request_element6)

    # 本级员工报销
    def CurrentLevel_employee_reimbursement(self):
        # 展开本级员工报销元素
        # curren_tlevel_employee_reimbursement_box_element = "//div[@class='ant-menu-submenu-title']//div[@title='本级员工报销'][contains(text(),'本级员工报销')]"
        curren_tlevel_employee_reimbursement_box_element = '[data-menu-id="/erp/workflow/expense/coreStaff"]'

        # 遍历本级员工报销元素
        # curren_tlevel_employee_reimbursement_1_element = "//li[@role='menuitem']//div[@title='本级员工报销'][contains(text(),'本级员工报销')]"
        # curren_tlevel_employee_reimbursement_2_element = "//li[@class='ant-menu-item ant-menu-item-only-child']//div[@title='审批'][contains(text(),'审批')]"
        # curren_tlevel_employee_reimbursement_3_element = "//li[@class='ant-menu-item ant-menu-item-only-child']//div[@title='明细查询'][contains(text(),'明细查询')]"
        # curren_tlevel_employee_reimbursement_4_element = "//div[@title='电子发票查询']"
        # curren_tlevel_employee_reimbursement_5_element = "//div[@title='报销专用发票类型']"

        # 遍历本级员工报销元素
        curren_tlevel_employee_reimbursement_1_element = '[data-menu-id="/erp/workflow/expense/coreStaff/index"]'
        curren_tlevel_employee_reimbursement_2_element = '[data-menu-id="/erp/workflow/expense/coreStaff/Approve"]'
        curren_tlevel_employee_reimbursement_3_element = '[data-menu-id="/erp/workflow/expense/coreStaff/DetailQuery"]'
        curren_tlevel_employee_reimbursement_4_element = '[data-menu-id="/erp/workflow/expense/eInvoiceQuery/index"]'
        curren_tlevel_employee_reimbursement_5_element = '[data-menu-id="/erp/workflow/expense/expenseInvoiceType/index"]'

        # 展开本级员工报销
        self.click('css_selector', curren_tlevel_employee_reimbursement_box_element)

        # 遍历本级员工报销
        self.click('css_selector', curren_tlevel_employee_reimbursement_1_element)
        self.click('css_selector', curren_tlevel_employee_reimbursement_2_element)
        self.click('css_selector', curren_tlevel_employee_reimbursement_3_element)
        self.click('css_selector', curren_tlevel_employee_reimbursement_4_element)
        self.click('css_selector', curren_tlevel_employee_reimbursement_5_element)

    # 折让金/补贴
    def Discount_gold(self):
        # 展开折让金/补贴元素
        # discount_gold_box_element = "//div[@title='折让金/补贴']"
        discount_gold_box_element = '[data-menu-id="/erp/workflow/allowance"]'

        # 遍历折让金/补贴元素
        # discount_gold_1_element = "//div[@title='折让金申请']"
        # discount_gold_2_element = "//div[@title='折让金审批']"
        # discount_gold_3_element = "//div[@title='政府补贴类申请']"
        # discount_gold_4_element = "//div[@title='政府补贴类审批']"

        # 遍历折让金/补贴元素
        discount_gold_1_element = '[data-menu-id="/erp/workflow/allowance/tradeAlowance/index"]'
        discount_gold_2_element = '[data-menu-id="/erp/workflow/allowance/tradeAlowance/Approve"]'
        discount_gold_3_element = '[data-menu-id="/erp/workflow/allowance/governmentSubsidies/index"]'
        discount_gold_4_element = '[data-menu-id="/erp/workflow/allowance/governmentSubsidies/Approve"]'

        # 展开折让金/补贴
        self.click('css_selector', discount_gold_box_element)

        # 遍历折让金/补贴
        self.click('css_selector', discount_gold_1_element)
        self.click('css_selector', discount_gold_2_element)
        self.click('css_selector', discount_gold_3_element)
        self.click('css_selector', discount_gold_4_element)

    # 外包员工报销
    def Outsourcing_Employee_Reimbursement(self):
        # 展开外包员工报销元素
        # outsourcing_employee_reimbursement_box_element = "//div[@class='ant-menu-submenu-title']//div[@title='外包员工报销'][contains(text(),'外包员工报销')]"
        outsourcing_employee_reimbursement_box_element = '[data-menu-id="/erp/workflow/expense/extStaff"]'

        # 遍历外包员工报销元素
        # outsourcing_employee_reimbursement_1_element = "//li[@role='menuitem']//div[@title='外包员工报销'][contains(text(),'外包员工报销')]"
        # outsourcing_employee_reimbursement_2_element = '//*[@id="sub_menu_6_$$_/erp/workflow/expense/extStaff-popup"]/li[2]/span'
        # outsourcing_employee_reimbursement_3_element = "//div[@title='特殊协议配置页面']"
        # outsourcing_employee_reimbursement_4_element = "//div[@title='明细']"

        # 遍历外包员工报销元素
        outsourcing_employee_reimbursement_1_element = '[data-menu-id="/erp/workflow/expense/extStaff/index"]'
        outsourcing_employee_reimbursement_2_element = '[data-menu-id="/erp/workflow/expense/extStaff/Approve"]'
        outsourcing_employee_reimbursement_3_element = '[data-menu-id="/erp/workflow/expense/extStaff/specialAgreement/index"]'
        outsourcing_employee_reimbursement_4_element = '[data-menu-id="/erp/workflow/expense/extStaff/DetailQuery"]'

        # 展开外包员工报销
        self.click('css_selector', outsourcing_employee_reimbursement_box_element)

        # 遍历外包员工报销
        self.click('css_selector', outsourcing_employee_reimbursement_1_element)
        self.click('css_selector', outsourcing_employee_reimbursement_2_element)
        self.click('css_selector', outsourcing_employee_reimbursement_3_element)
        self.click('css_selector', outsourcing_employee_reimbursement_4_element)

    # 内部派单
    def Internal_Dispatch_Order(self):
        # 展开内部派单元素
        # internal_dispatch_order_box_element = "//div[@title='内部派单']"
        internal_dispatch_order_box_element = '[data-menu-id="/erp/workflow/internalDispatching"]'

        # 遍历内部派单元素
        # internal_dispatch_order_1_element = "//div[@title='内部派单（业务）']"
        # internal_dispatch_order_2_element = "//div[@title='内部派单（审批）']"
        # internal_dispatch_order_3_element = "//li[@class='ant-menu-item ant-menu-item-only-child']//div[@title='配置页面'][contains(text(),'配置页面')]"

        # 遍历内部派单元素
        internal_dispatch_order_1_element = '[data-menu-id="/erp/workflow/internalDispatching/index"]'
        internal_dispatch_order_2_element = '[data-menu-id="/erp/workflow/internalDispatching/Approve"]'
        internal_dispatch_order_3_element = '[data-menu-id="/erp/workflow/internalDispatching/ConfigPage"]'

        # 展开内部派单
        self.click('css_selector', internal_dispatch_order_box_element)

        # 遍历内部派单
        self.click('css_selector', internal_dispatch_order_1_element)
        self.click('css_selector', internal_dispatch_order_2_element)
        self.click('css_selector', internal_dispatch_order_3_element)

        # self.click('xpath', "//span[contains(text(),'知道了')]")
        # self.click('xpath', "//span[contains(text(),'新 增')]")
        # self.click('xpath', "//span[contains(text(),'知道了')]")
        # self.click('xpath', "//span[@class='!ml-4px']")
        # time.sleep(2)
        # self.capture_prompt('xpath', "//div[@class='w-full break-all']", '未配置科目', "未配置科目截图")

    # 团队基金
    def Team_Fund(self):
        # 展开团队基金元素
        # team_fund_box_element = "//div[@title='团队基金']"
        team_fund_box_element = '[data-menu-id="/erp/workflow/teamfund"]'

        # 遍历团队基金元素
        # team_fund_1_element = "//li[@class='ant-menu-item ant-menu-item-only-child']//div[@title='申请'][contains(text(),'申请')]"
        # team_fund_2_element = "//div[@title='账户管理']"
        # team_fund_3_element = '/html/body/div[1]/section/section/aside/div/div/div/div[2]/ul/li[1]/ul/li[6]/ul/li[3]/span'

        # 遍历团队基金元素
        team_fund_1_element = '[data-menu-id="/erp/workflow/teamfund/apply/index"]'
        team_fund_2_element = '[data-menu-id="/erp/workflow/teamfund/accountManager/index"]'
        team_fund_3_element = '[data-menu-id="/erp/workflow/teamfund/approve/index"]'

        # 展开团队基金
        self.click('css_selector', team_fund_box_element)

        # 遍历团队基金
        self.click('css_selector', team_fund_1_element)
        self.click('css_selector', team_fund_2_element)
        self.click('css_selector', team_fund_3_element)

    # 薪资垫付审批
    def salary_advance_approval(self):
        # 薪资垫付审批元素
        # salary_advance_approval_element = "//div[@title='薪资垫付审批']"
        salary_advance_approval_element = '[data-menu-id="/erp/workflow/advancePayApply/index"]'

        # 点击薪资垫付审批
        self.click('css_selector', salary_advance_approval_element)

    # 采购
    def Procurement(self):
        # 展开采购元素
        # procurement_box_element = "//div[@title='采购']"
        procurement_box_element = '[data-menu-id="/erp/workflow/purchase"]'

        # 遍历采购元素，116环境
        # procurement_1_element = '//*[@id="sub_menu_12_$$_/erp/workflow/purchase-popup"]/li[1]/span'
        # procurement_2_element = '//*[@id="sub_menu_12_$$_/erp/workflow/purchase-popup"]/li[2]/span'
        # procurement_3_element = '//*[@id="sub_menu_12_$$_/erp/workflow/purchase-popup"]/li[3]/span'
        # procurement_4_element = '//*[@id="sub_menu_12_$$_/erp/workflow/purchase-popup"]/li[4]/span'

        # 遍历采购元素
        procurement_1_element = '[data-menu-id="/erp/workflow/purchase/apply/index"]'
        procurement_2_element = '[data-menu-id="/erp/workflow/purchase/detail/index"]'
        procurement_3_element = '[data-menu-id="/erp/workflow/purchase/goodsSetting/index"]'
        procurement_4_element = '[data-menu-id="/erp/workflow/purchase/approve/index"]'

        # 展开采购
        self.click('css_selector', procurement_box_element)

        # 遍历采购
        self.click('css_selector', procurement_1_element)
        self.click('css_selector', procurement_2_element)
        self.click('css_selector', procurement_3_element)
        self.click('css_selector', procurement_4_element)

    # 请款审批(财务)
    def Payment_Request_Approval(self):
        # 请款审批(财务)元素
        # payment_equest_approval_element = "//div[@title='请款审批（财务）']"
        payment_equest_approval_element = '[data-menu-id="/erp/workflow/financialNodes/index"]'

        # 遍历请款审批(财务)
        self.click('css_selector', payment_equest_approval_element)

    # 跑腿业务
    def Errand_Business(self):
        # 展开跑腿业务元素
        # errand_business_element = "//div[@title='跑腿业务']"
        errand_business_element = '[data-menu-id="/erp/workflow/business-running"]'

        # 遍历跑腿业务元素
        # errand_business_1_element = "//div[@title='跑腿业务(申请)']"
        # # errand_business_2_element = '//*[@id="sub_menu_13_$$_/erp/workflow/business-running-popup"]/li[2]/span'   # 116
        # errand_business_2_element = '/html/body/div[1]/section/section/aside/div/div/div/div[2]/ul/li[1]/ul/li[10]/ul/li[2]/span'   # test1
        # errand_business_3_element = "//div[@title='跑腿业务(审批)']"

        # 遍历跑腿业务元素
        errand_business_1_element = '[data-menu-id="/erp/workflow/business-running/index"]'
        errand_business_2_element = '[data-menu-id="/erp/workflow/business-running/ConfigPage"]'
        errand_business_3_element = '[data-menu-id="/erp/workflow/business-running/Approve"]'

        # 展开跑腿业务
        self.click('css_selector', errand_business_element)

        # 遍历跑腿业务
        self.click('css_selector', errand_business_1_element)
        self.click('css_selector', errand_business_2_element)
        self.click('css_selector', errand_business_3_element)

    # 原件寄出管理
    def Original_Send_Management(self):
        # 原件寄出管理元素
        # original_send_management_element = "//div[@title='原件寄出管理']"
        original_send_management_element = '[data-menu-id="/erp/workflow/originalSentOut/index"]'

        # 遍历原件寄出管理
        self.click('css_selector', original_send_management_element)

    # 还款管理
    def Repayment_Management(self):
        # 还款管理元素
        # repayment_management_element = "//div[@title='还款管理']"
        repayment_management_element = '[data-menu-id="/erp/workflow/repayment/index"]'

        # 遍历还款管理
        self.click('css_selector', repayment_management_element)

    # 还款管理（出纳审批）
    def Repayment_Management_Cashier_Approval(self):
        # 还款管理（出纳审批）元素
        # repayment_management_cashier_approval_element = "//div[@title='还款管理（出纳审批）']"
        repayment_management_cashier_approval_element = '[data-menu-id="/erp/workflow/repaymentAudit/index"]'

        # 遍历还款管理（出纳审批）
        self.click('css_selector', repayment_management_cashier_approval_element)

    # 延期申请审批管理
    def Postponement_Approval(self):
        # 延期申请审批管理元素
        # postponement_approval_element = "//div[@title='延期申请审批管理']"
        postponement_approval_element = '[data-menu-id="/erp/workflow/extensionRequestAudit/index"]'

        # 遍历延期申请审批管理元素
        self.click('css_selector', postponement_approval_element)

    # 垫付回款审批管理
    def Advance_Approval(self):
        # 垫付回款审批管理元素
        # advance_approval_element = "//div[@title='垫付回款审批管理']"
        advance_approval_element = '[data-menu-id="/erp/workflow/advancePaymentCollection/index"]'

        # 遍历垫付回款审批管理
        self.click('css_selector', advance_approval_element)

    # 回款管理
    def Payment_Collection_Approval(self):
        # 回款管理元素
        # payment_collection_approval_element = "//div[@title='回款管理']"
        payment_collection_approval_element = '[data-menu-id="/erp/workflow/paymentCollection/index"]'

        # 遍历回款管理
        self.click('css_selector', payment_collection_approval_element)

    # 简易报销
    def Simple_Reimbursement(self):
        # 简易报销元素
        # simple_reimbursement_element = "//div[@title='简易报销']"
        simple_reimbursement_element = '[data-menu-id="/erp/workflow/simpleReimbursement/apply/index"]'

        # 遍历简易报销
        self.click('css_selector', simple_reimbursement_element)

    # 简易请款
    def Simple_Payment_Request(self):
        # 简易请款元素
        # simple_payment_request_element = "//div[@title='简易请款']"
        simple_payment_request_element = '[data-menu-id="/erp/workflow/simpleReq/apply/index"]'

        # 遍历简易请款
        self.click('css_selector', simple_payment_request_element)

    # 退款
    def Refund(self):
        # 展开退款元素
        # refund_box_element = "//div[@title='退款']"
        refund_box_element = '[data-submenu-id="/erp/workflow/refund"]'

        # 遍历退款元素
        # refund_apply_1_element = '//*[@id="sub_menu_14_$$_/erp/workflow/refund-popup"]/li[1]/span'
        # refund_approval_2_element = '//*[@id="sub_menu_14_$$_/erp/workflow/refund-popup"]/li[2]/span'

        # 遍历退款元素
        refund_apply_1_element = '[data-menu-id="/erp/workflow/refund/index"]'
        refund_approval_2_element = '[data-menu-id="/erp/workflow/refund/Approve"]'

        # 展开退款
        self.click('css_selector', refund_box_element)

        # 遍历退款
        self.click('css_selector', refund_apply_1_element)
        self.click('css_selector', refund_approval_2_element)

    # 请款退回确认
    def Payment_Request_Return(self):
        # 请款退回确认元素
        # payment_request_return_element = "//div[@title='请款退回确认']"
        payment_request_return_element = '[data-menu-id="/erp/workflow/refundConfirm/index"]'

        # 遍历请款退回确认元素
        self.click('css_selector', payment_request_return_element)

    # 一事一议
    def discuss_one_matter_at_a_time(self):
        # 展开一事一议元素
        # discuss_one_matter_at_a_time_box_element = "//div[@title='一事一议']"
        discuss_one_matter_at_a_time_box_element = '[data-menu-id="/erp/workflow/oneProjectOne"]'

        # 遍历一事一议元素
        # discuss_one_matter_at_a_time_1_element = "//div[@title='一事一议(申请)']"
        # discuss_one_matter_at_a_time_2_element = "//div[@title='一事一议(审批)']"

        # 遍历一事一议元素
        discuss_one_matter_at_a_time_1_element = '[data-menu-id="/erp/workflow/oneProjectOne/index"]'
        discuss_one_matter_at_a_time_2_element = '[data-menu-id="/erp/workflow/oneProjectOne/Approve"]'

        # 展开一事一议
        self.click('css_selector', discuss_one_matter_at_a_time_box_element)

        # 遍历一事一议
        self.click('css_selector', discuss_one_matter_at_a_time_1_element)
        self.click('css_selector', discuss_one_matter_at_a_time_2_element)


# 流程审批盒子
class Process_Approval_ERP_Approval_Page(BasePage):
    # 展开流程审批元素
    # process_approval_box_element = "//div[@title='流程审批']"
    process_approval_box_element = '[data-menu-id="/liuchengshenpi"]'

    # 展开ERP审批元素
    # erp_approval_element = "//div[@title='ERP审批']"
    erp_approval_element = '[data-menu-id="/erp/approve"]'

    # 遍历ERP审批元素
    # erp_approval_1 = "//div[@title='协议审批']"
    # erp_approval_2 = "//div[@title='协议归档']"
    # erp_approval_3 = "//div[@title='协议编辑审批']"
    # erp_approval_4 = "//div[@title='协议续签']"
    # erp_approval_5 = "//div[@title='集团标签审批']"
    # erp_approval_6 = "//div[@title='客户品牌审批']"
    # erp_approval_7 = "//div[@title='潜在客户新增审批']"
    # erp_approval_8 = "//div[@title='同名潜在客户审批']"
    # erp_approval_9 = "//div[@title='营销待办审批']"
    # erp_approval_10 = "//div[@title='结算单审批']"
    # erp_approval_11 = "//div[@title='招投标待办审批']"
    # erp_approval_12 = "//div[@title='申请失效']"

    # 遍历ERP审批元素
    erp_approval_1 = '[data-menu-id="/erp/approve/business/agreementManagement/index"]'
    erp_approval_2 = '[data-menu-id="/erp/approve/business/agreementArchive/index"]'
    erp_approval_3 = '[data-menu-id="/erp/approve/business/agreementEditApprove/index"]'
    erp_approval_4 = '[data-menu-id="/erp/approve/business/agreementRenewal/index"]'
    erp_approval_5 = '[data-menu-id="/erp/approve/crm/modules/GroupLabel"]'
    erp_approval_6 = '[data-menu-id="/erp/approve/crm/modules/CustomBrand"]'
    erp_approval_7 = '[data-menu-id="/erp/approve/crm/modules/PotentialCustomerAdd"]'
    erp_approval_8 = '[data-menu-id="/erp/approve/crm/modules/PotentialApproval"]'
    erp_approval_9 = '[data-menu-id="/erp/approve/crm/modules/MarketingApproval"]'
    erp_approval_10 = '[data-menu-id="/erp/approve/business/settlementAudit/index"]'
    erp_approval_11 = '[data-menu-id="/erp/approve/crm/modules/TenderApproval"]'
    erp_approval_12 = '[data-menu-id="/erp/approve/crm/modules/InvalidTodo"]'

    # 流程审批-ERP审批
    def ERP_Approval(self):
        """调试方法"""
        # self.click('xpath', Process_Approval_Workflow_Page(self).process_approval_element)

        # 展开流程审批
        self.click('css_selector', self.process_approval_box_element)

        # 展开ERP审批
        self.click('css_selector', self.erp_approval_element)

        # 遍历ERP审批
        self.click('css_selector', self.erp_approval_1)
        self.click('css_selector', self.erp_approval_2)
        self.click('css_selector', self.erp_approval_3)
        self.click('css_selector', self.erp_approval_4)
        self.click('css_selector', self.erp_approval_5)
        self.click('css_selector', self.erp_approval_6)
        self.click('css_selector', self.erp_approval_7)
        self.click('css_selector', self.erp_approval_8)
        self.click('css_selector', self.erp_approval_9)
        self.click('css_selector', self.erp_approval_10)
        self.click('css_selector', self.erp_approval_11)
        self.click('css_selector', self.erp_approval_12)
