#-*- coding: utf-8 -*-
from django import forms
from trainings.models import Programm

class ProgrammForm(forms.ModelForm):
	class Meta:
		model = Programm