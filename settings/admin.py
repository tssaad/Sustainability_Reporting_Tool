from django.contrib import admin
from .models import Country, City, Province


admin.site.register(Country)
admin.site.register(Province)
admin.site.register(City)
