from django import forms
from django.contrib.auth.models import User
#from bootstrap_toolkit.widgets import BootstrapDateInput, BootstrapTextInput, BootstrapUneditableInput


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label="UserName",
        error_messages={'required': 'Please enter username'},
        widget=forms.TextInput(
            attrs={
                'placeholder': "Username",
            }
        ),
    )
    password = forms.CharField(
        required=True,
        label="Password",
        error_messages={'required': "Please Enter Password"},
        widget=forms.PasswordInput(
            attrs={
                'placeholder': "Password",
            }
        ),
    )

    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError("Username and Password Required.")
        else:
            cleaned_data = super(LoginForm, self).clean()

class RegisterForm(forms.Form):
    username = forms.CharField(
        required=True,
        label="UserName",
        error_messages={'required': 'Please enter username'},
        widget=forms.TextInput(
            attrs={
                'placeholder': "Username",
            }
        ),
    )
    password = forms.CharField(
        required=True,
        label="Password",
        error_messages={'required': "Please Enter Password"},
        widget=forms.PasswordInput(
            attrs={
                'placeholder': "Password",
            }
        ),
    )

    email = forms.CharField(
        required=True,
        label="Email",
        error_messages={'required': 'Please enter email'},
        widget=forms.TextInput(
            attrs={
                'placeholder': "Email",
            }
        ),
    )


    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError("Username and Password Required.")
        else:
            cleaned_data = super(RegisterForm, self).clean()