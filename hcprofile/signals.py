#-*- coding:utf-8 -*-

from registration.signals import user_registered
from hcprofile.models import UserProfile
from forms import ExRegistrationForm
from django.contrib import auth

def user_created(sender, user, request, **kwargs):
    form = ExRegistrationForm(request.POST)
    userprofile = UserProfile(user=user, fio=form.data['fio'], phone = form.data['phone'], discount = 0)
    userprofile.save()

user_registered.connect(user_created)