from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_detail
import eshop.views
from eshop.models import ArticleItem

urlpatterns = patterns('',
        url(r'^category/(?P<slug>[-\w]+)/$', eshop.views.category_detail, name='eshop_category_slug'),
        url(r'^item/(?P<slug>[-\w]+)/$', object_detail, {
            'queryset' : ArticleItem.objects.filter(published="+"),
            'template_object_name' : 'item',
            },
            name='eshop_item_slug'),
        url(r'^item/(?P<object_id>\d+)/addtocart/(?P<quantity>\d+)/',
            eshop.views.add_to_cart,
            name="add_to_cart"),
            url(r'cart/$', eshop.views.show_cart, name="eshop-showcart")
            )