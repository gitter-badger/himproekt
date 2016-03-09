#-*- coding:utf-8 -*-

from registration.forms import RegistrationForm
from django import forms
from main.forms import unibot_validator, phone_validator

class ExRegistrationForm(RegistrationForm):
    fio = forms.CharField(label = u"Ф.И.О.", max_length=50)
    city = forms.CharField(label = u"Город", max_length=50, required=False)
    phone = forms.CharField(label = u"Телефон", max_length=15, validators=[phone_validator])
    street = forms.CharField(label = u"Улица", max_length=50, required=False)
    house = forms.CharField(label = u"Дом", max_length=50, required=False)
    flat = forms.CharField(label = u"Квартира", max_length=50, required=False)
    index = forms.CharField(label = u"Почтовый индекс", max_length=50, required=False)
    discount = forms.CharField(validators=[unibot_validator], max_length=2, required=False, widget=forms.HiddenInput())
