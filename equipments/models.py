#-*- coding: utf-8 -*-
import os
import uuid

from django.db import models
from django.dispatch import receiver

class Brand(models.Model):
	name = models.CharField(max_length = 255, verbose_name = 'Nom')
	vendor = models.CharField(max_length = 255, null = True, blank = True, verbose_name = 'Vendeur')
	address = models.CharField(max_length = 255,null = True, blank = True,  verbose_name = 'Adresse')
	zip_code = models.PositiveIntegerField(null = True, blank = True, verbose_name = 'Code postal')
	locality = models.CharField(max_length = 255, null = True, blank = True, verbose_name = 'Ville')
	phone = models.CharField(max_length = 255, null = True, blank = True, verbose_name = 'Téléphone')
	mail = models.EmailField(null = True, blank = True, verbose_name = 'Adresse de messagerie')

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = u'Marque'
		verbose_name_plural = 'Marques'

class Equipment(models.Model):
	name = models.CharField(max_length = 255, verbose_name = 'Nom')
	brand = models.ForeignKey('Brand', null = True, blank = True, verbose_name = 'Marque')
	max_load = models.PositiveSmallIntegerField(null = True, blank = True, verbose_name = 'Charge maximale')
	min_load = models.PositiveSmallIntegerField(default = 0, blank = True, verbose_name = 'Charge minimale')
	description = models.TextField(null = True, blank = True, verbose_name = 'Description');
	picture = models.ImageField(upload_to = 'upload/equipments/equipments/', null = True, blank = True, verbose_name = 'Image')
	date_added = models.DateTimeField(auto_now_add = True, editable = False)
	date_modified = models.DateTimeField(auto_now = True, editable = False)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = u'Equipement'
		verbose_name_plural = 'Equipements'

@receiver(models.signals.post_delete, sender = Equipment)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.picture:
        if os.path.isfile(instance.picture.path):
            os.remove(instance.picture.path)

@receiver(models.signals.pre_save, sender = Equipment)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_file = Equipment.objects.get(pk = instance.pk).picture
    except MediaFile.DoesNotExist:
        return False

    if not old_file == instance.picture:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)