# -*- coding:utf-8 -*-
"""
Author:
    Vitaly Omelchuk <vitaly.omelchuk@gmail.com>

Description:
    ecomerce models
"""
import threading
import random

from django.db import models
from django.contrib.sitemaps import Sitemap
from django.utils.translation import ugettext as _
from django_extensions.db.fields import (CreationDateTimeField,
                                         ModificationDateTimeField, AutoSlugField)
from django.contrib.auth.models import User
from django.core.cache import cache
from django.db.models import Sum

from main.models import Constant
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField

import tagging
from tagging.models import Tag
from sorl.thumbnail.shortcuts import get_thumbnail

class ArticleItemManager(models.Manager):
    def popular_product(self):
        return self.get_query_set().filter(popular_product=True).order_by("order")

    def slider_new(self):
        return self.get_query_set().filter(new_product=True)

    def slider_action(self):
        return self.get_query_set().filter(action_product=True)


class ArticleCategory(MPTTModel):
    """ Model for article's category."""

    order = models.PositiveIntegerField(_('order'), default=0, db_column='_order')
    name = models.CharField(_('name'), max_length=255, unique=True)
    slug = models.SlugField(_('Slug'), max_length=255, editable=True)
    title = models.CharField(_('title'), max_length=255, blank=True)
    keywords = models.CharField(_('keywords'), max_length=255, blank=True)
    descriptions = models.CharField(_('descriptions'), max_length=255, blank=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', verbose_name=u'Родитель')
    #parent = models.ForeignKey('self', null=True, blank=True, related_name='children', verbose_name=u'Родитель')
    image = models.ImageField(_('image'), upload_to="pictures", blank=True)
    description = models.TextField(_('description'), blank=True)
    published = models.BooleanField(_('published'), default=True)
    created_date = CreationDateTimeField(_('creation date'))
    updated_date = ModificationDateTimeField(_('modification date'))

    def get_thumbnail_html(self):
        img = self.image
        img_resize_url = unicode(get_thumbnail(img, '50').url)
        html = '<a class="image-picker" href="%s"><img src="%s" alt="%s"/></a>'
        return html % (self.image.url, img_resize_url, self.name)
    get_thumbnail_html.short_description = 'Foto'
    get_thumbnail_html.allow_tags = True

    def get_children_articles(self):
        """ return queryset of published children articles """

        return self.articles.filter(published=True, present="+")

    def get_random_image(self):
        """ return random article image """
        try:
            return self.articles.exclude(published=True, present="+", image="img/no_photo.jpg").order_by('?').values_list('image', flat=True)[0]
        except IndexError:
            return self.image

    def __unicode__(self):
        return unicode(self.name)

    @models.permalink
    def get_absolute_url(self):
        """ return object url """
        if self.slug:
            return ('eshop_category_slug', (), {'slug': self.slug})
        else:
            return ('eshop_category', (), {'object_id': self.pk})

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')
        ordering = ['order', 'name']


class ArticleItem(models.Model):
    """ Model for article """

    order = models.PositiveIntegerField(_('order'), default=0, db_column='_order')
    union_name = models.CharField(u'Название товара', max_length=255, blank=True)
    name = models.CharField(_('name'), max_length=255)
    slug = models.SlugField(_('Slug'), max_length=255, editable=True)
    title = models.CharField(_('title'), max_length=255, blank=True)
    keywords = models.CharField(_('keywords'), max_length=255, blank=True)
    descriptions = models.CharField(_('descriptions'), max_length=255, blank=True)
    categories = TreeManyToManyField(ArticleCategory, null=True, related_name='articles')
    #categories = models.ForeignKey(ArticleCategory, null=True, related_name='articles', verbose_name=u'Категория')
    description = models.TextField(_('description'), blank=True)
    palette = models.CharField(u'Выберите цвет', max_length=7, blank=True, default="#ffffff")
    color = models.CharField(u'Название цвета', max_length=50, blank=True)
    kod_tovara = models.CharField(u'Код товара', max_length=50, blank=True)
    image = models.ImageField(_('image'), upload_to="upload", blank=True)
    published = models.BooleanField(_('published'), default=True)
    price = models.DecimalField(_('price'), max_digits=10, decimal_places=2, default=0)
    CURRENCY = (
        ('H', u'гривна'),
        ('S', u'доллар'),
        ('E', u'евро'),
    )
    currency = models.CharField(u'Валюта',max_length=1, choices=CURRENCY, default="H")
    created_date = CreationDateTimeField(_('creation date'))
    updated_date = ModificationDateTimeField(_('modification date'))
    present = models.BooleanField(u'Есть в наличии', default=True)
    can = models.CharField(u'Объем', max_length=10, blank=True)
    pack = models.DecimalField(u'упаковка (шт.)', max_digits=4, decimal_places=0, default=0, blank=True)
    popular_product = models.BooleanField(u'Популярное', default=False)
    new_product = models.BooleanField(u'Новинки', default=False)
    action_product = models.BooleanField(u'Акции и скидки', default=False)
    manufacturer = models.CharField(u'Производитель', max_length=32, blank=True)
    country = models.CharField(u'Страна', max_length=32, blank=True)
    property_name1 = models.CharField(u'Свойство1', max_length=255, blank=True)
    property_value1 = models.CharField(u'Значение1', max_length=255, blank=True)
    property_unit1 = models.CharField(u'Ед. измерения1', max_length=255, blank=True)
    property_name2 = models.CharField(u'Свойство2', max_length=255, blank=True)
    property_value2 = models.CharField(u'Значение2', max_length=255, blank=True)
    property_unit2 = models.CharField(u'Ед. измерения2', max_length=255, blank=True)
    property_name3 = models.CharField(u'Свойство3', max_length=255, blank=True)
    property_value3 = models.CharField(u'Значение3', max_length=255, blank=True)
    property_unit3 = models.CharField(u'Ед. измерения3', max_length=255, blank=True)
    property_name4 = models.CharField(u'Свойство4', max_length=255, blank=True)
    property_value4 = models.CharField(u'Значение4', max_length=255, blank=True)
    property_unit4 = models.CharField(u'Ед. измерения4', max_length=255, blank=True)
    property_name5 = models.CharField(u'Свойство5', max_length=255, blank=True)
    property_value5 = models.CharField(u'Значение5', max_length=255, blank=True)
    property_unit5 = models.CharField(u'Ед. измерения5', max_length=255, blank=True)
    property_name6 = models.CharField(u'Свойство6', max_length=255, blank=True)
    property_value6 = models.CharField(u'Значение6', max_length=255, blank=True)
    property_unit6 = models.CharField(u'Ед. измерения6', max_length=255, blank=True)
    property_name7 = models.CharField(u'Свойство7', max_length=255, blank=True)
    property_value7 = models.CharField(u'Значение7', max_length=255, blank=True)
    property_unit7 = models.CharField(u'Ед. измерения7', max_length=255, blank=True)
    property_name8 = models.CharField(u'Свойство8', max_length=255, blank=True)
    property_value8 = models.CharField(u'Значение8', max_length=255, blank=True)
    property_unit8 = models.CharField(u'Ед. измерения8', max_length=255, blank=True)
    property_name9 = models.CharField(u'Свойство9', max_length=255, blank=True)
    property_value9 = models.CharField(u'Значение9', max_length=255, blank=True)
    property_unit9 = models.CharField(u'Ед. измерения9', max_length=255, blank=True)
    property_name10 = models.CharField(u'Свойство10', max_length=255, blank=True)
    property_value10 = models.CharField(u'Значение10', max_length=255, blank=True)
    property_unit10 = models.CharField(u'Ед. измерения10', max_length=255, blank=True)
    property_name11 = models.CharField(u'Свойство11', max_length=255, blank=True)
    property_value11 = models.CharField(u'Значение11', max_length=255, blank=True)
    property_unit11 = models.CharField(u'Ед. измерения11', max_length=255, blank=True)
    property_name12 = models.CharField(u'Свойство12', max_length=255, blank=True)
    property_value12 = models.CharField(u'Значение12', max_length=255, blank=True)
    property_unit12 = models.CharField(u'Ед. измерения12', max_length=255, blank=True)
    property_name13 = models.CharField(u'Свойство13', max_length=255, blank=True)
    property_value13 = models.CharField(u'Значение13', max_length=255, blank=True)
    property_unit13 = models.CharField(u'Ед. измерения13', max_length=255, blank=True)
    property_name14 = models.CharField(u'Свойство14', max_length=255, blank=True)
    property_value14 = models.CharField(u'Значение14', max_length=255, blank=True)
    property_unit14 = models.CharField(u'Ед. измерения14', max_length=255, blank=True)
    property_name15 = models.CharField(u'Свойство15', max_length=255, blank=True)
    property_value15 = models.CharField(u'Значение15', max_length=255, blank=True)
    property_unit15 = models.CharField(u'Ед. измерения15', max_length=255, blank=True)
    property_name16 = models.CharField(u'Свойство16', max_length=255, blank=True)
    property_value16 = models.CharField(u'Значение16', max_length=255, blank=True)
    property_unit16 = models.CharField(u'Ед. измерения16', max_length=255, blank=True)
    property_name17 = models.CharField(u'Свойство17', max_length=255, blank=True)
    property_value17 = models.CharField(u'Значение17', max_length=255, blank=True)
    property_unit17 = models.CharField(u'Ед. измерения17', max_length=255, blank=True)
    property_name18 = models.CharField(u'Свойство18', max_length=255, blank=True)
    property_value18 = models.CharField(u'Значение18', max_length=255, blank=True)
    property_unit18 = models.CharField(u'Ед. измерения18', max_length=255, blank=True)
    property_name19 = models.CharField(u'Свойство19', max_length=255, blank=True)
    property_value19 = models.CharField(u'Значение19', max_length=255, blank=True)
    property_unit19 = models.CharField(u'Ед. измерения19', max_length=255, blank=True)
    property_name20 = models.CharField(u'Свойство20', max_length=255, blank=True)
    property_value20 = models.CharField(u'Значение20', max_length=255, blank=True)
    property_unit20 = models.CharField(u'Ед. измерения20', max_length=255, blank=True)

    objects = ArticleItemManager()

    @property
    def main_category(self):
        try:
            return self.categories.all()[0]
        except IndexError:
            return None

    def get_thumbnail_html(self):
        img = self.image
        img_resize_url = unicode(get_thumbnail(img, '50').url)
        html = '<a class="image-picker" href="%s"><img src="%s" alt="%s"/></a>'
        return html % (self.image.url, img_resize_url, self.name)
    get_thumbnail_html.short_description = 'Foto'
    get_thumbnail_html.allow_tags = True

    def get_price(self):
        """ calculate price """
        if self.currency == "H":
            return float(self.price)
        elif self.currency == "S":
            return float(self.price) * float(Constant.get_const('usd_currency'))
        elif self.currency == "E":
            return float(self.price) * float(Constant.get_const('euro_currency'))

    def set_tags(self, tags):
        Tag.objects.update_tags(self, tags)

    def get_tags(self, tags):
        return Tag.objects.get_for_object(self)

    def get_image(self):
        """ return or self image if it exist or image of category """

        try:
            return self.image
        except Exception:
            return None

    def __unicode__(self):
        return unicode(self.name)

    def get_absolute_url(self):
        """ return object url """
        return '/{category}/{slug}/'.format(category=self.categories.all()[0].slug, slug=self.slug)

    def get_cannonical_url(self):
        try:
            cannonical_article = ArticleItem.objects.filter(union_name=self.union_name).order_by('palette')[0]
        except IndexError:
            return self.get_absolute_url()
        else:
            return cannonical_article.get_absolute_url()

    class Meta:
        verbose_name = _('article')
        verbose_name_plural = _('articles')
        ordering = ['union_name', 'order']



class ArticleImage(models.Model):
    """ article item image """
    article = models.ForeignKey('ArticleItem')
    image = models.ImageField(upload_to="pictures")


CART_STATUS = (
    (1, _('created')),
    (2, _('not paid')),
    (3, _('paid')),
    (4, _('delivared')),
    (5, _('closed')),
)


class CartItem(models.Model):
    """ article item in cart """
    cart = models.ForeignKey('Cart')
    item = models.ForeignKey(ArticleItem)
    quantity = models.PositiveIntegerField(_('quantity'), default=0)
    price = models.DecimalField(_('price'), max_digits=10, decimal_places=2)

    def get_price(self):
        """ calculate price """
        if self.item.currency == "H":
            return float(self.price)
        elif self.item.currency == "S":
            return float(self.price) * float(Constant.get_const('usd_currency'))
        elif self.item.currency == "E":
            return float(self.price) * float(Constant.get_const('euro_currency'))

    def get_total_price(self):
        """ return item total price """
        if self.item.currency == "H":
            return float(self.price) * float(self.quantity)
        elif self.item.currency == "S":
            return float(self.price) * float(self.quantity) * float(Constant.get_const('usd_currency'))
        elif self.item.currency == "E":
            return float(self.price) * float(self.quantity) * float(Constant.get_const('euro_currency'))

    def __unicode__(self):
        return unicode(self.item)

    class Meta:
        unique_together = ('cart', 'item')


class Cart(models.Model):
    """ customers orders """
    status = models.PositiveSmallIntegerField(_('status'), choices=CART_STATUS, default=1)
    user = models.ForeignKey(User, blank=True, null=True)
    email = models.EmailField(_('email'), blank=True)
    name = models.CharField(_('name'), blank=True, max_length=127)
    comment = models.TextField(_('comment'), blank=True)
    created_date = CreationDateTimeField(_('creation date'))
    updated_date = ModificationDateTimeField(_('modification date'))

    def clear_cache(self):
        pass

    def add(self, item, quantity):
        """ add item to cart """
        cartitem, _created = CartItem.objects.get_or_create(cart=self, item=item, price=item.price)
        cartitem.quantity += quantity
        cartitem.save()
        self.clear_cache()

    def remove(self, item):
        """ remove item from cart """
        CartItem.objects.filter(cart=self, item=item).delete()
        self.clear_cache()

    def quantity(self):
        """ count total quantity of cart """
        try:
            quantity = CartItem.objects.filter(cart=self).aggregate(total_quantity=Sum('quantity'))['total_quantity']
        except IndexError:
            quantity = 0
        if quantity:
            return int(quantity)
        else:
            return 0

    def price(self):
        """ count total cart price """
        total_price = sum(float(item.price) * float(item.quantity) for item in self)
        return total_price

    def total_price(self):
        """ count total cart price """
        total_price = sum(item.get_total_price() for item in self)
        return total_price

    def __unicode__(self):
        return u"%s - %d" % (_('cart'), self.pk)

    def __iter__(self):
        """ cart items iterator """
        cartitems = list(CartItem.objects.filter(cart=self))
        for item in cartitems:
            yield item

    class Meta:
        verbose_name = _('cart')
        verbose_name_plural = _('carts')
        ordering = ['-updated_date', '-created_date']


class ArticleCategorySitemap(Sitemap):
    """Sitemap for articles category."""

    changefreq = "daily"
    priority = 0.5

    def items(self):
        return ArticleCategory.objects.filter(published=True)

    def lastmod(self, obj):
        return obj.updated_date


class ArticleItemSitemap(Sitemap):
    """Sitemap for articles."""

    changefreq = "daily"
    priority = 0.8

    def items(self):
        return ArticleItem.objects.filter(published=True)

    def lastmod(self, obj):
        return obj.updated_date


tagging.register(ArticleItem)