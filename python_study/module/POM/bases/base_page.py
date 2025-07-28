import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    # 封装 driver 和浏览器驱动，调起浏览器的driver
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10, 0.3)

    def open_url(self, url):
        self.driver.get(url)

    # 创建一个init方法把driver传进来
    # def __init__(self, driver):
        # self.driver = s_drivers()
        # 给所有浏览器操作增加显式登录

    # 定位一个元素(重写selenium方法)
    # def find_ele(self, xpath):
    #     try:
    #         # 隐式等待
    #         self.driver.implicitly_wait(10)
    #         ele = self.driver.find_element(By.XPATH, xpath)
    #         return ele
    #     except Exception:
    #         print(f"{xpath} 定位失败")

    # 定位多个元素(重写selenium方法)
    # def find_eles(self, xpath):
    #     try:
    #         # 隐式等待
    #         self.driver.implicitly_wait(10)
    #         eles = self.driver.find_elements(By.XPATH, xpath)
    #         return eles
    #     except Exception:
    #         print(f"{xpath} 定位失败")

    # 封装所有定位方式，根据传参指定定位方式，并增加显式等待
    def find_element(self, by_type, locator):
        if by_type == 'id':
            return self.wait.until(EC.element_to_be_clickable((By.ID, locator)))
        elif by_type == 'name':
            return self.wait.until(EC.element_to_be_clickable((By.NAME, locator)))
        elif by_type == 'class_name':
            return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, locator)))
        elif by_type == 'tag_name':
            return self.wait.until(EC.element_to_be_clickable((By.TAG_NAME, locator)))
        elif by_type == 'link_text':
            return self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, locator)))
        elif by_type == 'xpath':
            return self.wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
        elif by_type == 'css_selector':
            return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locator)))
        return None

    # 封装点击操作
    def click(self, by_type, locator):
        self.find_element(by_type, locator).click()

    # 封装输入操作
    def enter_text(self, by_type, locator, text):
        self.find_element(by_type, locator).send_keys(text)

    # 封装切换窗口句柄
    def switch_to_windows(self, title):
        # 获取所有窗口句柄
        handles = self.driver.window_handles
        # 用for循环遍历所有创建的标题，并if判断传入的标题和循环的标题是否一直，一致后切换并跳出循环
        for handle in handles:
            self.driver.switch_to.window(handle)
            if self.driver.title == title:
                break

    # 封装鼠标悬浮操作
    def hover_to_element(self,by_type , locator):
        # 创建 ActionChains 对象
        action = ActionChains(self.driver)
        # 定位元素传入hover
        # 将浏览器driver传进 Actionchains 对象，执行悬浮操作和.pause(2)是悬浮之前暂停2秒，以等待元素完全加载
        action.move_to_element(self.find_element(by_type, locator)).perform()

    # 封装截图保存到本地方法
    def screenshot(self, screenshot_path):
        self.driver.save_screenshot(screenshot_path)

    # 封装截图保存到allure报告的方法
    def allure_screenshot(self, name="screenshot_name"):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG,
            extension=".png"
        )

