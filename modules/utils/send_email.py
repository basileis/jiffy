import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from modules.utils import config
from django.template.loader import get_template
from django.template import Context
from modules.utils import common

logs = config.logs

def send_email_(reciever, subject, body):
    """Send email to the user from JIFFY_SUPPORT_EMAIL"""
    logs.info('Sending email to %s '%reciever)
    try:
        MESSAGE = MIMEMultipart('related')
        MESSAGE['subject'] = subject
        MESSAGE['To'] = reciever
        MESSAGE['From'] = config.JIFFY_SUPPORT_EMAIL
        MESSAGE.preamble = """
        Your mail reader does not support the report format.
        Please visit us <a href="http://www.jiffynow.in">online</a>!"""

        HTML_BODY = MIMEText(body, 'html')
        MESSAGE.attach(HTML_BODY)
        server = smtplib.SMTP_SSL(config.JIFFY_EMAIL_SERVER, config.JIFFY_EMAIL_PORT)
        server.ehlo()
        server.login(config.JIFFY_SUPPORT_EMAIL,config.JIFFY_SUPPORT_EMAIL_PWD)
        server.sendmail(config.JIFFY_SUPPORT_EMAIL, [reciever], MESSAGE.as_string())
        server.quit()
    except Exception as e:
        logs.warn('Exception occurred while sending email to:%s. [Desc: %s]'\
                    %(reciever, str(e)))
        raise

def send_welcome_email(user):
    """Send welcome/email confirmation email to the new registered user"""
    logs.info("Sending welcome email to new user!")
    templ = get_template('email_invite.html')
    welcome_email_content = templ.render(Context({'referree_name':user.name}))
    try:
        send_email_(user.email, 'Welcome to Jiffy!', welcome_email_content)
    except Exception as e :
        logs.error('Welcome email sending FAILED! [Details: %s]'% str(e))
        raise

def send_confirmation_email(user):
    """
    Send confirmation email to user
    """
    logs.info("Sending confirmation email to new user!")
    templ = get_template('email_confirmation.html')
    hash_val = common.get_sha224_hex_digest('%s%s%s'%(user.name, user.email, user.phone))

    confirmation_url = '%s/confirmUser?%s=True'%(config.JIFFY_WEBSITE, hash_val)
    confirmation_email_content = templ.render(Context({'name':user.name, 'confirmation_url': confirmation_url}))
    try:
        send_email_(user.email, 'Email Confirmation!', confirmation_email_content)
    except Exception as e :
        logs.error('Welcome email sending FAILED! [Details: %s]'% str(e))
        raise

def send_info_to_admin(user):
    """Send email to zoho support team about the new registration"""
    logs.info("Sending new user information to Admin!")
    content = "Congrats a new user is registered!\n Details:- \nName: %s \n Email: %s \n Contact No.: %s\n Location:%s"\
               %(user.name, user.email, user.phone, user.location)
    try:
        send_email_(config.JIFFY_SUPPORT_TEAM_1, 'New Registration Notification!', content)
        send_email_(config.JIFFY_SUPPORT_TEAM_2, 'New Registration Notification!', content)
    except Exception as e:
        logs.error('Info sending to ADMIN Failed! [Details: %s]'%str(e))
        raise

if __name__ == '__main__':
    class JiffyUser(object):
        """
        This class will contain all the detail of the user,
        including all the cross table information
        """
        email = ''
        name = ''
        phone = ''
        user_type = ''
        location = ''

        def __init__(self):
            pass

    user = JiffyUser()
    user.email = u'shanupant19@live.com'
    user.location = u'wakad'
    user.phone = u'7871277217'
    user.user_type = 2
    user.name= u'shanu'
    send_confirmation_email(user)
