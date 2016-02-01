from django.http import HttpResponse


def index(request):
    return HttpResponse("I hope this works. (Damian)")
