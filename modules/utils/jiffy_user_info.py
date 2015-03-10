from modules.utils.config import logs

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

    def __init__(self, params):
        """Get the user basic info from the httpRequest params"""
        try:
            self.email = params.get("email")
            self.name = params.get("name")
            self.phone = params.get("phone")
            self.user_type = int(params.get("type"))
            #self.location = params.get('location')
            self.location="pune"
        except Exception as e:
            logs.warning("Input params are invalid! [Details: %s]"%str(e))
            raise
        if not self.validate():
            logs.warning("Input params are invalid!")
            raise Exception("Input params are invalid!")

    def validate(self):
        """Write all validations on input values here!"""
        return True
