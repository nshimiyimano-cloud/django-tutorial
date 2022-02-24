
from django import forms
from .models import Participant


class RegistrationForm(forms.ModelForm):
    class Meta:
        model=Participant
        fields=['email']  #to restrict field allowed to filled by visitor to infer django field to fill or will be displayed on form  this 'email' its from our participant fields
    