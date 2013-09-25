from django.conf.urls import patterns, include, url
#from mysite.views import hello, current_datetime, hours_ahead, users, users_fill, model_of_users
from rest_api.urls import urlpatterns
from users import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = patterns('mysite.views',
    ('^hello/$', 'hello'),
    ('^time/$', 'current_datetime'),
    (r'^time/plus/(\d{1,2})/$', 'hours_ahead'),
    ('^users/$', 'users'),
    ('^users/fill/$', 'users_fill'),
    ('^users/model/$', 'model_of_users'),
)

urlpatterns += patterns('',
	('^api/', include('rest_api.urls'))
)

urlpatterns += patterns('',
	(r'^', include(router.urls))
)

urlpatterns += patterns('',
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
	)