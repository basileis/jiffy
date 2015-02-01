import smtplib

def send_email(reciever, content):
    JIFFY_SUPPORT_EMAIL = 'bpant@jiffynow.in'
    JIFFY_SUPPORT_PWD = 'bhanu123'
    JIFFY_NAME = 'JIFFY TEAM'
    smtpserver = smtplib.SMTP_SSL("smtp.zoho.com",465)
    smtpserver.ehlo()
    smtpserver.ehlo() # extra characters to permit edit
    smtpserver.login(JIFFY_SUPPORT_EMAIL, JIFFY_SUPPORT_PWD)
    header = ('To:%s\nFrom: %s\nSubject:New Registration\n\n'%(reciever,
    JIFFY_SUPPORT_EMAIL))
    msg = header + content
    smtpserver.sendmail(JIFFY_SUPPORT_EMAIL, reciever, msg)
    smtpserver.close()

