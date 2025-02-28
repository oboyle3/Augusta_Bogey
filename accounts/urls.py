from django.urls import path
from . import views
app_name = 'accounts' #This registers the namespace for the app
#created url pattern for login view
urlpatterns = [
    path('login/', views.login_view,name='login'),
    path('signup/', views.signup,name='signup'), #Sign up URL
    path('dashboard/' , views.dashboard, name='dashboard'), #Dashboard URL this will create the route accounts/dashboard/
    path('logout/', views.logout_view, name='logout'),
]