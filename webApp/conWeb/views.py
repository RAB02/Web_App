from django.shortcuts import render, redirect
from django.contrib import messages
from .models import signUp, Tasks  # This is your model
from django.shortcuts import get_object_or_404


# Home page view
def home(request):
    return render(request, "base.html", {"signed_in": False})


# Sign in page view
def signIn(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = signUp.objects.get(email=email, password=password)
            request.session["user_id"] = user.id
            request.session["user_first_name"] = user.first_name
            return redirect("tasks")
        except signUp.DoesNotExist:
            messages.error(request, "Invalid email or password.")

    return render(request, "sign_in.html", {})
# def signIn(request):
#     if request.method == "POST":
#         email = request.POST.get("email")
#         password = request.POST.get("password")
#         if signUp.objects.filter(email=email).exists():
#             obj1 = signUp.objects.get(email=email)
#             obj2 = signUp.objects.filter(password=password)
#             print(obj1)
#             print(obj2)
#             if obj1 in obj2:
#                 print("Condition Met")
#                 return redirect("tasks")
#                 # return render(request, "base.html", {"signed_in": True})

#     return render(request, "sign_in.html", {})


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
            return redirect("register")

        if signUp.objects.filter(email=email).exists():
            return redirect("register")

        user = signUp(
            first_name=first_name, last_name=last_name, email=email, password=password
        )
        user.save()
        return redirect("home")

    return redirect("signup")

def tasks(request):
    user_id = request.session.get("user_id")
    user_first_name = request.session.get("user_first_name")

    if not user_id:
        return redirect("signin")  # Redirect if not logged in

    tasks = Tasks.objects.filter(user_id=user_id)

    if request.method == "POST":
        task_name = request.POST.get("task_name")
        description = request.POST.get("description")
        status = request.POST.get("status") == "on"
        due_date = request.POST.get("due_date")

        # Save new task
        task = Tasks(
            task_name=task_name,
            description=description,
            status=status,
            due_date=due_date,
            user_id=user_id,
        )
        task.save()
        return redirect("tasks")

    return render(request, "tasks.html", {
        "tasks": tasks,
        "user_first_name": user_first_name
    })

def mark_done(request, task_id):
    if request.method == "POST":
        user_id = request.session.get("user_id")
        task = get_object_or_404(Tasks, id=task_id, user_id=user_id)
        task.status = True
        task.save()
    return redirect("tasks")

def delete_task(request, task_id):
    if request.method == "POST":
        user_id = request.session.get("user_id")
        task = get_object_or_404(Tasks, id=task_id, user_id=user_id)
        task.delete()
    return redirect("tasks")

def logout_view(request):
    request.session.flush()  # Clears all session data
    return redirect("signin")
