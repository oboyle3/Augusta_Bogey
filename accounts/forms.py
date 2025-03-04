from django import forms
from .models import Golfer, FavoriteGolfer

class FavoriteGolferForm(forms.Form):
    golfers = forms.ModelMultipleChoiceField(
        queryset=Golfer.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    def __init__(self, *args, **kwargs):
        # Get the current user from kwargs
        user = kwargs.pop('user', None)  # Get the current user from the view
        super().__init__(*args, **kwargs)

        # Pre-select golfers that are already favorites for the user
        if user:
            self.fields['golfers'].initial = Golfer.objects.filter(
                favoritegolfer__user=user
            )
