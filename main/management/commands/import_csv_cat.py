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
    'order',  # номер по порядку
    'id',  # айдишник
    'name',  # наименование
    'slug',  # слаг
    'parent_id',  # родительский айдишник
    'image',  # картинка
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
        category, _ = ArticleCategory.objects.get_or_create(id=row['id'])
        category.order = row['order'] if row['order'] else 0
        category.name = row['name']
        category.slug = row['slug']
        category.parent = ArticleCategory.objects.get(id=row['parent_id']) if row['parent_id'] else None
        category.image = row['image']
        category.save()

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