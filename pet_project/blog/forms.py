from django import forms 
from .models import Post, Profile

class Search_Post_Form(forms.ModelForm):
    username = forms.CharField(label='search_post', widget=forms.TextInput(attrs={'class': 'form-input'})),
    class Meta:
        model = Post
        fields = ('title',)
    

class ProfileForm(forms.ModelForm):
    biography = forms.CharField(label='biography', widget=forms.TextInput(attrs={'class': 'form-input'})),
    class Meta:
        model = Profile
        fields = ('biography',)

