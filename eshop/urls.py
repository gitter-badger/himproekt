from django.conf.urls import url, patterns
from django.contrib.auth.decorators import login_required

import eshop.views
from eshop.views import articleitem_detail, WishListView

urlpatterns = patterns('',
                       url(r'^eshop_item/(?P<object_id>\d+)/addtocart/(?P<quantity>\d+)/',
                           eshop.views.add_to_cart,
                           name="add_to_cart"),
                       url(r'eshop_item/wishlist/$', login_required(WishListView.as_view()), name='add_wishlist'),
                       url(r'^(?P<category>[-\w]+)/(?P<slug>[-\w]+)/$', articleitem_detail,
                           name='eshop_item_slug'),
                       url(r'^(?P<slug>[-\w]+)/$', eshop.views.category_detail, name='eshop_category_slug'),
                       )
