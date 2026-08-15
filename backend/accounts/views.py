from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, "accounts/register.html")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, "accounts/register.html")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return render(request, "accounts/register.html")

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Registration Successful!")
        print("User Created Successfully")
        return redirect("/login/")

    return render(request, "accounts/register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful!")
            return redirect("/dashboard/")
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "accounts/login.html")


@login_required
def dashboard(request):
    return render(request, "accounts/dashboard.html")

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect("/login/")

from .models import Project

def project_list(request):
    projects = Project.objects.all()
    return render(request, "projects.html", {"projects": projects})

def project_api(request):
    projects = Project.objects.all()

    data = []

    for project in projects:
        data.append({
            "project_name": project.project_name,
            "description": project.description,
            "status": project.status,
            "start_date": project.start_date.isoformat() if project.start_date else None,
            "end_date": project.end_date.isoformat() if project.end_date else None,
            "location": project.location,
            "budget": str(project.budget) if project.budget else None,
        })

    return JsonResponse(data, safe=False)