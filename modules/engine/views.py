import os
import json
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render
from modules.db_adapter.db_adapter import DBAdapter
from rest_framework.decorators import api_view

# Default Landing Page loader for Jiffy
@api_view(['GET'])
def home(request):
    templ = get_template('index.html')
    html = templ.render(Context())
    return HttpResponse(html)


@api_view(['POST'])
def sign_up_user(request):
    """Sign up the new user. This will also send the email to
     admins for each new registration"""
    data = request.DATA
    db_adapter = DBAdapter()
    try:
        user_existing = db_adapter.get_user(data.get('email'), data.get('phone'))
        if user_existing is None:
            new_user = db_adapter.create_user(dict(data)):
            if new_user:
		        print 'New User Created :) [ID: %s]'%(new_user.id) 
		        result = dict(success=True)
		        return HttpResponse(json.dumps(result))
            else:
		        print 'User creation Failed!'
        else:
            result = dict(success=False)
            return HttpResponse(json.dumps(result))
    except Exception as e:
        print str(e)
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

'''
#@api_view(['POST'])
def send_invite(request):
    # data = request.DATA
    # user_name = data.get('username')
    # password = data.get('password')
    try:
        gmail_contacts = ContactsEmail('bhupeshpant19jan@gmail.com', 'mail4bhanu')
        # gmail_contacts = ContactsEmail(user_name, password)
        phone_no, emails = gmail_contacts.ListAllContacts()
        print emails
        print phone_no
        emails = ['bhanupant19@live.com']
        for email in emails:
            try:
                ref_id = os.urandom(32).encode('hex')
                send_email(email, ref_id)
                db_adaptrer = DBAdapter()
                #user = db_adapter.get_user(data.get('email'), data.get('phone'))
                #db_adapter.create_referral(user, ref_id)
            except Exception as e:
                pass
    except Exception as e:
        return HttpResponse(str(e))
    return HttpResponse("<h1>The request has been sent to your friends... :) </h2></br><h2>Enjouy your referral bonus!!</h2>")
'''

