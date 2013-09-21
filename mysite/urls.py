from django.conf.urls import patterns, include, url

#from mysite.views import hello, current_datetime, hours_ahead, users, users_fill, model_of_users
#from rest_api.urls import urlpatterns

urlpatterns = patterns('mysite.views',
    ('^hello/$', 'hello'),
    ('^time/$', 'current_datetime'),
    (r'^time/plus/(\d{1,2})/$', 'hours_ahead'),
    ('^users/$', 'users'),
    ('^users/fill/$', 'users_fill'),
    ('^users/model/$', 'model_of_users')
)

urlpatterns += patterns('rest_api.views',
	('^api/users/$', 'model_of_users')
)