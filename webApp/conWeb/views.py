from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html", {})

def signIn(request):
    return render(request, "sign_in.html", {})

def signUp(request):
    return render(request, "sign_up.html", {})