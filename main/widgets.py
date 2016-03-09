# -*- coding:utf-8 -*-

from django.forms.widgets import TextInput
from django.utils.translation import gettext as _
from django.utils.html import mark_safe

class ColorPickerWidget(TextInput):
    class Media:
        css = {
            'all': ('css/farbtastic.css',)
            }
        js = ('js/colorpicker.js',
              'js/jquery-1.8.2.min.js',
              'js/farbtastic.js',)

    def render(self, name, value, attrs=None):
        text_input_html = super(ColorPickerWidget, self).render(name, value, attrs)
        text_link_html = u'<a id="id_color_picker" href="#" onclick="return false;">%s</a>' % _(u'Нажмите, что бы выбрать оттенок (белый по умолчанию)')
        return mark_safe('%s %s' % (text_input_html, text_link_html))