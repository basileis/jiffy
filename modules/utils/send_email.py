import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from modules.utils import config
from django.template.loader import get_template
from django.template import Context
from modules.utils import common
import json

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
    """Send welcome/email confirmation email to the new registered
    user those confirmed their email ids"""
    logs.info("Sending welcome email to new user!")
    templ = get_template('welcome_email.html')
    welcome_email_content = templ.render(Context({'name':user.name}))
    try:
        send_email_(user.email, 'Welcome to Jiffy!', welcome_email_content)
    except Exception as e :
        logs.error('Welcome email sending FAILED! [Details: %s]'% str(e))

def send_confirmation_email(user):
    """
    Send confirmation email to user
    """
    logs.info("Sending confirmation email to new user!")
    templ = get_template('email_confirmation.html')
    hash_val = common.get_sha224_hex_digest('%s%s%s'%(user.name, user.email, user.phone))

    confirmation_url = '%s/confirmUser?%s=True'%(config.JIFFY_WEBSITE, hash_val)
    logs.debug('The confirmation email is sent to user. [Details: Name: %s, Confirmation Link: %s ]'\
    %(user.name, confirmation_url))
    confirmation_email_content = templ.render(Context({'name':user.name, 'confirmation_url': confirmation_url}))
    try:
        send_email_(user.email, 'Email Confirmation!', confirmation_email_content)
    except Exception as e :
        logs.error('Welcome email sending FAILED! [Details: %s]'% str(e))

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

def send_invite_to_friends(user):
    """Send Invite email to friends"""
    friends_list = json.loads(user.friends)
    templ = get_template('email_invite.html')
    hash_val = common.get_sha224_hex_digest('%s%s%s'%(user.name, user.email, user.phone))
    confirmation_url = '%s/referral?%s=True'%(config.JIFFY_WEBSITE, hash_val)

    for friend in friends_list:
        emails = friend.get('emails')
        for email in emails:
            try:
                invite_email = templ.render(Context({'referree_name':user.name, 'referral_hash': confirmation_url}))
                send_email_(email, 'Invited by %s'%user.name, invite_email)
            except Exception as e:
                logs.error('Invite email sending FAILED! [Details: %s]'% str(e))

if __name__ == '__main__':

    send_email_('bhupeshpant19jan@gmail.com', 'test', 'this is the content')
    send_email_('8milelb@gmail.com', 'test', 'this is the content')

    from jiffy_user_info import JiffyUser
    user = JiffyUser()
    user.email = u'bhanupant19@live.com'
    user.location = u'wakad'
    user.phone = u'7871277217'
    user.user_type = 2
    user.name= u'shanu'
    user.friends = ''
    send_confirmation_email(user)
    send_welcome_email(user)
    send_invite_to_friends(user)
