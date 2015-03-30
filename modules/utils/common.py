import hashlib
import os
import json
from modules.utils.config import logs, PRELAUNCH_CSV_DATA_REP_PATH


def get_sha224_hex_digest(string):
    """Returns the hexdigest of the string"""
    h = hashlib.new('sha224')
    h.update(string)
    return h.hexdigest()

def prepare_csv_data_file(user):
    """Create the csv file od friends list"""
    path = '%s%s_%s.csv'%(PRELAUNCH_CSV_DATA_REP_PATH,
                            user.name,
                            user.email)
    try:
        csv_file = open(path, 'w')
        friend_list = json.loads(user.friends)
        for friend in friend_list:
            for email in friend['emails']:
                line = '%s,%s\n'%(email, friend['name'])
                csv_file.write(line)
        csv_file.flush()
        csv_file.close()
        logs.info("CSV file is saved for User: %s. [Path: %s]"%(user.name, path))
    except Exception as e:
        logs.warning("CSV file Creation Failed! [Detail: %s]"%str(e))

if __name__ == '__main__':
    print get_sha224_hex_digest('bhupesh is the dev')
    prepare_csv_data_file(None)