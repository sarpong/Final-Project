# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from models import Blog, Comment
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django import forms
from django.contrib.auth import authenticate, login, logout

def booking_detail(request):
	

def purchase_detail(request):
	pass

def contact_us(request):
	pass

def park_search(request):
	pass

def park_admin(request):
	pass

def park_confirmation(request):
	pass

def home(request):
	t = loader.get_template('park/base.html')
	c = Context(dict())
	return HttpResponse(t.render(c))

