from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.core.urlresolvers import reverse
from datetime import date
from .forms import *
from .models import (User, Client, SubUser, Memory, Calendar,
                     Picture, Video, SpecialPerson)


def authenticateLogin(request):
    context = {"error": "must provide a valid username and password"}
    form = AuthenticateForm(request.POST)
    print form

    if form.is_valid():
        try:
            UserName = form.cleaned_data.get('user_name')
            Password = form.cleaned_data.get('password')
            print UserName
            print Password
            CurrentUser = User.objects.get(
                UserName=UserName, Password=Password)

            try:
                ClientUser = Client.objects.get(User=CurrentUser)
                print "counted as client"
                return HttpResponseRedirect(
                    reverse('index', args=(CurrentUser.id,)))
            except:
                SubUserUser = SubUser.objects.get(User=CurrentUser)
                print "counted as subuser"
                return HttpResponseRedirect(
                    reverse('profile', args=(CurrentUser.id,)))
        except:
                return render(request, "mainApp/login.html", context)
    else:
        return render(request, "mainApp/login.html", context)

    # if request.method == 'POST':
    #     try:
    #         UserName = str(request.POST.get('username'))
    #         Password = str(request.POST.get('password'))
    #         CurrentUser = User.objects.get(UserName=UserName, Password=Password)
    #         try:
    #             ClientUser = Client.objects.get(User=CurrentUser)
    #             print "counted as client"
    #             return HttpResponseRedirect(reverse('index', args=(CurrentUser.id,)))
    #         except:
    #             SubUserUser = SubUser.objects.get(User=CurrentUser)
    #             print "counted as subuser"
    #             return HttpResponseRedirect(reverse('profile', args=(CurrentUser.id,)))
    #     except:
    #         return render(request, "mainApp/login_register.html", context)
    # else:
    #     return render(request, "mainApp/login_register.html", context)
    # coaches = User.objects.filter(MMR__range=(minRange,maxRange)).filter(coach__server=server, coach__champion=hero)



def authenticateRegister(request):
    return
    # if request.is_ajax:
    #     response_error = "Error getting your info from the form."
    #
    #     try:
    #         userid = request.GET.get('userid')
    #         password = request.GET.get('password')
    #         email = request.GET.get('email')
    #         pname = request.GET.get('pname')
    #         skypeid = request.GET.get('skypeid')
    #         twitchid = request.GET.get('twitchid')
    #     except:
    #         return HttpResponse(response_error)
    #
    #     try:
    #         login_userid = User.objects.get(userid=userid)
    #         return HttpResponse('input_error1')
    #     except:
    #         pass
    #     try:
    #         login_userid = User.objects.get(email=email)
    #         return HttpResponse('input_error2')
    #     except:
    #         pass
    #     try:
    #         login_userid = User.objects.get(pname=pname)
    #         return HttpResponse('input_error3')
    #     except:
    #         pass
    #     try:
    #         login_userid = User.objects.get(skypeid=skypeid)
    #         return HttpResponse('input_error4')
    #     except:
    #         pass
    #     try:
    #         login_userid = User.objects.get(twitchid=twitchid)
    #         return HttpResponse('input_error5')
    #     except:
    #         pass
    #
    #     summonerName = str(pname)
    #     r = requests.get('https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/'+summonerName+'?api_key=8340953c-a577-4057-bcfb-962e98780cb1')
    #     if r.status_code == 404:
    #         return HttpResponse("404")
    #     elif r.status_code == 400:
    #         return HttpResponse("400")
    #     elif r.status_code == 401:
    #         return HttpResponse("401")
    #     elif r.status_code == 429:
    #         return HttpResponse("429")
    #     elif r.status_code == 500:
    #         return HttpResponse("500")
    #     elif r.status_code == 503:
    #         return HttpResponse("503")
    #     else:
    #         key = r.json()
    #         summonerNameValue = key[summonerName]["name"]
    #         summonerId = str(key[summonerName]["id"])
    #         r = requests.get('https://na.api.pvp.net/api/lol/na/v2.5/league/by-summoner/'+summonerId+'/entry?api_key=8340953c-a577-4057-bcfb-962e98780cb1')
    #         summonerInfo = r.json()
    #         summonerRank = (summonerInfo[summonerId][0]["tier"]).lower()
    #         summonerDivision = summonerInfo[summonerId][0]['entries'][0]['division']
    #
    #         rank = ""
    #         for i in range(len(summonerRank)):
    #             if i==0:
    #                 rank+=(summonerRank[0]).upper()
    #             else:
    #                 rank+=summonerRank[i]
    #
    #         rank += " " + summonerDivision
    #         user = User(userid=userid, password=password, email=email, pname=pname, rank=rank, skypeid=skypeid, twitchid=twitchid)
    #         user.save()
    #         # context = {"value":summonerRank,
    #         #            "division":summonerDivision,
    #         #            "name":summonerNameValue}
    #         # return render(request, "authenticated.html", context)
    #     return HttpResponse(userid)
    # else:
    #     raise Http404
    # pass



def index(request, user_id):
    CurrentUser = User.objects.get(pk=user_id)
    ClientUser = Client.objects.get(User=CurrentUser)
    ListOfSubUsers = SubUser.objects.filter(Client=ClientUser)
    ListOfFriends = ListOfSubUsers.filter(RelationshipToClient="Friend")
    ListOfFamilyMembers = ListOfSubUsers.exclude(RelationshipToClient="Friend")
    # FavoritePeople = ListOfSubUsers.exclude(RelationshipToClient="Friend")
    # Favorite1 = FavoritePeople.filter(User=)
    context = {'client': ClientUser, 'ListOfFriends': ListOfFriends,
               'ListOfFamilyMembers': ListOfFamilyMembers}
    # coaches = User.objects.filter(MMR__range=(minRange,maxRange)).filter(coach__server=server, coach__champion=hero)
    return render(request, "mainApp/index.html", context)


def login(request):
    return render(request, 'mainApp/login.html')


def register(request):
    form = RegistrationForm(request.POST)
    # if form.is_valid():
    #     user_name = form.cleaned_data.get('user_name')
    #     # password = form.cleaned_data.get('password')
    #     # email = form.cleaned_data.get('email')
    #     # firstname = form.cleaned_data.get('firstname')
    #     # lastname = form.cleaned_data.get('lastname')
    # else:
    #     print "Invalid form"
    context = {"form": form}
    return render(request, "register.html", context)


def profile(request, user_id):
    current_user = User.objects.get(pk=user_id)
    subuser_user = SubUser.objects.get(User=current_user)
    client_user = subuser_user.Client
    today = date.today()
    birthdate = subuser_user.User.BirthDate
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

    spec_filter_mem = {'SubUser': subuser_user}
    memories = Memory.objects.filter(**spec_filter_mem)
    memory_list = []

    for memory in memories:
        spec_filter_pic = {'Memory': memory}
        pictures = Picture.objects.filter(**spec_filter_pic)
        pictures_list = []
        for picture in pictures:
            pictures_list.append(picture.Picture)
        memory_list.append({'title': memory.Title, 'description': memory.Description, 'date': memory.Date, 'pictures': pictures_list})

    context = {
        'subuser_firstname': current_user.FirstName,
        'subuser_lastname': current_user.LastName,
        'subuser_profile_picture': current_user.ProfilePicture,
        'subuser_age': age,
        'subuser_aboutme': current_user.AboutMe,
        'subuser_relationship': subuser_user.RelationshipToClient,
        'client_firstname': client_user.User.FirstName,
        'client_lastname': client_user.User.LastName,
        'memories': memory_list
    }

    return render(request, 'mainApp/profile.html', context)


def detail(request, user_id):
    return HttpResponse("You're looking at user %s." % user_id)


def results(request, user_id):
    response = "You're looking at the results of user %s."
    return HttpResponse(response % user_id)


def vote(request, user_id):
    return HttpResponse("You're voting on user %s." % user_id)
