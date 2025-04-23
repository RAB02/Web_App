from django.shortcuts import render, redirect
from django.contrib import messages
from .models import signUp, Tasks  # This is your model


# Home page view
def home(request):
    return render(request, "base.html", {"signed_in": False})


# Sign in page view
def signIn(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        if signUp.objects.filter(email=email).exists():
            obj1 = signUp.objects.get(email=email)
            obj2 = signUp.objects.filter(password=password)
            print(obj1)
            print(obj2)
            if obj1 in obj2:
                print("Condition Met")
                return render(request, "base.html", {"signed_in": True})

    return render(request, "sign_in.html", {})


# ✅ Sign up page view — RENAMED to avoid conflict
def signUpPage(request):
    return render(request, "sign_up.html")


# Register POST handler
def register(request):
    if request.method == "POST":
        print(request.POST)
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("/accounts/register")

        if signUp.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect("/accounts/register")

        user = signUp(
            first_name=first_name, last_name=last_name, email=email, password=password
        )
        user.save()
        return redirect("home")

    return redirect("/accounts/signup")


def tasks(request):
    return render(request, "tasks.html")
