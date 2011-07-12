from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	name = models.CharField(max_length=60)
	phone=models.CharField(max_length=40)
	email=models.EmailField()
	pin=models.IntegerField()
	def __unicode__(self):
		return self.name

class Location(models.Model):
	location = models.CharField(max_length=60)
	address=models.CharField(max_length=60)
	no_available=models.IntegerField()
	def __unicode__(self):
		return self.location

class Purchase(models.Model):
	spaces=models.IntegerField()
	location=models.ForeignKey(Location)
	duration=models.IntegerField()
	date=models.DateField(auto_now=True)
	time=models.TimeField(auto_now=True)
	def __unicode__(self):
		return str(self.location)+": "+str(self.spaces)+" , "+str(self.duration)+' hours.'

class PaymentMode(models.Model):
	payment_type = models.CharField(max_length=60)
	def __unicode__(self):
		return self.payment_type

class Company(models.Model):
	name=models.CharField(max_length=60)
	location=models.CharField(max_length=100)
	payment_mode=models.ForeignKey(PaymentMode)
	phone=models.CharField(max_length=40)
	email=models.EmailField()
	date=models.DateField(auto_now_add=True)
	spaces=models.IntegerField()
	def __unicode__(self):
		return self.name

#class Date(models.Models):
#	day_purchase=models.IntegerField()
#	month_purchase=models.IntegerField()
#	year_purchase=models.IntegerField()
#	def __unicode__(self):
#		return self.day

class Administrator(models.Model):
	sum_available=models.IntegerField()
	location=models.ForeignKey(Location)
	date=models.DateTimeField(auto_now=True)
	available=models.BooleanField()
	def __unicode__(self):
		return str(self.location) +' on '+str(self.date)

class PurchaseAdmin(admin.ModelAdmin):
	list_display=('spaces','location','duration','date','time')
	search_fields=('spaces','location','date','time')
	list_filter=['spaces','location','date','time']

class CompanyAdmin(admin.ModelAdmin):
	list_display=('name','location','spaces','payment_mode','date')
	search_fields=('name','location','spaces')
	list_filter=['name', 'location']

class LocationAdmin(admin.ModelAdmin):
	list_display=('location','address','no_available')
	search_fields=('location','address','no_available')
	list_filter=('location','address','no_available')

class UserProfileAdmin(admin.ModelAdmin):
	list_display=('name','phone','pin','email')
	search_fields=('name','pin','phone','email')
#	list_filter=['phone','pin']

class AdministratorAdmin(admin.ModelAdmin):
	list_display=('location','sum_available','date','available')
	search_fields=('location','sum_available','date','available')
	list_filter=['location','sum_available','date','available']

class PaymentModeAdmin(admin.ModelAdmin):
	list_display=['payment_type']
	search_fields=['payment_type']
	list_filter=['payment_type']
	
admin.site.register(Purchase,PurchaseAdmin)
admin.site.register(Company,CompanyAdmin)
admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Administrator,AdministratorAdmin)
admin.site.register(Location,LocationAdmin)
admin.site.register(PaymentMode,PaymentModeAdmin)

