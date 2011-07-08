# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from models import User, Purchase, Company, Administrator
from django.forms import ModelForm
from django import forms
from django.views.decorators.csrf import csrf_exempt
from django import forms
from django.contrib.auth import authenticate, login, logout

class PurchaseForm(ModelForm):
	class Meta:
		model = Purchase

class PurchaseForm(ModelForm):
	class Meta:
		model = Purchase

def booking_detail(request, id):
	pass

def purchase_detail(request):
	
	if request.method == 'POST':
		purchase = Purchase(request...)
		form = PurchaseForm(request.POST, instance=purchase)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('park/confirmation')
	else:
		form = PurchaseForm()
	t = loader.get_template('park/purchase.html')
	c = Context({'location':location,'spaces':spaces,'duration':duration,'user':user})
	return HttpResponse(t.render(c))

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

