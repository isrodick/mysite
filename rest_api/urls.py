from django.conf.urls import patterns, include, url

urlpatterns = patterns('rest_api.views',
    ('^users/$', 'model_of_users')
)