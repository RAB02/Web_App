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
    path("signin", views.signIn, name="signin"),
    path("signup", views.signUpPage, name="signup"),  # renamed here
    path("register", views.register, name="register"),
    path("tasks", views.tasks, name="tasks"),
    path("tasks/<int:task_id>/done", views.mark_done, name="mark_done"),
    path("tasks/<int:task_id>/delete", views.delete_task, name="delete_task"),
    path("logout", views.logout_view, name="logout"),
]

