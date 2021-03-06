from django import forms 
from .models import Post, Profile, Comment
from django.contrib.auth.models import User


class Search_Post_Form(forms.ModelForm):
    title = forms.CharField(label='title', widget=forms.TextInput(attrs={'class': 'form-input'})),
    class Meta:
        model = Post
        fields = ('title',)
    

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('biography', 'photo')

class CommentForm(forms.ModelForm):
    content = forms.CharField(label='content', widget=forms.TextInput(attrs={'class': 'form-input'}))
    class Meta:
        model = Comment
        fields = ('content',)

