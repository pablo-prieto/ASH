from django.conf.urls import url
from . import views
from django.views.generic import RedirectView


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^login/', views.login, name='login'),
    # ex: /polls/5/
    url(r'^(?P<user_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<user_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<user_id>[0-9]+)/vote/$', views.vote, name='vote'),
]