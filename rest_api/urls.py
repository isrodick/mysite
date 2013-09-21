from django.conf.urls import patterns, include, url

from mysite.views import hello, current_datetime, hours_ahead, users, users_fill, model_of_users

urlpatterns = patterns('',
    ('^api/users/$', model_of_users)
)