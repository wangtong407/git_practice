import pytest
from selenium import webdriver

# edge浏览器的导包
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

from work.script_data.T116_Environment_Page_Traverse.Base_Class.Base_Page import BasePage
# 日志方法传入
from work.script_data.T116_Environment_Page_Traverse.Tools.log_tool import Logging

# 登录方法导入
from work.script_data.T116_Environment_Page_Traverse.Page_Object_Class.login_page import Login

# Chrom浏览器的导包
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service

# 基类后置方法导入
# 登录前置操作导入

log = Logging()


# scope是固件的作用域，autouse是固件是否自动执行的属性
@pytest.fixture(scope="module", autouse=False)
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

    "注意：保持存活时后置不可调用quit方法，除非系统命令杀死浏览器资源"
    # 添加保持浏览器不关闭的参数（关键步骤）
    edge_options.add_experimental_option("detach", False)  # 保持或关闭浏览器进程存活

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
    # edge_options.add_experimental_option("detach", True)

    # 指定Edge和chrome的浏览器驱动
    # service = Service(r"C:\Users\31646\.wdm\drivers\edgedriver_win64\msedgedriver.exe")
    service = Service(r"./script_data/T116_Environment_Page_Traverse/driver/edgedriver_win64/msedgedriver.exe")

    # service = Service()
    # service.path = r"C:\Users\31646\.wdm\drivers\chromedriver-win32\chromedriver.exe"

    # 实例化浏览器
    # driver = webdriver.Chrome(options=options)
    driver = webdriver.Edge(options=edge_options, service=service)

    # 窗口最大化
    driver.maximize_window()

    # 获取URL
    # url = "http://192.168.0.114:18080/#/login"
    # url = "http://192.168.0.115:18080/#/login"
    url = "http://192.168.0.116:18080/"
    driver.get(url)
    log.logging_info(f"访问：{url}")

    # 调用登录方法
    # Login(driver).login_fun("BM000076", "123456")
    # Login(driver).login_fun("admin", "123456")
    Login(driver).login_fun("admin", "123456")
    BasePage(driver).allure_screenshot('登录成功截图')

    return driver

