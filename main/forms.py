#-*- coding:utf-8 -*-

from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, re
from django.utils.encoding import smart_unicode


def unibot_validator(value):
    if value:
        raise ValidationError('should be empty')

def phone_validator(value):
    if re.compile("^([0-9\(\)\/\+ \-]*)$").search(smart_unicode(value)):
        pass
    else:
        raise ValidationError('enter valid phone number')

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    city = forms.CharField(max_length=50, required=False)
    phone = forms.CharField(max_length=15, validators=[phone_validator], required=False)
    message = forms.CharField(widget=forms.Textarea)
    unibot = forms.CharField(validators=[unibot_validator], required=False, widget=forms.HiddenInput())