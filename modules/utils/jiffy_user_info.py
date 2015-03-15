from modules.utils.config import logs
import json


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
    friends = ''

    def __init__(self, params=None):
        """Get the user basic info from the httpRequest params"""
        if params:
            try:
                self.email = params.get("email")
                self.name = params.get("name")
                self.phone = params.get("phone")
                self.user_type = int(params.get("type"))
                self.location = params.get('location')
            except Exception as e:
                logs.warning("Input params are invalid! [Details: %s]"%str(e))
                raise
        if not self.validate():
            logs.warning("Input params are invalid!")
            raise Exception("Input params are invalid!")

    def validate(self):
        """Write all validations on input values here!"""
        return True

    def extract_info(self, json_data):
        """Extract the data from json string"""
        self.email = json_data.get(u'email')
        self.name = json_data.get(u'name')
        self.phone = json_data.get(u'phone')
        self.friends = json.dumps(json_data.get(u'friends'))
        self.user_type = json_data.get(u'type')
        self.location = json_data.get(u'location')
