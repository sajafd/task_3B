from django.http import JsonResponse
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import RestaurantListSerializer, ItemListSerializer, RestaurantItemSerializer
from .models import Restaurant, Item

# def restaurant_list(request):
# 	my_restaurants = []
# 	for restaurant in Restaurant.objects.all():
# 		my_restaurants.append({
# 			'name': restaurant.name,
# 			'description': restaurant.description,
# 			})
# 	return JsonResponse(my_restaurants, safe = False)


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

# class-based API views: 

class RestaurantList(ListAPIView): 
	queryset = Restaurant.objects.all() 
	serializer_class = RestaurantListSerializer 

class ItemList(ListAPIView): 
	queryset = Item.objects.all() 
	serializer_class = ItemListSerializer 

class RestaurantItemList(ListAPIView):
	serializer_class = RestaurantItemSerializer

	def get_queryset(self): 
		restaurant_id = self.kwargs['restaurant_id'] 
		restaurant = Restaurant.objects.get(id=restaurant_id)
		return restaurant.items.all()