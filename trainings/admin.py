from django.shortcuts import get_object_or_404
from django.contrib import admin
from users.models import Person
from trainings.models import Series, TrainingDay, Programm

class ProgrammAdmin(admin.ModelAdmin):
	def save_model(self, request, obj, form, change):
		if not obj.number and request.GET and request.GET['_popup']:
			obj.number = get_object_or_404(Person, user_ptr_id = request.GET['_popup']).training_programms_set.count()
			obj.is_model = True

		obj.save()

admin.site.register(Series)
admin.site.register(TrainingDay)
admin.site.register(Programm, ProgrammAdmin)