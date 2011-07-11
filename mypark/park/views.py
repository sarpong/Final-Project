# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from models import User, Purchase, Company, Administrator,Location
from django.forms import ModelForm
from django import forms
from django.views.decorators.csrf import csrf_exempt
from django import forms
from django.contrib.auth import authenticate, login, logout

class PurchaseForm(ModelForm):
	class Meta:
		model = Purchase
		exclude = ['user','location']

class ContactForm(ModelForm):
	class Meta:
		model = Company

def book_spots(request, id):
	pass

@csrf_exempt
def purchase_spots(request, loc_id):
	print loc_id
	loc = Location.objects.get(pk=loc_id)
	purchase = Purchase.objects.get(pk=loc_id)
	if request.method == 'POST':
		purchase = Purchase(user=request.user.username, location=loc)
		form = PurchaseForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('park/confirmation')
	else:
		form = PurchaseForm()
	t = loader.get_template('park/purchase.html')
	c = Context({'form':form.as_p(),'location':loc.location, 'spaces':purchase.spaces, 'duration':purchase.duration})
	return HttpResponse(t.render(c))

@csrf_exempt
def contact_us(request):
	company = Company.objects.all()
	if request.method == 'POST':
		company = Company()
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse('Your company has been registered. \nWe would get back to you soon.')
	else:
		form = ContactForm()
	t = loader.get_template('park/contact.html')
	c = Context({'form':form.as_p()})
	return HttpResponse(t.render(c))

def park_search(request, term):
	loc_list = Location.objects.filter(location__icontains=term)
	f = loader.get_template('park/search.html')
	g = Context({'loc_list':loc_list,'term':term})
	return HttpResponse(f.render(g))

def park_admin(request):
	pass

def park_confirm(request, loc_id):
	loc = Location.objects.get(pk=loc_id)
	purchase = Purchase.objects.get(pk=loc_id)
	t = loader.get_template('park/confirmation.html')
	c = Context({'location':loc.location, 'name':request.user.username, 'spaces':purchase.spaces, 'duration':purchase.duration, 'date':purchase.date, 'time':purchase.time})
	return HttpResponse(t.render(c))

def home(request):
	t = loader.get_template('park/base.html')
	c = Context(dict())
	return HttpResponse(t.render(c))

