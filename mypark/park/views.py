# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from models import User, Purchase, Company, Administrator,Location
from django.forms import ModelForm
from django import forms
from django.views.decorators.csrf import csrf_exempt
from django import forms
from django.contrib.auth import authenticate, login, logout
from time import mktime
import time

class PurchaseForm(ModelForm):
	class Meta:
		model = Purchase
		exclude = ['location']

class ContactForm(ModelForm):
	class Meta:
		model = Company

def book_spots(request, id):
	pass

def loc_list(request):
	location_list = Location.objects.all()
	t = loader.get_template('park/list.html')
	c = Context({'loc_list':location_list})
	return HttpResponse(t.render(c))

@csrf_exempt
def purchase_spots(request, loc_id):
	loc = Location.objects.get(pk=loc_id)
	purchases = Purchase.objects.filter(location=loc)
	nowTime = time.time()
	no_available = loc.no_available
	for purchase in purchases:
		print purchase.date
		startTime = mktime(purchase.date.timetuple())
		endTime = startTime + 60*60*purchase.duration

		if nowTime == endTime - startTime:
			no_available -= 1
		print purchase.duration
		print
		print startTime, endTime

	if request.method == 'POST':
		purchase = Purchase(location=loc)
		form = PurchaseForm(request.POST, instance=purchase)

		if form.is_valid():
			print form

			form.save()

			return HttpResponseRedirect('/park/confirmation/'+str(purchase.id))
	else:
		form = PurchaseForm()
	t = loader.get_template('park/purchase.html')
	print 'hello'
	print type(request.user.userprofile)
	print 'hello'
	c = Context({'form':form.as_p(),'location':loc.location, 'user':request.user.userprofile.name, 'email':request.user.userprofile.email, 'phone':request.user.userprofile.phone})
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

def park_confirm(request, pur_id):
	purchase = Purchase.objects.get(pk=pur_id)
	t = loader.get_template('park/confirmation.html')
	c = Context({'location':purchase.location, 'name':request.user.userprofile.name, 'spaces':purchase.spaces, 'duration':purchase.duration, 'date':purchase.date, 'time':purchase.time})
	return HttpResponse(t.render(c))

def home(request):
	t = loader.get_template('park/home.html')
	c = Context(dict())
	return HttpResponse(t.render(c))

#def homepage(request):
#	t = loader.get_template('park/home.html')
#	c = Context(dict())
#	return HttpResponse(t.render(c))
