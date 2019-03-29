from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Recipe

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class RecipeSerializer(serializers.ModelSerializer):
	author = serializers.PrimaryKeyRelatedField(many=True, read_only=True)	

	class Meta:
		model = Recipe
		fields = ('name','description','photo','author','likes','hashtags','status','creation_date','steps','dish_type')

class RecipePhotoSerializer(serializers.Serializer):
    photo = serializers.ImageField()

    def update(self, instance, validated_data):
        instance.photo = validated_data.get('content', instance.photo)
        instance.save()
        return instance
