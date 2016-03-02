from django.http import HttpResponse
from django.shortcuts import render
from .models import SubUser


def index(request):
    return render(request, 'mainApp/index.html')


def login(request):
    return render(request, 'mainApp/login_register.html')


def profile(request):
    return render(request, 'mainApp/profile.html')


def detail(request, user_id):
    return HttpResponse("You're looking at user %s." % user_id)


def results(request, user_id):
    response = "You're looking at the results of user %s."
    return HttpResponse(response % user_id)


def vote(request, user_id):
    return HttpResponse("You're voting on user %s." % user_id)
