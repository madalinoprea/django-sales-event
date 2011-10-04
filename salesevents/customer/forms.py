from django import forms
from salesevents.customer.models import SignupRequest

__author__ = 'madalinoprea'

class SignupRequestForm(forms.ModelForm):
    class Meta:
        model = SignupRequest