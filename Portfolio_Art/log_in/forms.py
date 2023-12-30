from django import forms
from django.contrib.auth.forms import AuthenticationForm
from core.models import User

class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'password']
