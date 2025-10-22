from work.script_data.T116_Environment_Page_Traverse.Base_Class.Base_Page import BasePage
from work.script_data.T116_Environment_Page_Traverse.Tools.log_tool import Logging

log = Logging()


class Basic_Configuration_Tab(BasePage):  # 进入基础配置Tab
    # 进入基础配置Tab
    basic_configuration_element = "//div[contains(text(),'基础配置')]"

    def Basic_Configuration_Tab(self):  # 进入基础配置Tab
        # 进入基础配置Tab
        self.click('xpath', self.basic_configuration_element)


class Intermediary_Management_Page(BasePage):  # 居间人管理模块
    # 进入基础配置模块元素
    # basic_configuration_element = "//div[contains(text(),'基础配置')]"

    # 居间人管理盒子
    # intermediary_management_element = "//div[@title='居间人管理']"
    intermediary_management_element = '[data-menu-id="/erp/basis/IntermediaryManagement/index"]'

    def Intermediary_Management(self):  # 居间人管理模块
        # 进入基础配置模块
        # self.click('xpath', self.basic_configuration_element)

        # 居间人管理
        self.click('css_selector', self.intermediary_management_element)


class Intermediary_Viewing_Page(BasePage):  # 居间人查看模块
    # 居间人查看盒子
    # intermediary_viewing_element = "//div[@title='居间人查看']"
    intermediary_viewing_element = '[data-menu-id="/erp/basis/IntermediaryManagementDetail/index"]'

    def Intermediary_Viewing(self):  # 居间人查看模块
        # 居间人查看
        self.click('css_selector', self.intermediary_viewing_element)


class Management_of_Public_Welfare_Schemes_Page(BasePage):  # 社公方案管理
    # 社公方案管理盒子
    # Management_of_Public_Welfare_Schemes_box_element = "//div[@title='社公方案管理']"
    Management_of_Public_Welfare_Schemes_box_element = '[data-menu-id="/shegongfanganguanli"]'

    # 遍历社公方案盒子
    # Management_of_Public_Welfare_Schemes_1_element = "//div[@title='险种配置']"
    # Management_of_Public_Welfare_Schemes_2_element = "//div[@title='社保公积金险种']"
    # Management_of_Public_Welfare_Schemes_3_element = "//div[@title='社保账户管理']"
    # Management_of_Public_Welfare_Schemes_4_element = "//div[@title='社保公积金方案']"
    # Management_of_Public_Welfare_Schemes_5_element = "//div[@title='社平工资']"
    # Management_of_Public_Welfare_Schemes_6_element = "//div[@title='工会费政策配置']"
    # Management_of_Public_Welfare_Schemes_7_element = "//div[@title='残保金政策配置']"

    # 遍历社公方案盒子
    Management_of_Public_Welfare_Schemes_1_element = '[data-menu-id="/erp/basis/InsuranceType/index"]'
    Management_of_Public_Welfare_Schemes_2_element = '[data-menu-id="/erp/basis/socialHouseProduct/index"]'
    Management_of_Public_Welfare_Schemes_3_element = '[data-menu-id="/erp/basis/socialAccount/index"]'
    Management_of_Public_Welfare_Schemes_4_element = '[data-menu-id="/erp/basis/socialProgramme/index"]'
    Management_of_Public_Welfare_Schemes_5_element = '[data-menu-id="/erp/basis/socialPay/index"]'
    Management_of_Public_Welfare_Schemes_6_element = '[data-menu-id="/erp/basis/unionFunds/index"]'
    Management_of_Public_Welfare_Schemes_7_element = '[data-menu-id="/erp/basis/securityFunds/index"]'

    def Management_of_Public_Welfare_Schemes(self):  # 社公方案管理
        # 展开社公方案管理盒子
        self.click('css_selector', self.Management_of_Public_Welfare_Schemes_box_element)

        # 遍历社公方案
        self.click('css_selector', self.Management_of_Public_Welfare_Schemes_1_element)
        self.click('css_selector', self.Management_of_Public_Welfare_Schemes_2_element)
        self.click('css_selector', self.Management_of_Public_Welfare_Schemes_3_element)
        self.click('css_selector', self.Management_of_Public_Welfare_Schemes_4_element)
        self.click('css_selector', self.Management_of_Public_Welfare_Schemes_5_element)
        self.click('css_selector', self.Management_of_Public_Welfare_Schemes_6_element)
        self.click('css_selector', self.Management_of_Public_Welfare_Schemes_7_element)


class Commercial_Insurance_Configuration_Page(BasePage):  # 商业险配置
    # 商业险配置盒子
    # commercial_insurance_configuration_box_element = "//div[@title='商业险配置']"
    commercial_insurance_configuration_box_element = '[data-menu-id="/shangyexianpeizhi"]'

    # 遍历商业险配置元素
    # commercial_insurance_configuration_1_element = "//div[@title='商业险险种']"
    # commercial_insurance_configuration_2_element = "//div[@title='商业险方案管理']"

    # 遍历商业险配置元素
    commercial_insurance_configuration_1_element = '[data-menu-id="/erp/basis/commercialProduct/index"]'
    commercial_insurance_configuration_2_element = '[data-menu-id="/erp/basis/commercialScheme/index"]'

    sending_rule_settings_button_element = "//span[contains(text(),'发件规则设置')]"  # 发件规则设置按钮
    return_button_element = "//span[@class='!ml-4px']"  # 返回按钮

    def Commercial_Insurance_Configuration(self):  # 商业险配置
        # 展开商业险配置盒子
        self.click('css_selector', self.commercial_insurance_configuration_box_element)

        # 遍历商业险配置
        self.click('css_selector', self.commercial_insurance_configuration_1_element)
        self.click('css_selector', self.commercial_insurance_configuration_2_element)

        # 点击发件规则设置按钮
        try:
            self.click('xpath', self.sending_rule_settings_button_element)
            self.click('xpath', self.return_button_element)
        except Exception as e:
            log.logging_error(f"点击发件规则设置出现异常：{e}")


class Template_Management_Page(BasePage):  # 模板管理盒子
    # 模板管理盒子
    # template_management_box_element = "//div[@title='模板管理']"
    template_management_box_element = '[data-menu-id="/mubanguanli"]'

    # 遍历模板管理
    # template_management_1_element = "//div[@title='人员合同模板管理']"
    template_management_1_element = '[data-menu-id="/erp/basis/personalContractTemp/index"]'

    def Template_Management(self):  # 模板管理盒子
        # 展开模板管理
        self.click('css_selector', self.template_management_box_element)

        # 遍历模板管理
        self.click('css_selector', self.template_management_1_element)


class Internal_Unit_Management_Page(BasePage):  # 内部单位管理
    # 内部单位管理盒子
    # Internal_Unit_Management_box_element = "//div[@title='内部单位管理']"
    Internal_Unit_Management_box_element = '[data-menu-id="/erp/basis/internalUnit/index"]'

    def Internal_Unit_Management(self):  # 内部单位管理
        # 内部单位管理
        self.click('css_selector', self.Internal_Unit_Management_box_element)


class Customer_Brand_Page(BasePage):  # 客户品牌
    # 客户品牌盒子
    # customer_brand_box_element = "//div[@title='客户品牌']"
    customer_brand_box_element = '[data-menu-id="/erp/basis/internalUnit/index"]'

    def Customer_Brand(self):  # 客户品牌
        # 客户品牌
        self.click('css_selector', self.customer_brand_box_element)


class Industry_Classification_Page(BasePage):  # 行业分类
    # 行业分类盒子
    # industry_classification_box_element = "//div[@title='行业分类']"
    industry_classification_box_element = '[data-menu-id="/erp/basis/trade/index"]'

    def Industry_Classification(self):  # 行业分类
        # 行业分类
        self.click('css_selector', self.industry_classification_box_element)


class Supplier_Management_Page(BasePage):  # 供应商管理
    # 供应商管理盒子
    # supplier_management_page_box_element = "//div[@title='供应商管理']"
    supplier_management_page_box_element = '[data-menu-id="/erp/basis/supplier/index"]'

    def Supplier_Management(self):  # 供应商管理
        # 供应商管理
        self.click('css_selector', self.supplier_management_page_box_element)


class Invoice_Category_Configuration_Page(BasePage):  # 发票类目配置
    # 发票类目配置盒子
    # invoice_category_configuration_box_element = "//div[@class='ant-menu-submenu-title']//div[@title='发票类目配置'][contains(text(),'发票类目配置')]"
    invoice_category_configuration_box_element = '[data-menu-id="/fapiaoleimupeizhi"]'

    # 遍历发票类目配置
    # invoice_category_configuration_1_element = "//div[@title='税收编码配置']"
    # invoice_category_configuration_2_element = "//li[@role='menuitem']//div[@title='发票类目配置'][contains(text(),'发票类目配置')]"
    # invoice_category_configuration_3_element = "//div[@title='科目配置']"

    # 遍历发票类目配置
    invoice_category_configuration_1_element = '[data-menu-id="/erp/basis/taxCode/index"]'
    invoice_category_configuration_2_element = '[data-menu-id="/erp/basis/invoiceCategory/index"]'
    invoice_category_configuration_3_element = '[data-menu-id="/erp/basis/subjectConfig/index"]'

    def Invoice_Category_Configuration(self):  # 发票类目配置
        # 发票类目配置
        self.click('css_selector', self.invoice_category_configuration_box_element)

        # 遍历发票类目配置
        self.click('css_selector', self.invoice_category_configuration_1_element)
        self.click('css_selector', self.invoice_category_configuration_2_element)
        self.click('css_selector', self.invoice_category_configuration_3_element)


class Extended_Field_Configuration_Page(BasePage):  # 扩展字段配置
    # 扩展字段配置盒子
    # Extended_Field_Configuration_box_element = "//div[@title='扩展字段配置']"
    Extended_Field_Configuration_box_element = '[data-menu-id="/erp/basis/userAdditional/index"]'

    def Extended_Field_Configuration(self):  # 扩展字段配置
        self.click('css_selector', self.Extended_Field_Configuration_box_element)


class Level_Configuration_of_Work_related_Injury_Disputes_Page(BasePage):  # 工伤纠纷等级配置
    # 工伤纠纷等级配置盒子
    # level_configuration_of_work_related_injury_disputes_box_element = "//div[@title='工伤纠纷等级配置']"
    level_configuration_of_work_related_injury_disputes_box_element = '[data-menu-id="/erp/basis/workInjuryConfiguration/index"]'

    def Level_Configuration_of_Work_related_Injury_Disputes(self):  # 工伤纠纷等级配置
        # 工伤纠纷等级配置
        self.click('css_selector', self.level_configuration_of_work_related_injury_disputes_box_element)


class Personnel_Material_Collection_Template_Page(BasePage):  # 人员材料收集模板
    # 人员材料收集模板盒子
    # personnel_material_collection_template_box_element = "//div[@title='人员材料收集模板']"
    personnel_material_collection_template_box_element = '[data-menu-id="/erp/basis/userMaterial/index"]'

    def Personnel_Material_Collection_Template(self):  # 人员材料收集模板
        # 人员材料收集模板
        self.click('css_selector', self.personnel_material_collection_template_box_element)


class Commercial_Insurance_Job_Classification_Maintenance_Page(BasePage):  # 商业险工种分类维护
    # 商业险工种分类维护
    # commercial_insurance_job_classification_maintenance_box_element = "//div[@title='商业险工种分类维护']"
    commercial_insurance_job_classification_maintenance_box_element = '[data-menu-id="/erp/basis/commercialProfessionType/index"]'

    def Commercial_Insurance_Job_Classification_Maintenance(self):  # 商业险工种分类维护
        # 商业险工种分类维护
        self.click('css_selector', self.commercial_insurance_job_classification_maintenance_box_element)


class Material_Library_Configuration_Page(BasePage):  # 材料库配置
    # 材料库配置
    # material_library_configuration_box_element = "//div[@title='材料库配置']"
    material_library_configuration_box_element = '[data-menu-id="/erp/basis/materialWarehouse/index"]'

    def Material_Library_Configuration(self):  # 材料库配置
        # 材料库配置
        self.click('css_selector', self.material_library_configuration_box_element)


class Template_Configuration_for_Commercial_Insurance_Policies_Page(BasePage):  # 商保保单模板配置
    # 商保保单模板配置
    # template_configuration_for_commercial_insurance_policies_box_element = "//div[@title='商保保单模板配置']"
    template_configuration_for_commercial_insurance_policies_box_element = '[data-menu-id="/erp/basis/guaranteeSlip/index"]'

    def Template_Configuration_for_Commercial_Insurance_Policies(self):  # 商保保单模板配置
        # 商保保单模板配置
        self.click('css_selector', self.template_configuration_for_commercial_insurance_policies_box_element)


class Industry_Classification_Management_Page(BasePage):  # 行业分类管理
    # 行业分类管理
    # industry_classification_management_box_element = "//div[@title='行业分类管理']"
    industry_classification_management_box_element = '[data-menu-id="/erp/basis/industryClass/index"]'

    def Industry_Classification_Management(self):  # 行业分类管理
        # 行业分类管理
        self.click('css_selector', self.industry_classification_management_box_element)


class Policy_Group_Configuration_Page(BasePage):  # 政策组配置
    # 政策组配置
    # policy_group_configuration_box_element = "//div[@title='政策组配置']"
    policy_group_configuration_box_element = '[data-menu-id="/erp/basis/policyUnit/index"]'

    def Policy_Group_Configuration(self):  # 政策组配置
        # 政策组配置
        self.click('css_selector', self.policy_group_configuration_box_element)
