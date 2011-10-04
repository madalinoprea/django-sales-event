from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Address(models.Model):
    pass

class CustomerProfile(models.Model):
    pass

class SignupRequest(models.Model):
    first_name = models.CharField(max_length=30, unique=True)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)

    # User address
    zip_code = models.PositiveSmallIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    approved_at = models.DateTimeField(null=True)


    def approve(self):
        user = User()
        user.first_name = self.first_name
        user.last_name = self.last_name
        user.email = self.email

        # TODO: create user profile

        self.approved_at = datetime.now()
        self.save()

    