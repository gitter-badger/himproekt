# -*- coding: utf-8 -*-
from __future__ import print_function
import six
import os
import csv
import codecs
from django.conf import settings
from django.core.management.base import NoArgsCommand
from django.core.cache import cache
from supplementary.models import Constant
from main.models import Category, Article, ImportList


fields_name = (
    'name',  # имя товара
    'id',  # айдишник товара
    'category_name',  # имя категории товара
    'category_id',  # айдишник категории
    'count',  # кол-во товара
    'article',  # артикул товара
    'image',  # путь к картинке
    'novelty',  # новинка 1 -да, 0 -нет
    'price1',  # цена по первой колонке
    'price2',  # цена по второй колонке
    'price3',  # цена по третьей колонке
    'hit',  # хит 1 - да, 0 - нет
    'our',  # эксклюзив 1 - да, 0 - нет
    'discount',  # акция 1 - да, 0 - нет
    'warehouse1',  # первый склад  1- присутствует, 0 - нет
    'warehouse2',  # второй склад  1- присутствует, 0 - нет
    'withoutdiscount',  # товар без скидки 1 - да, 0 - со скидкой
    'new_income',  # товар новый приход 1 - да, 0 - нет.
    'new_spec',  # товар спецпредложение 1 - да, 0 - нет.
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
    currency_stock_row = next(reader)
    const, _ = Constant.objects.get_or_create(name='currency')
    const.value = currency_stock_row['name']
    const.save()
    cache.delete('currency')
    Article.objects.all().update(published=False)
    for number, row in enumerate(reader):
        try:
            if 'other' in row:
                article, _ = Article.objects.get_or_create(id=row['id'])
                article.category_id = row['category_id']
                article.name = row['name']
                article.article = row['article']
                article.price1 = str(float(row['price1']))
                article.price2 = str(float(row['price2']))
                article.price3 = str(float(row['price3']))
                article.count = int(row['count'])
                article.warehouse1 = bool(row['warehouse1'] == '1')
                article.warehouse2 = bool(row['warehouse2'] == '1')
                article.discount = bool(row['withoutdiscount'] == '1')
                article.image = row['image'][16:].replace("\\", "/")
                article.new = bool(row['novelty'] == '1')
                article.our = bool(row['our'] == '1')
                article.action = bool(row['discount'] == '1')
                article.new_income = bool(row['new_income'] == '1')
                article.new_spec = bool(row['new_spec'] == '1')
                article.published = True
                article.save()
            else:
                category, _ = Category.objects.get_or_create(id=row['id'])
                category.name = row['name']
                category.parent = Category.objects.get(id=row['category_id']) if row['category_id'] else None
                category.save()
        except Exception as e:
            stderr.write(u'Error in line number {0}. Data: {1}\nError: {2}'.format(number, row, e))
            continue

    Category.objects.rebuild()
    ImportList.objects.create(import_count=number)


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