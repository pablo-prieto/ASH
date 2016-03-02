from django.contrib import admin

# Register your models here.
from .models import MasterUser, SubUser, Calendar, Memory, SpecialPeople, Picture, Video

admin.site.register(MasterUser)
admin.site.register(SubUser)
admin.site.register(Calendar)
admin.site.register(Memory)
admin.site.register(SpecialPeople)
admin.site.register(Picture)
admin.site.register(Video)
