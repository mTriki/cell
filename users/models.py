#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Sex(models.Model): 
	name = models.CharField(max_length = 255, verbose_name = 'Sexe')

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = u'Sexe'
		verbose_name_plural = 'Sexes'

class Person(User):
	address = models.CharField(max_length = 255, verbose_name = 'Adresse')
	zip_code = models.PositiveIntegerField(verbose_name = 'Code postal')
	locality = models.CharField(max_length = 255, verbose_name = 'Ville')
	birthday = models.DateField(verbose_name = 'Date de naissance')
	nationality = models.CharField(max_length = 255, verbose_name = 'Nationalité')
	residence_permit = models.CharField(null = True, blank = True, max_length = 255, verbose_name = 'Permis de séjour')
	sex = models.ForeignKey('Sex', null = True, blank = True, verbose_name = 'Sexe')
	phone = models.CharField(max_length = 255, verbose_name = 'Téléphone')
	badge = models.PositiveIntegerField(verbose_name = 'Numéro de badge')
	picture = models.ImageField(upload_to = 'upload/users/person/', null = True, blank = True, verbose_name = 'Image')
	training_programms = models.ManyToManyField('trainings.Programm', null = True, blank = True, verbose_name = u"Programmes d'entraînement")

	def __unicode__(self):
		return self.username

	class Meta:
		verbose_name = u'Personne'
		verbose_name_plural = 'Personnes'

class Employee(Person):

	class Meta:
		verbose_name = u'Employé'
		verbose_name_plural = 'Employés'

class Customer(Person):
	job = models.CharField(max_length = 255, verbose_name = 'Profession')

	class Meta:
		verbose_name = u'Client'
		verbose_name_plural = 'Clients'