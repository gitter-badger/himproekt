# -*- coding: utf-8 -*-
from __future__ import print_function
import six
import os
import csv
import codecs
from django.conf import settings
from django.core.management.base import NoArgsCommand
from eshop.models import ArticleCategory, ArticleItem
from time import strftime


fields_name = (
    'is_category',  # признак категории
    'kod_tovara', # Код товара
    'name',  # наименование
    'union_name',  # Название товара
    'slug',  # слаг
    'description',  # описание
    'item_price',  # цена
    'currency',  # валюта
    'pack',  # мин. объем заказа
    'image',  # картинка
    'parent_id',  # родительский айдишник
    'id',  # айдишник товара
    'manufacturer',  # Производитель
    'country',  # Страна
    'property_name1',  #Свойство1
    'property_unit1',  #Ед. измерения1
    'property_value1',  # Значение1
    'property_name2',  #Свойство2
    'property_unit2',  #Ед. измерения2
    'property_value2',  # Значение2
    'property_name3',  #Свойство3
    'property_unit3',  #Ед. измерения3
    'property_value3',  # Значение3
    'property_name4',  #Свойство4
    'property_unit4',  #Ед. измерения4
    'property_value4',  # Значение4
    'property_name5',  #Свойство5
    'property_unit5',  #Ед. измерения5
    'property_value5',  # Значение5
    'property_name6',  #Свойство6
    'property_unit6',  #Ед. измерения6
    'property_value6',  # Значение6
    'property_name7',  #Свойство7
    'property_unit7',  #Ед. измерения7
    'property_value7',  # Значение7
    'property_name8',  #Свойство8
    'property_unit8',  #Ед. измерения8
    'property_value8',  # Значение8
    'property_name9',  #Свойство9
    'property_unit9',  #Ед. измерения9
    'property_value9',  # Значение9
    'property_name10',  #Свойство10
    'property_unit10',  #Ед. измерения10
    'property_value10',  # Значение10
    'property_name11',  #Свойство11
    'property_unit11',  #Ед. измерения11
    'property_value11',  # Значение11
    'property_name12',  #Свойство12
    'property_unit12',  #Ед. измерения12
    'property_value12',  # Значение12
    'property_name13',  #Свойство13
    'property_unit13',  #Ед. измерения13
    'property_value13',  # Значение13
    'property_name14',  #Свойство14
    'property_unit14',  #Ед. измерения14
    'property_value14',  # Значение14
    'property_name15',  #Свойство15
    'property_unit15',  #Ед. измерения15
    'property_value15',  # Значение15
    'property_name16',  #Свойство16
    'property_unit16',  #Ед. измерения16
    'property_value16',  # Значение16
    'property_name17',  #Свойство17
    'property_unit17', #Ед. измерения17
    'property_value17',  # Значение17
    'property_name18',  #Свойство18
    'property_unit18',  #Ед. измерения18
    'property_value18',  # Значение18
    'property_name19',  #Свойство19
    'property_unit19',  #Ед. измерения19
    'property_value19',  # Значение19
)


class UTF8Recoder:
    """
    Iterator that reads an encoded stream and reencodes the input to UTF-8
    """
    def __init__(self, f, encoding):
        self.reader = codecs.getreader(encoding)(f)

    def __iter__(self):
        return self

    def next(self):
        return self.reader.next().encode('utf-8')


class UnicodeReader:
    """
    A CSV reader which will iterate over lines in the CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding='utf-8', reader=csv.reader, **kwargs):
        f = UTF8Recoder(f, encoding)
        self.reader = reader(f, dialect=dialect, **kwargs)

    def next(self):
        row = self.reader.next()
        if isinstance(row, (list, tuple)):
            return [unicode(s, 'utf-8') for s in row]
        if isinstance(row, dict):
            return dict((k, unicode(v.strip(), 'utf-8') if isinstance(v, six.string_types) else v) for k, v in six.iteritems(row))

    def __iter__(self):
        return self


def do_import_file(reader, stderr):
    ArticleItem.objects.all().update(published=False)
    for number, row in enumerate(reader):
        if number < 1:
            continue
        print(row)
        #try:
        article, _ = ArticleItem.objects.get_or_create(id=row['id'])
        article.categories.add(ArticleCategory.objects.get(id=row['parent_id']))
        article.name = row['name']
        article.union_name = row['union_name']
        article.slug = row['slug']
        article.description = row['description']
        article.price = row['item_price'].replace(',', '.') if row['item_price'] else 0
        article.currency = row['currency']
        article.pack = row['pack'] if row['pack'] else 0
        article.image = row['image']
        article.kod_tovara = row['kod_tovara']
        article.published = bool(row['item_price'])
        article.manufacturer = row['manufacturer']
        article.country = row['country']
        article.property_name1 = row['property_name1']
        article.property_unit1 = row['property_unit1']
        article.property_value1 = row['property_value1']
        article.property_name2 = row['property_name2']
        article.property_unit2 = row['property_unit2']
        article.property_value2 = row['property_value2']
        article.property_name3 = row['property_name3']
        article.property_unit3 = row['property_unit3']
        article.property_value3 = row['property_value3']
        article.property_name4 = row['property_name4']
        article.property_unit4 = row['property_unit4']
        article.property_value4 = row['property_value4']
        article.property_name5 = row['property_name5']
        article.property_unit5 = row['property_unit5']
        article.property_value5 = row['property_value5']
        article.property_name6 = row['property_name6']
        article.property_unit6 = row['property_unit6']
        article.property_value6 = row['property_value6']
        article.property_name7 = row['property_name7']
        article.property_unit7 = row['property_unit7']
        article.property_value7 = row['property_value7']
        article.property_name8 = row['property_name8']
        article.property_unit8 = row['property_unit8']
        article.property_value8 = row['property_value8']
        article.property_name9 = row['property_name9']
        article.property_unit9 = row['property_unit9']
        article.property_value9 = row['property_value9']
        article.property_name10 = row['property_name10']
        article.property_unit10 = row['property_unit10']
        article.property_value10 = row['property_value10']
        article.property_name11 = row['property_name11']
        article.property_unit11 = row['property_unit11']
        article.property_value11 = row['property_value11']
        article.property_name12 = row['property_name12']
        article.property_unit12 = row['property_unit12']
        article.property_value12 = row['property_value12']
        article.property_name13 = row['property_name13']
        article.property_unit13 = row['property_unit13']
        article.property_value13 = row['property_value13']
        article.property_name14 = row['property_name14']
        article.property_unit14 = row['property_unit14']
        article.property_value14 = row['property_value14']
        article.property_name15 = row['property_name15']
        article.property_unit15 = row['property_unit15']
        article.property_value15 = row['property_value15']
        article.property_name16 = row['property_name16']
        article.property_unit16 = row['property_unit16']
        article.property_value16 = row['property_value16']
        article.property_name17 = row['property_name17']
        article.property_unit17 = row['property_unit17']
        article.property_value17 = row['property_value17']
        article.property_name18 = row['property_name18']
        article.property_unit18 = row['property_unit18']
        article.property_value18 = row['property_value18']
        article.property_name19 = row['property_name19']
        article.property_unit19 = row['property_unit19']
        article.property_value19 = row['property_value19']
        article.save()

        #except Exception as e:
        #    stderr.write(u'Error in line number {0}. Data: {1}\nError: {2}'.format(number, row, e))
        #    continue

    ArticleCategory.objects.rebuild()


class Command(NoArgsCommand):
    """ Import price from csv file """

    help = "Import price from csv file"
    output_transaction = True

    def handle_noargs(self, **options):
        csv_file_name = settings.PRICE_FILE
        if not os.access(csv_file_name, os.R_OK):
            return

        with open(csv_file_name, 'rb') as f:
            reader = UnicodeReader(f, encoding='cp1251', delimiter=';', reader=csv.DictReader, fieldnames=fields_name, restkey='other')
            do_import_file(reader, self.stderr)

        os.system("mv %s %s.bak" % (csv_file_name, csv_file_name))