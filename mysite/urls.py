from django.conf.urls import patterns, include, url

from mysite.views import hello, current_datetime, hours_ahead, users

urlpatterns = patterns('',
    ('^hello/$', hello),
    ('^time/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    ('^users/$', users)
)
