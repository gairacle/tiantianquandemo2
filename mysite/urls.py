from django.conf.urls import *


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('mysite.views',
    ('^hello/$','hello'),
    ('^time/$','current_datetime'),
    (r'^time/plus/(\d{1,2})/$', 'hours_ahead'),
)
urlpatterns += patterns('books.views',
	(r'^search-form/$','search_form'),
	(r'^search/$','search'),
	(r'^contact/$','contact')
)

urlpatterns += patterns('',
	(r'^admin/',include(admin.site.urls)),
)

