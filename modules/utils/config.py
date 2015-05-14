import logging as logs

JIFFY_SUPPORT_EMAIL = "connect@jiffynow.in"
JIFFY_SUPPORT_EMAIL_PWD = "jiffy_12#$"
JIFFY_WEBSITE = "http://JiffyNow.in"
JIFFY_EMAIL_SERVER = "smtp.zoho.com"
JIFFY_EMAIL_PORT = 465
#JIFFY_SUPPORT_EMAIL = "thinkjiffy@gmail.com"
#JIFFY_SUPPORT_EMAIL_PWD = "jiffynow_123"
#JIFFY_EMAIL_SERVER = "smtp.gmail.com"
#JIFFY_EMAIL_PORT = 587
JIFFY_SUPPORT_TEAM_1 = 'bpant@jiffynow.in'
JIFFY_SUPPORT_TEAM_2 = 'sjoram@jiffynow.in'
INVITE_FRIENDS = True

PRELAUNCH_SERVER_LOGS = '/tmp/jiffy.log'
PRELAUNCH_CSV_DATA_REP_PATH = '/tmp/csv_data_repo/'
LOG_LEVEL = logs.DEBUG

root_logger = logs.getLogger()
logs.basicConfig(format='%(levelname)s %(asctime)s [****%(module)s_%(funcName)s***] %(message)s',
                level=LOG_LEVEL,
                filename=PRELAUNCH_SERVER_LOGS,
                filemode='a+')
