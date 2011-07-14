from django.db import models
#from django.contrib import admin
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


