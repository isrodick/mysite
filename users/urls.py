from django.conf.urls import patterns, include, url
from users.views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = patterns('',
	(r'^', include(router.urls))
)