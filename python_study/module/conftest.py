import pytest
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from python_study.module.POM.poms.login_page import LoginPage

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from python_study.module.POM.bases.base_page import BasePage


# scope是固件的作用域，autouse是固件是否自动执行的属性
@pytest.fixture(scope="function", autouse=False)
def all_case_fixture():
    # 用例的前置操作
    driver = driver_login_cd()
    yield driver

    # 用例的后置操作
    # 实例化基类
    bp = BasePage(driver)
    time.sleep(2)
    bp.allure_screenshot("后置截图")
    driver.quit()


def driver_login_cd():
    # 创建配置对象并启用 detach，使浏览器不关闭
    # edge_options = Options()
    # chrome_options = Options()

    # 添加保持浏览器不关闭的参数（关键步骤）
    # edge_options.add_experimental_option("detach", True)  # 保持浏览器进程存活
    # chrome_options.add_experimental_option("detach", True)  # 保持浏览器进程存活

    # EdgeChromiumDriverManager 配合 Service 类，下载浏览器驱动
    # service = Service(EdgeChromiumDriverManager().install())
    # service = Service(ChromeDriverManager().install())

    # 解决谷歌浏览器启动的慢
    service = Service()
    service.path = r"C:\Users\31646\.wdm\drivers\chromedriver\win64\138.0.7204.157\chromedriver-win32\chromedriver.exe"
    driver = webdriver.Chrome(service=service)

    # 实例化浏览器
    # driver = webdriver.Edge()
    driver.get("https://www.zentao.net/")
    driver.maximize_window()

    # 登录
    LoginPage(driver).login_cd("wx_655b149be0379", "w20040702")
    return driver

