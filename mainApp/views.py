from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from datetime import date, datetime
from .forms import *
from .models import (User, Client, SubUser, Memory, Picture)
from django.conf import settings
import json


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
            try:
                client_user = Client.objects.get(User=current_user)
                return HttpResponseRedirect(
                    reverse('index', args=(current_user.id,)))
            except:
                return HttpResponseRedirect(
                    reverse('profile', args=(current_user.id,)))
        except:
                return render(request, "mainApp/login.html", context)
    else:
        return render(request, "mainApp/login.html", context)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        response_error = "Error getting your info from the form."
        print "method is post"
        if form.is_valid():
            print "form valid"
            try:
                choice = request.POST.get('client_or_subuser')
                user_name = request.POST.get('user_name')
                password = request.POST.get('password')
                firstname = request.POST.get('firstname')
                lastname = request.POST.get('lastname')
                email = request.POST.get('email')
                birthdate_month = request.POST.get('birthdate_month')
                birthdate_day = request.POST.get('birthdate_day')
                birthdate_year = request.POST.get('birthdate_year')
                birthdate_str = str(birthdate_month + " " + birthdate_day + " " + birthdate_year)
                birthdate = datetime.strptime(birthdate_str, '%M %d %Y')
                phone_number = request.POST.get('phone_number')
                address = request.POST.get('address')
                try:
                    profile_picture = request.FILES['profile_picture']
                    with open(settings.BASE_DIR + "/static_in_env/media_root/Profile_Pictures/" + profile_picture.name, 'wb+') as destination:
                        for chunk in profile_picture.chunks():
                            destination.write(chunk)
                except:
                    profile_picture = ""

            except:
                return HttpResponse(response_error)

            user = User(UserName=user_name, Email=email, Password=password,
                        FirstName=firstname, LastName=lastname,
                        BirthDate=birthdate, ProfilePicture=profile_picture,
                        PhoneNumber=phone_number, HomeAddress=address,
                        AboutMe="Add some info about yourself :)")
            # Need to implement check for empty values.
            user.save()
            if choice == "Client":
                reference_id = "abc1234"
                client = Client(User=user, Reference_ID=reference_id)
                client.save()
            elif choice == "Family_Friend":
                reference_id = request.POST.get('reference_id')
                relationship_to_client = request.POST.get('relationship_to_client')
                try:
                    client = Client.objects.get(Reference_ID=reference_id)
                    subuser = SubUser(RelationshipToClient=relationship_to_client, User=user, Client=client)
                    subuser.save()
                except:
                    HttpResponse("Wrong Reference ID")
            else:
                print "nothing chosen"
            user_name_str = user.FirstName
            # print user_name_str

            return HttpResponse(user_name_str)
    else:
        form = RegistrationForm()
    context = {"form": form}
    return render(request, "register.html", context)


def authenticateRegister(request):
    if request.is_ajax:
        response_error = "Error getting your info from the form."

        try:
            choice = request.POST.get('client_or_subuser')
            user_name = request.POST.get('user_name')
            password = request.POST.get('password')
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            email = request.POST.get('email')
            birthdate_month = request.POST.get('birthdate_month')
            birthdate_day = request.POST.get('birthdate_day')
            birthdate_year = request.POST.get('birthdate_year')
            birthdate_str = str(birthdate_month + " " + birthdate_day + " " + birthdate_year)
            birthdate = datetime.strptime(birthdate_str, '%M %d %Y')
            phone_number = request.POST.get('phone_number')
            address = request.POST.get('address')
            try:
                profile_picture = request.FILES['profile_picture']
                with open(settings.BASE_DIR + "/static_in_env/media_root/Profile_Pictures/" + profile_picture.name, 'wb+') as destination:
                    for chunk in profile_picture.chunks():
                        destination.write(chunk)
            except:
                profile_picture = ""

        except:
            return HttpResponse(response_error)

        user = User(UserName=user_name, Email=email, Password=password,
                    FirstName=firstname, LastName=lastname,
                    BirthDate=birthdate, ProfilePicture=profile_picture,
                    PhoneNumber=phone_number, HomeAddress=address,
                    AboutMe="Add some info about yourself :)")
        # Need to implement check for empty values.
        user.save()
        if choice == "Client":
            reference_id = "abc1234"
            client = Client(User=user, Reference_ID=reference_id)
            client.save()
        elif choice == "Family_Friend":
            reference_id = request.POST.get('reference_id')
            relationship_to_client = request.POST.get('relationship_to_client')
            try:
                client = Client.objects.get(Reference_ID=reference_id)
                subuser = SubUser(RelationshipToClient=relationship_to_client, User=user, Client=client)
                subuser.save()
            except:
                HttpResponse("Wrong Reference ID")
        else:
            print "nothing chosen"
        user_name_str = user.FirstName
        # print user_name_str

        return HttpResponse(user_name_str)
    else:
        raise Http404


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
            'date': memory.StartDate,
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


def addMemory(request):
    if request.method == 'POST':
        if request.is_ajax:
            try:
                mem_title = request.POST.get('memory-title-input')
                mem_descp = request.POST.get('mem-descrip-input')
                date_start = request.POST.get('input-datestart')
                date_end = request.POST.get('input-dateend')

                print len(request.POST)
                form_data = json.dumps({'context': mem_title})
                return HttpResponse(form_data)

            except KeyError:
                form_data = json.dumps({"context": "There was an error creating the memory. Try again later..."})
                return HttpResponse(form_data)
        else:
            raise Http404


def detail(request, user_id):
    return HttpResponse("You're looking at user %s." % user_id)


def results(request, user_id):
    response = "You're looking at the results of user %s."
    return HttpResponse(response % user_id)


def vote(request, user_id):
    return HttpResponse("You're voting on user %s." % user_id)
