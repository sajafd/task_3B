from django.contrib import admin

# Register your models here.
from .models import Restaurant #,Whatever

admin.site.register(Restaurant)