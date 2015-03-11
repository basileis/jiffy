import logging as logs

JIFFY_SUPPORT_EMAIL = "connect@jiffynow.in"
JIFFY_SUPPORT_EMAIL_PWD = "jiffy_!@34"
JIFFY_WEBSITE = "http://JiffyNow.in"
JIFFY_EMAIL_SERVER = "smtp.zoho.com"
JIFFY_EMAIL_PORT = 465
JIFFY_SUPPORT_TEAM_1 = 'bpant@jiffynow.in'
JIFFY_SUPPORT_TEAM_2 = 'sjoram@jiffynow.in'

PRELAUNCH_SERVER_LOGS = '/tmp/jiffy.log'
LOG_LEVEL = logs.DEBUG

root_logger = logs.getLogger()
logs.basicConfig(format='%(levelname)s %(asctime)s [****%(module)s_%(funcName)s***] %(message)s',
                level=LOG_LEVEL,
                filename=PRELAUNCH_SERVER_LOGS,
                filemode='a+')
