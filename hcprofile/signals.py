#-*- coding:utf-8 -*-

from registration.signals import user_registered
from hcprofile.models import UserProfile
from forms import ExRegistrationForm
from django.contrib import auth

def user_created(sender, user, request, **kwargs):
    form = ExRegistrationForm(request.POST)
    userprofile = UserProfile(user=user, city = form.data['city'], phone = form.data['phone'], street = form.data['street'], house = form.data['house'], flat = form.data['flat'], index = form.data['index'], discount = 0)
    userprofile.save()

user_registered.connect(user_created)