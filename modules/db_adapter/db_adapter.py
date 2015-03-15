from modules.models import User, Referral
from modules.utils.config import logs
from modules.utils import common

class DBAdapter:
    DATABASE='default'

    def __init__(self):
        pass

    def get_users_list(self):
        """Get the list of all the registered users in database"""
        return User.objects.all()

    def user_exist(self, email, phone_number):
        """Check if the user exists"""
        if self.get_user(email, phone_number):
            return True
        else:
            return False

    def get_user(self, email, phone_number):
        """Get the details of the user based on email id OR phone no"""
        try:
            ##return User.objects.using(self.DATABASE).filter(email=email).get() or \
            ##           User.objects.using(self.DATABASE).filter(phone=phone_number).get()
            return  User.objects.filter(email=email) or User.objects.filter(phone=phone_number)
        except Exception as e:
            logs.warning("Exception occured when quering to DB. [Details: %s]"%str(e))
            raise

    def create_user(self, user):
        """Create new registered user"""
        try:
            new_user = User(email=user.email,
            name=user.name,
            phone=user.phone,
            user_type=user.user_type)
            new_user.save()
            logs.info("New User is Registered Successfully! [Details: Name=%s,  email=%s,  phone=%s,  type=%s"
                %(user.name, user.email, user.phone, user.user_type))
            return new_user
        except Exception as e:
            logs.warning("Exception occured when quering to DB. [Details: %s]"%str(e))
            raise

    def get_friends_list(self):
        """Return the complete friend list"""
        pass

    def save_friends_list(self, user):
        """Save the friends list in string format to user table"""
        try:
            db_user = User.objects.filter(email=user.email).get()
            if db_user:
                db_user.friends_list = user.friends
                db_user.save()
        except Exception as e:
            logs.warning("Exception Occurred while saving the friends list. [Details: %s]"%str(e))


    def get_unvalidate_users(self):
        """Return the record set that will contains all the unvalidated user"""
        try:
            return User.objects.filter(validated=0)
        except Exception as e:
            logs.warning("Exception occurred while retrieving the unvalidated user list")

    def validate_user(self, user):
        """Validate the user"""
        user.validated = 1
        try:
            user.save()
        except Exception as e:
            logs.warning("Unknown exception occurred! [details: %s]"%str(e))


    def create_referral_id(self, user):
        """Create a new referral id and update the referral table"""
        try:
            referral_id = common.get_sha224_hex_digest('%s%s%s'%(user.name, user.email, user.phone))
            db_user = User.objects.filter(email=user.email).get()
            ref = Referral(user=db_user, referral_id=referral_id)
            ref.save()
        except Exception as e:
            logs.warning("Unknown exception has occurred while creating the referral id. [Details: %s]"\
                         %str(e))


    '''def get_referral_by_id(self, ref_id):
          return Referral.objects.using(self.DATABASE).filter(referral_id=ref_id).get()
        except Exception as e:
            return None

    def update_referral(self, ref_id, status):
        try:
            Referral.objects.using(self.DATABASE).filter(referral_id=ref_id).update(status=status)
        except Exception as e:
            pass

    def create_referral(self, user, ref_id):
        try:
            Referral.objects.using(self.DATABASE).create(user=user, referral_id=ref_id)
        except Exception as e:
            pass'''
