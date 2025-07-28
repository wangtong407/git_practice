import logging
from time import strftime
import os

# 设置日志输出格式
fmt = "%(asctime)s - %(filename)s - [line:%(lineno)d] - %(levelname)s - %(message)s"

filename = strftime('%Y%m%d-%H%M%S')  # 转化为当前的时间格式
log_file_path = os.path.join(r'.\POM\logs', filename + '.log')  # 使用os.path.join方法，将两个字符串路径拼接
# 配置日志
logging.basicConfig(filename=log_file_path, filemode="a", format=fmt, level=logging.DEBUG, encoding="UTF-8")


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


print(os.getcwd())

