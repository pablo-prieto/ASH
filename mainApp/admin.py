from django.contrib import admin

# Register your models here.
from .models import User, Client, SubUser, Calendar, Memory, SpecialPerson, Picture, Video

admin.site.register(User)
admin.site.register(Client)
admin.site.register(SubUser)
admin.site.register(Calendar)
admin.site.register(Memory)
admin.site.register(SpecialPerson)
admin.site.register(Picture)
admin.site.register(Video)
