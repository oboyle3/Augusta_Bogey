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
    #fetch all the golfers from the database
    golfers = Golfer.objects.all()
    favorite_golfers = FavoriteGolfer.objects.filter(user=request.user)
    #favoriteGolfer = None
    print(golfers)
    #get the current users fav golfer
    #try:
    #    favorite_golfer = FavoriteGolfer.objects.get(user=request.user)
   # except FavoriteGolfer.DoesNotExist:
     #   favorite_golfer = None


    #pass the golfers to the template
    return render(request, 'accounts/dashboard.html', {
        'golfers': golfers,
        'favorite_golfer': favorite_golfers #Pass the favorite golfer to the template    
    })
    


@login_required
def select_favorite_golfers(request):
    # Get the golfers from the database
    golfers = Golfer.objects.all()

    if request.method == 'POST':
        form = FavoriteGolferForm(request.POST)
        
        if form.is_valid():
            # Get the selected golfers from the form
            selected_golfers = form.cleaned_data['golfers']

            # Delete the existing favorite golfers for the user
            FavoriteGolfer.objects.filter(user=request.user).delete()

            # Save the new favorite golfers
            for golfer in selected_golfers:
                FavoriteGolfer.objects.create(user=request.user, golfer=golfer)

            return redirect('dashboard')  # Redirect back to the dashboard after saving
    else:
        form = FavoriteGolferForm()

    return render(request, 'accounts/select_favorite_golfers.html', {
        'form': form,
        'golfers': golfers
    })           



    
