from django.contrib import admin
from models import Purchase, Company, UserProfile, Administrator, Location, PaymentMode

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

