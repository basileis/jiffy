import smtplib
from modules.utils import config

logs = config.logs

def send_email(reciever, content):
    """Send email to the user from JIFFY_SUPPORT_EMAIL"""
    logs.info('Sending email to %s '%reciever)
    try:
        smtpserver = smtplib.SMTP_SSL(
            config.JIFFY_EMAIL_SERVER, config.JIFFY_EMAIL_PORT)
        smtpserver.ehlo()
        smtpserver.ehlo() # extra characters to permit edit
        smtpserver.login(config.JIFFY_SUPPORT_EMAIL,
        config.JIFFY_SUPPORT_EMAIL_PWD)
        header = ('To:%s\nFrom: %s\nSubject:New Registration\n\n'%(reciever,
        config.JIFFY_SUPPORT_EMAIL))
        msg = header + content
        smtpserver.sendmail(config.JIFFY_SUPPORT_EMAIL, reciever, msg)
        logs.info('Email has been sent successfully to %s'%reciever)
        smtpserver.close()
    except Exception as e:
        logs.warn('Exception occurred while sending email to:%s. [Desc: %s]'\
                    %(reciever, str(e)))
        raise 

def send_welcome_email(user):
    """Send welcome/email confirmation email to the new registered user"""
    logs.info("Sending welcome email to new user!")
    welcome_email_content = "Welcome!\n Thanks Mr. %s for joining us. We will reach to you soon!"%user.name
    try:
        send_email(user.email, welcome_email_content)
    except:
        logs.error('Welcome email sending FAILED!')

def send_info_to_admin(user):
    """Send email to zoho support team about the new registration"""
    logs.info("Sending new user information to Admin!")
    content = "Congrats a new user is registered!\n Details:- \nName: %s \n Email: %s \n Contact No.: %s\n Location:%s"\
               %(user.name, user.email, user.phone, user.location)
    try:
        send_email(config.JIFFY_SUPPORT_TEAM_1, content)
        send_email(config.JIFFY_SUPPORT_TEAM_2, content)
    except:
        logs.error('Info sending to ADMIN Failed!')
