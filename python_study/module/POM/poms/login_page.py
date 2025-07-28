from python_study.module.POM.bases.base_page import BasePage
from python_study.module.POM.tools.log_tool import Logging
import time


class LoginPage(BasePage):
    # 写登录页面的属性和方法
    login_button_run = "//a[@class='btn-login']"
    password_login_button = "//a[contains(text(),'密码登录')]"
    account_input = "//input[@id='account']"
    password_input = "//input[@id='password']"
    login = "//div[@class='form-group']//input[@id='submit']"

    # 写登录页面的方法（操作）
    def login_cd(self, account, password):
        # 实例化日志方法
        l = Logging()
        # self.find_ele(self.login_button).click()
        # self.find_ele(self.password_login_button).click()
        # self.find_ele(self.account_input).send_keys(account)
        # self.find_ele(self.password_input).send_keys(password)
        # self.find_ele(self.login).click()

        # self.find_ele(self.Personal_Information).click()
        try:
            self.click('xpath', self.login_button_run)
            self.click('xpath', self.password_login_button)
            self.enter_text('xpath', self.account_input, text=account)
            self.enter_text('xpath', self.password_input, text=password)

            if account == 'wx_655b149be0379' and password == 'w20040702':
                l.logging_info(f"尝试登录，用户名: {account},密码：{password}")
                self.click('xpath', self.login)

                # 调用封装的截图方法
                time.sleep(2)
                self.allure_screenshot("登录成功截图")
                l.logging_info("登录成功")
            else:
                self.click('xpath', self.login)
                time.sleep(2)
                self.allure_screenshot("登录失败截图")
                l.logging_warning(f"登录失败,用户名或密码错误")
        except Exception as e:
            l.logging_error(f"出现错误提示：{e}")
            print(f"出现错误提示：{e}")


