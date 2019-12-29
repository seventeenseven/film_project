from django import forms
from .models import *


class AddFilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'release_date', 'cover_image', 'category', 'country', 'description']


class AddDirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = ['first_name', 'last_name', 'film']


class FilmUpdateForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'release_date', 'description','cover_image', 'country', 'category']


class DirectorUpdateForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = ['first_name', 'last_name']


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['content', 'rating']
