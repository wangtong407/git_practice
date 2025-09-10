import allure
import pytest
from python_study.module.POM.commons.excel_utiles import read_excel_to_list
from python_study.module.POM.poms.address_page import AddressPage
from python_study.module.POM.poms.upload_page import UploadPage


@allure.epic("项目名称：测试项目")
class Test_cd:

    # @pytest.mark.smoke
    def test_login(self, all_case_fixture):

        # 在allure报告中添加本地附件
        # path = r"C:\Users\31646\Desktop\Android_log\1.png"
        # allure.attach.file(source=path, name="截图", attachment_type=allure.attachment_type.PNG, extension=".png")

        # 定义用例严重等级
        allure.dynamic.severity('normal')

        allure.dynamic.feature("模块名称：登录")
        allure.dynamic.story("页面名称：登录页面")
        allure.dynamic.title("用例名称：账密登录")

        # 添加用例步骤
        with allure.step("步骤一：登录"):
            pass

    # @pytest.mark.skip(reason='暂不执行该用例')
    @pytest.mark.smoke
    def test_Upload(self, all_case_fixture):

        allure.dynamic.severity('minor')
        allure.dynamic.feature("模块名称：上传文件")
        allure.dynamic.story("页面名称：禅道伙伴")
        allure.dynamic.title(f"用例名称：上传图片")

        with allure.step("步骤一：上传图片"):
            UploadPage(all_case_fixture).Upload(
                r"C:\Users\31646\AppData\Local\Programs\Python\venv\python_study\module\POM\testcases\1.jpg")

        with allure.step("步骤二：上传图片"):
            UploadPage(all_case_fixture).Upload(
                r"C:\Users\31646\AppData\Local\Programs\Python\venv\python_study\module\POM\testcases\1.jpg")

    # 单独运行某个用例的方法
    # @pytest.mark.smoke
    # 重复运行指定次数用例的方法
    # @pytest.mark.repeat(2)
    # 跳过测试用例
    # @pytest.mark.skip(reason='暂不执行该用例')
    # 数据驱动方法
    @pytest.mark.parametrize("caseinfo", read_excel_to_list(
        r"C:\Users\31646\AppData\Local\Programs\Python\venv\python_study\module\POM\testcases\cases.xlsx", "Sheet1"))
    def test_Address(self, all_case_fixture, caseinfo):

        allure.dynamic.severity('blocker')
        allure.dynamic.feature("模块名称：地址管理")
        allure.dynamic.story("页面名称：增删地址")
        allure.dynamic.title(f"用例名称：{caseinfo["case_name"]}")

        with allure.step("步骤三：添加和删除地址"):
            # 数据驱动方式，读取Excel文件中的列，传入Address方法中
            AddressPage(all_case_fixture).Address(caseinfo['name'], caseinfo['phone'], caseinfo['address'],
                                                  caseinfo['zip_code'])
