
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from restaurants import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurants/list/',views.RestaurantList.as_view() ,name='restaurant-list'),
    path('restaurants/detail/<restaurant_id>',views.restaurant_detail ,name='restaurant-detail'),
    # path('restaurants/detail/<restaurant_id>/item-list',views.ItemList.as_view(), name = 'item-list'),
    path('restaurants/detail/<restaurant_id>/item-list',views.RestaurantItemList.as_view(), name = 'item-list'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)