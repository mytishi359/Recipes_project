from django.http import HttpResponse
from django.views import View
from .models import Customuser, Recipe
import json

class UserView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse(json.dumps(list(Customuser.objects.all().values())))

class RecipeView(View):

	def get(self, request, *args, **kwargs):
		return HttpResponse(json.dumps(list(Recipe.objects.all().values())))


# Create your views here.
