import time

from work.script_data.T116_Environment_Page_Traverse.Base_Class.Base_Page import BasePage
from work.script_data.T116_Environment_Page_Traverse.Tools.log_tool import Logging

log = Logging()


class Business_Processing_Tab(BasePage):    # 进入业务办理Tab
    # 进入业务办理Tab
    business_processing_element = "//div[contains(text(),'业务办理')]"

    def Business_Processing_Tab(self):  # 进入业务办理Tab
        # 进入商务中心模块Tab
        self.click('xpath', self.business_processing_element)
        # self.click('xpath', self.skip_guidance_element)


class Employee_Management_Page(BasePage):  # 员工管理模块
    # 进入业务办理模块元素
    # business_processing_element = "//div[contains(text(),'业务办理')]"

    # 员工管理盒子元素
    # employee_management_box_element = "//div[@title='员工管理']"
    #
    # # 遍历员工管理元素
    # employee_management_1_element = "//div[@title='订单查询']"
    # employee_management_2_element = "//div[@title='人员管理']"
    # employee_management_3_element = "//div[@title='人员合同填充']"
    # employee_management_4_element = "//div[@title='人员批量处理']"
    # employee_management_5_element = "//div[@title='人员合同管理']"
    #
    # # 展开人员转移盒子
    # employee_management_6_box_element = "//div[@title='人员转移']"
    # # 遍历人员转移元素
    # employee_management_6_box1_element = "//div[@title='我发起的']"
    # employee_management_6_box2_element = "//div[@title='待审核（客服）']"
    # employee_management_6_box3_element = "//div[@title='待审核（申报）']"
    #
    # # 展开黑白名单设置盒子
    # employee_management_7_box_element = "//div[@title='黑白名单设置']"
    # # 遍历黑白名单设置元素
    # employee_management_7_box1_element = "//div[@title='商业险白名单']"
    # employee_management_7_box2_element = "//div[@title='人员黑名单']"
    # employee_management_7_box3_element = "//div[@title='人员合同白名单']"
    # employee_management_7_box4_element = "//div[@title='正确身份证']"
    #
    # employee_management_8_element = "//div[@title='外部数据导入']"

    # 员工管理盒子元素
    employee_management_box_element = '[data-menu-id="/erp/personnel"]'

    # 遍历员工管理元素
    employee_management_1_element = '[data-menu-id="/erp/personnel/order/index"]'

    skip_guidance_element = "//*[contains(text(),'跳过引导')]"  # 首次会出现弹窗

    employee_management_view_button_element = '//*[@id="/erp/personnel/list/index"]/div[2]/div[1]/div[3]/div/div[3]/div/div/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td/div/div/button/span'  # 点击查看按钮
    employee_management_return_button_element = "//span[@class='!ml-4px']"  # 点击返回按钮

    employee_management_2_element = '[data-menu-id="/erp/personnel/list/index"]'
    employee_management_3_element = '[data-menu-id="/erp/personnel/contractFill/index"]'
    employee_management_4_element = '[data-menu-id="/erp/personnel/batch/index"]'
    employee_management_5_element = '[data-menu-id="/erp/personnel/contract/index"]'

    # 展开人员转移盒子
    employee_management_6_box_element = '[data-menu-id="/erp/personnel/transfer"]'
    # 遍历人员转移元素
    employee_management_6_box1_element = '[data-menu-id="/erp/personnel/transfer/MyInitiate/index"]'
    employee_management_6_box2_element = '[data-menu-id="/erp/personnel/transfer/AuditCustomerService/index"]'
    employee_management_6_box3_element = '[data-menu-id="/erp/personnel/transfer/AuditDeclaration/index"]'

    # 展开黑白名单设置盒子
    employee_management_7_box_element = '[data-menu-id="/erp/personnel/whiteList"]'
    # 遍历黑白名单设置元素
    employee_management_7_box1_element = '[data-menu-id="/erp/personnel/whiteList/businessWhite/index"]'
    employee_management_7_box2_element = '[data-menu-id="/erp/personnel/whiteList/personBlackList/index"]'
    employee_management_7_box3_element = '[data-menu-id="/erp/personnel/whiteList/contractWhite/index"]'
    employee_management_7_box4_element = '[data-menu-id="/erp/personnel/whiteList/correctIdentity/index"]'

    employee_management_8_element = '[data-menu-id="/erp/personnel/externalImport/index"]'

    def Employee_Management(self):  # 员工管理遍历
        # 进入业务办理模块
        # self.click('xpath', self.business_processing_element)

        # 员工管理盒子元素
        self.click('css_selector', self.employee_management_box_element)

        # 遍历员工管理元素
        self.click('css_selector', self.employee_management_1_element)
        try:
            self.click('xpath', self.skip_guidance_element)     # 关闭引导弹窗 test1环境出现，116环境关闭
        except Exception as e:
            log.logging_error(f"引导弹窗未出现{e}")

        try:
            self.click('css_selector', self.employee_management_2_element)
        except Exception as e:
            log.logging_error(f"人员管理页面出现异常：{e}")
            self.screenshot('人员管理页面出现异常截图')
        else:
            # 由于有多个查看按钮，获取所有查看按钮后根据索引点击
            view_buttons = self.visibility_of_all_elements('xpath', "//span[contains(text(),'查看')]")
            if len(view_buttons) > 2:
                view_buttons[2].click()
                time.sleep(1)
            # self.click('xpath', self.employee_management_view_button_element)    # 点击查看按钮
            self.click('xpath', self.employee_management_return_button_element)    # 点击返回按钮

        self.click('css_selector', self.employee_management_3_element)
        self.click('css_selector', self.employee_management_4_element)
        self.click('css_selector', self.employee_management_5_element)

        # 展开人员转移盒子
        self.click('css_selector', self.employee_management_6_box_element)
        # 遍历人员转移元素
        self.click('css_selector', self.employee_management_6_box1_element)
        self.click('css_selector', self.employee_management_6_box2_element)
        self.click('css_selector', self.employee_management_6_box3_element)

        # 展开黑白名单设置盒子
        self.click('css_selector', self.employee_management_7_box_element)
        # 遍历黑白名单设置
        self.click('css_selector', self.employee_management_7_box1_element)
        self.click('css_selector', self.employee_management_7_box2_element)
        self.click('css_selector', self.employee_management_7_box3_element)
        self.click('css_selector', self.employee_management_7_box4_element)

        self.click('css_selector', self.employee_management_8_element)


class Social_Security_And_Housing_Fund_Processing_Page(BasePage):  # 社保公积金办理模块
    # 社保公积金办理盒子
    # social_security_and_housing_fund_processing_box_element = "//div[@title='社保公积金办理']"
    social_security_and_housing_fund_processing_box_element = '[data-menu-id="/erp/personnel/serviceApply"]'

    # 社保公积金办理元素
    # social_security_and_housing_fund_processing_1_element = "//div[@title='社保申请']"
    # social_security_and_housing_fund_processing_2_element = "//div[@title='公积金申请']"

    # 社保公积金办理元素
    social_security_and_housing_fund_processing_1_element = '[data-menu-id="/erp/personnel/serviceApply/socialApply/index"]'
    social_security_and_housing_fund_processing_2_element = '[data-menu-id="/erp/personnel/serviceApply/accrualApply/index"]'

    def Social_Security_And_Housing_Fund_Processing(self):  # 社保公积金办理
        # 展开社保公积金办理
        self.click('css_selector', self.social_security_and_housing_fund_processing_box_element)

        # 遍历社保公积金办理
        self.click('css_selector', self.social_security_and_housing_fund_processing_1_element)
        self.click('css_selector', self.social_security_and_housing_fund_processing_2_element)


class Commercial_Insurance_Processing_Page(BasePage):  # 商业险办理模块
    # 商业险办理盒子
    # commercial_insurance_processing_box_element = "//div[@title='商业险办理']"
    commercial_insurance_processing_box_element = '[data-menu-id="/shangyexianbanli"]'

    # 遍历商业险办理
    # commercial_insurance_processing_1_element = "//div[@title='商业险申请']"
    commercial_insurance_processing_1_element = '[data-menu-id="/erp/personnel/serviceApply/businessApply/index"]'

    commercial_insurance_processing_view_button_element = '//*[@id="/erp/personnel/serviceApply/businessApply/index"]/div[2]/div[1]/div[3]/div/div[4]/div/div/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td/div/div/button[1]/span'  # 点击查看按钮
    commercial_insurance_processing_return_button_element = "//span[@class='!ml-4px']"  # 返回按钮

    def Commercial_Insurance_Processing(self):  # 商业险办理
        # 展开商业险办理
        self.click('css_selector', self.commercial_insurance_processing_box_element)

        # 遍历商业险办理
        try:
            self.click('css_selector', self.commercial_insurance_processing_1_element)
        except Exception as e:
            log.logging_error(f"商业险办理页面异常{e}")
            self.screenshot('商业险办理页面异常截图')
        else:
            # 由于有多个查看按钮，获取所有查看按钮后根据索引点击
            view_buttons = self.visibility_of_all_elements('xpath', "//span[contains(text(),'查看')]")
            if len(view_buttons) > 2:
                view_buttons[2].click()
                time.sleep(1)
            # self.click('xpath', self.commercial_insurance_processing_view_button_element)
            self.click('xpath', self.commercial_insurance_processing_return_button_element)


class Service_Handling_Page(BasePage):  # 服务办理
    # 服务办理盒子
    # service_handling_box_element = "//div[@title='服务办理']"
    service_handling_box_element = '[data-menu-id="/erp/serviceHandling"]'

    # 遍历服务办理元素
    # service_handling_1_element = "//div[@title='申报结果更正确认']"
    # service_handling_2_element = "//div[@title='社保管理']"
    # service_handling_3_element = "//div[@title='公积金管理']"
    # service_handling_4_element = "//div[@title='商保管理']"
    # service_handling_5_element = "//div[@title='特殊业务审核']"

    # 遍历服务办理元素
    service_handling_1_element = '[data-menu-id="/erp/serviceHandling/correctionDeclarationResults/index"]'
    service_handling_2_element = '[data-menu-id="/erp/serviceHandling/socialManage/index"]'
    service_handling_3_element = '[data-menu-id="/erp/serviceHandling/houseManage/index"]'
    service_handling_4_element = '[data-menu-id="/erp/serviceHandling/commercialManage/index"]'
    service_handling_5_element = '[data-menu-id="/erp/personnel/serviceApply/specialApply/index"]'

    def Service_Handling_Page(self):  # 服务办理
        # 展开服务办理盒子
        self.click('css_selector', self.service_handling_box_element)

        # 遍历服务办理盒子
        self.click('css_selector', self.service_handling_1_element)
        self.click('css_selector', self.service_handling_2_element)
        self.click('css_selector', self.service_handling_3_element)
        self.click('css_selector', self.service_handling_4_element)
        self.click('css_selector', self.service_handling_5_element)


class Ordinary_Salary_Page(BasePage):  # 普通工资
    # 普通工资盒子
    # ordinary_salary_box_element = "//div[@title='普通工资']"
    ordinary_salary_box_element = '[data-menu-id="/erp/generalSalary"]'

    # 人员专项抵扣盒子
    # personnel_specific_deduction_box_element = "//div[@class='ant-menu-submenu-title']//div[@title='人员专项抵扣'][contains(text(),'人员专项抵扣')]"
    # # 遍历人员专项抵扣元素
    # personnel_specific_deduction_1_element = "//div[@title='人员花名册']"
    # personnel_specific_deduction_2_element = "//div[@title='人员花名册统计']"
    # personnel_specific_deduction_3_element = "//li[@role='menuitem']//div[@title='人员专项抵扣'][contains(text(),'人员专项抵扣')]"
    # personnel_specific_deduction_4_element = "//div[@title='人员专项抵扣统计']"
    # personnel_specific_deduction_5_element = "//div[@title='减税六万人员查询']"
    # personnel_specific_deduction_6_element = "//div[@title='不享受减税六万人员']"

    # 人员专项抵扣盒子
    personnel_specific_deduction_box_element = '[data-menu-id="/erp/generalSalary/personalDeduction"]'
    # 遍历人员专项抵扣元素
    personnel_specific_deduction_1_element = '[data-menu-id="/erp/generalSalary/personalDeduction/roster/index"]'
    personnel_specific_deduction_2_element = '[data-menu-id="/erp/generalSalary/personalDeduction/rostetStatistics/index"]'
    personnel_specific_deduction_3_element = '[data-menu-id="/erp/generalSalary/personalDeduction/salaryDeduction/index"]'
    personnel_specific_deduction_4_element = '[data-menu-id="/erp/generalSalary/personalDeduction/salaryDeductionStatistic/index"]'
    personnel_specific_deduction_5_element = '[data-menu-id="/erp/generalSalary/personalDeduction/reductionTaxEmployeeList/index"]'
    personnel_specific_deduction_6_element = '[data-menu-id="/erp/generalSalary/personalDeduction/notReduceTaxEmployee/index"]'


    def Personnel_Specific_Deduction(self):  # 普通工资
        # 展开普通工资盒子
        self.click('css_selector', self.ordinary_salary_box_element)

        # 展开人员专项抵扣盒子
        self.click('css_selector', self.personnel_specific_deduction_box_element)
        # 遍历人员专项抵扣元素
        self.click('css_selector', self.personnel_specific_deduction_1_element)
        self.click('css_selector', self.personnel_specific_deduction_2_element)
        self.click('css_selector', self.personnel_specific_deduction_3_element)
        self.click('css_selector', self.personnel_specific_deduction_4_element)
        self.click('css_selector', self.personnel_specific_deduction_5_element)
        self.click('css_selector', self.personnel_specific_deduction_6_element)

    def Data_Validation(self):  # 数据校验
        # 展开数据校验盒子
        # data_validation_box_element = "//div[@title='数据校验']"
        data_validation_box_element = '[data-menu-id="/erp/generalSalary/dataValidation"]'

        # 遍历数据校验元素
        # data_validation_1_element = "//div[@title='正确证件号码']"
        # data_validation_2_element = "//div[@title='人员信息核实']"

        # 遍历数据校验元素
        data_validation_1_element = '[data-menu-id="/erp/generalSalary/dataValidation/validIdNumber/index"]'
        data_validation_2_element = '[data-menu-id="/erp/generalSalary/dataValidation/verifyPersonInfo/index"]'

        # 展开数据校验
        self.click('css_selector', data_validation_box_element)

        # 遍历数据校验
        self.click('css_selector', data_validation_1_element)
        self.click('css_selector', data_validation_2_element)

    def Data_Configuration(self):  # 数据配置
        # 展开数据配置盒子
        # data_configuration_box_element = "//div[@title='数据配置']"
        data_configuration_box_element = '[data-menu-id="/erp/generalSalary/dataConfig"]'

        # 遍历数据配置元素
        # data_configuration_1_element = "//div[@title='人员手机号编辑']"
        # data_configuration_2_element = "//div[@title='工资特殊限制白名单']"
        # data_configuration_3_element = "//div[@title='特殊0起征点人员']"
        # data_configuration_4_element = "//div[@title='委托代收白名单']"

        # 遍历数据配置元素
        data_configuration_1_element = '[data-menu-id="/erp/generalSalary/dataConfig/fixMobile/index"]'
        data_configuration_2_element = '[data-menu-id="/erp/generalSalary/dataConfig/salaryWhitelist/index"]'
        data_configuration_3_element = '[data-menu-id="/erp/generalSalary/dataConfig/specialPersonal/index"]'
        data_configuration_4_element = '[data-menu-id="/erp/generalSalary/dataConfig/delegateWhiteList/index"]'

        # 展开数据配置盒子
        self.click('css_selector', data_configuration_box_element)

        # 遍历数据配置元素
        self.click('css_selector', data_configuration_1_element)
        self.click('css_selector', data_configuration_2_element)
        self.click('css_selector', data_configuration_3_element)
        self.click('css_selector', data_configuration_4_element)

    def Salary_Tax_Application(self):  # 薪税申请
        # 展开薪税申请盒子元素
        # salary_tax_application_box_element = "//div[@title='薪税申请']"
        salary_tax_application_box_element = '[data-menu-id="/erp/generalSalary/salaryCalculate"]'

        # 遍历薪税申请元素
        # salary_tax_application_1_element = "//div[@title='工资导入生成']"
        # salary_tax_application_2_element = "//div[@title='协助人员工资管理']"
        # salary_tax_application_3_element = "//div[@title='申请(客服)']"
        # salary_tax_application_4_element = "//div[@title='薪资重发(客服)']"
        # salary_tax_application_5_element = "//div[@title='工资作废申请']"
        # salary_tax_application_6_element = "//div[@title='单人回单下载（发薪平台）']"

        # 遍历薪税申请元素
        salary_tax_application_1_element = '[data-menu-id="/erp/generalSalary/salaryCalculate/salaryImport/index"]'
        salary_tax_application_2_element = '[data-menu-id="/erp/generalSalary/salaryCalculate/assistPersonalManage/index"]'
        salary_tax_application_3_element = '[data-menu-id="/erp/generalSalary/salaryCalculate/apply/index"]'
        salary_tax_application_4_element = '[data-menu-id="/erp/generalSalary/salaryCalculate/salaryRetry/index"]'
        salary_tax_application_5_element = '[data-menu-id="/erp/generalSalary/salaryCalculate/salaryInvalidate/index"]'
        salary_tax_application_6_element = '[data-menu-id="/erp/generalSalary/salaryCalculate/singleReceipt/index"]'

        # 展开薪税申请
        self.click('css_selector', salary_tax_application_box_element)

        # 遍历薪税申请
        self.click('css_selector', salary_tax_application_1_element)
        self.click('css_selector', salary_tax_application_2_element)
        self.click('css_selector', salary_tax_application_3_element)
        self.click('css_selector', salary_tax_application_4_element)
        self.click('css_selector', salary_tax_application_5_element)
        self.click('css_selector', salary_tax_application_6_element)

    def Salary_Tax_Payment(self):  # 薪资发放
        # 展开薪资发放盒子元素
        # salary_tax_payment_box_element = "//div[@class='ant-menu-submenu-title']//div[@title='薪资发放'][contains(text(),'薪资发放')]"
        salary_tax_payment_box_element = '[data-submenu-id="/erp/generalSalary/salaryPayment"]'

        # 遍历薪资发放元素
        # salary_tax_payment_1_element = "//div[@title='待打印工资表']"
        # salary_tax_payment_2_element = "//div[@title='待打印错月工资表']"
        # salary_tax_payment_3_element = "//div[@title='薪资确认']"
        # salary_tax_payment_4_element = "//li[@role='menuitem']//div[@title='薪资发放'][contains(text(),'薪资发放')]"
        # salary_tax_payment_5_element = "//div[@title='薪资重发(财务)']"
        # salary_tax_payment_6_element = "//div[@title='工资作废审核']"
        # salary_tax_payment_7_element = "//li[@class='ant-menu-item ant-menu-item-only-child']//div[@title='上传反馈'][contains(text(),'上传反馈')]"
        # salary_tax_payment_8_element = "//div[@title='代扣款管理']"
        # salary_tax_payment_9_element = "//div[@title='薪资反馈配置表']"

        # 遍历薪资发放元素
        salary_tax_payment_1_element = '[data-menu-id="/erp/generalSalary/salaryPayment/waitPrinted/index"]'
        salary_tax_payment_2_element = '[data-menu-id="/erp/generalSalary/salaryPayment/waitPrintedWrong/index"]'
        salary_tax_payment_3_element = '[data-menu-id="/erp/generalSalary/salaryPayment/confirm/index"]'
        salary_tax_payment_4_element = '[data-menu-id="/erp/generalSalary/salaryPayment/grant/index"]'
        salary_tax_payment_5_element = '[data-menu-id="/erp/generalSalary/salaryPayment/salaryRetry/index"]'
        salary_tax_payment_6_element = '[data-menu-id="/erp/generalSalary/salaryCalculate/salaryInvalidate/approve"]'
        salary_tax_payment_7_element = '[data-menu-id="/erp/generalSalary/salaryPayment/uploadFeedback/index"]'
        salary_tax_payment_8_element = '[data-menu-id="/erp/generalSalary/salaryPayment/deduction/index"]'
        salary_tax_payment_9_element = '[data-menu-id="/erp/generalSalary/salaryPayment/feedbackConfig/index"]'

        # 展开薪资发放
        self.click('css_selector', salary_tax_payment_box_element)

        # 遍历薪资发放
        self.click('css_selector', salary_tax_payment_1_element)
        self.click('css_selector', salary_tax_payment_2_element)
        self.click('css_selector', salary_tax_payment_3_element)
        self.click('css_selector', salary_tax_payment_4_element)
        self.click('css_selector', salary_tax_payment_5_element)
        self.click('css_selector', salary_tax_payment_6_element)
        self.click('css_selector', salary_tax_payment_7_element)
        self.click('css_selector', salary_tax_payment_8_element)
        self.click('css_selector', salary_tax_payment_9_element)

    def Salary_Tax_Inquiry(self):  # 薪税查询
        # 展开薪税查询盒子元素
        # salary_tax_inquiry_box_element = "//div[@title='薪资查询']"
        salary_tax_inquiry_box_element = '[data-menu-id="/erp/generalSalary/salaryQuery"]'

        # 遍历薪税查询元素
        # salary_tax_inquiry_1_element = "//div[@title='客户单位人员薪资统计']"
        # salary_tax_inquiry_2_element = "//div[@title='薪资 (查询)']"
        # salary_tax_inquiry_3_element = "//div[@title='历史薪资查询']"

        # 遍历薪税查询元素
        salary_tax_inquiry_1_element = '[data-menu-id="/erp/generalSalary/salaryQuery/personalSalary/index"]'
        salary_tax_inquiry_2_element = '[data-menu-id="/erp/generalSalary/salaryQuery/salarySearch/index"]'
        salary_tax_inquiry_3_element = '[data-menu-id="/erp/generalSalary/salaryQuery/historySalary/index"]'

        # 展开薪税查询
        self.click('css_selector', salary_tax_inquiry_box_element)

        # 遍历薪税查询
        self.click('css_selector', salary_tax_inquiry_1_element)
        self.click('css_selector', salary_tax_inquiry_2_element)
        self.click('css_selector', salary_tax_inquiry_3_element)

    def Personal_Income_Tax_Management(self):  # 个税管理
        # 展开个税管理盒子元素
        # personal_income_tax_management_box_element = "//div[@title='个税管理']"
        personal_income_tax_management_box_element = '[data-menu-id="/erp/taxManage"]'

        # 遍历个税管理元素
        # personal_income_tax_management_1_element = "//div[@title='个税错月申报审核']"
        # personal_income_tax_management_2_element = "//div[@title='报税信息错误人员']"

        # 遍历个税管理元素
        personal_income_tax_management_1_element = '[data-menu-id="/erp/generalSalary/taxManage/taxErrorReview/index"]'
        personal_income_tax_management_2_element = '[data-menu-id="/erp/generalSalary/taxManage/taxErrorPeople/index"]'

        # 展开个税管理
        self.click('css_selector', personal_income_tax_management_box_element)

        # 遍历个税管理
        self.click('css_selector', personal_income_tax_management_1_element)
        self.click('css_selector', personal_income_tax_management_2_element)


class Yuncheng_Business_Page(BasePage):  # 昀丞业务
    # 展开昀丞业务盒子
    # Yuncheng_Business_box_element = "//div[@title='昀丞业务']"
    Yuncheng_Business_box_element = '[data-menu-id="/erp/generalSalary/yuncheng"]'

    # 遍历昀丞业务元素
    # Yuncheng_Business_1_element = "//div[@title='昀丞配置']"
    # Yuncheng_Business_2_element = "//div[@title='导入生成收入']"
    # Yuncheng_Business_3_element = "//div[@title='申请']"
    # Yuncheng_Business_4_element = "//div[@title='重发(客服)']"
    # Yuncheng_Business_5_element = "//div[@title='重发(财务)']"
    # Yuncheng_Business_6_element = "//div[@title='待处理']"
    # Yuncheng_Business_7_element = "//div[@title='待确认']"
    # Yuncheng_Business_8_element = "//div[@title='待打印']"
    # Yuncheng_Business_9_element = "//div[@title='待打印错月费用单']"
    # Yuncheng_Business_10_element = "//li[@class='ant-menu-item ant-menu-item-only-child']//div[@title='待发放'][contains(text(),'待发放')]"
    # Yuncheng_Business_11_element = "//div[@title='外部渠道发放']"
    # Yuncheng_Business_12_element = "//div[@title='外部渠道发放']"
    # Yuncheng_Business_13_element = "//li[@class='ant-menu-item ant-menu-item-only-child']//div[@title='已发放'][contains(text(),'已发放')]"
    # Yuncheng_Business_14_element = '/html/body/div[1]/section/section/aside/div/div/div/div[2]/ul/li[7]/ul/li[13]/span'
    # Yuncheng_Business_15_element = "//li[@class='ant-menu-item ant-menu-item-only-child']//div[@title='作废申请'][contains(text(),'作废申请')]"
    # Yuncheng_Business_16_element = "//div[@title='作废审核']"
    # Yuncheng_Business_17_element = "//div[@title='个体户开票']"
    # Yuncheng_Business_18_element = "//div[@title='历史收入查询']"

    # 遍历昀丞业务元素
    Yuncheng_Business_1_element = '[data-menu-id="/erp/generalSalary/yuncheng/yunchengConfig/index"]'
    Yuncheng_Business_2_element = '[data-menu-id="/erp/generalSalary/yuncheng/importGenerate/index"]'
    Yuncheng_Business_3_element = '[data-menu-id="/erp/generalSalary/yuncheng/apply/index"]'
    Yuncheng_Business_4_element = '[data-menu-id="/erp/generalSalary/yuncheng/retryCustomer/index"]'
    Yuncheng_Business_5_element = '[data-menu-id="/erp/generalSalary/yuncheng/retryFinance/index"]'
    Yuncheng_Business_6_element = '[data-menu-id="/erp/generalSalary/yuncheng/toPending/index"]'
    Yuncheng_Business_7_element = '[data-menu-id="/erp/generalSalary/yuncheng/toConfirmed/index"]'
    Yuncheng_Business_8_element = '[data-menu-id="/erp/generalSalary/yuncheng/toPrinted/index"]'
    Yuncheng_Business_9_element = '[data-menu-id="/erp/generalSalary/yuncheng/toPrintedMonthSheet/index"]'
    Yuncheng_Business_10_element = '[data-menu-id="/erp/generalSalary/yuncheng/toGrant/index"]'
    Yuncheng_Business_11_element = '[data-menu-id="/erp/generalSalary/yuncheng/externalChannelGrant/index"]'
    Yuncheng_Business_12_element = '[data-menu-id="/erp/generalSalary/yuncheng/alreadyGrant/index"]'
    Yuncheng_Business_13_element = '[data-menu-id="/erp/generalSalary/yuncheng/uploadFeedback/index"]'
    Yuncheng_Business_14_element = '[data-menu-id="/erp/generalSalary/yuncheng/cancelApply/index"]'
    Yuncheng_Business_15_element = '[data-menu-id="/erp/generalSalary/yuncheng/cancelAudit/index"]'
    Yuncheng_Business_16_element = '[data-menu-id="/erp/generalSalary/yuncheng/cancelAudit/index"]'
    Yuncheng_Business_17_element = '[data-menu-id="/erp/generalSalary/yuncheng/singlePersonInvoke/index"]'
    Yuncheng_Business_18_element = '[data-menu-id="/erp/generalSalary/yuncheng/historySalary/index"]'

    def Yuncheng_Business(self):
        # 展开昀丞业务
        self.click('css_selector', self.Yuncheng_Business_box_element)

        # 遍历昀丞业务
        self.click('css_selector', self.Yuncheng_Business_1_element)
        self.click('css_selector', self.Yuncheng_Business_2_element)
        self.click('css_selector', self.Yuncheng_Business_3_element)
        self.click('css_selector', self.Yuncheng_Business_4_element)
        self.click('css_selector', self.Yuncheng_Business_5_element)
        self.click('css_selector', self.Yuncheng_Business_6_element)
        self.click('css_selector', self.Yuncheng_Business_7_element)
        self.click('css_selector', self.Yuncheng_Business_8_element)
        self.click('css_selector', self.Yuncheng_Business_9_element)
        self.click('css_selector', self.Yuncheng_Business_10_element)
        self.click('css_selector', self.Yuncheng_Business_11_element)
        self.click('css_selector', self.Yuncheng_Business_12_element)
        self.click('css_selector', self.Yuncheng_Business_13_element)
        self.click('css_selector', self.Yuncheng_Business_14_element)
        self.click('css_selector', self.Yuncheng_Business_15_element)
        self.click('css_selector', self.Yuncheng_Business_16_element)
        self.click('css_selector', self.Yuncheng_Business_17_element)
        self.click('css_selector', self.Yuncheng_Business_18_element)


class Supplier_Payroll_Page(BasePage):  # 供应商发薪
    # 展开供应商发薪盒子
    # supplier_payroll_box_element = "//div[@title='供应商发薪']"
    supplier_payroll_box_element = '[data-menu-id="/erp/supplier"]'

    # 遍历供应商发薪元素
    # supplier_payroll_1_element = "//div[@title='工资导入']"
    # supplier_payroll_2_element = "//div[@title='导出待处理']"
    # supplier_payroll_3_element = "//div[@title='待上传反馈']"
    # supplier_payroll_4_element = "//div[@title='待请款']"
    # supplier_payroll_5_element = '/html/body/div[1]/section/section/aside/div/div/div/div[2]/ul/li[8]/ul/li[5]/span'
    # supplier_payroll_6_element = "/html/body/div[1]/section/section/aside/div/div/div/div[2]/ul/li[8]/ul/li[6]/span"
    # supplier_payroll_7_element = "/html/body/div[1]/section/section/aside/div/div/div/div[2]/ul/li[8]/ul/li[7]/span"
    # supplier_payroll_8_element = "//div[@title='作废审批']"

    # 遍历供应商发薪元素
    supplier_payroll_1_element = '[data-menu-id="/erp/generalSalary/supplier/Import/index"]'
    supplier_payroll_2_element = '[data-menu-id="/erp/generalSalary/supplier/Export/index"]'
    supplier_payroll_3_element = '[data-menu-id="/erp/generalSalary/supplier/PendingFeedback/index"]'
    supplier_payroll_4_element = '[data-menu-id="/erp/generalSalary/supplier/Payment/WaitingPayment"]'
    supplier_payroll_5_element = '[data-menu-id="/erp/generalSalary/supplier/Payment/PendingPay"]'
    supplier_payroll_6_element = '[data-menu-id="/erp/generalSalary/supplier/Payment/Paid"]'
    supplier_payroll_7_element = '[data-menu-id="/erp/generalSalary/supplier/Void/Apply"]'
    supplier_payroll_8_element = '[data-menu-id="/erp/generalSalary/supplier/Void/Audit"]'


    def Supplier_Payroll(self):  # 供应商发薪
        # 展开供应商发薪
        self.click('css_selector', self.supplier_payroll_box_element)

        # 遍历供应商发薪
        self.click('css_selector', self.supplier_payroll_1_element)
        self.click('css_selector', self.supplier_payroll_2_element)
        self.click('css_selector', self.supplier_payroll_3_element)
        self.click('css_selector', self.supplier_payroll_4_element)
        self.click('css_selector', self.supplier_payroll_5_element)
        self.click('css_selector', self.supplier_payroll_6_element)
        self.click('css_selector', self.supplier_payroll_7_element)
        self.click('css_selector', self.supplier_payroll_8_element)


class Personal_Proxy_Payment_Page(BasePage):  # 个人代缴
    # 个人代缴盒子
    # Personal_Proxy_Payment_box_element = "//div[@title='个人代缴']"
    Personal_Proxy_Payment_box_element = '[data-menu-id="/erp/personalDeduct"]'

    # 遍历个人代缴
    # Personal_Proxy_Payment_1_element = "//div[@title='收据配置']"
    # Personal_Proxy_Payment_2_element = "//div[@title='收据管理']"
    # Personal_Proxy_Payment_3_element = "//div[@title='个代退款']"
    #
    # # 个代账户盒子
    # Personal_Proxy_Payment_4_box_element = "//div[@class='ant-menu-submenu-title']//div[@title='个代账户'][contains(text(),'个代账户')]"
    # Personal_Proxy_Payment_4_box1_element = "//li[@role='menuitem']//div[@title='个代账户'][contains(text(),'个代账户')]"
    # Personal_Proxy_Payment_4_box2_element = "//div[@title='个代领款']"
    # Personal_Proxy_Payment_4_box3_element = "//div[@title='个代扣款']"
    #
    # Personal_Proxy_Payment_5_element = "//div[@title='账户充值']"

    # 遍历个人代缴
    Personal_Proxy_Payment_1_element = '[data-menu-id="/erp/personalDeduct/receiptConfig/index"]'
    Personal_Proxy_Payment_2_element = '[data-menu-id="/erp/personalDeduct/receiptManage/index"]'
    Personal_Proxy_Payment_3_element = '[data-menu-id="/erp/personalDeduct/rechargeRefund/index"]'

    # 个代账户盒子
    Personal_Proxy_Payment_4_box_element = '[data-menu-id="/erp/personalDeductAccount"]'
    Personal_Proxy_Payment_4_box1_element = '[data-menu-id="/erp/personalDeduct/account/index"]'
    Personal_Proxy_Payment_4_box2_element = '[data-menu-id="/erp/personalDeduct/withdrawal/index"]'
    Personal_Proxy_Payment_4_box3_element = '[data-menu-id="/erp/personalDeduct/deduction/index"]'

    Personal_Proxy_Payment_5_element = '[data-menu-id="/erp/personalDeduct/accountRecharge/index"]'

    def Personal_Proxy_Payment(self):   # 个人代缴
        # 展开个人代缴盒子
        self.click('css_selector', self.Personal_Proxy_Payment_box_element)

        # 遍历个人代缴
        self.click('css_selector', self.Personal_Proxy_Payment_1_element)
        self.click('css_selector', self.Personal_Proxy_Payment_2_element)
        self.click('css_selector', self.Personal_Proxy_Payment_3_element)

        # 个代账户盒子
        self.click('css_selector', self.Personal_Proxy_Payment_4_box_element)
        self.click('css_selector', self.Personal_Proxy_Payment_4_box1_element)
        self.click('css_selector', self.Personal_Proxy_Payment_4_box2_element)
        self.click('css_selector', self.Personal_Proxy_Payment_4_box3_element)

        self.click('css_selector', self.Personal_Proxy_Payment_5_element)


class Payment_Request_Page(BasePage):   # 请款单
    # 请款单盒子元素
    # payment_request_box_element = "//div[@title='请款单']"
    payment_request_box_element = '[data-menu-id="/erp/paymentRequests"]'

    # 遍历请款单
    # payment_request_1_element = "//div[@title='社保公积金请款单']"
    # payment_request_2_element = "//div[@title='供应商请款单']"
    # payment_request_3_element = "//div[@title='商保请款单']"

    # 遍历请款单
    payment_request_1_element = '[data-menu-id="/erp/paymentRequests/socialSecurityFundRequest/index"]'
    payment_request_2_element = '[data-menu-id="/erp/paymentRequests/vendorRequest/index"]'
    payment_request_3_element = '[data-menu-id="/erp/paymentRequests/businessReportRequest/index"]'

    def Payment_Request(self):  # 请款单
        # 展开请款单盒子
        self.click('css_selector', self.payment_request_box_element)

        # 遍历请款单
        self.click('css_selector', self.payment_request_1_element)
        self.click('css_selector', self.payment_request_2_element)
        self.click('css_selector', self.payment_request_3_element)


class Employee_Affairs_Handling_Center_Page(BasePage):   # 员工事务性办理中心
    # 展开员工事务性办理中心盒子
    # employee_affairs_handling_center_box_element = "//div[@title='员工事务性办理中心']"
    employee_affairs_handling_center_box_element = '[data-menu-id="/staffService"]'

    # 遍历员工事务性办理中心元素
    # employee_affairs_handling_center_1_element = "//div[@title='社保(非工伤)报销']"
    # employee_affairs_handling_center_2_element = "//div[@title='员工投诉处理']"
    # employee_affairs_handling_center_3_element = "//div[@title='个税汇算处理']"

    # 遍历员工事务性办理中心元素
    employee_affairs_handling_center_1_element = '[data-menu-id="/erp/staffService/socialExpenseManage/index"]'
    employee_affairs_handling_center_2_element = '[data-menu-id="/erp/staffService/complaintManage/index"]'
    employee_affairs_handling_center_3_element = '[data-menu-id="/erp/staffService/taxHander/index"]'

    def Employee_Affairs_Handling_Center(self):
        # 展开员工事务性办理中心
        self.click('css_selector', self.employee_affairs_handling_center_box_element)

        # 遍历员工事务性办理中心
        self.click('css_selector', self.employee_affairs_handling_center_1_element)
        self.click('css_selector', self.employee_affairs_handling_center_2_element)
        self.click('css_selector', self.employee_affairs_handling_center_3_element)


class Work_Injury_And_Dispute_Management_Center_Page(BasePage):  # 工伤/纠纷管理中心
    # 工伤/纠纷管理中心盒子
    # work_injury_and_dispute_management_center_box_element = "//div[@title='工伤/纠纷管理中心']"
    work_injury_and_dispute_management_center_box_element = '[data-menu-id="/erp/workInjurydispute"]'

    # # 遍历工伤/纠纷管理中心盒子
    # work_injury_and_dispute_management_center_1_element = "//div[@title='案件管理']"
    # work_injury_and_dispute_management_center_2_element = "//div[@title='社保工伤报销']"
    # work_injury_and_dispute_management_center_3_element = "//div[@title='商业险理赔']"
    #
    # # 法务系统盒子
    # work_injury_and_dispute_management_center_4_box_element = "//div[@title='法务系统']"
    # # 遍历法务系统元素
    # work_injury_and_dispute_management_center_4_box1_element = "//div[@title='被诉案件处理']"
    # work_injury_and_dispute_management_center_4_box2_element = "//div[@title='起诉案件处理']"
    # work_injury_and_dispute_management_center_4_box3_element = "//div[@title='案件提成']"
    # work_injury_and_dispute_management_center_4_box4_element = "//div[@title='法务专员提成统计']"
    # work_injury_and_dispute_management_center_4_box5_element = "//div[@title='法务专员业绩统计']"
    # work_injury_and_dispute_management_center_4_box6_element = "//div[@title='法务人员管理']"
    #
    # work_injury_and_dispute_management_center_5_element = "//div[@title='传票/被执管理']"
    # work_injury_and_dispute_management_center_6_element = "//div[@title='工伤申报员分配']"
    # work_injury_and_dispute_management_center_7_element = "//div[@title='工伤/纠纷余额池']"

    # 遍历工伤/纠纷管理中心盒子
    work_injury_and_dispute_management_center_1_element = '[data-menu-id="/erp/workInjurydispute/caseManagement/index"]'
    work_injury_and_dispute_management_center_2_element = '[data-menu-id="/erp/workInjurydispute/reimbursement/index"]'
    work_injury_and_dispute_management_center_3_element = '[data-menu-id="/erp/workInjurydispute/commercialinsurance/index"]'

    # 法务系统盒子
    work_injury_and_dispute_management_center_4_box_element = '[data-menu-id="/erp/workInjurydispute/law"]'
    # 遍历法务系统元素
    work_injury_and_dispute_management_center_4_box1_element = '[data-menu-id="/erp/workInjurydispute/law/accused/index"]'
    work_injury_and_dispute_management_center_4_box2_element = '[data-menu-id="/erp/workInjurydispute/law/approve/index"]'
    work_injury_and_dispute_management_center_4_box3_element = '[data-menu-id="/erp/workInjurydispute/law/statistics/index"]'
    work_injury_and_dispute_management_center_4_box4_element = '[data-menu-id="/erp/workInjurydispute/law/bonus/index"]'
    work_injury_and_dispute_management_center_4_box5_element = '[data-menu-id="/erp/workInjurydispute/law/performance/index"]'
    work_injury_and_dispute_management_center_4_box6_element = '[data-menu-id="/erp/workInjurydispute/law/personnel/index"]'

    work_injury_and_dispute_management_center_5_element = '[data-menu-id="/erp/workInjurydispute/subpoenaExecution/index"]'
    work_injury_and_dispute_management_center_6_element = '[data-menu-id="/erp/workInjurydispute/allocationDeclarants/index"]'
    work_injury_and_dispute_management_center_7_element = '[data-menu-id="/erp/workInjurydispute/balancePool/index"]'

    def Work_Injury_And_Dispute_Management_Center(self):    # 工伤/纠纷管理中心
        # 展开工伤/纠纷管理中心盒子
        self.click('css_selector', self.work_injury_and_dispute_management_center_box_element)

        # 遍历工伤/纠纷管理中心
        self.click('css_selector', self.work_injury_and_dispute_management_center_1_element)
        self.click('css_selector', self.work_injury_and_dispute_management_center_2_element)
        self.click('css_selector', self.work_injury_and_dispute_management_center_3_element)

        # 展开法务系统盒子
        self.click('css_selector', self.work_injury_and_dispute_management_center_4_box_element)
        # 遍历法务系统
        self.click('css_selector', self.work_injury_and_dispute_management_center_4_box1_element)
        self.click('css_selector', self.work_injury_and_dispute_management_center_4_box2_element)
        self.click('css_selector', self.work_injury_and_dispute_management_center_4_box3_element)
        self.click('css_selector', self.work_injury_and_dispute_management_center_4_box4_element)
        self.click('css_selector', self.work_injury_and_dispute_management_center_4_box5_element)
        self.click('css_selector', self.work_injury_and_dispute_management_center_4_box6_element)

        self.click('css_selector', self.work_injury_and_dispute_management_center_5_element)
        self.click('css_selector', self.work_injury_and_dispute_management_center_6_element)
        self.click('css_selector', self.work_injury_and_dispute_management_center_7_element)









