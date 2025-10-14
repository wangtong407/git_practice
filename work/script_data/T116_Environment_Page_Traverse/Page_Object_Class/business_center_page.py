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
    customer_management_box_element = "//div[@class='ant-menu-submenu-title']//div[@title='客户管理'][contains(text(),'客户管理')]"

    # 客户管理盒子元素
    customer_management_1_element = "//div[@title='客户黑名单']"
    customer_management_2_element = "//li[@role='menuitem']//div[@title='客户管理'][contains(text(),'客户管理')]"
    customer_management_3_element = "//div[@title='费用表白名单']"
    customer_management_4_element = "//div[@title='协议黑名单']"
    customer_management_5_element = "//div[@title='集团管理']"
    customer_management_6_element = "//div[@title='人员信息材料配置']"
    customer_management_7_element = "//div[@title='人员合同模板审批']"

    # 服务费公式盒子
    customer_management_8_box_element = "//div[@title='服务费公式管理']"
    customer_management_8_box1_element = "//div[@title='公式类别']"
    customer_management_8_box2_element = "//div[@title='公式列表']"

    customer_management_9_element = "//div[@title='派遣业务白名单']"

    # 客户管理遍历
    def Customer_Management(self):
        # 进入商务中心模块
        # self.click('xpath', self.business_center_element)

        # 展开客户管理
        self.click('xpath', self.customer_management_box_element)

        # 遍历客户管理
        self.click('xpath', self.customer_management_1_element)
        self.click('xpath', self.customer_management_2_element)
        self.click('xpath', self.customer_management_3_element)
        self.click('xpath', self.customer_management_4_element)
        self.click('xpath', self.customer_management_5_element)
        self.click('xpath', self.customer_management_6_element)
        self.click('xpath', self.customer_management_7_element)

        self.click('xpath', self.customer_management_8_box_element)
        self.click('xpath', self.customer_management_8_box1_element)
        self.click('xpath', self.customer_management_8_box2_element)

        self.click('xpath', self.customer_management_9_element)


# 协议管理模块
class Agreement_Management_Page(BasePage):
    # 展开协议管理盒子元素
    agreement_management_box_element = "//div[@class='ant-menu-submenu-title']//div[@title='协议管理'][contains(text(),'协议管理')]"

    # 遍历协议管理元素
    agreement_management_1_element = "//li[@class='ant-menu-item ant-menu-item-only-child']//div[@title='协议管理'][contains(text(),'协议管理')]"
    agreement_management_2_element = "//div[@title='立项单管理']"
    agreement_management_3_element = "//div[@title='账单管理']"
    agreement_management_4_element = "//div[@title='业务场景管理（审批）']"
    agreement_management_5_element = "//div[@title='业务场景管理（业务员）']"
    agreement_management_6_element = "//div[@title='风险金管理']"
    agreement_management_7_element = "//div[@title='垫付金管理']"

    # 原件管理盒子元素
    agreement_management_8_box_element = "//div[@title='原件管理']"
    agreement_management_8_box1_element = "//div[@title='待关联原件编号']"
    agreement_management_8_box2_element = "//div[@title='已关联原件编号']"
    agreement_management_8_box3_element = "//div[@title='原件编号配置']"

    def Agreement_Management(self):
        # 展开协议管理盒子
        self.click('xpath', self.agreement_management_box_element)

        # 遍历协议管理
        self.click('xpath', self.agreement_management_1_element)
        self.click('xpath', self.agreement_management_2_element)
        self.click('xpath', self.agreement_management_3_element)
        self.click('xpath', self.agreement_management_4_element)
        self.click('xpath', self.agreement_management_5_element)
        self.click('xpath', self.agreement_management_6_element)
        self.click('xpath', self.agreement_management_7_element)

        # # 展开原件管理盒子
        self.click('xpath', self.agreement_management_8_box_element)
        self.click('xpath', self.agreement_management_8_box1_element)
        self.click('xpath', self.agreement_management_8_box2_element)
        self.click('xpath', self.agreement_management_8_box3_element)


# 事业部协议模块
class Business_Division_Agreement_Page(BasePage):
    # 事业部协议盒子
    business_division_agreement_box_element = "//div[@title='事业部协议']"

    # 遍历事业部协议元素
    business_division_agreement_1_element = "//div[@title='协议模板管理']"
    business_division_agreement_2_element = "//div[@title='协议录入']"
    business_division_agreement_3_element = "//div[@title='协议审核']"
    business_division_agreement_4_element = '/html/body/div[1]/section/section/aside/div/div/div/div[2]/ul/li[4]/ul/li[4]/span'
    business_division_agreement_5_element = "//div[@title='协议单位管理']"
    business_division_agreement_6_element = "//div[@title='协议业务线管理']"

    def Business_Division_Agreement(self):
        # 展开事业部协议盒子
        self.click('xpath', self.business_division_agreement_box_element)

        # 遍历事业部协议
        self.click('xpath', self.business_division_agreement_1_element)
        self.click('xpath', self.business_division_agreement_2_element)
        self.click('xpath', self.business_division_agreement_3_element)
        self.click('xpath', self.business_division_agreement_4_element)
        self.click('xpath', self.business_division_agreement_5_element)
        self.click('xpath', self.business_division_agreement_6_element)

