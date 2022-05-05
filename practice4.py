import smtplib
from email.message import EmailMessage
import re

def sendEmail(addr):
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    if bool(re.match(reg,addr)):
        smtp.send_message(msg)
        print("정상적으로 메일이 발송되었습니다.")
    else:
        print("유효한 이메일 주소가 아닙니다.")

server = "smtp.gmail.com"
port = 465

msg = EmailMessage()
msg.set_content("본문")

msg["Subject"] = "pythonhw#4"
msg["From"] = "lishavxn@yonsei.ac.kr"
msg["To"] = "ksjoon28@naver.com"

smtp = smtplib.SMTP_SSL(server,port)
smtp.login("lishavxn@yonsei.ac.kr","pw")
sendEmail()
smtp.quit()