#-*- coding: utf-8 -*-
from django.db import models

class Series(models.Model):
	day = models.ForeignKey('TrainingDay', verbose_name = u"Jour d'entraînement")
	order = models.PositiveIntegerField(verbose_name = u'Ordre')
	times_number = models.PositiveIntegerField(verbose_name = u'Nombre de fois')
	exercise = models.ForeignKey('exercises.Exercise', verbose_name = 'Exercice')
	repetition = models.PositiveIntegerField(verbose_name = u'Nombre de répétition')
	strength = models.PositiveIntegerField(verbose_name = u'Résistance')
	time = models.TimeField(null = True, blank = True, verbose_name = u'Temps')
	pause_time = models.TimeField(null = True, blank = True, verbose_name = u'Temps de pause')

	class Meta:
		verbose_name = u"Série"
		verbose_name_plural = u"Séries"

class TrainingDay(models.Model):
	number = models.PositiveIntegerField(verbose_name = u'Numéro du jour')
	programm = models.ForeignKey('Programm', verbose_name = u"Programme d'entraînement")

	class Meta:
		verbose_name = u"Jour d'entraînement"
		verbose_name_plural = u"Jours d'entraînement"

class Programm(models.Model):
	number = models.PositiveIntegerField(editable = False, verbose_name = u"Numéro de l'entraînement")
	is_model = models.BooleanField(editable = False, default = False, verbose_name = u'Définir en tant que modèle')
	name = models.CharField(max_length = 255, null = True, blank = True, verbose_name = 'Nom')
	period = models.PositiveIntegerField(null = True, blank = True, verbose_name = u"Nombre de mois")

	class Meta:
		verbose_name = u"Programme d'entraînement"
		verbose_name_plural = u"Programmes d'entraînement"