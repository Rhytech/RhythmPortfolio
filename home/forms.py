from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30,help_text="Letters, digits and @/./+/-/_ only.")
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username:
            if User.objects.filter(username=username).exists():
                raise forms.ValidationError('Username already used.')
        return username
    email = forms.EmailField(max_length=200)
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('Email already used.')
        return email

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )