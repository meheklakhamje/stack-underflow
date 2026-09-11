from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import RegisterForm
from .models import Question


def home(request):
    questions = Question.objects.all()

    return render(request, "home.html", {"questions": questions})


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()

            return redirect("home")
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})