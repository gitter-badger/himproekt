# -*- coding:utf-8 -*-
"""
Eshop views

Author:
    Vitaly Omelchuk <vitaly.omelchuk@gmail.com>
"""
import os
from PIL import Image

from django.views.decorators.cache import never_cache
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.list_detail import object_detail
from django.views.generic.simple import direct_to_template
from django.utils import simplejson as json
from eshop.models import ArticleItem, ArticleCategory, Cart


@never_cache
def add_to_cart(request, object_id, quantity=0):
    """ add item in cart """
    try:
        object_id = int(object_id)
    except ValueError:
        object_id = 0
    item = get_object_or_404(ArticleItem, pk=object_id) if object_id else None
    if request.session.get('cart', None) and Cart.objects.filter(pk=request.session.get('cart')).exists():
        cart = Cart.objects.get(pk=request.session.get('cart'))
    else:
        cart = Cart()
        if request.user.is_authenticated():
            cart.user = request.user
            cart.email = request.user.email
            cart.name = request.user.get_full_name()
        cart.save()
        request.session['cart'] = cart.pk
    try:
        quantity = int(quantity)
    except ValueError:
        quantity = 0
    if quantity:
        cart.add(item, quantity)
    else:
        cart.remove(item)
    if request.is_ajax():
        data = {
            'total_count': u"%s" % cart.quantity(),
            'total_price': u"%.1f" % cart.total_price(),
        }
        return HttpResponse(json.dumps(data), mimetype="application/json")
    else:
        return redirect(request.META.get('HTTP_REFERER', '/'))


@never_cache
def show_cart(request):
    """ show cart """
    if request.session.get('cart', None):
        cart = get_object_or_404(Cart, pk=request.session.get('cart'))
    else:
        cart = Cart()
        if request.user.is_authenticated():
            cart.user = request.user
            cart.email = request.user.email
            cart.name = request.user.get_full_name()
        cart.save()
        request.session['cart'] = cart.pk
    if request.method == "POST" and cart is not None:
        for item in cart:
            try:
                new_quantity = int(request.POST.get(str(item.id), None))
            except ValueError:
                continue
            if new_quantity is not None and item.quantity != new_quantity:
                if new_quantity:
                    item.quantity = new_quantity
                    item.save()
                else:
                    item.delete()
    cart.clear_cache()
    return direct_to_template(request, 'eshop/cart.html', extra_context={'cart': cart})


def category_detail(request, slug):
    category = get_object_or_404(ArticleCategory, slug=slug)
    child_articles = category.articles.filter(published=True).order_by('union_name', 'palette')
    manufacturers = request.GET.getlist('sort_by')
    if manufacturers:
        child_articles = child_articles.filter(manufacturer__in=manufacturers)
    extra_context = {
        'category': category,
        'child_categories': category.get_children().filter(published=True).order_by('name'),
        'child_articles': child_articles,
        'filter_articles': set(category.articles.exclude(manufacturer="").order_by('manufacturer').values_list('manufacturer', flat=True)),
        'selected_manufactures': manufacturers,
    }
    return direct_to_template(request, 'eshop/articlecategory_detail.html', extra_context=extra_context)


def articleitem_detail(request, slug, category, **kwargs):
    return object_detail(request, slug=slug, template_object_name='item', queryset=ArticleItem.objects.filter(published="+"))