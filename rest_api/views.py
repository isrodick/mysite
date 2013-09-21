# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from users.models import User

def render_with_tamplate(template):
	def decorator(func):
		def wrapper(*args):
			return render_to_response( template, func(*args) )
		return wrapper
	return decorator
@render_with_tamplate('users.html')

def model_of_users(request):
	users_filter = request.GET
	filter_value = 'name'

	if( len(users_filter) and filter_value in users_filter ):
		users = User.objects.filter(full_name = users_filter[filter_value])
	else:
		users = User.objects.all()

	return {'users': users}