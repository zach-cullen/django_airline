from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def index(request):
  if not request.user.is_authenticated:
    return HttpResponseRedirect(reverse("users:login"))

  return render(request, "users/index.html", {
    "users": User.objects.all()
  })

def login_view(request):
  # POST
  if request.method == "POST":
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return HttpResponseRedirect(reverse("users:index"))
    else:
      return render(request, "users/login.html", {
        "message": "Invalid Credentials."
      })
  
  # GET
  return render(request, "users/login.html")

def logout_view(request):
  logout(request)
  return render(request, "users/login.html", {
    "message": "You have been logged out"
  })
