from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template
from django.conf import settings
from django.views.generic.list_detail import object_detail
from eshop.models import ArticleCategorySitemap, ArticleItemSitemap
from eshop.views import show_cart
from main.models import News
from main.views import cached_sitemap, search_view, contact, send_cart
from hcprofile.forms import ExRegistrationForm
from registration.backends.default.views import RegistrationView
from hcprofile.signals import *
from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
admin.autodiscover()

sitemaps = {
    'eshop_categories' : ArticleCategorySitemap,
    'eshop_items'      : ArticleItemSitemap,
    'flatpages': FlatPageSitemap,
}

urlpatterns = patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'accounts/register/$', RegistrationView.as_view(form_class = ExRegistrationForm), name = 'registration_register'),
    (r'^accounts/', include('registration.urls')),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page':'/production/'}),
    (r'^admin/', include(admin.site.urls)),
    #(r'^robots.txt$', include('robots.urls')),
    (r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    (r'^captcha/', include('captcha.urls')),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^search/$', search_view, {}, 'search'),
    url(r'^news/(?P<slug>[-\w]+)/$', object_detail, {
        'queryset' : News.objects.filter(published=True),
        'template_object_name' : 'news',
        },
        name='main_news_slug'),
    url(r'contact-form/$', contact, {}, 'contact_form'),
    url(r'^send-cart/$', send_cart, name="send_cart"),
    (r'^$', direct_to_template, {
        'template': 'index.html',
        }),
    (r'^production/', direct_to_template, {
        'template':'production.html',
        }),
    (r'^news/', direct_to_template, {
        'template': 'news.html',
        'extra_context': {
            'all_news': News.objects.all_news(),
            },
        }),
    (r'^price/', direct_to_template, {
        'template': 'price.html',
        }),
    (r'^actions/', direct_to_template, {
        'template': 'actions.html',
        }),
    (r'^new/', direct_to_template, {
        'template': 'new.html',
        }),
    (r'^popular/', direct_to_template, {
        'template': 'popular.html',
        }),
    (r'^robots.txt$', direct_to_template, {
        'template': 'robots.txt',
        }),
    url(r'cart/$', show_cart, name="eshop-showcart"),
    (r'^', include('eshop.urls')),
)