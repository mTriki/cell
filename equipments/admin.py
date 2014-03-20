#-*- coding: utf-8 -*-
from django.contrib import admin
from equipments.models import Equipment, Brand

class BrandAdmin(admin.ModelAdmin):
	list_display = ('name', 'vendor', 'locality', 'phone', 'mail')
	list_filter = ('name', 'vendor', 'locality')
	ordering = ('name', )
	search_fields = ('name', 'vendor', 'address', 'zip_code', 'locality', 'phone', 'mail')

class EquipmentAdmin(admin.ModelAdmin):
	list_display = ('name', 'brand', 'date_added', 'date_modified')
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

admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Brand, BrandAdmin)