from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone

class User(models.Model):
    UserName = models.CharField(max_length=18, blank=False, null=False, unique=True)
    Email = models.EmailField(blank=False, null=False)
    Password = models.CharField(max_length=18, blank=False, null=False)
    FirstName = models.CharField(max_length = 500, blank = False, null = False)
    LastName = models.CharField(max_length = 500, blank = False, null = False)
    BirthDate = models.DateTimeField(auto_now_add = False, auto_now = "True")
    ProfilePicture = models.ImageField(upload_to='Profile Picures')
    PhoneNumber = models.CharField(max_length = 11, blank = False, null = False)
    HomeAddress = models.TextField(blank=True)
    AboutMe = models.TextField(blank=True)

    def __unicode__(self):
        return u'%s %s' % (self.FirstName, self.LastName)

class Client(models.Model):
    User = models.ForeignKey(User)
    Token = models.CharField(max_length=18, blank=False, null=False)
    CreatedDate = models.DateTimeField(auto_now_add = False, auto_now = "True")

    def __unicode__(self):
        return 'Client %s %s' % (self.User.FirstName, self.User.LastName)

class SpecialPerson(models.Model):
    FirstName = models.CharField(max_length = 500, blank = False, null = False)
    LastName = models.CharField(max_length = 500, blank = False, null = False)
    RelationshipDescription = models.CharField(max_length = 500, blank=  False, null = False)
    Client = models.ForeignKey(Client)

    def __unicode__(self):
        return '%s %s' % (self.FirstName, self.LastName)

class Calendar(models.Model):
    Description = models.CharField(max_length=500, blank=False, null=False)
    Client = models.ForeignKey(Client)

    def __unicode__(self):
        return 'Calendar for %s %s' % (self.Client.User.FirstName, self.Client.User.LastName)

class SubUser(models.Model):
    CreatedDate = models.DateTimeField(auto_now_add = False, auto_now = "True")
    #RelationshipToClient = models.CharField(max_length = 500, blank = False, null = False)
    User = models.ForeignKey(User)
    Client = models.ForeignKey(Client)

    def __unicode__(self):
        return u'%s %s' % (self.User.FirstName, self.User.LastName)

class Picture(models.Model):
    Picture = models.ImageField(upload_to='Pictures')
    PictureTitle = models.CharField(max_length=500, blank=False, null=False)
    Description = models.CharField(max_length=500, blank=False, null=False)
    SubUser = models.ForeignKey(SubUser)

    def __unicode__(self):
        return '%s: %s %s' % (self.PictureTitle, self.SubUser.User.FirstName, self.SubUser.User.LastName)

class Video(models.Model):
    Video = models.FileField(upload_to='Videos/')
    VideoTitle = models.CharField(max_length=500, blank=False, null=False)
    Description = models.CharField(max_length=500, blank=False, null=False)
    SubUser = models.ForeignKey(SubUser)

    def __unicode__(self):
        return '%s: %s %s' % (self.VideoTitle, self.SubUser.User.FirstName, self.SubUser.User.LastName)

class Memory(models.Model):
    #ID = models.CharField(primary_key=True, max_length=100, blank=False, null=False)
    CreatedOn = models.DateTimeField(auto_now_add = False, auto_now = "True")
    Title = models.CharField(max_length=500, blank=False, null=False)
    Description = models.CharField(max_length=500, blank=False, null=False)
    Location = models.TextField(blank=True)
    Date = models.DateTimeField(auto_now_add = False, auto_now = "True")
    OtherRelated = models.CharField(max_length=500, blank=False, null=False)
    SubUser = models.ForeignKey(SubUser)

    def __unicode__(self):
        return '%s, Memory of: %s %s' % (self.Title, self.SubUser.User.FirstName, self.SubUser.User.LastName)
