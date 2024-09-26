from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib.auth import authenticate, login


# Create your views here.
def register(request):
    if request.method == "GET":
        # form = UserCreationForm()
        form = RegisterForm()
        context = {
            "form": form
        }
        return render(request, "register/register.html", context=context)
    elif request.method == "POST":
        # form = UserCreationForm(request.POST)
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

            # LOGIN THE USER
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")

            user = authenticate(username=username, password=password)

            if user:
                login(request, user)

            return redirect("/")