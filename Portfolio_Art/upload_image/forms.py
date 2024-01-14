from django import forms
from core.models import Post

class PostForm(forms.ModelForm):

    image = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'URL', 'class': 'form-control', 'id':'id_image'}))
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Título de la imagen', 'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Descripción', 'class': 'form-control form-textarea', 'id':'description', 'rows':7, 'cols':45}))
    hashtag = forms.CharField(widget=forms.Textarea(attrs={'placesholder':'Hashtags', 'class':'form-control form-textarea', 'id':'hashtags', 'row':7, 'cols':45}))

    class Meta:
        model = Post
        fields = ['image', 'title', 'description']