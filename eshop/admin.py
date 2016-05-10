from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from eshop.models import ArticleCategory, ArticleItem, Cart, CartItem, ArticleImage
from eshop.forms import ArticleItemAdminForm, CartItemAdminForm
from tagging.fields import TagField
from django.utils.translation import ugettext as _
from main.widgets import ColorPickerWidget

class ArticleImageInlineAdmin(admin.TabularInline):
    model = ArticleImage
    exta = 1

class ArticleItemInlineAdmin(admin.TabularInline):
    """ customize cart item admin page """
    fields = ('order', 'name', 'description', 'image', 'published', 'price')
    model  = ArticleItem
    extra  = 1

class ArticleCategoryAdmin(MPTTModelAdmin):
    """Customize article's category admin page."""

    search_fields = ('id', 'name',)
    list_display = ('get_thumbnail_html', 'name', 'published', 'order',)
    list_filter  = ('published',)
    ordering     = ('name', 'published')
    list_display_links = ('name',)
    #inlines      = (ArticleItemInlineAdmin, )
    list_editable = ('published',)
    prepopulated_fields = {"slug": ("name",)}
    save_on_top  = True

    class Media:
        js = ('tiny_mce/tiny_mce.js', 'tiny_mce/init.js')

class ArticleItemAdmin(admin.ModelAdmin):
    """Customize article admin page"""

    form = ArticleItemAdminForm
    search_fields = ('id', 'name', 'kod_tovara')
    list_display = ('name', 'price', 'currency', 'action_product', 'popular_product','new_product','present', 'published')
    list_display_links = ('name',)
    list_filter  = ('action_product', 'published', 'categories')
    ordering     = ('name', 'categories', 'published')
    inlines = (ArticleImageInlineAdmin, )
    prepopulated_fields = {"slug": ("name",)}
    list_editable = ('price', 'currency', 'action_product', 'popular_product','new_product', 'present', 'published')

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'palette':
            kwargs['widget'] = ColorPickerWidget
        return super(ArticleItemAdmin, self).formfield_for_dbfield(db_field, **kwargs)


    class Media:
        js = ('tiny_mce/tiny_mce.js', 'tiny_mce/init.js')

class CartItemInlineAdmin(admin.TabularInline):
    """ customize cart item admin page """

    #form = CartItemAdminForm
    model = CartItem
    extra = 1
    #raw_id_fields = ('item',)
    fields = ('price', 'quantity')
    readonly_fields = ('price', 'quantity')

class CartAdmin(admin.ModelAdmin):
    """ customize cart admin page """

    fieldsets = (
            (_('Options'), {
                'classes'  : ('collapse',),
                'fields'   : ('user', 'email', 'name', 'status', 'comment', 'created_date', 'updated_date')
                }),
            )
    save_on_top     = True
    save_as         = True
    list_display    = ('__unicode__', 'quantity', 'price')
    list_filter     = ('user', )
    date_hierarchy  = 'created_date'
    readonly_fields = ('status', 'created_date', 'updated_date')
    search_fields   = ('id',)
    inlines = [
            CartItemInlineAdmin,
            ]

admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(ArticleItem, ArticleItemAdmin)
admin.site.register(Cart, CartAdmin)
