#-*- coding: utf-8 -*-
import os
import uuid

from django.db import models
from django.dispatch import receiver

class ExerciseType(models.Model):
	name = models.CharField(max_length = 255, verbose_name = 'Nom')
	description = models.TextField(null = True, blank = True, verbose_name = 'Description');

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = u"Type d'exercice"
		verbose_name_plural = u"Types d'exercice"

class BodyPart(models.Model):
	name = models.CharField(max_length = 255, verbose_name = 'Nom')
	description = models.TextField(null = True, blank = True, verbose_name = 'Description');

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = u'Partie du corps'
		verbose_name_plural = 'Parties du corps'

class Exercise(models.Model):
	name = models.CharField(max_length = 255, verbose_name = 'Nom')
	exercise_type = models.ForeignKey('ExerciseType', null = True, blank = True, verbose_name = "Type d'exercice")
	equipment = models.ManyToManyField('equipments.Equipment', null = True, blank = True, verbose_name = 'Equipement nécessaire')
	difficult_level = models.PositiveIntegerField(null = True, blank = True, verbose_name = u'Niveau de difficulté')
	media_file = models.FileField(upload_to = 'upload/exercises/exercises/', null = True, blank = True, verbose_name = u'Démo')
	body_parts = models.ManyToManyField(BodyPart, null = True, blank = True, verbose_name = u'Parties du corps travaillées')
	advice = models.TextField(null = True, blank = True, verbose_name = "Conseil d'utilisation");

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = u'Exercice'
		verbose_name_plural = 'Exercices'

@receiver(models.signals.post_delete, sender = Exercise)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.media_file:
        if os.path.isfile(instance.media_file.path):
            os.remove(instance.media_file.path)

@receiver(models.signals.pre_save, sender = Exercise)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_file = Equipment.objects.get(pk = instance.pk).media_file
    except MediaFile.DoesNotExist:
        return False

    if not old_file == instance.media_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)