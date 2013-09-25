# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core import serializers
from users.models import User
import json

def model_of_users(request):
	users_filter = request.GET
	filter_value = 'name'

	users = User.objects.all()
	j_users = serializers.serialize("json" ,  users)

	return HttpResponse(j_users, mimetype = "application/json")