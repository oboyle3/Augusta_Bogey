from django import forms
from .models import Golfer, FavoriteGolfer

class FavoriteGolferForm(forms.Form):
    golfers = forms.ModelMultipleChoiceField(
        queryset=Golfer.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="Select your top 6 golfers"
    )
    
    def clean_golfers(self):
        golfers = self.cleaned_data.get('golfers')
        if len(golfers) > 6:
            raise forms.ValidationError("You can only select 6")
        return golfers