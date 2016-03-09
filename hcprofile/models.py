#-*- coding:utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    fio = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    street = models.CharField(max_length=50, blank=True)
    house = models.CharField(max_length=10, blank=True)
    flat = models.CharField(max_length=5, blank=True)
    index = models.CharField(max_length=10, blank=True)
    discount = models.CharField(max_length=2, blank=True)

    def __unicode__(self):
        return '%s' % self.user