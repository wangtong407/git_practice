from work.script_data.T116_Environment_Page_Traverse.Base_Class.Base_Page import BasePage
from work.script_data.T116_Environment_Page_Traverse.Tools.log_tool import Logging

log = Logging()


class Login(BasePage):

    username_input = "#login_username"
    password_input = "#login_password"

    login_button = "button[class='css-1e9l0kj ant-btn ant-btn-primary login-submit'] span"
    login_success_prompt = '.flex.items-end.font-600.text-20px.inline-flex.leading-20px'

    # 登录方法，并判断是否真的登录成功
    def login_fun(self, username, password):
        # try:

        self.enter_text('css_selector', self.username_input, username)
        self.enter_text('css_selector', self.password_input, password)

        log.logging_info("输入用户名和密码")

        self.click('css_selector', self.login_button)
        self.screenshot('执行成功截图')

        log.logging_info("点击登录按钮")

        # 捕捉提示“邦芒综合服务平台\nTes”，确认是否登录成功
        # if self.text_present_in_element('css_selector', self.login_success_prompt, '邦芒综合服务平台\nFat'):
        #     log.logging_info(r"捕捉成功:邦芒综合服务平台\nFat，确认登录成功，进入首页")
        #     log.logging_info(f"789789功:{self.get_title()}")
        #
        #     try:
        #         # 截图查看是否登录成功
        #         self.screenshot('登录成功截图')
        #     except Exception as e:
        #         log.logging_error(f"出现异常请确认截图是否保存成功：{e}")


        # else:
        #     log.logging_error(f"请确认是否登录成功")
        # except Exception as e:
        #         log.logging_error(f"出现错误提示：{e}")
