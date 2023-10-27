# smtp： 发件
import smtplib
from email.header import Header
from email.mime.text import MIMEText

email_value_config = {
    'smtp_server': 'smtp.qq.com',
    'username': '2448906309@qq.com',
    'password': '*******',
}

# 登录邮箱
smtp_server = email_value_config['smtp_server']
server = smtplib.SMTP_SSL(email_value_config['smtp_server'], 465)  # qq邮箱smtp端口号是465
from_addr = email_value_config['username']  # 发件邮箱
password = email_value_config['password']  # 邮箱密码(或者客户端授权码)

try:
    server.login(from_addr, password)  # 登录邮箱
except Exception as e:
    print('Error:', e)

message = '''您好，这是一封测试邮件'''
msg = MIMEText(message, 'plain', 'utf-8')

msg['Subject'] = Header("回复：测试", 'utf-8')
msg['From'] = Header(email_value_config['username'])

to_addr_list = ['843043431@qq.com', '3253631974@qq.com']

try:
    for to_addr in to_addr_list:
        msg['To'] = Header(to_addr, 'utf-8')
        server.sendmail(from_addr, to_addr, msg.as_string())  # 将msg转化成string发出
except Exception as e:
    print('Error:', e)

server.quit()
