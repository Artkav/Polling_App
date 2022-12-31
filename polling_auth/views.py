from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout


# Create your views here.

@login_required
def profile(request):
    return render(request, "polling_auth/profile.html")


