from django.urls import path, include
from . import views

urlpatterns = [
	path('',views.home, name = 'home'),
	path('signIn/',views.signIn, name = 'signIn'),
	path('signUp/',views.signUp, name = 'signUp'),
    
]