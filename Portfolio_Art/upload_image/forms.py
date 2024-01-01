from django import forms
from core.models import Post, Hashtag

class PostForm(forms.ModelForm):

    image = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'URL', 'class': 'form-control', 'id':'id_image'}))
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Título de la imagen', 'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Descripción', 'class': 'form-control', 'id':'description', 'rows':7, 'cols':45}))

    class Meta:
        model = Post
        fields = ['image', 'title', 'description']

class HashtagForm(forms.ModelForm):
    name_hashtag = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Hashtags', 'class': 'form-control', 'id':'hashtag', 'rows':7 , 'cols':45}))

    class Meta:
        model = Hashtag
        fields = ['name_hashtag']