from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Calendar(models.Model):
    ID = models.CharField(primary_key=True, max_length=100, blank=False, null=False)
    Description = models.CharField(max_length=500, blank=False, null=False)

class Memory(models.Model):
    ID = models.CharField(primary_key=True, max_length=100, blank=False, null=False)
    CreatedOn = models.DateTimeField(auto_now_add = False, auto_now = "True")
    Title = models.CharField(max_length=500, blank=False, null=False)
    Description = models.CharField(max_length=500, blank=False, null=False)
    Location = models.TextField(blank=True)
    Date = models.DateTimeField(auto_now_add = False, auto_now = "True")
    OtherRelated = models.CharField(max_length=500, blank=False, null=False)

class SpecialPeople(models.Model):
    ID = models.CharField(primary_key=True, max_length=100, blank=False, null=False)
    FirstName = models.CharField(max_length = 500, blank = False, null = False)
    LastName = models.CharField(max_length = 500, blank = False, null = False)
    RelationshipDescription = models.CharField(max_length=500, blank=False, null=False)

class Picture(models.Model):
    ID = models.CharField(primary_key=True, max_length=100, blank=False, null=False)
    MemoryLink = models.CharField(max_length=500, blank=False, null=False)
    Picture = models.CharField(max_length=500, blank=False, null=False)
    Description = models.CharField(max_length=500, blank=False, null=False)

class Video(models.Model):
    ID = models.CharField(primary_key=True, max_length=100, blank=False, null=False)
    MemoryLink = models.CharField(max_length=500, blank=False, null=False)
    Video = models.CharField(max_length=500, blank=False, null=False)
    Description = models.CharField(max_length=500, blank=False, null=False)

class SubUser(models.Model):
    ID = models.CharField(primary_key=True, max_length=100, blank=False, null=False)
    Password = models.CharField(max_length=18, blank=False, null=False)
    Email = models.EmailField(blank=False, null=False)
    CreatedDate = models.DateTimeField(auto_now_add = False, auto_now = "True")
    BirthDate = models.DateTimeField(auto_now_add = False, auto_now = "True")
    FirstName = models.CharField(max_length = 500, blank = False, null = False)
    LastName = models.CharField(max_length = 500, blank = False, null = False)

    def __str__(self):
        return self.userid

    def was_created_recently(self):
        return self.createdDate >= timezone.now() - datetime.timedelta(days=1)

class MasterUser(models.Model):
    ID = models.CharField(primary_key=True, max_length=100, blank=False, null=False)
    SubUserID = models.ForeignKey('SubUser', on_delete=models.CASCADE)
    CalendarID = models.ForeignKey('Calendar', on_delete=models.CASCADE)
    Password = models.CharField(max_length=18, blank=False, null=False)
    Token = models.CharField(max_length=18, blank=False, null=False)
    FirstName = models.CharField(max_length = 500, blank = False, null = False)
    LastName = models.CharField(max_length = 500, blank = False, null = False)
    BirthDate = models.DateTimeField(auto_now_add = False, auto_now = "True")
    PhoneNumber = models.CharField(max_length = 11, blank = False, null = False)
    HomeAddress = models.TextField(blank=True)
    AboutMe = models.TextField(blank=True)
    ProfilePicture = models.CharField(max_length = 500, blank = False, null = False)
    # pricerate = models.PositiveIntegerField(default = 0,  blank = False, null = False)
    # avatar = models.URLField(blank=False, null=False)
    # rating = models.IntegerField(default = 0,  blank = False, null = True)
    # overview = models.TextField(blank=True)
    # def __str__(self):
    #     return  self.userid.userid + " " + self.champion + " " + str(self.rating) + " " + self.server + " " + str(self.pricerate) + " " + self.overview

    def __str__(self):
        return self.userid
