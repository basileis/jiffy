import logging as logs

JIFFY_SUPPORT_EMAIL = "bpant@jiffynow.in"
JIFFY_SUPPORT_EMAIL_PWD = "bhanu123"
JIFFY_WEBSITE = ""
JIFFY_EMAIL_SERVER = "smtp.zoho.com"
JIFFY_EMAIL_PORT = 465
JIFFY_SUPPORT_TEAM_1 = 'bpant@jiffynow.in'
JIFFY_SUPPORT_TEAM_2 = 'sjoram@jiffynow.in'

PRELAUNCH_SERVER_LOGS = '/var/www/jiffy/jiffy.log'
LOG_LEVEL = logs.DEBUG

root_logger = logs.getLogger()
logs.basicConfig(format='%(levelname)s****%(module)s_%(funcName)s*** %(message)s',
                level=LOG_LEVEL,
                filename=PRELAUNCH_SERVER_LOGS,
                filemode='a+')