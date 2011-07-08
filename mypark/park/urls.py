from django.conf.urls.defaults import *

urlpatterns = patterns('',
	url(r'^$', 'park.views.home'),
	url(r'^purchase/(\d+)?$', 'park.views.purchase_detail'),
	url(r'^booking/(\d+)?$', 'park.views.booking_detail'),
	url(r'^contactus/$', 'park.views.contact_us'),
	url(r'^search/(.*)$', 'park.views.park_search'),
	url(r'^Admin/$', 'park.views.park_admin'),
	url(r'^confirmation/(?P<id>\d+)?$', 'park.views.park_confirmation'),
)

