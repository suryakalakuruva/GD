from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# Form for Sign up
class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()


	class Meta:
		model = User
		fields = ['username', 'email','password1','password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

# Form for profile update
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','cover','worked','studied','company','lives','Home']