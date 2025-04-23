# from django.urls import path, include
# from . import views

# urlpatterns = [
# 	path('',views.home, name = 'home'),
# 	path('signIn/',views.signIn, name = 'signIn'),
# 	path('signUp/',views.signUp, name = 'signUp'),
#     path('accounts/register', views.register, name='register'),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("accounts/signin", views.signIn, name="signin"),
    path("accounts/signup", views.signUpPage, name="signup"),  # renamed here
    path("accounts/register", views.register, name="register"),
    path("accounts/tasks", views.tasks, name="tasks"),
]

