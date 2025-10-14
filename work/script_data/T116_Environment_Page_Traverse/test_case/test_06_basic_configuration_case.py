import allure
import pytest

from work.script_data.T116_Environment_Page_Traverse.Page_Object_Class.basic_configuration_page import \
    Intermediary_Management_Page, Intermediary_Viewing_Page, Management_of_Public_Welfare_Schemes_Page, \
    Commercial_Insurance_Configuration_Page, Template_Management_Page, Internal_Unit_Management_Page, \
    Customer_Brand_Page, Industry_Classification_Page, Supplier_Management_Page, Invoice_Category_Configuration_Page, \
    Extended_Field_Configuration_Page, Level_Configuration_of_Work_related_Injury_Disputes_Page, \
    Personnel_Material_Collection_Template_Page, Material_Library_Configuration_Page, \
    Template_Configuration_for_Commercial_Insurance_Policies_Page, Industry_Classification_Management_Page, \
    Policy_Group_Configuration_Page, Commercial_Insurance_Job_Classification_Maintenance_Page, Basic_Configuration_Tab
from work.script_data.T116_Environment_Page_Traverse.Base_Class.Base_Page import BasePage


# 基础配置页面
# @pytest.mark.smoke
class Test_06_case:

    @allure.feature("基础配置")
    @allure.story("基础配置页面")
    @allure.title("进入基础配置页面")
    def test_Basic_Configuration_Page_01(self, all_case_fixture):   # 进入基础配置Tab
        with allure.step("步骤一：进入基础配置页面"):

            Basic_Configuration_Tab(all_case_fixture).Basic_Configuration_Tab()

    @allure.feature("基础配置")
    @allure.story("居间人管页面")
    @allure.title("进入居间人管页面")
    def test_Basic_Configuration_Page_02(self, all_case_fixture):   # 居间人管理模块
        with allure.step("步骤二：进入居间人管页面"):

            Intermediary_Management_Page(all_case_fixture).Intermediary_Management()

    @allure.feature("基础配置")
    @allure.story("居间人查看页面")
    @allure.title("进入居间人查看页面")
    def test_Basic_Configuration_Page_03(self, all_case_fixture):   # 居间人查看模块
        with allure.step("步骤三：进入居间人查看页面"):

            Intermediary_Viewing_Page(all_case_fixture).Intermediary_Viewing()

    @allure.feature("基础配置")
    @allure.story("社公方案管理页面")
    @allure.title("进入社公方案管理页面")
    def test_Basic_Configuration_Page_04(self, all_case_fixture):   # 社公方案管理
        with allure.step("步骤四：进入社公方案管理页面"):

            Management_of_Public_Welfare_Schemes_Page(all_case_fixture).Management_of_Public_Welfare_Schemes()

    @allure.feature("基础配置")
    @allure.story("商业险配置页面")
    @allure.title("进入商业险配置页面")
    def test_Basic_Configuration_Page_05(self, all_case_fixture):   # 商业险配置
        with allure.step("步骤五：进入商业险配置页面"):

            Commercial_Insurance_Configuration_Page(all_case_fixture).Commercial_Insurance_Configuration()

    @allure.feature("基础配置")
    @allure.story("模板管理页面")
    @allure.title("进入模板管理页面")
    def test_Basic_Configuration_Page_06(self, all_case_fixture):   # 模板管理
        with allure.step("步骤六：进入模板管理页面"):

            Template_Management_Page(all_case_fixture).Template_Management()

    @allure.feature("基础配置")
    @allure.story("内部单位管理页面")
    @allure.title("进入内部单位管理页面")
    def test_Basic_Configuration_Page_07(self, all_case_fixture):   # 内部单位管理
        with allure.step("步骤七：进入内部单位管理页面"):

            Internal_Unit_Management_Page(all_case_fixture).Internal_Unit_Management()

    @allure.feature("基础配置")
    @allure.story("客户品牌页面")
    @allure.title("进入客户品牌页面")
    def test_Basic_Configuration_Page_08(self, all_case_fixture):   # 客户品牌
        with allure.step("步骤八：进入客户品牌页面"):

            Customer_Brand_Page(all_case_fixture).Customer_Brand()

    @allure.feature("基础配置")
    @allure.story("行业分类页面")
    @allure.title("进入行业分类页面")
    def test_Basic_Configuration_Page_09(self, all_case_fixture):   # 行业分类
        with allure.step("步骤九：进入行业分类页面"):

            Industry_Classification_Page(all_case_fixture).Industry_Classification()

    @allure.feature("基础配置")
    @allure.story("供应商管理页面")
    @allure.title("进入供应商管理页面")
    def test_Basic_Configuration_Page_10(self, all_case_fixture):   # 供应商管理
        with allure.step("步骤十：进入供应商管理页面"):

            Supplier_Management_Page(all_case_fixture).Supplier_Management()

    @allure.feature("基础配置")
    @allure.story("发票类目配置页面")
    @allure.title("进入发票类目配置页面")
    def test_Basic_Configuration_Page_11(self, all_case_fixture):   # 发票类目配置
        with allure.step("步骤十一：进入发票类目配置页面"):

            Invoice_Category_Configuration_Page(all_case_fixture).Invoice_Category_Configuration()

    @allure.feature("基础配置")
    @allure.story("扩展字段配置页面")
    @allure.title("进入扩展字段配置页面")
    def test_Basic_Configuration_Page_12(self, all_case_fixture):   # 扩展字段配置
        with allure.step("步骤十二：进入扩展字段配置页面"):

            Extended_Field_Configuration_Page(all_case_fixture).Extended_Field_Configuration()

    @allure.feature("基础配置")
    @allure.story("工伤纠纷等级配置盒子页面")
    @allure.title("进入工伤纠纷等级配置盒子页面")
    def test_Basic_Configuration_Page_13(self, all_case_fixture):   # 工伤纠纷等级配置盒子
        with allure.step("步骤十三：进入工伤纠纷等级配置盒子页面"):

            Level_Configuration_of_Work_related_Injury_Disputes_Page(all_case_fixture).Level_Configuration_of_Work_related_Injury_Disputes()

    @allure.feature("基础配置")
    @allure.story("人员材料收集模板盒子页面")
    @allure.title("进入人员材料收集模板盒子页面")
    def test_Basic_Configuration_Page_14(self, all_case_fixture):   # 人员材料收集模板盒子
        with allure.step("步骤十四：进入人员材料收集模板盒子页面"):

            Personnel_Material_Collection_Template_Page(all_case_fixture).Personnel_Material_Collection_Template()

    @allure.feature("基础配置")
    @allure.story("商业险工种分类维护页面")
    @allure.title("进入商业险工种分类维护页面")
    def test_Basic_Configuration_Page_15(self, all_case_fixture):   # 商业险工种分类维护
        with allure.step("步骤十五：进入商业险工种分类维护页面"):

            Commercial_Insurance_Job_Classification_Maintenance_Page(all_case_fixture).Commercial_Insurance_Job_Classification_Maintenance()

    @allure.feature("基础配置")
    @allure.story("材料库配置页面")
    @allure.title("进入材料库配置页面")
    def test_Basic_Configuration_Page_16(self, all_case_fixture):   # 材料库配置
        with allure.step("步骤十六：进入材料库配置页面"):

            Material_Library_Configuration_Page(all_case_fixture).Material_Library_Configuration()

    @allure.feature("基础配置")
    @allure.story("商保保单模板配置页面")
    @allure.title("进入商保保单模板配置页面")
    def test_Basic_Configuration_Page_17(self, all_case_fixture):   # 商保保单模板配置
        with allure.step("步骤十七：进入商保保单模板配置页面"):

            Template_Configuration_for_Commercial_Insurance_Policies_Page(all_case_fixture).Template_Configuration_for_Commercial_Insurance_Policies()

    @allure.feature("基础配置")
    @allure.story("行业分类管理页面")
    @allure.title("进入行业分类管理页面")
    def test_Basic_Configuration_Page_18(self, all_case_fixture):   # 行业分类管理
        with allure.step("步骤十八：进入行业分类管理页面"):

            Industry_Classification_Management_Page(all_case_fixture).Industry_Classification_Management()

    @allure.feature("基础配置")
    @allure.story("政策组配置页面")
    @allure.title("进入政策组配置页面")
    def test_Basic_Configuration_Page_19(self, all_case_fixture):   # 政策组配置
        with allure.step("步骤十九：进入政策组配置页面"):

            Policy_Group_Configuration_Page(all_case_fixture).Policy_Group_Configuration()

    # def test_Basic_Configuration_quit_Webdriver(self, all_case_fixture):  # 退出浏览器，释放资源
    #     BasePage(all_case_fixture).quit_Webdriver()

