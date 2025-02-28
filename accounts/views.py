from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirects

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

#Use the login_required decorator to ensure only authnticated users can access the page
@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')





    
