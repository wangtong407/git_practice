import time

from python_study.module.POM.bases.base_page import BasePage


class UploadPage(BasePage):

    # 禅道伙伴页面的属性和方法
    Partner_button = "//a[contains(text(),'禅道伙伴')]"
    logo_button = '//*[@id="logo"]'

    # 登录后的头像按钮
    Personal_Information = "//div[@class='emoji-avatar']"

    # 我的消息，文本
    me_ssage = '我的消息'

    # 禅道伙伴页面的方法（操作）
    def Upload(self, file_path):
        # self.find_ele(self.Partner_button).click()
        # self.find_ele(self.logo_button).send_keys(file_path)

        # 悬浮头像并点击我的消息
        self.hover_to_element('xpath', self.Personal_Information)
        self.click('link_text', self.me_ssage)

        # 点击禅道伙伴，上传文件
        self.click('xpath', self.Partner_button)
        self.enter_text('xpath', self.logo_button, file_path)

        self.allure_screenshot("截图2")
        # 调用封装的截图方法
        # self.allure_screenshot("上传图片截图")

