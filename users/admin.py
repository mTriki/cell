#-*- coding: utf-8 -*-
from django.contrib import admin
from users.models import Sex, Employee, Customer

class CustomerAdmin(admin.ModelAdmin):
	list_display = ('username', 'training_programms_link', )

	def training_programms_link(self, customer):
		return '<a href="#">Lol</a>'
	training_programms_link.short_description = u"Programme d'entraînement"
	training_programms_link.allow_tags = True

admin.site.register(Sex)
admin.site.register(Employee)
admin.site.register(Customer, CustomerAdmin)