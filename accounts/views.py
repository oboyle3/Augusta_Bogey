from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Golfer, FavoriteGolfer
from .forms import FavoriteGolferForm
from django.core.exceptions import ObjectDoesNotExist

#Here we are using djangos's built in authentication to handle form login, this form will handle authentication
def login_view(request):
    form = AuthenticationForm
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('accounts:dashboard') #Redirect to home after successful login
        else:
            form = AuthenticationForm
        
        
    return render(request, 'accounts/login.html', {'form':form})
    
#Here we create a simple sign up form
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') #Redirect to the login page after sign up
    else:
        form = UserCreationForm


    return render(request, 'accounts/signup.html', {'form': form})


@login_required
def dashboard(request):
    golfers = Golfer.objects.all()
    favorite_golfers = FavoriteGolfer.objects.filter(user=request.user)# Get the user's favorite golfers
    print(golfers)
    # If you want to limit to the top 6, you can slice the query:
    top_favorite_golfers = favorite_golfers[:6]  # Get only the first 6 favorite golfers (if there are more)

    return render(request, 'accounts/dashboard.html', {
        'golfers': golfers,
        'favorite_golfers': top_favorite_golfers,  # Pass the top favorite golfers to the template
    })
    

    
@login_required
def select_favorite_golfers(request):
    golfers = Golfer.objects.all()  # All golfers available for selection

    if request.method == 'POST':
        form = FavoriteGolferForm(request.POST, user=request.user)  # Pass the user to the form
        
        if form.is_valid():
            selected_golfers = form.cleaned_data['golfers']  # Get the selected golfers

            # Get the user's current favorite golfers
            current_favorites = FavoriteGolfer.objects.filter(user=request.user)

            # Add new favorites
            for golfer in selected_golfers:
                # Check if the golfer is not already a favorite
                if not current_favorites.filter(golfer=golfer).exists():
                    FavoriteGolfer.objects.create(user=request.user, golfer=golfer)

            # Remove any golfers that were previously favorites but are no longer selected
            for favorite in current_favorites:
                if favorite.golfer not in selected_golfers:
                    favorite.delete()

            return redirect('accounts:dashboard')  # Redirect to dashboard after saving
    else:
        form = FavoriteGolferForm(user=request.user)  # Pass the user to the form

    return render(request, 'accounts/select_favorite_golfers.html', {
        'form': form,
        'golfers': golfers
    })
