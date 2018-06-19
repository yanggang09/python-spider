#coding='utf-8'
# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
import time
import os
my_sender = '*****@126.com'  # 发件人邮箱账号
my_pass = '******'  # 发件人邮箱密码
my_user = '****@qq.com'  # 收件人邮箱账号，我这边发送给自己
file_path = os.getcwd()
name = time.strftime("%Y%m%d%H",time.localtime(time.time()))
file_path02 = file_path + '\\' + 'Data' + name + '\\' + 'GUpiaoinfo.txt'
excel_name = file_path + '\\' + 'Data' + name + '\\' + name + 'StockInfo.xls'
list_00 = []
f08 = open(file_path02,'ab+')
for lines in f08.readlines():
    list_00.append(lines)
msg_html = "".join(list_00[:138])



def mail():
    ret = True
    try:
        #msg = MIMEText(msg_html, 'html', 'utf-8')
        msg = MIMEMultipart()
        msg['From'] = formataddr(["股票涨跌行情", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["知情人1", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "%s时预报的股票和上涨前100股票行情"%name  # 邮件的主题，也可以说是标题

        #邮件正文内容
        msg.attach(MIMEText(msg_html,'html','utf-8'))
        att1 = MIMEText(open(excel_name,'rb').read(),'base64','utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename=' + 'test1.xls'
        msg.attach(att1)

        server = smtplib.SMTP_SSL("smtp.126.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret



ret = mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")