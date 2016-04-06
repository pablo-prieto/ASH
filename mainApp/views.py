from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.core.urlresolvers import reverse
from .models import User, Client, SubUser, Memory, Calendar, Picture, Video, SpecialPerson
from datetime import date

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
            try:
                ClientUser = Client.objects.get(User=CurrentUser)
                print "counted as client"
                return HttpResponseRedirect(reverse('index', args=(CurrentUser.id,)))
            except:
                SubUserUser = SubUser.objects.get(User=CurrentUser)
                print "counted as subuser"
                return HttpResponseRedirect(reverse('profile', args=(CurrentUser.id,)))
        except:
            return render(request, "mainApp/login_register.html", context)
    else:
        return render(request, "mainApp/login_register.html", context)
    #coaches = User.objects.filter(MMR__range=(minRange,maxRange)).filter(coach__server=server, coach__champion=hero)


def index(request, user_id):
    CurrentUser = User.objects.get(pk=user_id)
    ClientUser = Client.objects.get(User=CurrentUser)
    ListOfSubUsers = SubUser.objects.filter(Client=ClientUser)
    ListOfFriends = ListOfSubUsers.filter(RelationshipToClient="Friend")
    ListOfFamilyMembers = ListOfSubUsers.exclude(RelationshipToClient="Friend")
    # FavoritePeople = ListOfSubUsers.exclude(RelationshipToClient="Friend")
    # Favorite1 = FavoritePeople.filter(User=)
    context = {'client': ClientUser, 'ListOfFriends': ListOfFriends, 'ListOfFamilyMembers': ListOfFamilyMembers}
    # coaches = User.objects.filter(MMR__range=(minRange,maxRange)).filter(coach__server=server, coach__champion=hero)
    return render(request, "mainApp/index.html", context)


def login(request):
    return render(request, 'mainApp/login_register.html')


def profile(request, user_id):
    CurrentUser = User.objects.get(pk=user_id)
    SubUserUser = SubUser.objects.get(User=CurrentUser)
    SubUserClient = SubUserUser.Client
    Today = date.today()
    BirthDate = SubUserUser.User.BirthDate
    Age = Today.year - BirthDate.year - ((Today.month, Today.day) < (BirthDate.month, BirthDate.day))
    ProfilePic = SubUserUser.User.ProfilePicture

    spec_filter_mem = {'SubUser':user_id}
    Memories = Memory.objects.filter(**spec_filter_mem)

    memory_list = []
    for memory in Memories:
        spec_filter_pic = {'Memory':memory}
        Pictures = Picture.objects.filter(**spec_filter_pic)
        pictures_list = []
        for picture in Pictures:
            pictures_list.append(picture.Picture)
        memory_list.append({'title':memory.Title, 'description':memory.Description, 'date':memory.Date, 'pictures':pictures_list})


    Pictures = Picture.objects.all()
    context = {'subuser':SubUserUser, 'subuserclient':SubUserClient, 'Age':Age, 'ProfilePicture':ProfilePic, 'memories':memory_list,}
    return render(request, 'mainApp/profile.html', context)


def detail(request, user_id):
    return HttpResponse("You're looking at user %s." % user_id)


def results(request, user_id):
    response = "You're looking at the results of user %s."
    return HttpResponse(response % user_id)


def vote(request, user_id):
    return HttpResponse("You're voting on user %s." % user_id)
