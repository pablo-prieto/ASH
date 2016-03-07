from django.http import HttpResponse
from django.shortcuts import render
from .models import User, Client, SubUser, Memory, Calendar, Picture, Video, SpecialPeople


def index(request):
    AllUsers = User.objects.all()
    context = {'users':AllUsers}
    #coaches = User.objects.filter(MMR__range=(minRange,maxRange)).filter(coach__server=server, coach__champion=hero)
    return render(request, "mainApp/index.html", context)


def login(request):
    return render(request, 'mainApp/login_register.html')


def profile(request):
    AllUsers = User.objects.all()
    subuser1 = SubUser.objects.all()
    # for subuser in subuser1:
    #     subuser1id = subuser1.id
    #subuser1id = subuser1.id
    Memories = Memory.objects.all()
    FirstPicture = Picture.objects.all()
    context = {'users':AllUsers, 'memories':Memories, 'picture':FirstPicture}
    return render(request, 'mainApp/profile.html', context)


def detail(request, user_id):
    return HttpResponse("You're looking at user %s." % user_id)


def results(request, user_id):
    response = "You're looking at the results of user %s."
    return HttpResponse(response % user_id)


def vote(request, user_id):
    return HttpResponse("You're voting on user %s." % user_id)
