import allure
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os
from datetime import datetime
from selenium.webdriver.common.keys import Keys
import time

from work.script_data.T116_Environment_Page_Traverse.Tools.error_info_element import error_1, error_2, error_3, error_4, \
    error_5, error_6

from work.script_data.T116_Environment_Page_Traverse.Tools.log_tool import Logging

log = Logging()


class BasePage:
    # 封装 driver 和浏览器驱动，调起浏览器的driver
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 300, 0.5)

    # 封装访问URL链接的方法，这个方法获取到的内容本身在底层中
    def open_url(self, url):
        self.driver.get(url)

    # 封装获取页面标签页内容的方法，这个方法获取到的内容本身在底层中
    def get_title(self):
        return self.driver.title
        # return title

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

    # 封装元素不可见的所有定位方式，根据传参指定定位方式，并增加显式等待
    def invisibility_find_element(self, by_type, locator):
        if by_type == 'id':
            return self.wait.until(EC.invisibility_of_element_located((By.ID, locator)))
        elif by_type == 'name':
            return self.wait.until(EC.invisibility_of_element_located((By.NAME, locator)))
        elif by_type == 'class_name':
            return self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, locator)))
        elif by_type == 'tag_name':
            return self.wait.until(EC.invisibility_of_element_located((By.TAG_NAME, locator)))
        elif by_type == 'link_text':
            return self.wait.until(EC.invisibility_of_element_located((By.LINK_TEXT, locator)))
        elif by_type == 'xpath':
            return self.wait.until(EC.invisibility_of_element_located((By.XPATH, locator)))
        elif by_type == 'css_selector':
            return self.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, locator)))
        return None

    # 封装元素是否存在于 DOM 树中，包括被隐藏的，根据传参指定定位方式，并增加显式等待
    def presence_find_element(self, by_type, locator):
        if by_type == 'id':
            return self.wait.until(EC.presence_of_element_located((By.ID, locator)))
        elif by_type == 'name':
            return self.wait.until(EC.presence_of_element_located((By.NAME, locator)))
        elif by_type == 'class_name':
            return self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, locator)))
        elif by_type == 'tag_name':
            return self.wait.until(EC.presence_of_element_located((By.TAG_NAME, locator)))
        elif by_type == 'link_text':
            return self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, locator)))
        elif by_type == 'xpath':
            return self.wait.until(EC.presence_of_element_located((By.XPATH, locator)))
        elif by_type == 'css_selector':
            return self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)))
        return None

    # 封装检查指定元素中是否包含了预期的文本字符串，根据传参指定定位方式，并增加显式等待
    def text_present_in_element(self, by_type, locator, text):
        if by_type == 'id':
            return self.wait.until(EC.text_to_be_present_in_element((By.ID, locator), text))
        elif by_type == 'name':
            return self.wait.until(EC.text_to_be_present_in_element((By.NAME, locator), text))
        elif by_type == 'class_name':
            return self.wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, locator), text))
        elif by_type == 'tag_name':
            return self.wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, locator), text))
        elif by_type == 'link_text':
            return self.wait.until(EC.text_to_be_present_in_element((By.LINK_TEXT, locator), text))
        elif by_type == 'xpath':
            # return self.wait.until(EC.text_to_be_present_in_element((By.XPATH, locator), text))
            return WebDriverWait(self.driver, 0.5, 0.1).until(EC.text_to_be_present_in_element((By.XPATH, locator), text))

        elif by_type == 'css_selector':
            return self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, locator), text))
        return None

    # 封装检查指定元素中是否包含了预期的文本字符串，根据传参指定定位方式，并增加显式等待
    def visibility_of_all_elements(self, by_type, locator):
        if by_type == 'id':
            return self.wait.until(EC.visibility_of_all_elements_located((By.ID, locator)))
        elif by_type == 'name':
            return self.wait.until(EC.visibility_of_all_elements_located((By.NAME, locator)))
        elif by_type == 'class_name':
            return self.wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, locator)))
        elif by_type == 'tag_name':
            return self.wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, locator)))
        elif by_type == 'link_text':
            return self.wait.until(EC.visibility_of_all_elements_located((By.LINK_TEXT, locator)))
        elif by_type == 'xpath':
            # return self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, locator)))
            return WebDriverWait(self.driver, 2, 0.5).until(EC.visibility_of_all_elements_located((By.XPATH, locator)))
        elif by_type == 'css_selector':
            return self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, locator)))
        return None

    # 封装捕捉错误提示方法，使用循环检查，添加截图捕捉错误提示方法，执行js代码进行点击关闭1个或n个弹窗，在适时跳出循环，并及时抛出异常
    def capture_prompt(self, by_type, locator, screenshot_name, error_text=None):
        try:
            while True:
                # 捕捉错误提示弹窗方法
                if self.text_present_in_element(by_type, locator, error_text):
                    log.logging_info("捕捉成功")
                    time.sleep(0.5)
                    self.screenshot(screenshot_name)    # 捕捉后截图
                    self.allure_screenshot(screenshot_name)

                try:
                    def close():
                        elements = self.visibility_of_all_elements('xpath', "//span[contains(text(),'知道了')]")  # 定位目标元素
                        for element in elements:
                            self.driver.execute_script("arguments[0].click();", element)  # 用 JS 执行点击

                    if self.visibility_of_all_elements('xpath', "//span[contains(text(),'知道了')]"):  # 定位目标元素:
                        close()     # 关闭所有错误提示弹窗
                        time.sleep(0.5)

                except Exception as e:
                    log.logging_error(f"捕捉点击知道了按钮出现异常：{e}")

                else:
                    break

        except Exception as e:
            log.logging_error(f"没有出现要捕捉的: {error_text} 异常提示")

    # 封装捕捉加载超时的元素，使用循环检查，最多等等10秒，每0.5秒进行检查，超时后进行截图捕捉，未超时跳出(locator, screenshot_name, error_text=None)
    # def capture_Loading_timeout_prompt(self):
    #     try:
    #         if WebDriverWait(self.driver, 2, 1).until(EC.visibility_of_any_elements_located((By.XPATH, '//*[@id="app-main"]/div[2]/section/div'))):
    #             log.logging_info("成功捕捉：页面元素")
    #             while True:
    #                 try:
    #                     if self.wait.until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="app-main"]/div[2]/section/div'), '页面加载中')):
    #                         # if WebDriverWait(self.driver, 1, 0.2).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.flex.items-end.font-600.text-20px.inline-flex.leading-20px'), '邦芒综合服务平台\nMig')):
    #                         continue
    #                 except Exception as e:
    #                     self.screenshot('页面加载超时截图')
    #                     log.logging_error(f"页面加载超时提示：{e}")
    #                     break
    #                     # if self.text_present_in_element(by_type, locator, error_text):
    #                     # time.sleep(0.3)
    #                     # self.screenshot(screenshot_name)
    #
    #                     # def close():
    #                     #     elements = self.visibility_of_all_elements('xpath',
    #                     #                                                "//span[contains(text(),'知道了')]")  # 定位目标元素
    #                         # for element in elements:
    #                         #     self.driver.execute_script("arguments[0].click();", element)  # 用 JS 执行点击
    #
    #                     # close()
    #
    #                     # break
    #                 else:
    #                     while True:
    #                         if WebDriverWait(self.driver, 2, 1).until(EC.visibility_of_any_elements_located((By.XPATH, '//*[@id="/erp/policy/cooperationRequirements/index"]/div[2]/div[1]/div[2]/div/div[3]/div/div/div[6]/div/div/span'))):
    #                             log.logging_info("成功捕捉：页面DOM元素")
    #                             try:
    #                                 if self.wait.until(EC.visibility_of_any_elements_located((By.XPATH, '//*[@id="/erp/policy/cooperationRequirements/index"]/div[2]/div[1]/div[2]/div/div[3]/div/div/div[6]/div/div/span'))):
    #                                     continue
    #
    #                                 if self.wait.until(EC.visibility_of_any_elements_located((By.XPATH, '//*[@id="/erp/policy/cooperationRequirements/index"]/div[2]/div[1]/div[2]/div/div[3]/div/div/div[6]/div/div/span'))):
    #                                     continue
    #                             except Exception as e:
    #                                 self.screenshot('页面DOM加载超时截图')
    #                                 log.logging_error(f"页面加载超时提示：{e}")
    #                                 break
    #                         break
    #                 break
    #         else:
    #             return None
    #     except Exception as e:
    #         log.logging_error(f"捕捉加载超时的异常信息：{e}")

    # 封装捕捉加载超时的元素，使用循环检查，最多等等10秒，每0.5秒进行检查，超时后进行截图捕捉，未超时跳出(locator, screenshot_name, error_text=None)
    # 封装捕捉异常加载元素，包括页面加载元素和页面DOM加载元素
    def capture_Loading_timeout_prompt(self):
        try:
            # 判断页面加载元素是否是不存在
            if WebDriverWait(self.driver, 5, 0.3).until_not(EC.visibility_of_any_elements_located((By.XPATH, error_1))):
                pass
                log.logging_info("没有捕获到页面加载元素1")
        except Exception as e:
            # 页面加载元素抛出异常时执行
            log.logging_error(f"捕获到页面加载元素1：{e}")
            while True:
                try:
                    if self.wait.until_not(EC.text_to_be_present_in_element((By.XPATH, error_1), '页面加载中')):
                        continue
                except Exception as e:
                    # time.sleep(1)
                    self.screenshot('ERROR_1-页面加载超时_截图')
                    self.allure_screenshot('ERROR_1-页面加载超时_截图')
                    log.logging_error(f"页面加载超时提示：{e}")
                    break

        try:
            # 判断页面DOM加载元素是否是不存在
            if WebDriverWait(self.driver, 2, 0.3).until_not(EC.visibility_of_any_elements_located((By.XPATH, error_2))):
                log.logging_info("没有捕获到页面DOM加载元素2")
                pass
        except Exception as e:
            # 页面DOM加载元素抛出异常时执行
            log.logging_error(f"捕获到页面DOM加载元素2：{e}")
            while True:
                try:
                    if self.wait.until_not(EC.visibility_of_any_elements_located((By.XPATH, error_2))):
                        continue
                except Exception as e:
                    # time.sleep(1)
                    self.screenshot('ERROR_2-页面DOM加载超时_截图')
                    self.allure_screenshot('ERROR_2-页面DOM加载超时_截图')
                    log.logging_error(f"页面加载超时提示：{e}")
                    break
                break

        try:
            # 判断页面DOM加载元素是否是不存在·出现1次
            if WebDriverWait(self.driver, 2, 0.3).until_not(EC.visibility_of_any_elements_located((By.XPATH, error_3))):
                log.logging_info("没有捕获到页面DOM加载元素3")
                pass
        except Exception as e:
            # 页面DOM加载元素抛出异常时执行
            log.logging_error(f"捕获到页面DOM加载元素3：{e}")
            while True:
                try:
                    if self.wait.until_not(EC.visibility_of_any_elements_located((By.XPATH, error_3))):
                        continue
                except Exception as e:
                    # time.sleep(1)
                    self.screenshot('ERROR_3-页面DOM加载超时_截图')
                    self.allure_screenshot('ERROR_3-页面DOM加载超时_截图')
                    log.logging_error(f"页面加载超时提示：{e}")
                    break
                break

        try:
            # 判断页面DOM加载元素是否是不存在·出现12次
            if WebDriverWait(self.driver, 2, 0.1).until_not(EC.visibility_of_any_elements_located((By.XPATH, error_4))):
                log.logging_info("没有捕获到页面DOM加载元素4")
                pass
        except Exception as e:
            # 页面DOM加载元素抛出异常时执行
            log.logging_error(f"捕获到页面DOM加载元素4：{e}")
            while True:
                try:
                    if self.wait.until_not(EC.visibility_of_any_elements_located((By.XPATH, error_4))):
                        continue
                except Exception as e:
                    # time.sleep(1)
                    self.screenshot('ERROR_4-页面DOM加载超时_截图')
                    self.allure_screenshot('ERROR_4-页面DOM加载超时_截图')
                    log.logging_error(f"页面加载超时提示：{e}")
                    break
                break

        try:
            # 判断页面DOM加载元素是否是不存在
            if WebDriverWait(self.driver, 2, 0.3).until_not(EC.visibility_of_any_elements_located((By.XPATH, error_5))):
                log.logging_info("没有捕获到页面DOM加载元素5")
                pass
        except Exception as e:
            # 页面DOM加载元素抛出异常时执行
            log.logging_error(f"捕获到页面DOM加载元素5：{e}")
            while True:
                try:
                    if self.wait.until_not(EC.visibility_of_any_elements_located((By.XPATH, error_5))):
                        continue
                except Exception as e:
                    # time.sleep(1)
                    self.screenshot('ERROR_5-页面DOM加载超时_截图')
                    self.allure_screenshot('ERROR_5-页面DOM加载超时_截图')
                    log.logging_error(f"页面加载超时提示：{e}")
                    break
                break

        try:
            # 这个重复的error_4代码块是有个页面同时出现了2个error_4的加载元素，所以可能需要捕捉两次，但存疑，加上最好
            # 判断页面DOM加载元素是否是不存在
            if WebDriverWait(self.driver, 2, 0.3).until_not(EC.visibility_of_any_elements_located((By.XPATH, error_6))):
                log.logging_info("没有捕获到页面DOM加载元素6")
                pass
        except Exception as e:
            # 页面DOM加载元素抛出异常时执行
            log.logging_error(f"捕获到页面DOM加载元素：{e}")
            while True:
                try:
                    if self.wait.until_not(EC.visibility_of_any_elements_located((By.XPATH, error_6))):
                        continue
                except Exception as e:
                    self.screenshot('ERROR_6-页面DOM加载超时_截图')
                    self.allure_screenshot('ERROR_6-页面DOM加载超时_截图')
                    log.logging_error(f"页面加载超时提示：{e}")
                    break
                break

    # self.click('xpath', "//span[contains(text(),'新 增')]")
    # if self.click('xpath', "//span[@class='!ml-4px']"):
    #     self.click(by_type, error_info_button_element)
    # if self.text_present_in_element('css_selector',
    #                                 '.flex.items-end.font-600.text-20px.inline-flex.leading-20px',
    #                                 '邦芒综合服务平台\nMig'):
    #     break

    # self.refresh()  # 死循环，考虑用其他元素，文案来判断是否有弹窗
    # time.sleep(3)
    # msg = self.invisibility_find_element(by_type, "//span[contains(text(),'知道了')]")
    # log.logging_info(f"这是1：{msg}")
    # break

    # def a(self, by_type, locator):
    #     elements = self.visibility_of_all_elements(by_type, locator)  # 定位目标元素
    #     for element in elements:
    #         self.driver.execute_script("arguments[0].click();", element)  # 用 JS 执行点击

    # 封装获取错误提示并截图
    # def get_prompt(self, by_type, locator, error_text):
    #     if self.text_present_in_element(by_type, locator, error_text):
    #         log.logging_info(f"这是2：{self.text_present_in_element(by_type, locator, error_text)}")
    #         self.click(by_type, error_info_button_element)

    # 封装点击操作
    def click(self, by_type, locator):
        # time.sleep(0.5)
        self.find_element(by_type, locator).click()

        # 这里添加加载异常元素判断和捕捉
        self.capture_Loading_timeout_prompt()

        # 这里加封装捕捉异常提示
        self.capture_prompt('xpath', "//div[@class='w-full break-all']", '未配置科目_截图', "未配置科目")
        self.capture_prompt('xpath', "//div[@class='w-full break-all']", 'ERROR_后端服务返回了错误_截图', "后端服务返回了错误，请联系管理员。")
        self.capture_prompt('xpath', "//div[@class='request-error-modal']", 'ERROR_失败截图_截图')
        # self.capture_prompt('xpath', "//div[@class='flex items-center']", 'ERROR_出现提示弹窗_截图', "提示")    # 取消捕捉这个元素，会导致日志太大

        # 临时添加截图方法
        time.sleep(0.3) # 防止运行过快而导致错误截图
        self.screenshot('执行通过截图')
        self.allure_screenshot('执行通过截图')

        # self.capture_Loading_timeout_prompt('//*[@id="base-loading"]/div/div', '页面加载超时截图', '页面加载中')
        #
        # self.capture_Loading_timeout_prompt(
        #                     "//div[@class='css-1e9l0kj ant-spin ant-spin-lg ant-spin-spinning']//span[@class='ant-spin-dot ant-spin-dot-spin']",
        #                     '页面DOM加载超时截图')

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
    def hover_to_element(self, by_type, locator):
        # 创建 ActionChains 对象
        action = ActionChains(self.driver)
        # 定位元素传入hover
        # 将浏览器driver传进 Actionchains 对象，执行悬浮操作和.pause(2)是悬浮之前暂停2秒，以等待元素完全加载
        action.move_to_element(self.find_element(by_type, locator)).perform()

    # 封装截图保存到本地方法
    # def screenshot(self, screenshot_path):
    #     self.driver.save_screenshot(screenshot_path)

    # 封装截图保存的路径
    # def screenshot_path(self, screenshot_name):
    #     s_path = os.path.join(path, screenshot_name)
    #     return s_path + ".png"

    # 只用于 screenshot 方法调用的方法，用作截图顺序的排序
    # 简单的闭包，用作截图顺序的排序
    # def screenshot_num(self):
    #     count = 0
    #     def conuter():
    #         nonlocal count
    #         count += 1
    #         return count
    #     return str(conuter())

    # range() 方法也可以实现
    # for i in range(0, 1000):
    #     i += 1
    #     return str(i)

    # print(datetime.now().strftime("%Y%m%d%H%M%S"))

    # 优化后的封装截图保存到本地方法
    def screenshot(self, screenshot_name):
        # path = r"C:\Users\31646\AppData\Local\Programs\Python\venv\work\script_data\T116_Environment_Page_Traverse\Screenshot"
        path = r"./script_data/T116_Environment_Page_Traverse/Screenshot"
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        s_path = os.path.join(path, timestamp + '_' + screenshot_name + '.png')
        self.driver.save_screenshot(s_path)

    # 封装截图保存到 allure 报告的方法
    def allure_screenshot(self, name="screenshot_name"):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG,
            extension=".png"
        )

    # 封装输入框内容清空方法
    def clear_input(self, by_type, locator):
        self.find_element(by_type, locator).clear()

    # 封装键盘回车键，输入内容并点击回车
    def enter_and_text(self, by_type, locator, text=None):
        self.find_element(by_type, locator).send_keys(text + Keys.ENTER)

    # 封装页面刷新
    def refresh(self):
        self.driver.refresh()

    # 封装退出浏览器方法
    def quit_Webdriver(self):
        self.driver.quit()
