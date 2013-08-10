# -*- coding: utf-8 -*-

from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
#from django.template import Context
import datetime

def render_with_tamplate(template):
	def decorator(func):
		def wrapper(*args):
			return render_to_response( template, func(*args) )
		return wrapper
	return decorator


def hello(request):
	return HttpResponse("Sid корпарейшен")

@render_with_tamplate('current_datetime.html')
def current_datetime(request):
	now = datetime.datetime.now()

	return {'current_date': now}

@render_with_tamplate('hours_ahead.html')
def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except valueError:
		raise Http404()

	dt = datetime.datetime.now() + datetime.timedelta(hours = offset)

	return {'hour_offset': offset, 'next_time': dt}

@render_with_tamplate('users.html')
def users(request):
	user1 = {'Login': 'Sid', 'Full_name': 'Родион', 'Date_birthday': "04-07-1993"}
	user2 = {'Login': 'dark', 'Full_name': 'Антон', 'Date_birthday': "10-10-1993"}
	user3 = {'Login': 'Enzo', 'Full_name': 'Глеб', 'Date_birthday': "30-03-1993"}
	user4 = {'Login': 'Storm', 'Full_name': 'Сергей', 'Date_birthday': "13-05-1992"}
	user5 = {'Login': 'Avenger', 'Full_name': 'Павлуша', 'Date_birthday': "04-07-1993"}
	users = (user1, user2, user3, user4, user5)

	return {'users': users}