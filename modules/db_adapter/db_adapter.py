from modules.models import User, Referral

class DBAdapter:
    DATABASE='default'

    def __init__(self):
        pass

    def get_users_list(self):
       """Get the list of all the registered users in database"""
       return User.objects.all()

    def get_user(self, email, phone_number):
        try:
            return User.objects.using(self.DATABASE).filter(email=email, phone=phone_number).get()
        except Exception as e:
            return None

    def create_user(self, data):
        """Create new registered user"""
        try:
            new_user = User(email=data.get("email")[0], 
            name =data.get("name")[0],
            phone = data.get("phone")[0],
            user_type = int(data_get("type")[0]))

            return new_user 

        except Exception as e:
            return None

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
