#-*- coding:utf-8 -*-
"""
Common project views

Author:
    Vitaly Omelchuk <vitaly.omelchuk@gmail.com>
"""

from django.contrib.sitemaps.views import sitemap
from django.http import HttpResponse
from django.views.generic.list_detail import object_list
from django.contrib.sitemaps import FlatPageSitemap
from django.core.mail import mail_managers
from django.conf import settings
from django.shortcuts import redirect, get_object_or_404
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from main.forms import ContactForm

import os

from datetime import date, timedelta
from main.models import News
from eshop.models import (ArticleCategorySitemap, ArticleItemSitemap,
        ArticleItem, Cart, ArticleCategory)


def cached_sitemap(request):
    """ generate simap.xml onec a day and show saved version """
    sitemap_filename = os.path.join(settings.PROJECT_ROOT, 'sitemap.xml')
    if os.path.exists(sitemap_filename) and (date.fromtimestamp(os.path.getmtime(sitemap_filename)) - date.today()) < timedelta(days=1):
        with open(sitemap_filename, "r") as sitemap_file:
            raw_data = HttpResponse(sitemap_file.read(), mimetype="text/xml")
    else:
        sitemaps = {
                'eshop_categories' : ArticleCategorySitemap,
                'eshop_items'      : ArticleItemSitemap,
                'flatpages'        : FlatPageSitemap,
                }
        raw_data = sitemap(request, sitemaps=sitemaps)
        with open(sitemap_filename, "w") as sitemap_file:
            sitemap_file.write(raw_data.content)
    return raw_data

def search_view(request):
    """ full-text articles search """
    lookup_text = unicode(request.GET.get('q', None))
    if lookup_text is None:
        query = ArticleItem.objects.none()
    else:
        query = ArticleItem.objects.filter(Q(name__icontains=lookup_text) | Q(kod_tovara__icontains=lookup_text) | Q(categories__name=lookup_text))
    return object_list(request, queryset = query, template_name = "search.html", extra_context={'lookup_text':lookup_text})


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        city = form.cleaned_data['city']
        phone = form.cleaned_data['phone']
        message = form.cleaned_data['message']
        mail_managers('Letter from Himproekt.com', u'\n{name} \n{email} \n{city} \n{phone} \n{message}'.format(name=name, email=email, city=city, phone=phone, message=message))
        return HttpResponseRedirect(redirect_to='/')
    return render(request,'contact_form.html', {'form': form})

def send_cart(request):
    if request.method == "POST":
        if request.POST.get('honeypot'):
            return redirect('/cart')
        if request.session.get('cart', None):
            cart = get_object_or_404(Cart, pk=request.session.get('cart'))
        else:
            cart = Cart()
            if request.user.is_authenticated():
                cart.user  = request.user
                cart.email = request.user.email
                cart.name  = request.user.get_full_name()
            cart.save()
            request.session['cart'] = cart.pk

        if request.POST.get('submit') == u'Пересчитать':
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

            return redirect('/cart')

        if request.POST.get('submit') == u'Оформить заказ':
            if request.user.is_authenticated():
                cart.user = request.user
                cart.save()
            message = u"Ф.И.О. - %s\ne-mail: %s\nТелефон: %s\nСпособ оплаты: %s\nСпособ доставки: %s\nСлужба доставки: %s\nНомер почтового отделения: %s\nПримечание: %s\n \n" % (
                request.POST.get('name', request.user.get_profile().fio),
                request.POST.get('email', request.user.email),
                request.POST.get('phone', request.user.get_profile().phone),
                request.POST.get('pay'),
                request.POST.get('cargo'),
                request.POST.get('cargo-info'),
                request.POST.get('post-number'),
                request.POST.get('text', ''))
            for item in cart:
                message += u"%s, %s шт. (цена за шт. %s грн.) - Итого: %s грн.\n" % (item, item.quantity, item.price, item.get_total_price())
            message += u"\nОбщая сумма заказа: %s грн." % (cart.total_price())
            del request.session['cart']
            mail_managers("User cart", message, fail_silently=True)
    return redirect('/')
