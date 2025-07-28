from python_study.module.POM.bases.base_page import BasePage


class AddressPage(BasePage):

    # 地址管理页面的属性和方法
    address_button = "//a[contains(text(),'地址管理')]"
    add_address_button = "//a[@id='createBtn']"

    # 姓名，电话，地址，邮编元素
    name_input = "//input[@id='contact']"
    number_input = "//input[@id='phone']"
    address_input = "//input[@id='address']"
    zip_code_input = "//input[@id='zipcode']"

    # 保存
    save_button = "//input[@id='submit']"

    # 删除，确认删除
    del_address = "//a[@class='deleter']"
    del_popup = "/html/body/div[7]/div/div/div[2]/button[1]"

    # 地址管理页面的方法（操作）
    def Address(self, name_input, number_input, address_input, zip_code_input):
        # self.find_ele(self.address_button).click()
        # self.find_ele(self.add_address_button).click()

        # self.find_ele(self.name_input).send_keys(name_input)
        # self.find_ele(self.number_input).send_keys(number_input)
        # self.find_ele(self.address_input).send_keys(address_input)
        # self.find_ele(self.zip_code_input).send_keys(zip_code_input)

        # self.find_ele(self.save_button).click()

        # self.find_ele(self.del_address).click()
        # self.find_ele(self.del_popup).click()

        self.click('xpath', self.address_button)
        self.click('xpath', self.add_address_button)

        self.enter_text('xpath', self.name_input, text=name_input)
        self.enter_text('xpath', self.number_input, text=number_input)
        self.enter_text('xpath', self.address_input, text=address_input)
        self.enter_text('xpath', self.zip_code_input, text=zip_code_input)
        self.click('xpath', self.save_button)

        self.click('xpath', self.del_address)
        self.click('xpath', self.del_popup)



