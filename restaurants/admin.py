from django.contrib import admin

# Register your models here.
from .models import Restaurant, Item 

admin.site.register(Restaurant)
admin.site.register(Item)