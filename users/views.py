from rest_framework import viewsets
from users.serializers import UserSerializer
from users.models import User
from rest_framework.response import Response

#class UserViewSet(viewsets.ModelViewSet):
#	queryset = User.objects.all()
#	serializer_class = UserSerializer

class UserViewSet(viewsets.ViewSet):
	def list(self, request):
		queryset = User.objects.all()
		serializer = UserSerializer(queryset, many = True)

		return Response(serializer.data)