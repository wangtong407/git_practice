import allure
from functools import wraps


def allure_wrapper(module, page, case_name):  # allure 报告集成方法
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # with allure.step(f"模块: {module}"):
            allure.dynamic.feature(f"模块: {module}")
            # with allure.step(f"页面: {page}"):
            allure.dynamic.story(f"页面: {page}")
            # with allure.step(f"用例: {case_name}"):
            allure.dynamic.title(f"用例: {case_name}")
            return func(*args, **kwargs)

        return wrapper

    return decorator


# 使用示例
@allure_wrapper(module="登录模块", page="登录页", case_name="验证正确用户名密码登录")
def test_login_success():
    # 测试逻辑
    pass


"""
这个是allure报告集成方法，和上面的区别是：allure.step 和 allure.dynamic.feature 等的方法，前者可以用 with 方法管理，后者不可
这两个都可以用，但是后者简洁些
下次可以考虑将模块，页面，用例名称，步骤都封装到这里面，更加简洁了
import allure
from functools import wraps

def allure_wrapper(module, page, case_name):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with allure.step(f"模块: {module}"):
                with allure.step(f"页面: {page}"):
                    with allure.step(f"用例: {case_name}"):
                        return func(*args, **kwargs)
        return wrapper
    return decorator

# 使用示例
@allure_wrapper(module="登录模块", page="登录页", case_name="验证正确用户名密码登录")
def test_login_success():
    # 测试逻辑
    pass
"""
