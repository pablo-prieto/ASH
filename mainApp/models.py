from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    userid = models.CharField(primary_key=True, max_length=100, blank=False, null=False)
    password = models.CharField(max_length=18, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    createdDate = models.DateTimeField('Date Created')
    birthDate = models.DateTimeField('Birth Date')
    fullName = models.CharField(max_length = 500, blank = False, null = False)

    def __str__(self):
        return self.userid

    def was_created_recently(self):
        return self.createdDate >= timezone.now() - datetime.timedelta(days=1)
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

class MasterUser(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    # fullName = models.CharField(max_length = 500, blank = False, null = False)
    # birthDate = models.CharField(max_length = 500, blank = False, null = False)
    # pricerate = models.PositiveIntegerField(default = 0,  blank = False, null = False)
    # avatar = models.URLField(blank=False, null=False)
    # rating = models.IntegerField(default = 0,  blank = False, null = False)
    # overview = models.TextField(blank=True)
    # def __str__(self):
    #     return  self.userid.userid + " " + self.champion + " " + str(self.rating) + " " + self.server + " " + str(self.pricerate) + " " + self.overview

    def __str__(self):
        return self.userid
