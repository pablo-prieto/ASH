from django.conf.urls import url
from . import views
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^(?P<user_id>[0-9]+)/$', views.index, name='index'),
    url(r'^(?P<user_id>[0-9]+)/profile/', views.profile, name='profile'),
    url(r'^login/', views.login, name='login'),
    url(r'^register/', views.register, name='register'),
    url(r'^authenticateLogin/', views.authenticateLogin, name='authenticateLogin'),
    url(r'^addMemory/(?P<subuser_username>[-\w]+)', views.addMemory, name='addMemory'),
    url(r'^addPicture/(?P<subuser_username>[-\w]+)', views.addPicture, name='addPicture'),
    # url(r'^(?P<user_id>[0-9]+)/vote/$', views.vote, name='vote'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
