# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ArticleItem.currency'
        db.add_column('eshop_articleitem', 'currency',
                      self.gf('django.db.models.fields.CharField')(default='H', max_length=1),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ArticleItem.currency'
        db.delete_column('eshop_articleitem', 'currency')


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
            'appearance': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'application_method': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'base_enamel': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'base_paint': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'batcher': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'bonded_materials': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'bonding_time': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '3', 'decimal_places': '0', 'blank': 'True'}),
            'chemical_composition': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'composition_type': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'consistency': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'consumption': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'current_max': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '3', 'decimal_places': '0', 'blank': 'True'}),
            'current_min': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '3', 'decimal_places': '0', 'blank': 'True'}),
            'current_race': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'decor_view': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'density': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'drying_time': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'dynamic_viscosity': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'electrode_consumption': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'electrode_cover': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'electrode_diameter': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'electrode_length': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'electrode_positions': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'electrode_type': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'electrode_use': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'filler_type': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'gloss': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'gloves_material': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'gloves_size': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'gloves_type': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'glue_type': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'glue_view': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'impact_strength': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'material_appointment': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'material_condition': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'material_proces_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'material_type': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'db_column': "'_order'"}),
            'package_weight': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '3', 'decimal_places': '1', 'blank': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['eshop.ArticleCategory']"}),
            'primer_type': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'product_type': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'protection': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'relative_extension': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'shelf_life': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '3', 'decimal_places': '0', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'soat_type': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'solvent_type': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'storage_temp_max': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '2', 'decimal_places': '0', 'blank': 'True'}),
            'storage_temp_min': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '2', 'decimal_places': '0', 'blank': 'True'}),
            'substances_content': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'tensile_strength': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'texture': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'treated_surface': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'updated_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'use_filler': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'using_material': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'using_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'varnish_type': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'video': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'warranty': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '3', 'decimal_places': '0', 'blank': 'True'}),
            'welding_rate': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'when_temp_20': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'work_temp_max': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '2', 'decimal_places': '0', 'blank': 'True'}),
            'work_temp_min': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '2', 'decimal_places': '0', 'blank': 'True'})
        },
        'eshop.articleimage': {
            'Meta': {'object_name': 'ArticleImage'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eshop.ArticleItem']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'eshop.articleitem': {
            'Meta': {'object_name': 'ArticleItem'},
            'action_product': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'can': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'categories': ('mptt.fields.TreeManyToManyField', [], {'symmetrical': 'False', 'related_name': "'articles'", 'null': 'True', 'to': "orm['eshop.ArticleCategory']"}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'currency': ('django.db.models.fields.CharField', [], {'default': "'H'", 'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'kod_tovara': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'new_product': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'db_column': "'_order'"}),
            'pack': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '2', 'decimal_places': '0', 'blank': 'True'}),
            'palette': ('django.db.models.fields.CharField', [], {'default': "'#ffffff'", 'max_length': '7', 'blank': 'True'}),
            'popular_product': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'present': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '10', 'decimal_places': '2'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'updated_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'})
        },
        'eshop.cart': {
            'Meta': {'ordering': "['-updated_date', '-created_date']", 'object_name': 'Cart'},
            'comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '127', 'blank': 'True'}),
            'status': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'updated_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
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