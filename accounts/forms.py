from django import forms
from .models import Golfer, FavoriteGolfer

class FavoriteGolferForm(forms.ModelForm):
    class Meta:
        model = FavoriteGolfer
        fields = ['golfer', 'rank']
        widgets = {
            'rank': forms.NumberInput(attrs={'min': 1, 'max': 6}),
        }