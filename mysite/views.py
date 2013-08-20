# -*- coding: utf-8 -*-

from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from users.models import User
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

def users_fill(request):
	user1 = User(login = "Sid", full_name = "Родион", date_birthday = "1993-07-04")
	user1.save()
	user2 = User(login = "dark", full_name = "Антон", date_birthday = "1993-10-10")
	user2.save()
	user3 = User(login = "Enzo", full_name = "Глеб", date_birthday = "1993-03-30")
	user3.save()
	user4 = User(login = "Storm", full_name = "Сергей", date_birthday = "1992-05-13")
	user4.save()
	user5 = User(login = "Avenger", full_name = "Павлуша", date_birthday = "1993-07-04")
	user5.save()

	return HttpResponse("Users filled")

@render_with_tamplate('users_model.html')
def model_of_users(request):
	users1 = User.objects.get(id = 1)
	users2 = User.objects.get(id = 2)
	users3 = User.objects.get(id = 3)
	users4 = User.objects.get(id = 4)
	users5 = User.objects.get(id = 5)

	return {'users1': users1, 'users2': users2, 
	'users3': users3, 'users4': users4, 'users5': users5}