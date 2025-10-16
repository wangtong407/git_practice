from work.script_data.T116_Environment_Page_Traverse.Base_Class.Base_Page import BasePage
from work.script_data.T116_Environment_Page_Traverse.Tools.log_tool import Logging

log = Logging()


class Settlement_Center_Tab(BasePage):  # 进入结算中心Tab
    # 进入结算中心Tab
    settlement_center_element = "//div[contains(text(),'结算中心')]"

    def Settlement_Center_Tab(self):
        self.click('xpath', self.settlement_center_element)


class Accounts_Receivable_Management_Page(BasePage):  # 应收管理模块
    # 进入结算中心模块元素
    # settlement_center_element = "//div[contains(text(),'结算中心')]"

    # 应收管理盒子
    # settlement_center_box_element = "//div[@title='应收管理']"
    settlement_center_box_element = '[data-menu-id="/yingshouguanli"]'

    # 遍历应收管理盒子
    # settlement_center_1_element = "//div[@title='应收账单']"
    # settlement_center_2_element = "//div[@title='坏账管理']"
    # settlement_center_3_element = "//div[@title='结算单管理']"

    # 遍历应收管理盒子
    settlement_center_1_element = '[data-menu-id="/erp/finance/receivable/index"]'
    settlement_center_2_element = '[data-menu-id="/erp/finance/badDebt/index"]'
    settlement_center_3_element = '[data-menu-id="/erp/finance/settlementManagement/index"]'

    def Accounts_Receivable_Management(self):    # 应收管理
        # 进入结算中心模块元素
        # self.click('xpath', self.settlement_center_element)

        # 展开应收管理盒子
        self.click('css_selector', self.settlement_center_box_element)

        # 遍历应收管理
        self.click('css_selector', self.settlement_center_1_element)
        self.click('css_selector', self.settlement_center_2_element)
        self.click('css_selector', self.settlement_center_3_element)


class Payment_Management_Page(BasePage):    # 到款管理
    # 展开到款管理盒子元素
    # payment_management_box_element = "//div[@title='到款管理']"
    payment_management_box_element = '[data-menu-id="/daokuanguanli"]'

    # 遍历到款管理元素
    # payment_management_1_element = "//div[@title='到款账户分类设置']"
    # payment_management_2_element = "//div[@title='到款重复确认']"
    # payment_management_3_element = "//div[@title='到款认领']"
    # payment_management_4_element = "//div[@title='客户资金池']"
    # payment_management_5_element = "//div[@title='到款三方协议关联管理']"
    # payment_management_6_element = "//div[@title='确认函管理']"

    # 遍历到款管理元素
    payment_management_1_element = '[data-menu-id="/erp/finance/classifySetting/index"]'
    payment_management_2_element = '[data-menu-id="/erp/finance/repeatConfirm/index"]'
    payment_management_3_element = '[data-menu-id="/erp/finance/accountClaim/index"]'
    payment_management_4_element = '[data-menu-id="/erp/finance/claimRecord/index"]'
    payment_management_5_element = '[data-menu-id="/erp/finance/tripleAgreement/index"]'
    payment_management_6_element = '[data-menu-id="/erp/finance/confirmLetter/index"]'

    def Payment_Management(self):   # 到款管理
        # 展开到款管理盒子
        self.click('css_selector', self.payment_management_box_element)

        # 遍历到款盒子
        self.click('css_selector', self.payment_management_1_element)
        self.click('css_selector', self.payment_management_2_element)
        self.click('css_selector', self.payment_management_3_element)
        self.click('css_selector', self.payment_management_4_element)
        self.click('css_selector', self.payment_management_5_element)
        self.click('css_selector', self.payment_management_6_element)


class Value_Added_Service_Page(BasePage):   # 增值服务盒子
    # 展开增值服务盒子
    # value_added_service_box_element = "//div[@title='增值服务']"
    value_added_service_box_element = '[data-menu-id="/erp/valueAddedServices"]'

    # 遍历增值服务元素
    # value_added_service_1_element = "//div[@title='折让金管理']"
    # value_added_service_2_element = "//div[@title='折让金余额池']"
    # value_added_service_3_element = "//div[@title='佣金管理']"
    # value_added_service_4_element = "//div[@title='佣金余额池']"
    # value_added_service_5_element = "//div[@title='工资形式发放']"
    #
    # # 抵扣/请款管理盒子
    # value_added_service_7_box_element = "//div[@title='抵扣/请款管理']"
    # # 遍历抵扣/请款管理元素
    # value_added_service_7_box1_element = "//div[@title='折让金']"
    # value_added_service_7_box2_element = "//div[@title='佣金']"
    # value_added_service_7_box3_element = "//li[@class='ant-menu-item ant-menu-item-only-child']//div[@title='退伍军人补贴'][contains(text(),'退伍军人补贴')]"
    # value_added_service_7_box4_element = "//li[@class='ant-menu-item ant-menu-item-only-child']//div[@title='附加税返还'][contains(text(),'附加税返还')]"
    #
    # # 补贴管理盒子
    # value_added_service_8_box_element = "//div[@title='补贴管理']"
    # # 遍历补贴管理元素
    # value_added_service_8_box1_element = "/html/body/div[1]/section/section/aside/div/div/div/div[2]/ul/li[5]/ul/li[7]/ul/li[1]/span"   # 退伍军人补贴
    # value_added_service_8_box2_element = "//div[@title='退伍军人补贴余额池']"
    # value_added_service_8_box3_element = "/html/body/div[1]/section/section/aside/div/div/div/div[2]/ul/li[5]/ul/li[7]/ul/li[3]/span"   # 附加税返还
    # # 政府类补贴盒子
    # value_added_service_8_box4_box_element = "//div[@title='政府类补贴']"
    # # 展开政府类补贴
    # value_added_service_8_box4_box1_element = "//div[@title='补贴申请 ( 分公司经理 )']"
    # value_added_service_8_box4_box2_element = "//div[@title='补贴分配结果']"
    # value_added_service_8_box4_box3_element = "//div[@title='收款单位账户池']"
    # value_added_service_8_box4_box4_element = "//div[@title='客户余额池']"
    # value_added_service_8_box4_box5_element = "//div[@title='补贴科目维护']"

    # 遍历增值服务元素
    value_added_service_1_element = '[data-menu-id="/erp/valueAddedServices/discountManage/index"]'
    value_added_service_2_element = '[data-menu-id="/erp/valueAddedServices/discountBalancePool/index"]'
    value_added_service_3_element = '[data-menu-id="/erp/valueAddedServices/brokerageManage/index"]'
    value_added_service_4_element = '[data-menu-id="/erp/valueAddedServices/brokerageBalancePool/index"]'
    value_added_service_5_element = '[data-menu-id="/erp/valueAddedServices/paymentWages/index"]'

    # 抵扣/请款管理盒子
    value_added_service_7_box_element = '[data-menu-id="/erp/valueAddedServices/deduction"]'
    # 遍历抵扣/请款管理元素
    value_added_service_7_box1_element = '[data-menu-id="/erp/valueAddedServices/deductionDiscount/index"]'
    value_added_service_7_box2_element = '[data-menu-id="/erp/valueAddedServices/deductionBrokerage/index"]'
    value_added_service_7_box3_element = '[data-menu-id="/erp/valueAddedServices/deductionVeteran/index"]'
    value_added_service_7_box4_element = '[data-menu-id="/erp/valueAddedServices/deductionTaxRefund/index"]'

    # 补贴管理盒子
    value_added_service_8_box_element = '[data-menu-id="/erp/valueAddedServices/subsidy"'
    # 遍历补贴管理元素
    value_added_service_8_box1_element = '[data-menu-id="/erp/valueAddedServices/subsidyVeteran/index"]'   # 退伍军人补贴
    value_added_service_8_box2_element = '[data-menu-id="/erp/valueAddedServices/subsidyVeteranPool/index"]'
    value_added_service_8_box3_element = '[data-menu-id="/erp/valueAddedServices/subsidyTaxRefund/index"]'   # 附加税返还
    # 政府类补贴盒子
    value_added_service_8_box4_box_element = '[data-menu-id="/erp/valueAddedServices/subsidy/government"]'
    # 展开政府类补贴
    value_added_service_8_box4_box1_element = '[data-menu-id="/erp/valueAddedServices/subsidyApply/index"]'
    value_added_service_8_box4_box2_element = '[data-menu-id="/erp/valueAddedServices/subsidyApplyResult/index"]'
    value_added_service_8_box4_box3_element = '[data-menu-id="/erp/valueAddedServices/collectionUnit/index"]'
    value_added_service_8_box4_box4_element = '[data-menu-id="/erp/valueAddedServices/customerBalance/index"]'
    value_added_service_8_box4_box5_element = '[data-menu-id="/erp/valueAddedServices/subsidySubjects/index"]'

    def Value_Added_Service(self):      # 增值服务
        # 展开增值服务盒子
        self.click('css_selector', self.value_added_service_box_element)

        # 遍历增值服务
        self.click('css_selector', self.value_added_service_1_element)
        self.click('css_selector', self.value_added_service_2_element)
        self.click('css_selector', self.value_added_service_3_element)
        self.click('css_selector', self.value_added_service_4_element)
        self.click('css_selector', self.value_added_service_5_element)

        # 展开抵扣/请款管理盒子
        self.click('css_selector', self.value_added_service_7_box_element)
        # 遍历抵扣/请款管理盒子
        self.click('css_selector', self.value_added_service_7_box1_element)
        self.click('css_selector', self.value_added_service_7_box2_element)
        self.click('css_selector', self.value_added_service_7_box3_element)
        self.click('css_selector', self.value_added_service_7_box4_element)

        # 补贴管理盒子
        self.click('css_selector', self.value_added_service_8_box_element)
        # 遍历补贴管理
        self.click('css_selector', self.value_added_service_8_box1_element)
        self.click('css_selector', self.value_added_service_8_box2_element)
        self.click('css_selector', self.value_added_service_8_box3_element)
        # 展开政府类补贴盒子
        self.click('css_selector', self.value_added_service_8_box4_box_element)
        # 遍历政府类补贴
        self.click('css_selector', self.value_added_service_8_box4_box1_element)
        self.click('css_selector', self.value_added_service_8_box4_box2_element)
        self.click('css_selector', self.value_added_service_8_box4_box3_element)
        self.click('css_selector', self.value_added_service_8_box4_box4_element)
        self.click('css_selector', self.value_added_service_8_box4_box5_element)


class Bid_Security_Management_Page(BasePage):   # 投标保证金管理
    # 进入投标保证金管理元素
    # bid_security_management_element = "//div[@title='投标保证金管理']"
    bid_security_management_element = '[data-menu-id="/erp/finance/bidBondWhitelist/index"]'

    def Bid_Security_Management(self):      # 投标保证金管理
        self.click('css_selector', self.bid_security_management_element)


class Performance_Bond_Management_Page(BasePage):   # 履约保证金管理
    # 履约保证金管理元素
    # performance_bond_management_element = "//div[@title='履约保证金管理']"
    performance_bond_management_element = '[data-menu-id="/erp/finance/performanceBond/index"]'

    def Performance_Bond_Management(self):    # 履约保证金管理
        self.click('css_selector', self.performance_bond_management_element)


class Accounts_Receivable_Audit_Page(BasePage):   # 应收账款审核
    # 应收账款审核元素
    # accounts_receivable_audit_page_element = "//li[@class='ant-menu-item']//div[@title='应收账款审核'][contains(text(),'应收账款审核')]"
    accounts_receivable_audit_page_element = '[data-menu-id="/erp/finance/receivableAudit/index"]'

    def Accounts_Receivable_Audit(self):    # 应收账款审核
        self.click('css_selector', self.accounts_receivable_audit_page_element)


class Interest_Whitelist_Page(BasePage):   # 利息白名单
    # 利息白名单元素
    # interest_whitelist_element = "//div[@title='利息白名单']"
    interest_whitelist_element = '[data-menu-id="/erp/finance/interestWhitelist/index"]'

    def Interest_Whitelist(self):    # 利息白名单
        self.click('css_selector', self.interest_whitelist_element)


class White_List_of_Guarantee_Deposit_Page(BasePage):   # 保证金白名单
    # 保证金白名单元素
    # white_list_of_guarantee_deposit_element = "//div[@title='保证金白名单']"
    white_list_of_guarantee_deposit_element = '[data-menu-id="/erp/finance/marginWhitelist/index"]'

    def White_List_of_Guarantee_Deposit(self):    # 保证金白名单
        self.click('css_selector', self.white_list_of_guarantee_deposit_element)


class Tax_Return_Page(BasePage):    # 个税申报
    # 个税申报盒子
    # tax_return_box_element = "//div[@class='ant-menu-submenu-title']//div[@title='个税申报'][contains(text(),'个税申报')]"
    tax_return_box_element = '[data-menu-id="/tax"]'

    # 部分遍历个税申报盒子
    # tax_return_1_element = "//div[@title='系统报税截止日设置']"
    # tax_return_2_element = "//div[@title='分部门申报个税']"
    # tax_return_3_element = "//div[@title='报税文件导出']"

    # 部分遍历个税申报盒子
    tax_return_1_element = '[data-menu-id="/tax/tax-systemEndSetting/index"]'
    tax_return_2_element = '[data-menu-id="/tax/tax-deptApply/index"]'
    tax_return_3_element = '[data-menu-id="/tax/tax-documentExport/index"]'

    def Tax_Return(self):   # 个税申报
        # 个税申报盒子
        self.click('css_selector', self.tax_return_box_element)

        # 部分遍历个税申报
        self.click('css_selector', self.tax_return_1_element)
        self.click('css_selector', self.tax_return_2_element)
        self.click('css_selector', self.tax_return_3_element)



