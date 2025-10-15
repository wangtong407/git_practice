error_info_element = "//span[contains(text(),'后端服务返回了错误，请联系管理员。')]"
error_info_button_element = "//span[contains(text(),'知道了')]"


# 大部分页面的页面加载元素
error_1 = '//*[@id="app-main"]/div[2]/section/div'

# 大部分页面DOM的加载元素
error_2 = '//*[@id="/erp/policy/cooperationRequirements/index"]/div[2]/div[1]/div[2]/div/div[3]/div/div/div[6]/div/div/spann'

# 政策库-社保代理合作要求页面的DOM加载元素
error_3 = '//*[@id="/erp/policy/cooperationRequirements/index"]/div[2]/div[1]/div[2]/div/div[3]/div/div/div[6]/div/div'

# 政策库-社公转移至邦芒页面DOM加载元素
# 结算中心-应收管理-应收账单的页面DOM加载元素
error_4 = '//div[@class="vxe-loading--wrapper"]//div[1]'

# 业务办理-人员花名册统计页面DOM加载元素
error_5 = '//*[@id="/erp/generalSalary/personalDeduction/rostetStatistics/index"]/div[2]/div/section/div'


"""
116 和 test1 的元素差异
流程审批：
本级员工报销审批按钮
团队基金的审批按钮
采购下的所有按钮
跑腿业务的配置页面
退款下的申请，审批按钮

业务办理：
员工管理-订单查询出现引导弹窗 test1 出现这个弹窗，116没有

"""

