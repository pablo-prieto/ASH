from django.contrib import admin

# Register your models here.
from .models import SubUser

admin.site.register(SubUser)

from .models import MasterUser

admin.site.register(MasterUser)
