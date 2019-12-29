from django.contrib import admin
from .models import Category, Country

# Register your models here.

admin.site.register(Country)
admin.site.register(Category)