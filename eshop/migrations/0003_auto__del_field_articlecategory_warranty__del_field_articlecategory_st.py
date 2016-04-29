# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ArticleCategory.warranty'
        db.delete_column('eshop_articlecategory', 'warranty')

        # Deleting field 'ArticleCategory.storage_temp_max'
        db.delete_column('eshop_articlecategory', 'storage_temp_max')

        # Deleting field 'ArticleCategory.electrode_length'
        db.delete_column('eshop_articlecategory', 'electrode_length')

        # Deleting field 'ArticleCategory.electrode_cover'
        db.delete_column('eshop_articlecategory', 'electrode_cover')

        # Deleting field 'ArticleCategory.using_type'
        db.delete_column('eshop_articlecategory', 'using_type')

        # Deleting field 'ArticleCategory.material_type'
        db.delete_column('eshop_articlecategory', 'material_type')

        # Deleting field 'ArticleCategory.electrode_positions'
        db.delete_column('eshop_articlecategory', 'electrode_positions')

        # Deleting field 'ArticleCategory.glue_view'
        db.delete_column('eshop_articlecategory', 'glue_view')

        # Deleting field 'ArticleCategory.composition_type'
        db.delete_column('eshop_articlecategory', 'composition_type')

        # Deleting field 'ArticleCategory.work_temp_max'
        db.delete_column('eshop_articlecategory', 'work_temp_max')

        # Deleting field 'ArticleCategory.soat_type'
        db.delete_column('eshop_articlecategory', 'soat_type')

        # Deleting field 'ArticleCategory.storage_temp_min'
        db.delete_column('eshop_articlecategory', 'storage_temp_min')

        # Deleting field 'ArticleCategory.current_race'
        db.delete_column('eshop_articlecategory', 'current_race')

        # Deleting field 'ArticleCategory.batcher'
        db.delete_column('eshop_articlecategory', 'batcher')

        # Deleting field 'ArticleCategory.filler_type'
        db.delete_column('eshop_articlecategory', 'filler_type')

        # Deleting field 'ArticleCategory.consumption'
        db.delete_column('eshop_articlecategory', 'consumption')

        # Deleting field 'ArticleCategory.chemical_composition'
        db.delete_column('eshop_articlecategory', 'chemical_composition')

        # Deleting field 'ArticleCategory.impact_strength'
        db.delete_column('eshop_articlecategory', 'impact_strength')

        # Deleting field 'ArticleCategory.gloves_type'
        db.delete_column('eshop_articlecategory', 'gloves_type')

        # Deleting field 'ArticleCategory.gloss'
        db.delete_column('eshop_articlecategory', 'gloss')

        # Deleting field 'ArticleCategory.base_paint'
        db.delete_column('eshop_articlecategory', 'base_paint')

        # Deleting field 'ArticleCategory.texture'
        db.delete_column('eshop_articlecategory', 'texture')

        # Deleting field 'ArticleCategory.use_filler'
        db.delete_column('eshop_articlecategory', 'use_filler')

        # Deleting field 'ArticleCategory.treated_surface'
        db.delete_column('eshop_articlecategory', 'treated_surface')

        # Deleting field 'ArticleCategory.bonded_materials'
        db.delete_column('eshop_articlecategory', 'bonded_materials')

        # Deleting field 'ArticleCategory.application_method'
        db.delete_column('eshop_articlecategory', 'application_method')

        # Deleting field 'ArticleCategory.gloves_size'
        db.delete_column('eshop_articlecategory', 'gloves_size')

        # Deleting field 'ArticleCategory.using_material'
        db.delete_column('eshop_articlecategory', 'using_material')

        # Deleting field 'ArticleCategory.work_temp_min'
        db.delete_column('eshop_articlecategory', 'work_temp_min')

        # Deleting field 'ArticleCategory.decor_view'
        db.delete_column('eshop_articlecategory', 'decor_view')

        # Deleting field 'ArticleCategory.base_enamel'
        db.delete_column('eshop_articlecategory', 'base_enamel')

        # Deleting field 'ArticleCategory.drying_time'
        db.delete_column('eshop_articlecategory', 'drying_time')

        # Deleting field 'ArticleCategory.current_max'
        db.delete_column('eshop_articlecategory', 'current_max')

        # Deleting field 'ArticleCategory.current_min'
        db.delete_column('eshop_articlecategory', 'current_min')

        # Deleting field 'ArticleCategory.gloves_material'
        db.delete_column('eshop_articlecategory', 'gloves_material')

        # Deleting field 'ArticleCategory.solvent_type'
        db.delete_column('eshop_articlecategory', 'solvent_type')

        # Deleting field 'ArticleCategory.electrode_use'
        db.delete_column('eshop_articlecategory', 'electrode_use')

        # Deleting field 'ArticleCategory.varnish_type'
        db.delete_column('eshop_articlecategory', 'varnish_type')

        # Deleting field 'ArticleCategory.substances_content'
        db.delete_column('eshop_articlecategory', 'substances_content')

        # Deleting field 'ArticleCategory.when_temp_20'
        db.delete_column('eshop_articlecategory', 'when_temp_20')

        # Deleting field 'ArticleCategory.protection'
        db.delete_column('eshop_articlecategory', 'protection')

        # Deleting field 'ArticleCategory.package_weight'
        db.delete_column('eshop_articlecategory', 'package_weight')

        # Deleting field 'ArticleCategory.electrode_type'
        db.delete_column('eshop_articlecategory', 'electrode_type')

        # Deleting field 'ArticleCategory.electrode_consumption'
        db.delete_column('eshop_articlecategory', 'electrode_consumption')

        # Deleting field 'ArticleCategory.material_appointment'
        db.delete_column('eshop_articlecategory', 'material_appointment')

        # Deleting field 'ArticleCategory.dynamic_viscosity'
        db.delete_column('eshop_articlecategory', 'dynamic_viscosity')

        # Deleting field 'ArticleCategory.glue_type'
        db.delete_column('eshop_articlecategory', 'glue_type')

        # Deleting field 'ArticleCategory.relative_extension'
        db.delete_column('eshop_articlecategory', 'relative_extension')

        # Deleting field 'ArticleCategory.shelf_life'
        db.delete_column('eshop_articlecategory', 'shelf_life')

        # Deleting field 'ArticleCategory.bonding_time'
        db.delete_column('eshop_articlecategory', 'bonding_time')

        # Deleting field 'ArticleCategory.welding_rate'
        db.delete_column('eshop_articlecategory', 'welding_rate')

        # Deleting field 'ArticleCategory.electrode_diameter'
        db.delete_column('eshop_articlecategory', 'electrode_diameter')

        # Deleting field 'ArticleCategory.product_type'
        db.delete_column('eshop_articlecategory', 'product_type')

        # Deleting field 'ArticleCategory.density'
        db.delete_column('eshop_articlecategory', 'density')

        # Deleting field 'ArticleCategory.appearance'
        db.delete_column('eshop_articlecategory', 'appearance')

        # Deleting field 'ArticleCategory.material_condition'
        db.delete_column('eshop_articlecategory', 'material_condition')

        # Deleting field 'ArticleCategory.tensile_strength'
        db.delete_column('eshop_articlecategory', 'tensile_strength')

        # Deleting field 'ArticleCategory.consistency'
        db.delete_column('eshop_articlecategory', 'consistency')

        # Deleting field 'ArticleCategory.primer_type'
        db.delete_column('eshop_articlecategory', 'primer_type')

        # Deleting field 'ArticleCategory.material_proces_type'
        db.delete_column('eshop_articlecategory', 'material_proces_type')

        # Adding field 'ArticleCategory.property_name1'
        db.add_column('eshop_articlecategory', 'property_name1',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.property_value1'
        db.add_column('eshop_articlecategory', 'property_value1',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.property_name2'
        db.add_column('eshop_articlecategory', 'property_name2',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.property_value2'
        db.add_column('eshop_articlecategory', 'property_value2',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.property_name3'
        db.add_column('eshop_articlecategory', 'property_name3',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.property_value3'
        db.add_column('eshop_articlecategory', 'property_value3',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.property_name4'
        db.add_column('eshop_articlecategory', 'property_name4',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.property_value4'
        db.add_column('eshop_articlecategory', 'property_value4',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.property_name5'
        db.add_column('eshop_articlecategory', 'property_name5',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.property_value5'
        db.add_column('eshop_articlecategory', 'property_value5',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.property_name6'
        db.add_column('eshop_articlecategory', 'property_name6',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.property_value6'
        db.add_column('eshop_articlecategory', 'property_value6',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.property_name7'
        db.add_column('eshop_articlecategory', 'property_name7',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.property_value7'
        db.add_column('eshop_articlecategory', 'property_value7',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.property_name8'
        db.add_column('eshop_articlecategory', 'property_name8',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.property_value8'
        db.add_column('eshop_articlecategory', 'property_value8',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.property_name9'
        db.add_column('eshop_articlecategory', 'property_name9',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.property_value9'
        db.add_column('eshop_articlecategory', 'property_value9',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.property_name10'
        db.add_column('eshop_articlecategory', 'property_name10',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.property_value10'
        db.add_column('eshop_articlecategory', 'property_value10',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.property_name11'
        db.add_column('eshop_articlecategory', 'property_name11',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.property_value11'
        db.add_column('eshop_articlecategory', 'property_value11',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.property_name12'
        db.add_column('eshop_articlecategory', 'property_name12',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.property_value12'
        db.add_column('eshop_articlecategory', 'property_value12',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.property_name13'
        db.add_column('eshop_articlecategory', 'property_name13',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.property_value13'
        db.add_column('eshop_articlecategory', 'property_value13',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.property_name14'
        db.add_column('eshop_articlecategory', 'property_name14',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.property_value14'
        db.add_column('eshop_articlecategory', 'property_value14',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.property_name15'
        db.add_column('eshop_articlecategory', 'property_name15',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.property_value15'
        db.add_column('eshop_articlecategory', 'property_value15',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.property_name16'
        db.add_column('eshop_articlecategory', 'property_name16',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.property_value16'
        db.add_column('eshop_articlecategory', 'property_value16',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.property_name17'
        db.add_column('eshop_articlecategory', 'property_name17',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.property_value17'
        db.add_column('eshop_articlecategory', 'property_value17',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.property_name18'
        db.add_column('eshop_articlecategory', 'property_name18',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.property_value18'
        db.add_column('eshop_articlecategory', 'property_value18',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.property_name19'
        db.add_column('eshop_articlecategory', 'property_name19',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.property_value19'
        db.add_column('eshop_articlecategory', 'property_value19',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.property_name20'
        db.add_column('eshop_articlecategory', 'property_name20',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.property_value20'
        db.add_column('eshop_articlecategory', 'property_value20',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'ArticleCategory.warranty'
        db.add_column('eshop_articlecategory', 'warranty',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=0, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.storage_temp_max'
        db.add_column('eshop_articlecategory', 'storage_temp_max',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=2, decimal_places=0, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.electrode_length'
        db.add_column('eshop_articlecategory', 'electrode_length',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.electrode_cover'
        db.add_column('eshop_articlecategory', 'electrode_cover',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=64, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.using_type'
        db.add_column('eshop_articlecategory', 'using_type',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.material_type'
        db.add_column('eshop_articlecategory', 'material_type',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.electrode_positions'
        db.add_column('eshop_articlecategory', 'electrode_positions',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=64, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.glue_view'
        db.add_column('eshop_articlecategory', 'glue_view',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.composition_type'
        db.add_column('eshop_articlecategory', 'composition_type',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.work_temp_max'
        db.add_column('eshop_articlecategory', 'work_temp_max',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=2, decimal_places=0, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.soat_type'
        db.add_column('eshop_articlecategory', 'soat_type',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.storage_temp_min'
        db.add_column('eshop_articlecategory', 'storage_temp_min',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=2, decimal_places=0, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.current_race'
        db.add_column('eshop_articlecategory', 'current_race',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.batcher'
        db.add_column('eshop_articlecategory', 'batcher',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.filler_type'
        db.add_column('eshop_articlecategory', 'filler_type',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.consumption'
        db.add_column('eshop_articlecategory', 'consumption',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=64, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.chemical_composition'
        db.add_column('eshop_articlecategory', 'chemical_composition',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.impact_strength'
        db.add_column('eshop_articlecategory', 'impact_strength',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.gloves_type'
        db.add_column('eshop_articlecategory', 'gloves_type',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.gloss'
        db.add_column('eshop_articlecategory', 'gloss',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.base_paint'
        db.add_column('eshop_articlecategory', 'base_paint',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.texture'
        db.add_column('eshop_articlecategory', 'texture',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.use_filler'
        db.add_column('eshop_articlecategory', 'use_filler',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.treated_surface'
        db.add_column('eshop_articlecategory', 'treated_surface',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.bonded_materials'
        db.add_column('eshop_articlecategory', 'bonded_materials',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.application_method'
        db.add_column('eshop_articlecategory', 'application_method',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.gloves_size'
        db.add_column('eshop_articlecategory', 'gloves_size',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.using_material'
        db.add_column('eshop_articlecategory', 'using_material',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.work_temp_min'
        db.add_column('eshop_articlecategory', 'work_temp_min',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=2, decimal_places=0, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.decor_view'
        db.add_column('eshop_articlecategory', 'decor_view',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.base_enamel'
        db.add_column('eshop_articlecategory', 'base_enamel',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=64, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.drying_time'
        db.add_column('eshop_articlecategory', 'drying_time',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=4, decimal_places=2, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.current_max'
        db.add_column('eshop_articlecategory', 'current_max',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=0, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.current_min'
        db.add_column('eshop_articlecategory', 'current_min',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=0, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.gloves_material'
        db.add_column('eshop_articlecategory', 'gloves_material',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.solvent_type'
        db.add_column('eshop_articlecategory', 'solvent_type',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.electrode_use'
        db.add_column('eshop_articlecategory', 'electrode_use',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=64, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.varnish_type'
        db.add_column('eshop_articlecategory', 'varnish_type',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.substances_content'
        db.add_column('eshop_articlecategory', 'substances_content',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.when_temp_20'
        db.add_column('eshop_articlecategory', 'when_temp_20',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.protection'
        db.add_column('eshop_articlecategory', 'protection',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.package_weight'
        db.add_column('eshop_articlecategory', 'package_weight',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=1, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.electrode_type'
        db.add_column('eshop_articlecategory', 'electrode_type',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.electrode_consumption'
        db.add_column('eshop_articlecategory', 'electrode_consumption',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.material_appointment'
        db.add_column('eshop_articlecategory', 'material_appointment',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.dynamic_viscosity'
        db.add_column('eshop_articlecategory', 'dynamic_viscosity',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.glue_type'
        db.add_column('eshop_articlecategory', 'glue_type',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.relative_extension'
        db.add_column('eshop_articlecategory', 'relative_extension',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.shelf_life'
        db.add_column('eshop_articlecategory', 'shelf_life',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=0, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.bonding_time'
        db.add_column('eshop_articlecategory', 'bonding_time',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=0, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.welding_rate'
        db.add_column('eshop_articlecategory', 'welding_rate',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.electrode_diameter'
        db.add_column('eshop_articlecategory', 'electrode_diameter',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.product_type'
        db.add_column('eshop_articlecategory', 'product_type',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.density'
        db.add_column('eshop_articlecategory', 'density',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.appearance'
        db.add_column('eshop_articlecategory', 'appearance',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.material_condition'
        db.add_column('eshop_articlecategory', 'material_condition',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.tensile_strength'
        db.add_column('eshop_articlecategory', 'tensile_strength',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.consistency'
        db.add_column('eshop_articlecategory', 'consistency',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.primer_type'
        db.add_column('eshop_articlecategory', 'primer_type',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True),
                      keep_default=False)

        # Adding field 'ArticleCategory.material_proces_type'
        db.add_column('eshop_articlecategory', 'material_proces_type',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Deleting field 'ArticleCategory.property_name1'
        db.delete_column('eshop_articlecategory', 'property_name1')

        # Deleting field 'ArticleCategory.property_value1'
        db.delete_column('eshop_articlecategory', 'property_value1')

        # Deleting field 'ArticleCategory.property_name2'
        db.delete_column('eshop_articlecategory', 'property_name2')

        # Deleting field 'ArticleCategory.property_value2'
        db.delete_column('eshop_articlecategory', 'property_value2')

        # Deleting field 'ArticleCategory.property_name3'
        db.delete_column('eshop_articlecategory', 'property_name3')

        # Deleting field 'ArticleCategory.property_value3'
        db.delete_column('eshop_articlecategory', 'property_value3')

        # Deleting field 'ArticleCategory.property_name4'
        db.delete_column('eshop_articlecategory', 'property_name4')

        # Deleting field 'ArticleCategory.property_value4'
        db.delete_column('eshop_articlecategory', 'property_value4')

        # Deleting field 'ArticleCategory.property_name5'
        db.delete_column('eshop_articlecategory', 'property_name5')

        # Deleting field 'ArticleCategory.property_value5'
        db.delete_column('eshop_articlecategory', 'property_value5')

        # Deleting field 'ArticleCategory.property_name6'
        db.delete_column('eshop_articlecategory', 'property_name6')

        # Deleting field 'ArticleCategory.property_value6'
        db.delete_column('eshop_articlecategory', 'property_value6')

        # Deleting field 'ArticleCategory.property_name7'
        db.delete_column('eshop_articlecategory', 'property_name7')

        # Deleting field 'ArticleCategory.property_value7'
        db.delete_column('eshop_articlecategory', 'property_value7')

        # Deleting field 'ArticleCategory.property_name8'
        db.delete_column('eshop_articlecategory', 'property_name8')

        # Deleting field 'ArticleCategory.property_value8'
        db.delete_column('eshop_articlecategory', 'property_value8')

        # Deleting field 'ArticleCategory.property_name9'
        db.delete_column('eshop_articlecategory', 'property_name9')

        # Deleting field 'ArticleCategory.property_value9'
        db.delete_column('eshop_articlecategory', 'property_value9')

        # Deleting field 'ArticleCategory.property_name10'
        db.delete_column('eshop_articlecategory', 'property_name10')

        # Deleting field 'ArticleCategory.property_value10'
        db.delete_column('eshop_articlecategory', 'property_value10')

        # Deleting field 'ArticleCategory.property_name11'
        db.delete_column('eshop_articlecategory', 'property_name11')

        # Deleting field 'ArticleCategory.property_value11'
        db.delete_column('eshop_articlecategory', 'property_value11')

        # Deleting field 'ArticleCategory.property_name12'
        db.delete_column('eshop_articlecategory', 'property_name12')

        # Deleting field 'ArticleCategory.property_value12'
        db.delete_column('eshop_articlecategory', 'property_value12')

        # Deleting field 'ArticleCategory.property_name13'
        db.delete_column('eshop_articlecategory', 'property_name13')

        # Deleting field 'ArticleCategory.property_value13'
        db.delete_column('eshop_articlecategory', 'property_value13')

        # Deleting field 'ArticleCategory.property_name14'
        db.delete_column('eshop_articlecategory', 'property_name14')

        # Deleting field 'ArticleCategory.property_value14'
        db.delete_column('eshop_articlecategory', 'property_value14')

        # Deleting field 'ArticleCategory.property_name15'
        db.delete_column('eshop_articlecategory', 'property_name15')

        # Deleting field 'ArticleCategory.property_value15'
        db.delete_column('eshop_articlecategory', 'property_value15')

        # Deleting field 'ArticleCategory.property_name16'
        db.delete_column('eshop_articlecategory', 'property_name16')

        # Deleting field 'ArticleCategory.property_value16'
        db.delete_column('eshop_articlecategory', 'property_value16')

        # Deleting field 'ArticleCategory.property_name17'
        db.delete_column('eshop_articlecategory', 'property_name17')

        # Deleting field 'ArticleCategory.property_value17'
        db.delete_column('eshop_articlecategory', 'property_value17')

        # Deleting field 'ArticleCategory.property_name18'
        db.delete_column('eshop_articlecategory', 'property_name18')

        # Deleting field 'ArticleCategory.property_value18'
        db.delete_column('eshop_articlecategory', 'property_value18')

        # Deleting field 'ArticleCategory.property_name19'
        db.delete_column('eshop_articlecategory', 'property_name19')

        # Deleting field 'ArticleCategory.property_value19'
        db.delete_column('eshop_articlecategory', 'property_value19')

        # Deleting field 'ArticleCategory.property_name20'
        db.delete_column('eshop_articlecategory', 'property_name20')

        # Deleting field 'ArticleCategory.property_value20'
        db.delete_column('eshop_articlecategory', 'property_value20')


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
            'country': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'db_column': "'_order'"}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['eshop.ArticleCategory']"}),
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
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'updated_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'video': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
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