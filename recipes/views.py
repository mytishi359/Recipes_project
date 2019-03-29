from django.http import HttpResponse
from django.conf import settings
from django.views import View
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Customuser, Recipe
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from recipes.serializers import UserSerializer, RecipeSerializer, RecipePhotoSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import generics
from datetime import datetime
import json

class UserView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse(json.dumps(list(Customuser.objects.all().values())))

class RecipeView(View):

	def get(self, request, *args, **kwargs):
		return HttpResponse(json.dumps(list(Recipe.objects.all().values())))

class RecipeViewSet(viewsets.ModelViewSet):

	def list(self, request):
		queryset = Recipe.objects.all()
		serializer = RecipeSerializer(queryset, many=True)
		return Response(serializer.data)

	def retrieve(self, request, pk=None):
		queryset = Recipe.objects.all()
		recipe = get_object_or_404(queryset, pk=pk)
		serializer = RecipeSerializer
		return Response(serializer.data)

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		#headers = self.get_success_headers(serializer.data)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)

	serializer_class = RecipeSerializer

class UserViewSet(viewsets.ModelViewSet):

	"""
	A simple ViewSet for listing or retrieving users.
	"""
	def list(self, request):
		queryset = User.objects.all()
		serializer = UserSerializer(queryset, many=True)
		return Response(serializer.data)

	def retrieve(self, request, pk=None):
		queryset = User.objects.all()
		user = get_object_or_404(queryset, pk=pk)
		serializer = UserSerializer(user)
		return Response(serializer.data)

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		#headers = self.get_success_headers(serializer.data)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)

	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer

	"""
	Example empty viewset demonstrating the standard
	actions that will be handled by a router class.

	If you're using format suffixes, make sure to also include
	the `format=None` keyword argument for each action.
	"""

class PhotoUpload(generics.UpdateAPIView):
	queryset = Recipe.objects.all()
	serializer = RecipePhotoSerializer

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

for user in User.objects.all():
    Token.objects.get_or_create(user=user)

# Create your views here.
