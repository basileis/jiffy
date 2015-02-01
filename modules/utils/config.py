import logging as logs

JIFFY_SUPPORT_EMAIL = ''
JIFFY_SUPPORT_EMAIL_PWD = ''
JIFFY_WEBSITE = ""

PRELAUNCH_SERVER_LOGS = 'D:/jiffy.log'
LOG_LEVEL = logs.DEBUG

root_logger = logs.getLogger()
logs.basicConfig(format='%(levelname)s****%(module)s_%(funcName)s*** %(message)s',
                level=LOG_LEVEL,
                filename=PRELAUNCH_SERVER_LOGS,
                filemode='a+')