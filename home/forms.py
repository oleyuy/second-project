from django import forms 


class Loginform(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email...'}))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder':'Password...'}))


class RegisterForm(forms.Form):
   None
#дописать логику