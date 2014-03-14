#-*- coding: utf-8 -*-
from django.contrib import admin
from equipments.models import Equipment, Brand

class BrandAdmin(admin.ModelAdmin):
	list_display = ('name', 'vendor', 'locality', 'phone', 'mail')
	list_filter = ('name', 'vendor', 'locality')
	ordering = ('name', )
	search_fields = ('name', 'vendor', 'address', 'zip_code', 'locality', 'phone', 'mail')

class EquipmentAdmin(admin.ModelAdmin):
	list_display = ('name', 'brand', 'date_added', 'date_modified', 'trunc_description')
	list_filter = ('name', 'brand')
	date_hierarchy = 'date_added'
	ordering = ('date_added', )
	search_fields = ('name', )
	
	fieldsets = (
       (u'Information de base', {
            'fields': ('name', )
        }),
        (u'Informations supplémentaires', {
           'fields': ('brand', 'min_load', 'max_load', 'description', 'picture')
        })
    )

	def trunc_description(self, equipment):
		text = equipment.description[0:40]

		if len(equipment.description) > 40:
			return '%s...' % text
		else:
			return text

	trunc_description.short_description = u'Description'

admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Brand, BrandAdmin)