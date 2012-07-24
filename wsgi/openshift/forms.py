# This Python file uses the following encoding: utf-8
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from openshift.models import Estudiante
from django.contrib import auth


class RegistrationForm(ModelForm): #formulario de registro
	#Asignando tipos del formulario
	username = forms.CharField(label=(u'Nombre de usuario'))
	email = forms.EmailField(label=(u'Dirección Email'))
	password = forms.CharField(label=(u'Contraseña'),widget=forms.PasswordInput(render_value=False))
	password1 = forms.CharField(label=(u'Verificar contraseña'),widget=forms.PasswordInput(render_value=False))

	#Hacemos el meta para excluir campos del modelo que no queremos en el formulario
	class Meta:
		model = Estudiante
		exclude = ('user', 'puntosMate', 'puntosFis', 'puntosQuim', 'puntosColab', 'fechaInicio', 'cinturon',)

	def clean_username(self): #Verifica nombre de usuario
		username = self.cleaned_data['username']
		try:
				User.objects.get(username=username)
		except User.DoesNotExist:
				return username
		raise forms.ValidationError("El nombre de usuario ya existe, por favor seleccione otro.")
    
	def clean_email(self): #Verifica email de usuario
		email = self.cleaned_data.get('email')
		username = self.cleaned_data.get('username')
		if email and User.objects.filter(email=email).exclude(username=username).count():
			raise forms.ValidationError(u'La Dirección de correo electrónico debe ser única.')
		return email
	
	def clean(self): #Verifica los campos de passwords
		password = self.cleaned_data.get('password', None)
		password1 = self.cleaned_data.get('password1', None)
		if password and password1 and password == password1:
			return self.cleaned_data
		else:	
			raise forms.ValidationError('Las contraseñas no coinciden, por favor intente nuevamente.')


class LoginForm(forms.Form):
	username = forms.CharField(label=(u'Nombre de usuario'))
	password = forms.CharField(label=(u'Contraseña'), widget=forms.PasswordInput(render_value=False))









