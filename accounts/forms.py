from django import forms
from django.contrib.auth.forms import UserCreationForm

from authentication.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','first_name', 'last_name', 'institute', 'phone']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model= User
        fields = ['first_name', 'last_name', 'phone']
