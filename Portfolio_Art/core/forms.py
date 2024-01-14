from .models import Board, Comments
from django import forms

class BoardForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Nombre de tablero', 'class':'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Descripción del tablero', 'class':'form-control', 'rows':7, 'cols':75}))

    class Meta:
        model = Board
        fields = ['name', 'description']

class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Escribe tu comentario', 'name':'field-comment', 'class':'form-control', 'rows':7, 'cols':45}))
    
    class Meta:
        model = Comments
        fields = ['comment']