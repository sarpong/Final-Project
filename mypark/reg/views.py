# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

@csrf_exempt
def loginView(request):
	if request.method == 'POST':
		usname = request.POST['username']
		pswd = request.POST['password']
		user = authenticate(username = usname, password = pswd)
		if user is not None:
			if user.is_active:
				login(request, user)
			else:
				return 'Your account has been disabled.'
		else:
			return 'Invalid username or password.'
	form = LoginForm()
	return render_to_response('reg/login.html', {'form': form, 'logged_in':request.user.is_authenticated(), 'user':request.user.username})

@csrf_exempt
def logoutView(request):
	logout(request)
	return render_to_response('reg/logout.html')

