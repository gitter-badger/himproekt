#-*- coding:utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    fio = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True)
    discount = models.CharField(max_length=2, blank=True)

    def __unicode__(self):
        return '%s' % self.user