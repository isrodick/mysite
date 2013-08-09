# -*- coding: utf-8 -*-

from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
import datetime


def hello(request):
	return HttpResponse("Sid корпарейшен")


def current_datetime(request):
	now = datetime.datetime.now()

	return render_to_response('current_datetime.html', {'current_date': now})


def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except valueError:
		raise Http404()

	dt = datetime.datetime.now() + datetime.timedelta(hours = offset)

	return render_to_response('hours_ahead.html', {'hour_offset': offset, 'next_time': dt})


def users(request):
	user1 = {'Login': 'Sid', 'Full name': 'Родион', 'Date birthday': "04-07-1993"}
	user2 = {'Login': 'dark', 'Full name': 'Антон', 'Date birthday': "10-10-1993"}
	user3 = {'Login': 'Enzo', 'Full name': 'Глеб', 'Date birthday': "30-03-1993"}
	user4 = {'Login': 'Storm', 'Full name': 'Сергей', 'Date birthday': "13-05-1992"}
	user5 = {'Login': 'Avenger', 'Full name': 'Павлуша', 'Date birthday': "04-07-1993"}
	users = (user1, user2, user3, user4, user5)

	return render_to_response('users.html', {'users': users})