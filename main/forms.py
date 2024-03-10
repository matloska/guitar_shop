# Contains forms

from django import forms
from django.contrib.auth.models import User

#User registration
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                         widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat the password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    #clean the password and compare
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('The entered passwords are not identical')
        return cd['password2']