#-*- coding: utf-8 -*-
from django.db import models

class Series(models.Model):
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
	series = models.ManyToManyField(Series, null = True, blank = True, verbose_name = u'Séries')

	class Meta:
		verbose_name = u"Jour d'entraînement"
		verbose_name_plural = u"Jours d'entraînement"

class Programm(models.Model):
	number = models.PositiveIntegerField(verbose_name = u"Numéro de l'entraînement")
	training_days = models.ManyToManyField(TrainingDay, null = True, blank = True, verbose_name = u"Jours d'entraînement")

	class Meta:
		verbose_name = u"Programme d'entraînement"
		verbose_name_plural = u"Programmes d'entraînement"