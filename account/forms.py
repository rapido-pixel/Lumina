from django import forms
from django.contrib.auth.models import User
from django.forms import FileInput

from .models import Profile


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords don't match.")
        return cd['password2']


class UserEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    photo = forms.ImageField(label='Select Profile Image', required=False, widget=FileInput)

    class Meta:
        model = Profile
        fields = ('about', 'photo', 'link')
        widgets = {'about': forms.Textarea(attrs={'rows': 4, 'cols': 15})}
