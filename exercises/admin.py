from django.contrib import admin
from exercises.models import Exercise, BodyPart, ExerciseType

admin.site.register(Exercise)
admin.site.register(BodyPart)
admin.site.register(ExerciseType)