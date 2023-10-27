# imap： 收件
import imaplib
import email
from email.utils import parsedate_to_datetime
from email.header import make_header, decode_header

email_value_config = {
	'imap_server': 'imap.qq.com',
	'username': '2448906309@qq.com',
	'password': '*******',
}
email_server = imaplib.IMAP4_SSL(email_value_config['imap_server'])
email_server.login(email_value_config["username"], email_value_config['password'])

"""
INBOX 收件箱
Sent Messages 已发送
Drafts 草稿箱
Deleted Messages 已删除
Junk 垃圾箱
"""
# 查看所有邮箱
for i in email_server.list()[1]:
	l = i.decode().split(' "/" ')
	print(l[0] + " = " + l[1])

email_server.select('INBOX')
_typ, _search_data = email_server.search(None, 'ALL')
# 开始解析
mailidlist = _search_data[0].split()  # 转成标准列表,获得所有邮件的ID
print(f'一共解析邮件数量：{len(mailidlist)}')
# 解析内容：
for mail_id in mailidlist[-10:]:
	result, data = email_server.fetch(mail_id, '(RFC822)')  # 通过邮件id获取邮件
	email_message = email.message_from_bytes(data[0][1])  # 邮件内容（未解析）
	# print(email_message.get_payload())  # 内容
	subject = make_header(decode_header(email_message['SUBJECT']))  # 主题
	mail_from = make_header(decode_header(email_message['From']))  # 发件人
	mail_dt = parsedate_to_datetime(email_message['Date']).strftime("%Y-%m-%d %H:%M:%S")  # 收件时间
	email_info = {
		"主题": str(subject),
		"发件人": str(mail_from),
		"收件时间": mail_dt,
	}
	print(email_info)




