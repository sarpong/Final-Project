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



class Purchase(models.Model):
	user=models.ForeignKey(User)
	spaces=models.IntegerField()
	location=models.CharField(max_length=100)
	duration=models.IntegerField()
	def __unicode__(self):
		return str(self.spaces)+" , "+self.location+" , "+str(self.duration)

class Company(models.Model):
	name=models.CharField(max_length=100)
	location=models.CharField(max_length=100)
	service_type=models.CharField(max_length=40)
	payment_mode=models.CharField(max_length=40)
	phone=models.CharField(max_length=40)
	email=models.EmailField()
	date=models.DateField(auto_now_add=True)
	space=models.IntegerField()
	def __unicode__(self):
		return self.name+" , "+self.location+" , "+self.service+" , "+str(self.space)+" , "+self.payment_mode+" , "+str(self.date)

class Admin(models.Model):
	sold_spaces=models.IntegerField()
	location=models.CharField(max_length=100)
	date=models.DateTimeField(auto_now=True)



#class PurchaseInline(admin.TabularInline):
      #model=Purchase
     

class PurchaseAdmin(admin.ModelAdmin):
	pass
      #list_display=('user', 'spaces','location','duration')
      #search_fields=('spaces','location')
      #list_filter=['spaces','location']
      #inlines=[PurchaseInline]

class CompanyAdmin(admin.ModelAdmin):
      #list_display=('name','location','space','service_type','payment_mode','date')
      #search_fields=('name','location'.'service_type','space')
      #list_filter=[]
     
class UserAdmin(admin.ModelAdmin):
	pass 

admin.site.register(Purchase,PurchaseAdmin)
admin.site.register(Company,CompanyAdmin)
admin.site.register(User,UserAdmin)


