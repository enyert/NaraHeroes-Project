from openshift.models import *
from django.contrib import admin
from django.contrib.auth.models import User


class EstudianteAdmin(admin.ModelAdmin):
	list_display = ('user','fechaInicio','puntosColab')


class InstructorAdmin(admin.ModelAdmin):
	list_display = ('user','cedula','materia')

class MisionEstudianteAdmin(admin.ModelAdmin):
	list_display = ('nombre','materia')

class TemaAdmin(admin.ModelAdmin):
	list_display = ('nombre','materia')


admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(MisionInstructor)
admin.site.register(MisionEstudiante, MisionEstudianteAdmin)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Tema, TemaAdmin)
admin.site.register(Guia)
admin.site.register(Examen)
admin.site.register(Problema)
admin.site.register(HistorialMisionesEstudiante)
admin.site.register(HistorialMisionesInstructor)