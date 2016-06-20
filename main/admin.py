#-*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.contrib.sites.models import Site
from django.contrib.flatpages.admin import FlatPageAdmin as DefaultFlatPageAdmin
from django.conf import settings

from eshop.models import WishList
from main.models import Constant, News, FLatPageImage

admin.site.unregister(FlatPage)


class WishListInline(admin.TabularInline):

    model = WishList


class ConstantAdmin(admin.ModelAdmin):
    """Customize constants admin page"""

    list_display = ('name', 'value', 'description')

    def queryset(self, request):
        """show only current site constants"""
        queryset = super(ConstantAdmin, self).queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(site=Site.objects.get_current())

    def save_model(self, request, obj, form, change):
        """ pre save actions """
        obj.site_id = settings.SITE_ID
        obj.save()


class FlatPageAdmin(DefaultFlatPageAdmin):
    """Customize flatpage admin page"""

    def queryset(self, request):
        """ show flatpages only for current site """
        return super(FlatPageAdmin, self).queryset(request).filter(
            sites=Site.objects.get_current())

    def save_model(self, request, obj, form, change):
        """ pre save actions """
        obj.save()
        if obj.sites.count() == 0:
            obj.sites.add(Site.objects.get_current())
            obj.save()

    class Media:
        js = ('tiny_mce/tiny_mce.js', 'tiny_mce/init.js')


class NewsAdmin(admin.ModelAdmin):
    """Customize news admin page"""

    list_display = ('name', 'published', 'created_date')
    list_filter = ('published',)
    ordering = ('name', 'created_date', 'published')
    prepopulated_fields = {"slug": ("name",)}

    class Media:
        js = ('tiny_mce/tiny_mce.js', 'tiny_mce/init.js')


class FlatPageImageAdmin(admin.ModelAdmin):
    """Customize certificates admin page"""

    list_display = ('page', 'name', 'created_date')
    ordering = ('name', 'created_date')


admin.site.register(FlatPage, FlatPageAdmin)
admin.site.register(Constant, ConstantAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(FLatPageImage, FlatPageImageAdmin)
