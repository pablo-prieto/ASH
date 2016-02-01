from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index. Hello, this is Damian's Test")
