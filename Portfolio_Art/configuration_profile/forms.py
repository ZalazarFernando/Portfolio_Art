from core.models import User
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import PasswordChangeForm

class NicknameForm(forms.ModelForm):
    nickname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['nickname']

    def clean_nickname(self):
        nickname = self.cleaned_data.get('nickname')
        existing_user = User.objects.filter(nickname=nickname).exclude(id=self.instance.id)

        if existing_user.exists():
            raise ValidationError('Este nickname ya está en uso. Por favor, elige otro.')

        return nickname

class ImageUserForm(forms.ModelForm):
    image = forms.CharField(widget=forms.TextInput(attrs={'class':'forms-control'}))

    class Meta:
        model = User
        fields = ['image']