from django.conf.urls.defaults import *

urlpatterns = patterns('',
	url(r'^$', 'park.views.home'),
	url(r'^list/$', 'park.views.loc_list'),
	url(r'^purchase/(?P<loc_id>\d+)?$', 'park.views.purchase_spots'),
	url(r'^booking/(?P<loc_id>\d+)?$', 'park.views.book_spots'),
	url(r'^contactus/$', 'park.views.contact_us'),
	url(r'^search/(.*)$', 'park.views.park_search'),
	url(r'^Admin/$', 'park.views.park_admin'),
	url(r'^confirmation/(?P<pur_id>\d+)?$', 'park.views.park_confirm'),
)

