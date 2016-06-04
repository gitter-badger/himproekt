from django.conf.urls import url, patterns
import eshop.views
from eshop.views import articleitem_detail

urlpatterns = patterns('',
                       url(r'^(?P<category>[-\w]+)/(?P<slug>[-\w]+)/$', articleitem_detail,
                           name='eshop_item_slug'),
                       url(r'^eshop_item/(?P<object_id>\d+)/addtocart/(?P<quantity>\d+)/',
                           eshop.views.add_to_cart,
                           name="add_to_cart"),
                       url(r'cart/$', eshop.views.show_cart, name="eshop-showcart"),
                       url(r'^(?P<slug>[-\w]+)/$', eshop.views.category_detail, name='eshop_category_slug'),
                       )
