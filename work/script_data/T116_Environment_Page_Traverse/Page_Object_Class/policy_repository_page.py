from work.script_data.T116_Environment_Page_Traverse.Base_Class.Base_Page import BasePage
from work.script_data.T116_Environment_Page_Traverse.Tools.log_tool import Logging

log = Logging()


class Policy_Repository_Tab(BasePage):      # 进入政策库模块Tab
    # 进入政策库模块Tab
    policy_repository_element = "//div[contains(text(),'政策库')]"

    def Policy_Repository_Tab(self):    # 进入政策库模块Tab
        self.click('xpath', self.policy_repository_element)


# 政策库模块
class Policy_Repository_Page(BasePage):
    # 进入政策库模块元素
    # policy_repository_element = "//div[contains(text(),'政策库')]"

    # 遍历政策库元素
    policy_repository_01_element = "//div[@title='社保公积金方案查看']"
    policy_repository_02_element = "//div[@title='商业险方案查看']"
    policy_repository_03_element = "//div[@title='企业年金方案查看']"
    policy_repository_04_element = "//div[@title='方案政策']"
    policy_repository_05_element = "//div[@title='全国残保金政策']"
    policy_repository_06_element = "//div[@title='全国工会政策']"
    policy_repository_07_element = "//div[@title='全国婚育假期一览表']"
    policy_repository_08_element = "//div[@title='全国工伤赔偿标准']"
    policy_repository_09_element = "//div[@title='全国最低工资标准']"
    policy_repository_10_element = "//div[@title='社保代理合作要求']"
    policy_repository_11_element = "//div[@title='社公转移至邦芒']"
    policy_repository_12_element = "//div[@title='工伤待遇申领条件及流程']"
    policy_repository_13_element = "//div[@title='社公调基补差政策']"
    policy_repository_14_element = "//div[@title='社公断缴影响']"
    policy_repository_15_element = "//div[@title='社公补缴政策']"

    # 商业险理赔流程盒子
    policy_repository_16_box_element = "//div[@class='ant-menu-submenu-title']//div[@title='商业险理赔流程'][contains(text(),'商业险理赔流程')]"

    # 遍历商业险理赔流程元素
    policy_repository_16_box1_element = "//div[@title='待遇申领前提条件']"
    policy_repository_16_box2_element = "//li[@role='menuitem']//div[@title='商业险理赔流程'][contains(text(),'商业险理赔流程')]"
    policy_repository_16_box3_element = "//div[@title='职业类别表']"
    policy_repository_16_box4_element = "//div[@title='商保百问百答']"

    policy_repository_17_element = "//div[@title='政策维护配置']"
    policy_repository_18_element = "//div[@title='通知公告']"

    # 政策库遍历
    def Policy_Repository(self):
        # 进入政策库模块
        # self.click('xpath', self.policy_repository_element)

        # 遍历政策库
        self.click('xpath', self.policy_repository_01_element)
        self.click('xpath', self.policy_repository_02_element)
        self.click('xpath', self.policy_repository_03_element)
        self.click('xpath', self.policy_repository_04_element)
        self.click('xpath', self.policy_repository_05_element)
        self.click('xpath', self.policy_repository_06_element)
        self.click('xpath', self.policy_repository_07_element)
        self.click('xpath', self.policy_repository_08_element)
        self.click('xpath', self.policy_repository_09_element)
        self.click('xpath', self.policy_repository_10_element)
        self.click('xpath', self.policy_repository_11_element)
        self.click('xpath', self.policy_repository_12_element)
        self.click('xpath', self.policy_repository_13_element)
        self.click('xpath', self.policy_repository_14_element)
        self.click('xpath', self.policy_repository_15_element)

        # 遍历商业险理赔流程
        self.click('xpath', self.policy_repository_16_box_element)
        self.click('xpath', self.policy_repository_16_box1_element)
        self.click('xpath', self.policy_repository_16_box2_element)
        self.click('xpath', self.policy_repository_16_box3_element)
        self.click('xpath', self.policy_repository_16_box4_element)

        self.click('xpath', self.policy_repository_17_element)
        self.click('xpath', self.policy_repository_18_element)
