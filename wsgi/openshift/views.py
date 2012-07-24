from django.views.generic.simple import direct_to_template
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from openshift.models import Tema
from django.http import HttpResponseRedirect
from openshift.forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render_to_response('home/home.html', {}, context_instance=RequestContext(request))

def profile(request):
    return render_to_response('profile.html', {}, context_instance=RequestContext(request))

def EstudianteRegistration(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/profile/')
	if request.method == 'POST':
		form1 = RegistrationForm(request.POST)
		if form1.is_valid():
			user = User.objects.create_user(form1.cleaned_data['username'],
				form1.cleaned_data['email'],
				form1.cleaned_data['password'])
			user.save()
			estudiante = user.get_profile()
			estudiante.save()
			return HttpResponseRedirect('/profile/')
		else:
			return render_to_response('register.html', {'form1':form1}, 
				context_instance = RequestContext(request))


	else:
			''' Usuario no esta pasando el formulario, buscar un espacio en blanco.'''
			form1 = RegistrationForm()
			context = {'form1':form1}
			return render_to_response('register.html', context, context_instance=RequestContext(request))

def LoginRequest(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/profile/')
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			usuario = authenticate(username=username, password=password)
			if usuario is not None:
				login(request, usuario)
				return HttpResponseRedirect('/profile/')
			else:
				return render_to_response('login.html', {'form': form}, context_instance = RequestContext(request))
		else:
			return render_to_response('login.html', {'form': form}, context_instance = RequestContext(request))
	else:
		'''User is not submitting the form, shot the login form'''
		form = LoginForm()
		context = {'form': form}
		return render_to_response('login.html', context, context_instance = RequestContext(request))

def LogoutRequest(request):
	logout(request)
	return HttpResponseRedirect('/')
