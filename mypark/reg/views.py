# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, AnonymousUser
from django.shortcuts import render_to_response
from park.models import UserProfile

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

class SignupForm(ModelForm):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = UserProfile
		exclude = ['user']

'''	username = forms.CharField()
	full_name = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
	phone = forms.CharField()
	email = forms.EmailField()'''

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
def signUpView(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(username=request.POST['username'], email=request.POST['email'], password=request.POST['password'])
			args = request.POST.copy()
			args['user'] = user
			userprofile = UserProfile(user=user,name=request.POST['name'],phone=request.POST['phone'],email=request.POST['email'], pin=request.POST['pin'])
			userprofile.save()
			#userprofile.user.set_password(request.POST['password'])
			#form.save()
		usname = request.POST['username']
		pswd = request.POST['password']
		user = authenticate(username = usname, password = pswd)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/reg/login')
			else:
				return 'Your account has been disabled.'
		else:
			return 'Invalid username or password.'
	form = SignupForm()
	t = loader.get_template('reg/signup.html')
	c = Context({'form':form.as_p(), 'logged_in':request.user.is_authenticated(), 'user':request.user.username})
	return HttpResponse(t.render(c))

@csrf_exempt
def logoutView(request):
	logout(request)
	return render_to_response('reg/logout.html')

