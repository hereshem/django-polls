
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from blogs.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["rate", "review"]


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class SigninForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]