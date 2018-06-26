"""
1. 从配置文件中读取stmp配置
2. 从report文件夹下打开report.html,发送邮件
"""
import smtplib
from email.mime.text import MIMEText
import os
import sys
sys.path.append("..")
from common.config import Config, pro_path
from common.log import Log


def send_email(report_name):
    cf = Config()
    logger = Log.get_logger()
    report_file = os.path.join(pro_path, cf.get_runtime("report_dir"),report_name)

    with open(report_file, "rb") as f:
        body = f.read()

    # 格式化email正文
    msg = MIMEText(body, "html", "utf-8")

    # 配置email头
    msg["Subject"] = cf.get_email("subject")
    msg["From"] = cf.get_email("user")
    msg["To"] = cf.get_email("receiver")

    
    # 连接smtp服务器,发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(cf.get_email("server"))
    smtp.login(cf.get_email("user"),cf.get_email("pwd"))
    smtp.sendmail(cf.get_email("user"), cf.get_email("receiver"), msg.as_string())
    print("邮件发送成功")

if __name__ == "__main__":
    send_email("report.html")
    
