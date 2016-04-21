from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from datetime import date, datetime
from .forms import *
from .models import (User, Client, SubUser, Memory, Picture)


def login(request):
    return render(request, 'mainApp/login.html')


def authenticateLogin(request):
    context = {"error": "must provide a valid username and password"}
    form = AuthenticateForm(request.POST)

    if form.is_valid():
        try:
            user_name = form.cleaned_data.get('user_name')
            password = form.cleaned_data.get('password')
            current_user = User.objects.get(UserName=user_name,
                                            Password=password)
            print current_user
            try:
                client_user = Client.objects.get(User=current_user)
                return HttpResponseRedirect(
                    reverse('index', args=(current_user.id,)))
            except:
                # subuser_user = SubUser.objects.get(User=current_user)
                return HttpResponseRedirect(
                    reverse('profile', args=(current_user.id,)))
        except:
                return render(request, "mainApp/login.html", context)
    else:
        return render(request, "mainApp/login.html", context)

    # if request.method == 'POST':
    #     try:
    #         UserName = str(request.POST.get('username'))
    #         Password = str(request.POST.get('password'))
    #         current_user = User.objects.get(UserName=UserName,
    #                                         Password=password)
    #         try:
    #             client_user = Client.objects.get(User=current_user)
    #             print "counted as client"
    #             return HttpResponseRedirect(reverse('index',
    #                                                 args=(current_user.id,)))
    #         except:
    #             subuser_user = SubUser.objects.get(User=current_user)
    #             print "counted as subuser"
    #             return HttpResponseRedirect(reverse('profile',
    #                                                 args=(current_user.id,)))
    #     except:
    #         return render(request, "mainApp/login_register.html", context)
    # else:
    #     return render(request, "mainApp/login_register.html", context)
    # coaches = User.objects.filter(MMR__range=(minRange,maxRange)).filter(coach__server=server, coach__champion=hero)


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


def authenticateRegister(request):
    if request.is_ajax:
        response_error = "Error getting your info from the form."

        try:
            choice = request.GET.get('client_or_subuser')
            user_name = request.GET.get('user_name')
            password = request.GET.get('password')
            firstname = request.GET.get('firstname')
            lastname = request.GET.get('lastname')
            email = request.GET.get('email')
            birthdate_month = request.GET.get('birthdate_month')
            birthdate_day = request.GET.get('birthdate_day')
            birthdate_year = request.GET.get('birthdate_year')
            birthdate_str = str(birthdate_month + " " + birthdate_day + " " + birthdate_year)
            birthdate = datetime.strptime(birthdate_str, '%M %d %Y')
            print birthdate
            phone_number = request.GET.get('phone_number')
            address = request.GET.get('address')
            profile_picture = request.GET.get('profile_picture')
        except:
            return HttpResponse(response_error)

        # user = User(UserName=user_name, Email=email, Password=password,
        #             FirstName=firstname, LastName=lastname,
        #             BirthDate=birthdate, ProfilePicture=profile_picture,
        #             PhoneNumber=phone_number, HomeAddress=address,
        #             AboutMe="Add some info about yourself :)")
        #user.save()
        if choice == "Client":
            reference_id = "randomly generated id + 1234"
            #client = Client(User=user, Reference_ID=reference_id,CreatedOn=datetime.now())
            #client.save()
        elif choice == "Family_Friend":
            reference_id = request.GET.get('reference_id')

        else:
            print "nothing chosen"
        user_name_str = str(user_name)
        print user_name_str

        # key = r.json()
        # summonerNameValue = key[summonerName]["name"]
        # summonerId = str(key[summonerName]["id"])
        # r = requests.get('https://na.api.pvp.net/api/lol/na/v2.5/league/by-summoner/'+summonerId+'/entry?api_key=8340953c-a577-4057-bcfb-962e98780cb1')
        # summonerInfo = r.json()
        # summonerRank = (summonerInfo[summonerId][0]["tier"]).lower()
        # summonerDivision = summonerInfo[summonerId][0]['entries'][0]['division']
        #
        # rank = ""
        # for i in range(len(summonerRank)):
        #     if i==0:
        #         rank+=(summonerRank[0]).upper()
        #     else:
        #         rank+=summonerRank[i]
        #
        #         rank += " " + summonerDivision
        #         user = User(userid=userid, password=password, email=email, pname=pname, rank=rank, skypeid=skypeid, twitchid=twitchid)
        #         user.save()
        #         # context = {"value":summonerRank,
        #         #            "division":summonerDivision,
        #         #            "name":summonerNameValue}
        #         # return render(request, "authenticated.html", context)
        return HttpResponse(user_name_str)
    else:
        raise Http404
    pass


def index(request, user_id):
    current_user = User.objects.get(pk=user_id)
    client_user = Client.objects.get(User=current_user)
    list_subusers = SubUser.objects.filter(Client=client_user)
    list_friends = list_subusers.filter(RelationshipToClient="Friend")
    list_family_members = list_subusers.exclude(RelationshipToClient="Friend")
    # FavoritePeople = list_subusers.exclude(RelationshipToClient="Friend")
    # Favorite1 = FavoritePeople.filter(User=)
    context = {
        'client': client_user,
        'list_friends': list_friends,
        'list_family_members': list_family_members
    }
    return render(request, "mainApp/index.html", context)


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

        memory_list.append({
            'title': memory.Title,
            'description': memory.Description,
            'date': memory.Date,
            'pictures': pictures_list
        })

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
