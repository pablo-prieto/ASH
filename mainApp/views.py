from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.core.urlresolvers import reverse
from .models import User, Client, SubUser, Memory, Calendar, Picture, Video, SpecialPerson

# class IndexView(generic.DetailView):
#     model = User
#     template_name = 'mainApp/index.html'

def authenticate(request):
    context = {"error":"must provide a valid username and password"}
    if request.method == 'POST':
        try:
            UserName = str(request.POST.get('username'))
            Password = str(request.POST.get('password'))
            CurrentUser = User.objects.get(UserName=UserName, Password=Password)
            context = {'user':CurrentUser}
            return HttpResponseRedirect(reverse('index', args=(CurrentUser.id,)))
        except:
            return render(request, "mainApp/login_register.html", context)

    else:
        return render(request, "mainApp/login_register.html", context)
    #coaches = User.objects.filter(MMR__range=(minRange,maxRange)).filter(coach__server=server, coach__champion=hero)


def index(request, user_id):
    CurrentUser = User.objects.get(pk=user_id)
    context = {'user':CurrentUser}
    # context = {"error":"must provide a valid username and password"}
    # if request.method == 'POST':
    #     try:
    #         UserName = str(request.POST.get('username'))
    #         Password = str(request.POST.get('password'))
    #         CurrentUser = User.objects.get(UserName=UserName, Password=Password)
    #         context = {'user':CurrentUser}
    #     except:
    #         return render(request, "mainApp/login_register.html", context)
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
