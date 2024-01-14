from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from . import views
from django.http import HttpResponse
from django.contrib import messages


# Create your views here.
def Register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # check if passwords match
        if password1 != password2:
            error_message = "passwords does not match. please use a common password"
            return render(
                request,
                "authentication/register.html",
                {"error_message": error_message},
            )

        # check if username already exists
        if User.objects.filter(username=username).exists():
            error_message = "The user exists. please login!"
            return render(
                request,
                "authentication/register.html",
                {"error_message": error_message},
            )

        # check if the email is already reister to another account
        if User.objects.filter(email=email).exists():
            error_message = "the email address is registered to another account"
            return render(
                request,
                "authentication/register.html",
                {"error_message": error_message},
            )

        # create the user
        new_user = User.objects.create_user(
            username=username, email=email, password=password1
        )
        new_user.username = username
        new_user.save()

        messages.success = (request, "The Account successsfully Create")
        return redirect("authentication:login")
    return render(request, "authentication/register.html", {})


def Login(request):
    error_message = None
    if request.method == "POST":
        username = request.POST.get("fname")
        password = request.POST.get("pwd")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect("homepage:mainpage")

        else:
            error_message = "Error! The User Does Not Exist"

    return render(
        request, "authentication/login.html", {"error_message": error_message}
    )
