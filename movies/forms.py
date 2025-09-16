from django import forms
from .models import MovieRequest

class MovieRequestForm(forms.ModelForm):
    class Meta:
        model = MovieRequest
        fields = ['movie_name', 'movie_description']
        widgets = {
            'movie_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter movie name',
                'required': True
            }),
            'movie_description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter movie description',
                'rows': 4,
                'required': True
            })
        }
        labels = {
            'movie_name': 'Movie Name',
            'movie_description': 'Movie Description'
        }
