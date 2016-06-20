# -*- coding:utf-8 -*-

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from eshop.models import WishList
from hcprofile.models import UserProfile


class WishList(admin.TabularInline):
    model = WishList
    raw_id_fields = ['article']
    extra = 0


class UserProfileInLine(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'profile'


class UserAdmin(UserAdmin):
    inlines = (UserProfileInLine, WishList)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
