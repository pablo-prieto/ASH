from django.http import HttpResponse
from django.shortcuts import render


from .models import User

def index(request):

    birthDate_user_list = User.objects.order_by('-birthDate')[:5]
    context = {
        'birthDate_user_list': birthDate_user_list,
    }
    return render(request, 'mainApp/index.html', context)

def profile(request):
    return render(request, 'mainApp/profile.html')

def detail(request, user_id):
    return HttpResponse("You're looking at user %s." % user_id)

def results(request, user_id):
    response = "You're looking at the results of user %s."
    return HttpResponse(response % user_id)

def vote(request, user_id):
    return HttpResponse("You're voting on user %s." % user_id)
