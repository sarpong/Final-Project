from django.db import models
from django.contrib import admin

# Create your models here.
class User(models.Model):
	name=models.CharField(max_length=60)
	phone=models.CharField(max_length=40)
	email=models.EmailField()
	pin=models.IntegerField()
	def __unicode__(self):
		return self.name+ " , "+str(self.pin)

class Location(models.Model):
	location = models.CharField(max_length=60)
	address=models.CharField(max_length=60)
	no_available=models.IntegerField()
	def __unicode__(self):
		return self.location+' at '+self.address

class Purchase(models.Model):
	user=models.ForeignKey(User)
	spaces=models.IntegerField()
	location=models.ForeignKey(Location)
	duration=models.IntegerField()
	def __unicode__(self):
		return str(self.spaces)+" , "+str(self.location)+" , "+str(self.duration)

class Company(models.Model):
	name=models.CharField(max_length=100)
	location=models.ForeignKey(Location)
	service_type=models.CharField(max_length=40)
	payment_mode=models.CharField(max_length=40)
	phone=models.CharField(max_length=40)
	email=models.EmailField()
	date=models.DateField(auto_now_add=True)
	space=models.IntegerField()
	def __unicode__(self):
		return self.name+" , "+str(self.location)+" , "+self.service_type+" , "+str(self.space)+" , "+self.payment_mode+" , "+str(self.date)

class Administrator(models.Model):
	sold_spaces=models.IntegerField()
	location=models.ForeignKey(Location)
	date=models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return str(self.location) +' on '+str(self.date)+': '+str(self.sold_spaces)

class PurchaseAdmin(admin.ModelAdmin):
	list_display=('user', 'spaces','location','duration')
	search_fields=('spaces','location')
	list_filter=['spaces','location']

class CompanyAdmin(admin.ModelAdmin):
	list_display=('name','location','space','service_type','payment_mode','date')
	search_fields=('name','location','service_type','space')
	list_filter=['name', 'location', 'service_type']

class LocationAdmin(admin.ModelAdmin):
	list_display=('location','address','no_available')
	search_fields=('location','address','no_available')
	list_filter=('location','address','no_available')

class UserAdmin(admin.ModelAdmin):
	list_display=('name','phone','pin')
	search_fields=('name','pin','phone')
	list_filter=['name']	
	
class AdministratorAdmin(admin.ModelAdmin):
	list_display=('location','sold_spaces','date')
	search_fields=('location','sold_spaces','date')
	list_filter=['location','sold_spaces','date']
	
admin.site.register(Purchase,PurchaseAdmin)
admin.site.register(Company,CompanyAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(Administrator,AdministratorAdmin)
admin.site.register(Location,LocationAdmin)

