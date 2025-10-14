import pytest
import time
from selenium import webdriver

# edge浏览器的导包
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Chrom浏览器的导包
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
from python_study.module.POM.bases.base_page import BasePage

# from python_study.module.POM.poms.login_page import LoginPage
from python_study.module.POM.poms.IHRM_Loging_page import LoginPage


# scope是固件的作用域，autouse是固件是否自动执行的属性
@pytest.fixture(scope="function", autouse=False)
def all_case_fixture():
    # 用例的前置操作
    driver = driver_login_cd()
    yield driver

    # 用例的后置操作
    # 实例化基类
    # bp = BasePage(driver)
    # time.sleep(2)
    # bp.allure_screenshot("后置截图")
    driver.quit()


def driver_login_cd():
    # 创建配置对象并启用 detach，使浏览器不关闭
    edge_options = Options()

    # 添加保持浏览器不关闭的参数（关键步骤）
    edge_options.add_experimental_option("detach", True)  # 保持浏览器进程存活

    # EdgeChromiumDriverManager 配合 Service 类，下载浏览器驱动(Edge因为墙的问题无法自动下载)
    # service = Service(EdgeChromiumDriverManager().install())
    # service = Service(ChromeDriverManager().install())

    # 解决谷歌浏览器启动的慢
    # service = Service()
    # service.path = r"C:\Users\31646\.wdm\drivers\chromedriver\win64\139.0.7258.154\chromedriver-win32\chromedriver.exe"
    # driver = webdriver.Chrome(options=options, service=service)

    # 1. 启用浏览器缓存（关键：使用用户数据目录，保留缓存）
    # user_data_dir = r"C:\Users\31646\Desktop\SeleniumCache"  # 自定义缓存目录
    # edge_options.add_argument(f"--user-data-dir={user_data_dir}")
    # edge_options.add_argument("--profile-directory=Default")  # 使用默认配置文件

    # 2. 开启优化功能
    # edge_options.add_argument("--enable-gpu")  # 启用GPU加速
    # edge_options.add_argument("--enable-preload")  # 启用预加载
    # edge_options.add_argument("--enable-parallel-downloading")  # 启用并行下载
    # edge_options.add_argument("--disable-extensions")  # 禁用不必要的扩展（减少开销）

    # 3. 保持浏览器不关闭（调试用，正式运行可删除）
    edge_options.add_experimental_option("detach", False)

    # 指定Edge浏览器驱动
    # service = Service(r"C:\Users\31646\.wdm\drivers\edgedriver\win64\131.0.2903.146\msedgedriver.exe")

    # 实例化浏览器
    # driver = webdriver.Chrome(options=options)
    driver = webdriver.Edge(options=edge_options)

    # 窗口最大化
    driver.maximize_window()

    # LoginPage(driver).login_cd("wx_655b149be0379", "w20040702")
    LoginPage(driver).login_fun()

    return driver

