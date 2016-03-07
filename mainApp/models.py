from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone

class Picture(models.Model):
    MemoryLink = models.CharField(max_length=500, blank=False, null=False)
    Picture = models.CharField(max_length=500, blank=False, null=False)
    Description = models.CharField(max_length=500, blank=False, null=False)

class Video(models.Model):
    MemoryLink = models.CharField(max_length=500, blank=False, null=False)
    Video = models.CharField(max_length=500, blank=False, null=False)
    Description = models.CharField(max_length=500, blank=False, null=False)

class Client(models.Model):
    User = models.ForeignKey('User', on_delete=models.CASCADE)
    Token = models.CharField(max_length=18, blank=False, null=False)
    CreatedDate = models.DateTimeField(auto_now_add = False, auto_now = "True")
    # SubUser = models.ManyToManyField(SubUser)#this relationship will relate all clients to subusers and vice-versa
    # def __str__(self):
    #     return  self.userid.userid + " " + self.champion + " " + str(self.rating) + " " + self.server + " " + str(self.pricerate) + " " + self.overview
    # def __str__(self):
    #     return self.User

class Calendar(models.Model):
    Description = models.CharField(max_length=500, blank=False, null=False)
    Client = models.ForeignKey(Client)

class SpecialPeople(models.Model):
    FirstName = models.CharField(max_length = 500, blank = False, null = False)
    LastName = models.CharField(max_length = 500, blank = False, null = False)
    RelationshipDescription = models.CharField(max_length = 500, blank=  False, null = False)
    Client = models.ForeignKey(Client)

class SubUser(models.Model):
    User = models.ForeignKey('User', on_delete=models.CASCADE)
    CreatedDate = models.DateTimeField(auto_now_add = False, auto_now = "True")
    Videos = models.ManyToManyField(Video)
    Pictures = models.ManyToManyField(Picture)
    Client = models.ForeignKey(Client)

class Memory(models.Model):
    #ID = models.CharField(primary_key=True, max_length=100, blank=False, null=False)
    CreatedOn = models.DateTimeField(auto_now_add = False, auto_now = "True")
    Title = models.CharField(max_length=500, blank=False, null=False)
    Description = models.CharField(max_length=500, blank=False, null=False)
    Location = models.TextField(blank=True)
    Date = models.DateTimeField(auto_now_add = False, auto_now = "True")
    OtherRelated = models.CharField(max_length=500, blank=False, null=False)
    SubUser = models.ForeignKey(SubUser)

    # def __str__(self):
    #     return self.User

class User(models.Model):
    UserName = models.CharField(max_length=18, blank=False, null=False)
    Email = models.EmailField(blank=False, null=False)
    Password = models.CharField(max_length=18, blank=False, null=False)
    FirstName = models.CharField(max_length = 500, blank = False, null = False)
    LastName = models.CharField(max_length = 500, blank = False, null = False)
    BirthDate = models.DateTimeField(auto_now_add = False, auto_now = "True")
    ProfilePicture = models.CharField(max_length = 500, blank = False, null = False)
    PhoneNumber = models.CharField(max_length = 11, blank = False, null = False)
    HomeAddress = models.TextField(blank=True)
    AboutMe = models.TextField(blank=True)
