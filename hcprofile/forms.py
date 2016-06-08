#-*- coding:utf-8 -*-

from registration.forms import RegistrationForm
from django import forms
from main.forms import unibot_validator, phone_validator

class ExRegistrationForm(RegistrationForm):
    fio = forms.CharField(label = u"Ф.И.О.", max_length=50)
    phone = forms.CharField(label = u"Телефон", max_length=15, required=False, validators=[phone_validator])
    discount = forms.CharField(validators=[unibot_validator], max_length=2, required=False, widget=forms.HiddenInput())
