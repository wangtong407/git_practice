import logging
from time import strftime
import os


# 设置日志输出格式
fmt = "%(asctime)s - %(filename)s - [line:%(lineno)d] - %(levelname)s - %(message)s"

filename = strftime('%Y%m%d-%H%M%S')  # 转化为当前的时间格式
path = r'./script_data/T116_Environment_Page_Traverse/logs_file/'
# log_file_path = os.path.join(r'..\logs', filename + '.log')  # 使用os.path.join方法，将两个字符串路径拼接
log_file_path = os.path.join(path, filename + '.log')  # 使用os.path.join方法，将两个字符串路径拼接
# print(log_file_path)
# 配置日志
logging.basicConfig(filename=log_file_path, filemode="w", format=fmt, level=logging.DEBUG, encoding="UTF-8")


class Logging:

    def logging_debug(self, msg):
        logging.debug(msg)

    def logging_info(self, msg):
        logging.info(msg)

    def logging_warning(self, msg):
        logging.warning(msg)

    def logging_error(self, msg):
        logging.error(msg)

    def logging_critical(self, msg):
        logging.critical(msg)


# 获取当前路径和logs的路径相对位置
# print(os.path.relpath(
#     r'C:\Users\31646\AppData\Local\Programs\Python\venv\work\script_data\T116_Environment_Page_Traverse\logs_file',
#     r'C:\Users\31646\AppData\Local\Programs\Python\venv\work\script_data\T116_Environment_Page_Traverse\Tools\log_tool.py'
# ))
# 获取当前路径
# print(os.getcwd())
