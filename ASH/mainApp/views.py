from django.http import HttpResponse


def index(request):
    return HttpResponse("Main page.")

def detail(request, user_id):
    return HttpResponse("You're looking at user %s." % user_id)

def results(request, user_id):
    response = "You're looking at the results of user %s."
    return HttpResponse(response % user_id)

def vote(request, user_id):
    return HttpResponse("You're voting on user %s." % user_id)
