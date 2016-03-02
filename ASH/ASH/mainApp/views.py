from django.http import HttpResponse


def index(request):
    return HttpResponse("Ok, my first commit worked! Let's see if my second commit works...(Damian)")
