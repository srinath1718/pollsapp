from django.db import models

class SignUpInfo(models.Model):
    username = models.CharField(max_length=50)
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)

    class Meta:
        db_table = "user_signup"

class UserProfile(models.Model):

    user_id = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    photo = models.CharField(max_length=2000,null=True, blank=True, default=None)

    class Meta:
        db_table = "profile"



