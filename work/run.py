import time

import pytest
import os
import zipfile

from work.script_data.T116_Environment_Page_Traverse.Tools.delete_image import delete_png
from work.script_data.T116_Environment_Page_Traverse.Tools.send_email import send_email_with_attachment


# 创建压缩报告的函数
def zip_folder(folder_path, output_path):
    """
    将指定文件夹压缩为ZIP文件
    :param folder_path: 要压缩的文件夹路径（绝对或相对路径）
    :param output_path: 生成的ZIP文件路径（如 "output.zip"）
    """
    # 确保文件夹路径是绝对路径
    folder_path = os.path.abspath(folder_path)

    # 计算文件夹的父目录（用于生成相对路径）
    parent_dir = os.path.dirname(folder_path)

    # 创建ZIP文件
    # 三个参数：生成的 ZIP 文件路径、以写入模式打开 ZIP 文件、使用压缩算法（默认选项）。
    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        # 遍历文件夹
        """
        os.walk 递归遍历 folder_path 下的所有子目录和文件，返回一个三元组 (root, dirs, files)
        root：当前目录的绝对路径（如 /home/user/project/my_folder/subdir）。
        dirs：当前目录下的子目录列表。
        files：当前目录下的文件列表。
        """
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                # 获取文件的绝对路径
                file_path = os.path.join(root, file)
                # 生成文件在ZIP中的相对路径（保留目录结构）
                arcname = os.path.relpath(file_path, parent_dir)
                # 将文件添加到 ZIP 中，并指定其在 ZIP 中的路径为 arcname。
                zipf.write(file_path, arcname)


# 设置全局pytest框架启动方法
if __name__ == '__main__':
    # 启动pytest框架
    pytest.main()

    # allure generate 构建allure报告
    # ./POM//temps 使用该文件下的临时json报告
    # -o ./reports 将转化的html报告输出到reports目录下
    # --clean 当目录中有报告会删除后再生成报告
    os.system("allure generate ./script_data/T116_Environment_Page_Traverse//temps -o ./script_data/T116_Environment_Page_Traverse//reports --clean")

    # 调用压缩文件夹的方法，生成zip压缩包
    zip_folder(r"./script_data/T116_Environment_Page_Traverse/reports", r"./script_data/T116_Environment_Page_Traverse/reports.zip")
    zip_folder(r"./script_data/T116_Environment_Page_Traverse/Screenshot", r"./script_data/T116_Environment_Page_Traverse/Screenshot.zip")
    # time.sleep(2)

    # send_email_with_attachment('ytttfxjgbhvddebi', '2873978343@qq.com')     # 邮件发送截图附件方法
    # send_email_with_attachment('ytttfxjgbhvddebi', 'zsm@50bm.com')     # 邮件发送截图附件方法

    # delete_png(r"./script_data/T116_Environment_Page_Traverse/Screenshot")    # 删除截图方法


