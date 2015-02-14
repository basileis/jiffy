from modules.models import User, Referral
from modules.utils.config import logs

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
