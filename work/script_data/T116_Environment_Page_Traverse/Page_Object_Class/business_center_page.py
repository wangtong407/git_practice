import time

from work.script_data.T116_Environment_Page_Traverse.Base_Class.Base_Page import BasePage
from work.script_data.T116_Environment_Page_Traverse.Tools.log_tool import Logging

log = Logging()


class Business_Center_Tab(BasePage):    # 进入商务中心模块Tab
    # 进入商务中心模块Tab
    business_center_element = "//div[contains(text(),'商务中心')]"

    def Business_Center_Tab(self):  # 进入商务中心模块Tab
        # 进入商务中心模块Tab
        self.click('xpath', self.business_center_element)


# 客户管理模块
class Customer_Management_Page(BasePage):
    # 进入商务中心模块元素
    # business_center_element = "//div[contains(text(),'商务中心')]"

    # 客户管理盒子元素
    # customer_management_box_element = "//div[@class='ant-menu-submenu-title']//div[@title='客户管理'][contains(text(),'客户管理')]"
    #
    # # 客户管理盒子元素
    # customer_management_1_element = "//div[@title='客户黑名单']"
    # customer_management_2_element = "//li[@role='menuitem']//div[@title='客户管理'][contains(text(),'客户管理')]"
    # customer_management_3_element = "//div[@title='费用表白名单']"
    # customer_management_4_element = "//div[@title='协议黑名单']"
    # customer_management_5_element = "//div[@title='集团管理']"
    # customer_management_6_element = "//div[@title='人员信息材料配置']"
    # customer_management_7_element = "//div[@title='人员合同模板审批']"
    #
    # # 服务费公式盒子
    # customer_management_8_box_element = "//div[@title='服务费公式管理']"
    # customer_management_8_box1_element = "//div[@title='公式类别']"
    # customer_management_8_box2_element = "//div[@title='公式列表']"
    #
    # customer_management_9_element = "//div[@title='派遣业务白名单']"

    # 客户管理盒子元素
    customer_management_box_element = '[data-menu-id="/customer"]'

    # 客户管理盒子元素
    customer_management_1_element = '[data-menu-id="/erp/business/blackList/index"]'
    customer_management_2_element = '[data-menu-id="/erp/business/customerManage/index"]'
    customer_management_3_element = '[data-menu-id="/erp/business/whiteList/index"]'
    customer_management_4_element = '[data-menu-id="/erp/business/protocolBlacklist/index"]'
    customer_management_5_element = '[data-menu-id="/erp/business/corporateManage/index"]'
    customer_management_6_element = '[data-menu-id="/erp/business/personnelMaterial/index"]'
    customer_management_7_element = '[data-menu-id="/erp/business/personnelContractApprove/index"]'

    # 服务费公式盒子
    customer_management_8_box_element = '[data-menu-id="/"]'
    customer_management_8_box1_element = '[data-menu-id="/erp/business/formulaCategory/index"]'
    customer_management_8_box2_element = '[data-menu-id="/erp/business/formulaList/index"]'

    customer_management_9_element = '[data-menu-id="/erp/business/whiteListOfDiapatch/index"]'

    # 客户管理遍历
    def Customer_Management(self):
        # 进入商务中心模块
        # self.click('xpath', self.business_center_element)

        # 展开客户管理
        self.click('css_selector', self.customer_management_box_element)

        # 遍历客户管理
        self.click('css_selector', self.customer_management_1_element)
        self.click('css_selector', self.customer_management_2_element)
        self.click('css_selector', self.customer_management_3_element)
        self.click('css_selector', self.customer_management_4_element)
        self.click('css_selector', self.customer_management_5_element)
        self.click('css_selector', self.customer_management_6_element)
        self.click('css_selector', self.customer_management_7_element)

        self.click('css_selector', self.customer_management_8_box_element)
        self.click('css_selector', self.customer_management_8_box1_element)
        self.click('css_selector', self.customer_management_8_box2_element)

        self.click('css_selector', self.customer_management_9_element)


# 协议管理模块
class Agreement_Management_Page(BasePage):
    # 展开协议管理盒子元素
    # agreement_management_box_element = "//div[@class='ant-menu-submenu-title']//div[@title='协议管理'][contains(text(),'协议管理')]"
    agreement_management_box_element = '[data-menu-id="/xieyi"]'

    # 遍历协议管理元素
    # agreement_management_1_element = "//li[@class='ant-menu-item ant-menu-item-only-child']//div[@title='协议管理'][contains(text(),'协议管理')]"
    # agreement_management_2_element = "//div[@title='立项单管理']"
    # agreement_management_3_element = "//div[@title='账单管理']"
    # agreement_management_4_element = "//div[@title='业务场景管理（审批）']"
    # agreement_management_5_element = "//div[@title='业务场景管理（业务员）']"
    # agreement_management_6_element = "//div[@title='风险金管理']"
    # agreement_management_7_element = "//div[@title='垫付金管理']"
    #
    # # 原件管理盒子元素
    # agreement_management_8_box_element = "//div[@title='原件管理']"
    # agreement_management_8_box1_element = "//div[@title='待关联原件编号']"
    # agreement_management_8_box2_element = "//div[@title='已关联原件编号']"
    # agreement_management_8_box3_element = "//div[@title='原件编号配置']"

    # 遍历协议管理元素
    agreement_management_1_element = '[data-menu-id="/erp/business/agreementManagement/index"]'

    agreement_management_details_button = '//*[@id="/erp/business/agreementManagement/index"]/div[2]/div/div[3]/div/div[3]/div/div/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td/div/div/button/span'     # 详情按钮
    agreement_management_other_configurations_button = "//div[contains(text(),'其他配置')]"     # 其他配置按钮
    # agreement_management_other_configurations_page_fwfpz_element = "//div[contains(text(),'服务费配置')]"
    # agreement_management_other_configurations_page_ghfcbjpz_element = "//div[contains(text(),'工会费残保金配置')]"
    # agreement_management_other_configurations_page_kpxx_element = "//div[contains(text(),'开票信息')]"
    # agreement_management_other_configurations_page_zzfw_element = "//div[contains(text(),'增值服务')]"
    # agreement_management_other_configurations_page_gwgl_element = "//div[contains(text(),'岗位管理')]"
    # agreement_management_other_configurations_page_scfj_element = "//div[contains(text(),'上传附件')]"
    # agreement_management_other_configurations_page_fxjpz_element = "//div[contains(text(),'风险金配置')]"
    agreement_management_other_configurations_page_return_element = "//span[@class='!ml-4px']"  # 返回按钮

    agreement_management_2_element = '[data-menu-id="/erp/business/projectInit/index"]'
    agreement_management_3_element = '[data-menu-id="/erp/business/invoiceManage/index"]'
    agreement_management_4_element = '[data-menu-id="/erp/business/sceneManage/Approval"]'
    agreement_management_5_element = '[data-menu-id="/erp/business/sceneManage/SalesStaff"]'
    agreement_management_6_element = '[data-menu-id="/erp/business/indemnity/index"]'
    agreement_management_7_element = '[data-menu-id="/erp/business/advance/index"]'

    # 原件管理盒子元素
    agreement_management_8_box_element = '[data-menu-id="/yuanjian"]'
    agreement_management_8_box1_element = '[data-menu-id="/erp/business/docManage/unlinkedDoc"]'
    agreement_management_8_box2_element = '[data-menu-id="/erp/business/docManage/linkedDoc"]'
    agreement_management_8_box3_element = '[data-menu-id="/erp/basis/originalNumber/index"]'

    def Agreement_Management(self):
        # 展开协议管理盒子
        self.click('css_selector', self.agreement_management_box_element)

        # 遍历协议管理
        try:
            self.click('css_selector', self.agreement_management_1_element)
        except Exception as e:
            log.logging_error(f"协议管理页面出现异常：{e}")
            self.screenshot('协议管理页面出现异常截图')
        else:
            # 点击详情按钮，遍历协议内容，由于有多个详情按钮，获取所有详情按钮后根据索引点击
            view_buttons = self.visibility_of_all_elements('xpath', "//span[contains(text(),'详情')]")
            if len(view_buttons) > 2:
                view_buttons[2].click()
                time.sleep(1)
            # self.click('xpath', self.agreement_management_details_button)
            self.click('xpath', self.agreement_management_other_configurations_button)
            self.click('xpath', self.agreement_management_other_configurations_page_return_element)

        self.click('css_selector', self.agreement_management_2_element)
        self.click('css_selector', self.agreement_management_3_element)
        self.click('css_selector', self.agreement_management_4_element)
        self.click('css_selector', self.agreement_management_5_element)
        self.click('css_selector', self.agreement_management_6_element)
        self.click('css_selector', self.agreement_management_7_element)

        # 展开原件管理盒子
        self.click('css_selector', self.agreement_management_8_box_element)
        self.click('css_selector', self.agreement_management_8_box1_element)
        self.click('css_selector', self.agreement_management_8_box2_element)
        self.click('css_selector', self.agreement_management_8_box3_element)


# 事业部协议模块
class Business_Division_Agreement_Page(BasePage):
    # 事业部协议盒子
    # business_division_agreement_box_element = "//div[@title='事业部协议']"
    business_division_agreement_box_element = '[data-menu-id="/agreement"]'

    # 遍历事业部协议元素
    # business_division_agreement_1_element = "//div[@title='协议模板管理']"
    # business_division_agreement_2_element = "//div[@title='协议录入']"
    # business_division_agreement_3_element = "//div[@title='协议审核']"
    # business_division_agreement_4_element = '/html/body/div[1]/section/section/aside/div/div/div/div[2]/ul/li[4]/ul/li[4]/span'
    # business_division_agreement_5_element = "//div[@title='协议单位管理']"
    # business_division_agreement_6_element = "//div[@title='协议业务线管理']"

    # 遍历事业部协议元素
    business_division_agreement_1_element = '[data-menu-id="/agreement/templates/index"]'
    business_division_agreement_2_element = '[data-menu-id="/agreement/entering/index"]'
    business_division_agreement_3_element = '[data-menu-id="/agreement/examine/index"]'
    business_division_agreement_4_element = '[data-menu-id="/agreement/management/index"]'
    business_division_agreement_5_element = '[data-menu-id="/agreement/company/index"]'
    business_division_agreement_6_element = '[data-menu-id="/agreement/bizManage/index"]'

    def Business_Division_Agreement(self):
        # 展开事业部协议盒子
        self.click('css_selector', self.business_division_agreement_box_element)

        # 遍历事业部协议
        self.click('css_selector', self.business_division_agreement_1_element)
        self.click('css_selector', self.business_division_agreement_2_element)
        self.click('css_selector', self.business_division_agreement_3_element)
        self.click('css_selector', self.business_division_agreement_4_element)
        self.click('css_selector', self.business_division_agreement_5_element)
        self.click('css_selector', self.business_division_agreement_6_element)

