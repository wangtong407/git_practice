import smtplib  # 用于SMTP协议通信
from email.mime.multipart import MIMEMultipart  # 创建多部分邮件
from email.mime.text import MIMEText  # 处理文本内容
from email.mime.application import MIMEApplication  # 处理附件
import os


def send_email_with_attachment(password, recipient):
    # 邮件配置（需修改为你的信息）
    sender = '3164635379@qq.com'  # 发件人邮箱
    password = password  # QQ邮箱授权码（不是密码）
    receiver = recipient  # 收件人邮箱
    subject = '自动化脚本执行结果邮件'  # 邮件主题
    # body = '您好，\n\n这是一封来自Python的测试邮件，包含附件。\n请查收。'  # 邮件正文

    # 附件路径（多个附件用列表，用逗号隔开）
    attachments = [r"./script_data/T116_Environment_Page_Traverse/Screenshot.zip"]  # 替换为实际文件路径
    # attachments = [r"../Screenshot.zip"]  # 替换为实际文件路径，失败
    # attachments = [r"C:\Users\31646\AppData\Local\Programs\Python\venv\work\script_data\T116_Environment_Page_Traverse\Screenshot.zip"]  # 替换为实际文件路径

    # 创建邮件对象
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject

    # 添加html的邮件正文
    # <p><a href="https://www.qq.com">点击访问QQ官网</a></p> 这个是邮件中的链接标签，可以添加超链接
    html_content = """
    <html>
      <body>
        <h1 style="color: blue;">您好，这是一封来自系统的邮件，此邮件为系统自动发送，请勿直接回复。</h1>
        <p>这是本次自动化执行 ERP系统的一级页面遍历 执行结果邮件，包含附件，请查收~</p>
        <p>附件中<strong> Screenshot.zip </strong>文件是本次执行结束的<strong> 截图附件 </strong>，请解压后查看</p>
        <p>截图名称中出现<strong> “执行通过截图” </strong>文本，即表示通过</p>
        <p>截图名称中出现<strong> “ERROR” </strong>文本，即表示某个模块出现错误提示，请反馈给相关人员排查</p>
      </body>
    </html>
    """
    msg.attach(MIMEText(html_content, 'html', 'utf-8'))
    # 添加普通邮件正文
    # msg.attach(MIMEText(body, 'plain', 'utf-8'))

    # 添加附件
    for file_path in attachments:
        if not os.path.isfile(file_path):
            print(f"警告：附件 {file_path} 不存在，跳过")
            continue

        # "rb" 表示以二进制模式只读打开文件，适用于读取非文本文件（如图片、PDF、Excel、压缩包等）
        with open(file_path, 'rb') as f:
            file_data = f.read()
            file_name = os.path.basename(file_path)

        part = MIMEApplication(file_data, Name=file_name)
        part['Content-Disposition'] = f'attachment; filename="{file_name}"'
        msg.attach(part)

    try:
        # 连接QQ邮件服务器 (SSL加密)+
        server = smtplib.SMTP_SSL('smtp.qq.com', 465)
        server.login(sender, password)

        # 发送邮件
        server.sendmail(sender, receiver, msg.as_string())
        print("邮件发送成功！")

    except Exception as e:
        print(f"发送失败: {str(e)}")
    finally:
        server.quit()


# 执行发送
# if __name__ == "__main__":
#     send_email_with_attachment('ytttfxjgbhvddebi', '2873978343@qq.com')
