from django.db import models
from django.contrib.postgres import fields

class Customuser(models.Model):
	name = models.CharField(max_length=20)
	BLOCKED = 0
	ACTIVE = 1
	USER_STATUS_CHOICES = (
		(BLOCKED, 'Blocked'),
		(ACTIVE, 'Active'),
	)
	status = models.IntegerField(
		choices=USER_STATUS_CHOICES,
		default=ACTIVE,
	)
	favorites = models.ManyToManyField('Recipe',related_name='users')

class Recipe(models.Model):
	name = models.CharField(max_length=20)
	description = models.CharField(max_length=200)
	photo = models.ImageField(null=True)
	author = models.ForeignKey(Customuser,on_delete=models.CASCADE)
	likes = models.IntegerField()
	hashtags = fields.ArrayField(
		models.CharField(max_length=10),
		),
	BLOCKED = 0
	ACTIVE = 1
	RECIPE_STATUS_CHOICES = (
		(BLOCKED, 'Blocked'),
		(ACTIVE, 'Active'),
	)

	status = models.IntegerField(
		choices=RECIPE_STATUS_CHOICES,
		default=ACTIVE,
	)
	creation_date =	models.DateTimeField(auto_now_add=True)

	steps = fields.ArrayField(
		models.CharField(max_length=200),
		),	

	SALAD = 0
	FIRST = 1
	SECOND = 2
	SOUP = 3
	DESSERT = 4
	DRINK = 5
	DISH_TYPE_CHOICES = (
		(SALAD, 'Salad'),
		(FIRST, 'FIRST'),
		(SECOND, 'SECOND'),
		(SOUP, 'SOUP'),
		(DESSERT, 'DESSERT'),
		(DRINK, 'DRINK'),
	)
	dish_type = models.IntegerField(
		choices=DISH_TYPE_CHOICES,
	)
# Create your models here.
