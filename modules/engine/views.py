import os
import json
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from modules.db_adapter.db_adapter import DBAdapter
from rest_framework.decorators import api_view
from modules.utils import send_email, common, config
from modules.utils.config import logs
from modules.utils.jiffy_user_info import JiffyUser

# Default Landing Page loader for Jiffy

def open_home_page():
    """opens the home page of prelaunch"""
    templ = get_template('index.html')
    html = templ.render(Context())
    return HttpResponse(html)

@api_view(['GET'])
def home(request):
    logs.info('/home/')
    return open_home_page()

@api_view(['POST'])
def sign_up_user(request):
    """Sign up the new user. This will also send the email to
     admins for each new registration"""
    logs.info('/signup/ endpoint is called!')
    try:
        user = JiffyUser(request.DATA)
        logs.debug('User request came with data.[Name: %s, email: %s, phone: %s]'%(user.name, user.email, user.phone))
    except Exception as e:
        logs.warning("Could not create the user!. The inputs are invalid")
        result = dict(success=False)
        return HttpResponse(json.dumps(result))

    db_adapter = DBAdapter()
    try:
        if not db_adapter.user_exist(user.email, user.phone):
            new_user = db_adapter.create_user(user)
            if new_user:
                logs.info('New User Created :) [ID: %s]'%(new_user.id))
                result = dict(success=True)
                try:
                    logs.info('sending email to New User: [%s]'%user.name)
                    send_email.send_confirmation_email(user)
                    send_email.send_info_to_admin(user)
                except Exception as e:
                    logs.warning('Email cannot be sent. Error info: %s'%str(e))
                return HttpResponse(json.dumps(result))
            else:
                logs.warning('User registraction failed!')
                result = dict(success=False)
                return HttpResponse(json.dumps(result))
        else:
            logs.warning(
                'User Registration Railed. User Already Exists! [Details: name = %s, email = %s]'
                %(user.name, user.email))
            result = dict(success=False)
            return HttpResponse(json.dumps(result))
    except Exception as e:
        logs.warning('New Account for %s is not created. [Details: %s]'%(user.name, str(e)))
        result = dict(success=False)
        return HttpResponse(json.dumps(result))

@api_view(['GET'])
def users_list(request):
    """Return the list of all the users"""
    db_adapter = DBAdapter()
    user_list = db_adapter.get_users_list()
    data = ''
    for index in user_list:
        name = index.name
        email = index.email
        data = '%s</b><h1><p>name %s email = %s</p></h1>'%(data, name, email)
    return HttpResponse(data)

@api_view(['GET','POST'])
def sign_up_invite(request):
    return HttpResponse('<p1>SIGNUPNI got hit</p1>')

@api_view(['GET'])
def confirm_user(request):
    """Confirmation of the user to be processed"""
    db_adapter = DBAdapter()
    user_validated = False
    if  len(request.GET.keys()) > 0:
        user_conf = request.GET.keys()[0]
    else:
        result = dict(success=False)
        return HttpResponse(json.dumps(result))
    users_list = db_adapter.get_unvalidate_users()
    for user in users_list:
        hash_val = common.get_sha224_hex_digest('%s%s%s'%(user.name, user.email, user.phone))
        if hash_val == user_conf:
            db_adapter.validate_user(user)
            logs.debug("User [%s] is validated. [email: %s phone: %s]"%\
                (user.name, user.email, user.phone))
            #send_email.send_welcome_email(user)
            user_validated = True
    if not user_validated:
        logs.info("Confirm User request contains invalid hash! No user is matched")
    #This will open the home page

    return open_home_page()


@api_view(['POST'])
def invite_friends(request):
    """Invite friends and enjoy the referral bonus"""
    try:
        data = request.DATA.get(u'invite_data')
        user_data = json.loads(data)
        user = JiffyUser()
        user.extract_info(user_data)
        save_friends_data(user)
        logs.debug("Friends data is saved!")
        if config.INVITE_FRIENDS:
            send_email.send_invite_to_friends(user)
        db_adapter = DBAdapter()
        db_adapter.create_referral_id(user)
        logs.info("Referral id for user:%s is created!"%user.name)
        result = dict(success=True)
        return HttpResponse(json.dumps(result))
    except Exception as e:
        logs.warning("Exception info: Details: %s"%str(e))
        result = dict(success=False)
        return HttpResponse(json.dumps(result))

def save_friends_data(user):
    """Parse the json data"""
    db_adapter = DBAdapter()
    db_adapter.save_friends_list(user)

@api_view(['GET'])
def invited_friends(request):
    """Takes the interested people to the home page"""
    return open_home_page()
