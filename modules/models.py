from django.db import models

class User(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False)
    email = models.CharField(max_length=64, null=False, blank=False)
    phone = models.CharField(max_length=32, null=False, blank=False)
    validated = models.BooleanField(default=False)
    location = models.CharField(max_length=64, null=True, blank=True)
    description = models.CharField(max_length=640, null=True, blank=True)
    user_type = models.IntegerField(default=-1, null=False, blank=False)
    referral_id = models.CharField(max_length=32, null=True, blank=True)
    friends_list = models.CharField(max_length=1024, null=True, blank=True)
    contacted = models.BooleanField(default=False)
    answered = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'user'

class Referral(models.Model):
    user = models.ForeignKey('User')
    referral_id = models.CharField(max_length=64L)
    status = models.IntegerField(default=0)
    class Meta:
        db_table = 'referral'
