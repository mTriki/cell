from django.contrib import admin
from trainings.models import Series, TrainingDay, Programm
from trainings.forms import ProgrammForm

class ProgrammAdmin(admin.ModelAdmin):
	form = ProgrammForm

	def change_view(self, request, object_id, form_url = '', extra_context = None):
		if request.method == 'POST':
			data = request.POST
			data['number'] = 0
			return super(ProgrammAdmin, self).change_view(data, object_id, form_url, extra_context=extra_context)
		else:
			return super(ProgrammAdmin, self).change_view(request, object_id, form_url, extra_context=extra_context)

admin.site.register(Series)
admin.site.register(TrainingDay)
admin.site.register(Programm, ProgrammAdmin)