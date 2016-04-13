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
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', verbose_name=u'Родитель')
    image = models.ImageField(_('image'), upload_to="pictures", blank=True)
    description = models.TextField(_('description'), blank=True)
    video = models.CharField(u'Youtube', max_length=255, blank=True)
    published = models.BooleanField(_('published'), default=True)
    created_date = CreationDateTimeField(_('creation date'))
    updated_date = ModificationDateTimeField(_('modification date'))
    manufacturer = models.CharField(u'Производитель', max_length=32, blank=True)
    country = models.CharField(u'Страна', max_length=32, blank=True)
    using_type = models.CharField(u'Тип использования', max_length=200, blank=True)
    using_material = models.CharField(u'Тип окрашиваемого материала', max_length=200, blank=True)
    base_paint = models.CharField(u'Основа краски', max_length=100, blank=True)
    consumption = models.CharField(u'Расход (кв.м)', max_length=64, blank=True)
    drying_time = models.DecimalField(u'Время высыхания (час)', max_digits=4, decimal_places=2, blank=True, default=0)
    gloss = models.CharField(u'Степень блеска', max_length=32, blank=True)
    work_temp_min = models.DecimalField(u'Мин. рабочая температора', max_digits=2, decimal_places=0, blank=True, default=0)
    work_temp_max = models.DecimalField(u'Макс. рабочая температора', max_digits=2, decimal_places=0, blank=True, default=0)
    storage_temp_min = models.DecimalField(u'Мин. температора хранения', max_digits=2, decimal_places=0, blank=True, default=0)
    storage_temp_max = models.DecimalField(u'Макс. температора хранения', max_digits=2, decimal_places=0, blank=True, default=0)
    application_method = models.CharField(u'Способ нанесения', max_length=100, blank=True)
    shelf_life = models.DecimalField(u'Срок храниения (мес)', max_digits=2, decimal_places=0, blank=True, default=0)
    base_enamel = models.CharField(u'Основа эмали', max_length=64, blank=True)
    material_proces_type = models.CharField(u'Вид обрабатываемого материала', max_length=200, blank=True)
    primer_type = models.CharField(u'Вид грунтовки', max_length=32, blank=True)
    varnish_type = models.CharField(u'Вид лака', max_length=32, blank=True)
    glue_type = models.CharField(u'Тип клея', max_length=32, blank=True)
    glue_view = models.CharField(u'Вид клея', max_length=32, blank=True)
    bonded_materials = models.CharField(u'Вид склеиваемых материалов', max_length=255, blank=True)
    consistency = models.CharField(u'Консистенция', max_length=32, blank=True)
    batcher = models.CharField(u'Дозатор', max_length=32, blank=True)
    bonding_time = models.DecimalField(u'Время склеивания (сек)', max_digits=3, decimal_places=0, blank=True, default=0)
    shelf_life = models.DecimalField(u'Срок годности (мес)', max_digits=3, decimal_places=0, blank=True, default=0)
    filler_type = models.CharField(u'Тип шпатлевки', max_length=32, blank=True)
    use_filler = models.CharField(u'Назначение шпатлевки', max_length=100, blank=True)
    treated_surface = models.CharField(u'Тип обрабатываемой поверхности', max_length=255, blank=True)
    soat_type = models.CharField(u'Вид пропитки', max_length=32, blank=True)
    composition_type = models.CharField(u'Тип по составу', max_length=32, blank=True)
    decor_view = models.CharField(u'Вид декоративной штукатурки', max_length=32, blank=True)
    texture = models.CharField(u'Фактура', max_length=32, blank=True)
    material_appointment = models.CharField(u'Назначение материала', max_length=32, blank=True)
    material_condition = models.CharField(u'Состояние материала', max_length=32, blank=True)
    appearance = models.CharField(u'Внешний вид', max_length=32, blank=True)
    substances_content = models.CharField(u'Содержание нелетучих веществ, %', max_length=32, blank=True)
    dynamic_viscosity = models.CharField(u'Динамическая вязкость, мПа*с', max_length=32, blank=True)
    density = models.CharField(u'Плотность, кг/л', max_length=32, blank=True)
    product_type = models.CharField(u'Вид изделия', max_length=32, blank=True)
    protection = models.CharField(u'Защита от', max_length=32, blank=True)
    gloves_type = models.CharField(u'Типы перчаток', max_length=32, blank=True)
    gloves_size = models.CharField(u'Размер перчаток', max_length=32, blank=True)
    gloves_material = models.CharField(u'Материал перчаток', max_length=32, blank=True)
    solvent_type = models.CharField(u'Вид растворителя', max_length=32, blank=True)
    material_type = models.CharField(u'Вид материала', max_length=32, blank=True)
    electrode_diameter = models.CharField(u'Диаметр электрода (мм)', max_length=32, blank=True)
    electrode_length = models.CharField(u'Длина электрода (мм)', max_length=32, blank=True)
    electrode_type = models.CharField(u'Тип электрода', max_length=32, blank=True)
    electrode_cover = models.CharField(u'Тип покрытого электрода по покрытию', max_length=64, blank=True)
    electrode_use = models.CharField(u'Тип покрытого электрода по применению', max_length=64, blank=True)
    electrode_positions = models.CharField(u'Тип покрытого электрода по положениям сварки в пространстве', max_length=64, blank=True)
    current_max = models.DecimalField(u'Максимальный сварочный ток (А)', max_digits=3, decimal_places=0, blank=True, default=0)
    current_min = models.DecimalField(u'Минимальный сварочный ток (А)', max_digits=3, decimal_places=0, blank=True, default=0)
    package_weight = models.DecimalField(u'Вес упаковки (кг)', max_digits=3, decimal_places=0, blank=True, default=0)
    warranty = models.DecimalField(u'Гарантийный срок (мес)', max_digits=3, decimal_places=0, blank=True, default=0)
    current_race = models.CharField(u'Род тока', max_length=32, blank=True)
    welding_rate = models.CharField(u'Коэффициент наплавки, г/Ач', max_length=32, blank=True)
    electrode_consumption = models.CharField(u'Расход электродов на 1кг наплавленного металла, кг', max_length=32, blank=True)
    tensile_strength = models.CharField(u'Временное сопротивление разрыву, МПа', max_length=32, blank=True)
    relative_extension = models.CharField(u'Относительное удлинение, %', max_length=32, blank=True)
    impact_strength = models.CharField(u'Ударная вязкость, Дж/см2', max_length=32, blank=True)
    when_temp_20 = models.CharField(u'При t - 20 °С', max_length=32, blank=True)
    chemical_composition = models.CharField(u'Химический состав наплавленного металла, %', max_length=32, blank=True)

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
    name = models.CharField(_('name'), max_length=255, unique=True)
    slug = models.SlugField(_('Slug'), max_length=255, editable=True)
    categories = TreeManyToManyField(ArticleCategory, null=True, related_name='articles')
    palette = models.CharField(u'Выберите цвет', max_length=7, blank=True, default="#ffffff")
    color = models.CharField(u'Название цвета', max_length=50, blank=True)
    kod_tovara = models.CharField(u'Код товара', max_length=50, blank=True)
    image = models.ImageField(_('image'), upload_to="upload", blank=True)
    published = models.BooleanField(_('published'), default=True)
    price = models.DecimalField(_('price'), max_digits=10, decimal_places=2, default=0)
    created_date = CreationDateTimeField(_('creation date'))
    updated_date = ModificationDateTimeField(_('modification date'))
    present = models.BooleanField(u'Есть в наличии', default=True)
    can = models.CharField(u'Объем', max_length=10, blank=True)
    pack = models.DecimalField(u'упаковка (шт.)', max_digits=2, decimal_places=0, default=0, blank=True)
    popular_product = models.BooleanField(u'Популярное', default=False)
    new_product = models.BooleanField(u'Новинки', default=False)
    action_product = models.BooleanField(u'Акции и скидки', default=False)

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
        try:
            return float(self.price) * float(Constant.get_const('currency'))
        except TypeError:
            return float(self.price)

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

    @models.permalink
    def get_absolute_url(self):
        """ return object url """
        if self.slug:
            return ('eshop_item_slug', (), {'slug': self.slug})
        else:
            return ('eshop_item', (), {'object_id': self.pk})

    class Meta:
        verbose_name = _('article')
        verbose_name_plural = _('articles')


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
        try:
            return float(self.price) * float(Constant.get_const('currency'))
        except TypeError:
            return float(self.price)

    def get_total_price(self):
        """ return item total price """
        try:
            return float(self.price) * float(self.quantity) * float(Constant.get_const('currency'))
        except TypeError:
            return float(self.price) * float(self.quantity)

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
