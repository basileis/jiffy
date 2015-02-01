import smtplib


def send_email(reciever, content):
    JIFFY_SUPPORT_EMAIL = 'bpant@jiffynow.in'
    JIFFY_SUPPORT_PWD = 'bhanu123'
    JIFFY_NAME = 'JIFFY TEAM'
    smtpserver = smtplib.SMTP_SSL("smtp.zoho.com",465)
    smtpserver.ehlo()
    smtpserver.ehlo() # extra characters to permit edit
    smtpserver.login(user, pwd)
    header = ('To: %s \n From: %s \n Subject: New Registration! \n'%(reciever,
    JIFFY_NAME))
    msg = header + content
    smtpserver.sendmail(user, reciever, msg)
    smtpserver.close()
