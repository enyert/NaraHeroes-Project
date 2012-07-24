# This Python file uses the following encoding: utf-8
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.db.models.signals import post_save
# Create your models here.

materia_opciones = (('MAT','Matemática'),('FIS','Física'),('QUI','Química'),('COL','Colaboración'),)
problema_opciones = (('opA','a'),('opB','b'),('opC','c'),('opD','d'),('opE','e'),)


class Estudiante(models.Model): #perfil de un estudiante
    puntosMate = models.PositiveIntegerField(default=0) #puntos obtenidos en matematica
    puntosFis = models.PositiveIntegerField(default=0) #puntos obtenidos en fisica
    puntosQuim = models.PositiveIntegerField(default=0) #puntos obtenidos en quimica
    puntosColab = models.PositiveIntegerField(default=0) #puntos de colaboracion.
    fechaInicio = models.DateField(auto_now_add=True) #fecha de registro
    cinturon = models.CharField(max_length=20, default="Blanco") #cinturon del estudiante
    user = models.ForeignKey(User, unique=True) #clase user para datos esenciales

    def __unicode__(self):
        return unicode(self.user)

def create_user_profile(sender, instance, **kwargs):
    estudiante, new = Estudiante.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, User)

class MisionEstudiante(models.Model): #Misiones a cumplir por los estudiantes 
    nombre = models.CharField(max_length=60, unique=True) #nombre de la mision
    descripcion = models.TextField(max_length=1000) #descripcion de la mision
    objetivos = models.TextField(max_length=200) #objetivos a lograr en la mision
    materia = models.CharField(max_length=3, choices=materia_opciones) #materia de la mision
    reQuim = models.PositiveIntegerField() #requisitos de puntos en quimica
    reMate = models.PositiveIntegerField() #requisitos de puntos en matematica
    reFisi = models.PositiveIntegerField() #requisitos de puntos en fisica
    reColab = models.PositiveIntegerField() #requisitos de puntos de colaboracion
    premioColab = models.PositiveIntegerField() #puntos de colaboracion de premio 
    premioMat = models.PositiveIntegerField() #puntos de matematica que otorga la mision al ser cumplida
    premioFis = models.PositiveIntegerField() #puntos de fisica que otorga la mision al ser cumplida
    premioQui = models.PositiveIntegerField() #puntos de quimica que otorga la mision al ser ejecutada
        

    def __unicode__(self):
        return unicode(self.nombre)


class HistorialMisionesEstudiante(models.Model): 
	estudiante = models.OneToOneField(Estudiante) #estudiante asociado
	misionesComp = models.ManyToManyField(MisionEstudiante) #misiones completadas 

	def __unicode__(self):
		return unicode(self.estudiante)


class Instructor(models.Model): #perfil del instructor del curso
    cedula = models.CharField(max_length = 15, unique=True) #cedula de identidad del instructor
    puntosColab = models.PositiveIntegerField() #Puntos de colaboracion
    materia = models.CharField(max_length=3, choices=materia_opciones)
    esEvaluador = models.BooleanField() #define si un instructor es evaluador o no
    user = models.ForeignKey(User, unique=True) #clase user para datos esenciales

    def __unicode__(self):
        return unicode(self.user)
    

class MisionInstructor(models.Model):
    nombre = models.CharField(max_length=60, unique=True) #nombre de la mision
    descripcion = models.TextField(max_length=1000) #descripcion de la mision
    objetivos = models.TextField(max_length=200) #objetivos a lograr en la mision
    reColab = models.PositiveIntegerField() #requisitos de puntos de colaboracion
    premioColab = models.PositiveIntegerField() #puntos de colaboracion de premio
    
    def __unicode__(self):
        return unicode(self.nombre)


class HistorialMisionesInstructor(models.Model):
	instructor = models.OneToOneField(Instructor) #instructor asociado 
	misionesComp = models.ManyToManyField(MisionInstructor) #misiones completadas


class Tema(models.Model): #Tema de las Guias del curso
    nombre = models.CharField(max_length=60)
    descripcion = models.TextField()
    materia = models.CharField(max_length=3, choices=materia_opciones) 

    def __unicode__(self):
        return u"%s (%s)" % (self.nombre, self.materia)


class Guia(models.Model): #Representa una guía del curso
    nombreAutor = models.CharField(max_length=30)
    apellidoAutor = models.CharField(max_length=30)
    titulo = models.CharField(max_length=50) #titulo de la guia
    fecha_publicacion = models.DateField() #fecha en que se publicará la guía
    materia = models.CharField(max_length=3, choices=materia_opciones) #materia de la guia
    contenido = models.FileField(upload_to='guias') #contenido de la guía estara en formato pdf
    puntuacion = models.PositiveIntegerField() #valoracion de la calidad de la guia
    temas = models.ManyToManyField(Tema) #temas que abarcará la guia 

    def __unicode__(self):
        return u"%s (%s)" % (self.titulo, self.materia)


class Examen(models.Model):
    materia = models.CharField(max_length=3, choices=materia_opciones) #materia que vamos a evaluar 
    tema = models.ForeignKey(Tema) #tema que vamos a evaluar en el examen
    tiempo = models.PositiveIntegerField() # tiempo en minutos para resolver el examen

    def __unicode__(self):
        return u"%s %s" % (self.materia, self.tiempo)


class Problema(models.Model):
    enunciado = models.TextField(max_length=200) #enunciado de la pregunta
    opcionA = models.CharField(max_length=100)
    opcionB = models.CharField(max_length=100)
    opcionC = models.CharField(max_length=100)
    opcionD = models.CharField(max_length=100)
    opcionE = models.CharField(max_length=100)
    correcta = models.CharField(max_length=3, choices=problema_opciones) #opcion correcta
    dificultad = models.PositiveIntegerField() #dificultad del problema. Del 1 al 5
    tiempoPromedio = models.PositiveIntegerField() #tiempo promedio para resolver el problema
    prueba = models.ForeignKey(Examen) #Una prueba sera un conjunto de problemas

    def __unicode__(self):
        return u"%s %s" % (self.enunciado, self.dificultad)
