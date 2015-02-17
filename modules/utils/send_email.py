import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from modules.utils import config
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render

logs = config.logs

def send_email_(reciever, content, user):
    """Send email to the user from JIFFY_SUPPORT_EMAIL"""
    logs.info('Sending email to %s '%reciever)
    email_templ = get_template('email.html')
    mail_html = email_templ.render(Context ({'name': user}))
    email_msg = MIMEMultipart('alternative')
    try:
        smtpserver = smtplib.SMTP_SSL(
            config.JIFFY_EMAIL_SERVER, config.JIFFY_EMAIL_PORT)
        smtpserver.ehlo()
        smtpserver.ehlo() # extra characters to permit edit
        smtpserver.login(config.JIFFY_SUPPORT_EMAIL,
            config.JIFFY_SUPPORT_EMAIL_PWD)
        email_msg['Subject'] = "Welcome to Jiffy"
        email_msg['From'] = config.JIFFY_SUPPORT_EMAIL
        email_msg['To'] = reciever
        #header = ('To:%s\nFrom: %s\nSubject:Welcome to Jiffy\n\n'%(reciever, config.JIFFY_SUPPORT_EMAIL))
        #msg = header + mail_html
        msg = MIMEText(mail_html, 'html')
        email_msg.attach(msg)
        smtpserver.sendmail(config.JIFFY_SUPPORT_EMAIL, reciever, email_msg.as_string())
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
        send_email_(user.email, welcome_email_content, user.name)
    except Exception as e :
        logs.error('Welcome email sending FAILED! [Details: %s]'% str(e))

def send_info_to_admin(user):
    """Send email to zoho support team about the new registration"""
    logs.info("Sending new user information to Admin!")
    content = "Congrats a new user is registered!\n Details:- \nName: %s \n Email: %s \n Contact No.: %s\n Location:%s"\
               %(user.name, user.email, user.phone, user.location)
    try:
        send_email_(config.JIFFY_SUPPORT_TEAM_1, content, user)
        send_email_(config.JIFFY_SUPPORT_TEAM_2, content, user)
    except Exception as e:
        logs.error('Info sending to ADMIN Failed! [Details: %s]'%str(e))
