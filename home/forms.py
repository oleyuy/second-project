from django import forms 
from django.core.exceptions import ValidationError
from .models import MyUser


class Loginform(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email...'}))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder':'Password...'}))


class RegisterForm(forms.Form):

    name = forms.CharField(min_length=3,max_length=15,widget=forms.TextInput(
        attrs={'placeholder':'Name...'}))

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder':'Email...'}))

    birth_year = forms.IntegerField(min_value=1900,max_value=2027,widget=forms.NumberInput(
        attrs={'placeholder':'Birth year...'}))

    password = forms.CharField(min_length=8,max_length=16,
        widget=forms.PasswordInput(
            attrs={'placeholder':'Password...'}))

    def clean_email(self):
        email = self.cleaned_data['email']

        if MyUser.objects.filter(email=email).exists():
            raise ValidationError("email already exists")

        return email
    def clean_name(self):
        name = self.cleaned_data['name']

        if MyUser.objects.filter(name=name).exists():
            raise ValidationError("username already taken")

        return name