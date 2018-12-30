from rest_framework import serializers
from .models import Restaurant, Item

class RestaurantListSerializer(serializers.ModelSerializer):
	class Meta: #creating association between ModelSerializes and the model = Article below
		model = Restaurant
		fields = ['id','name','description','logo', 'reference','owner', 'items']

# class RestaurantDetailSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Restaurant
# 		fields = ['id','name','description','opening_time', 'closing_time',]



class ItemListSerializer(serializers.ModelSerializer):
	class Meta: #creating association between ModelSerializes and the model = Article below
		model = Item
		fields = ['id','name','description','price', 'restaurant',]

class RestaurantItemSerializer(serializers.ModelSerializer):
	class Meta: 
		model = Item
		fields = ['id','name','description','price',]