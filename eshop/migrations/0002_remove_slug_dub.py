# -*- coding: utf-8 -*-
import string

import random
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Don't use "from appname.models import ModelName". 
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.
        for article_item in orm['eshop.ArticleItem'].objects.all():
            for dub_article_item in orm['eshop.ArticleItem'].objects.filter(slug=article_item.slug).exclude(pk=article_item.pk):
                dub_article_item.slug = dub_article_item.slug + '_{}'.format(random.choice(string.ascii_uppercase))
                dub_article_item.save()

    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'eshop.articlecategory': {
            'Meta': {'ordering': "['order', 'name']", 'object_name': 'ArticleCategory'},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'descriptions': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'db_column': "'_order'"}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['eshop.ArticleCategory']"}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'updated_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'eshop.articleimage': {
            'Meta': {'object_name': 'ArticleImage'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eshop.ArticleItem']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'eshop.articleitem': {
            'Meta': {'ordering': "['union_name', 'order']", 'object_name': 'ArticleItem'},
            'action_product': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'can': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'categories': ('mptt.fields.TreeManyToManyField', [], {'symmetrical': 'False', 'related_name': "'articles'", 'null': 'True', 'to': "orm['eshop.ArticleCategory']"}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'currency': ('django.db.models.fields.CharField', [], {'default': "'H'", 'max_length': '1'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'descriptions': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'kod_tovara': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'new_product': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'db_column': "'_order'"}),
            'pack': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '4', 'decimal_places': '0', 'blank': 'True'}),
            'palette': ('django.db.models.fields.CharField', [], {'default': "'#ffffff'", 'max_length': '7', 'blank': 'True'}),
            'popular_product': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'present': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '10', 'decimal_places': '2'}),
            'property_name1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_name10': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_name11': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_name12': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_name13': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_name14': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_name15': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_name16': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_name17': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_name18': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_name19': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_name2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_name20': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_name3': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_name4': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_name5': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_name6': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_name7': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_name8': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_name9': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_unit1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_unit10': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_unit11': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_unit12': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_unit13': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_unit14': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_unit15': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_unit16': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_unit17': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_unit18': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_unit19': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_unit2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_unit20': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_unit3': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_unit4': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_unit5': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_unit6': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_unit7': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_unit8': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_unit9': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_value1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_value10': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_value11': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_value12': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_value13': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_value14': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_value15': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_value16': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_value17': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_value18': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_value19': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_value2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_value20': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_value3': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_value4': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_value5': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_value6': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_value7': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_value8': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_value9': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'union_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'updated_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'eshop.cart': {
            'Meta': {'ordering': "['-updated_date', '-created_date']", 'object_name': 'Cart'},
            'comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '127', 'blank': 'True'}),
            'status': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'updated_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'eshop.cartitem': {
            'Meta': {'unique_together': "(('cart', 'item'),)", 'object_name': 'CartItem'},
            'cart': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eshop.Cart']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eshop.ArticleItem']"}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'quantity': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['eshop']
    symmetrical = True
