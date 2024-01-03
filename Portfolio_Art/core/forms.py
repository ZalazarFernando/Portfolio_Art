from .models import Board
from django import forms

class BoardForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Nombre de tablero', 'class':'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Descripción del tablero', 'class':'form-control', 'rows':7, 'cols':45}))

    class Meta:
        model = Board
        fields = ['name', 'description']
