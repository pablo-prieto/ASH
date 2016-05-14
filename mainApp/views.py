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
        form = RegistrationForm(request.POST, request.FILES)
        response_error = "Error getting your info from the form."
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
                except Exception as e:
                    print '%s (%s)' % (e.message, type(e))
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
                except Exception as e:
                    print '%s (%s)' % (e.message, type(e))
            else:
                print "nothing chosen"
            user_name_str = user.FirstName
            # print user_name_str

            return HttpResponse(user_name_str)
        else:
            print "not valid"
    else:
        form = RegistrationForm()
        print "called plain form"
    context = {"form": form}
    return render(request, "register.html", context)


def index(request, user_id):
    current_user = User.objects.get(pk=user_id)
    client_user = Client.objects.get(User=current_user)
    list_subusers = SubUser.objects.filter(Client=client_user)
    list_friends = list_subusers.filter(RelationshipToClient="Friend")
    list_family_members = list_subusers.exclude(RelationshipToClient="Friend")
    list_special_people = SpecialPerson.objects.filter(Client=client_user)
    number_special_people = len(list_special_people)
    number_remaining_spots = 3 - number_special_people
    string_remaining_spots = ""
    for i in range(number_remaining_spots):
        string_remaining_spots += "1"

    context = {
        'client': client_user,
        'list_friends': list_friends,
        'list_family_members': list_family_members,
        'list_subusers': list_subusers,
        'list_special_people': list_special_people,
        'string_remaining_spots': string_remaining_spots
    }
    return render(request, "mainApp/index.html", context)


def addSpecialPerson(request):
    # context = RequestContext(request)
    mem_id = None
    if request.method == 'GET':
        str_member_id = request.GET['member_id']
        print str_member_id
        member_id = ""
        for index in range(len(str_member_id)):
            if index > 15:
                member_id += str_member_id[index]

        print member_id
        sub_user = SubUser.objects.get(id=member_id)
        client_user = Client.objects.get(subuser=sub_user)

        special_person = SpecialPerson(SubUser=sub_user, Client=client_user)
        special_person.save()

        list_subusers = SubUser.objects.filter(Client=client_user)
        list_special_people = SpecialPerson.objects.filter(Client=client_user)
        number_special_people = len(list_special_people)
        number_remaining_spots = 3 - number_special_people
        string_remaining_spots = ""

        for i in range(number_remaining_spots):
            string_remaining_spots += "1"

        context = {
            'list_subusers': list_subusers,
            'list_special_people': list_special_people,
            'string_remaining_spots': string_remaining_spots
        }

    return HttpResponse(context)

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
            pictures_list.append({
                'title': picture.PictureTitle,
                'descrip': picture.Description,
                'file': picture.Picture
            })

        memory_list.append({
            'title': memory.Title,
            'description': memory.Description,
            'location': memory.Location,
            'start_date': memory.StartDate.date(),
            'end_date': memory.EndDate.date(),
            'others_related': memory.OtherRelated,
            'pictures': pictures_list
        })

    context = {
        'subuser_username': current_user.UserName,
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


def addMemory(request, subuser_username):
    if request.method == 'POST':
        if request.is_ajax:
            try:
                # First we store the information of the memory in the Memory Table
                mem_title = request.POST.get('mem-title-input')
                mem_descp = request.POST.get('mem-descrip-input')
                mem_location = request.POST.get('mem-location-input')
                others_related = request.POST.get('mem-related-people-input')
                date_start = request.POST.get('input-datestart')
                date_end = request.POST.get('input-dateend')

                # Replace the dashes to spaces to then convert it into a date format that can be stored in the DB
                temp = date_start.replace('-', " ")
                start = datetime.strptime(temp, '%M %d %Y')
                temp = date_end.replace('-', " ")
                end = datetime.strptime(temp, '%M %d %Y')

                # Find the corresponding subuser
                user = User.objects.get(UserName=subuser_username)
                subuser = SubUser.objects.get(User=user)

                # User the above information to create the new memory
                new_memory = Memory(Title=mem_title,
                                    Description=mem_descp,
                                    Location=mem_location,
                                    StartDate=start,
                                    EndDate=end,
                                    OtherRelated=others_related,
                                    SubUser=subuser)

                # Save the new created memory
                new_memory.save()

                # Now, we store the picture(s) of the memory with the respective information(s) in the Picture table
                # Since we don't know the names of the pictures files, titles and description fields, we loop thru the
                # dictionary of the request.POST and find them all. Every time we find one we see the index number that was
                # attached to it when it was created and use the same indices for the picture file names. The title,
                # and description of a picture should have the same index attached at the end of the basename.
                # We do this because those indices are not consistent if the user deletes
                # one of the panels in the form (refer to the function 'addImgPanel()' in the script of the profile.html)
                for key in request.FILES.keys():
                    index = key[len(key) - 1]
                    picture_title = request.POST.get('mem-pic-title' + index)
                    picture_descrip = request.POST.get('mem-pic-descrip' + index)

                    # Try to retreive the picture file and save it
                    try:
                        picture_file = request.FILES[key]
                        with open(settings.BASE_DIR + "/static_in_env/media_root/Pictures/" + picture_file.name, 'wb+') as destination:
                            for chunk in picture_file.chunks():
                                destination.write(chunk)
                    except:
                        picture_file = ""

                    mem_picture = Picture(Picture=picture_file,
                                          PictureTitle=picture_title,
                                          Description=picture_descrip,
                                          Memory=new_memory)
                    mem_picture.save()

                form_data = json.dumps({'context': "successful"})
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
