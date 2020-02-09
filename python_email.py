# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

msg = EmailMessage()
msg.set_content(
"""測試訊息
盤後資訊""")

msg['Subject'] = "股票資訊"
msg['From'] = ['stock@info.com']#傳送的電子郵件
msg['To'] = ['test@gmail.com']#接收的電子郵件

# Send the message via our own SMTP server.
try:
	smtpObj = smtplib.SMTP('msa.hinet.net',25)#SMTP伺服器
#	smtpObj.login(account_mail,password)
	smtpObj.send_message(msg)
	print("Successfully sent email")
except Exception:  
	print("Error: unable to send email")
smtpObj。退出（）
#https://wyp8711.blogspot.com/2020/02/python-ispsmtpemail.html
