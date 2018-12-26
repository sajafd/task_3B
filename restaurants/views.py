from django.shortcuts import render
from django.http import JsonResponse
from .models import Restaurant

def restaurant_list(request):
	my_restaurants = []
	for restaurant in Restaurant.objects.all():
		my_restaurants.append({
			'name': restaurant.name,
			'description': restaurant.description,
			})
	return JsonResponse(my_restaurants, safe = False)


def restaurant_detail(request, restaurant_id):
	restaurant_obj = Restaurant.objects.get(id = restaurant_id)
	my_restaurant = {
	'index': restaurant_obj.id,
	'name': restaurant_obj.name,
	'description': restaurant_obj.description,
	'opening_time' : restaurant_obj.opening_time,
	'closing_time' : restaurant_obj.closing_time,
	}
	return JsonResponse(my_restaurant)
