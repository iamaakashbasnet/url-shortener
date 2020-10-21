from django import forms
from accounts.models import Account
from django.contrib.auth.forms import UserCreationForm


class AccountCreationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'username',
                  'email', 'password1', 'password2',)


class AccountUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'username',
                  'email',)
