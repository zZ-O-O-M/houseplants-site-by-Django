from django.contrib import admin

from .models import Plant, PlantType, WindowType

admin.site.register(Plant)
admin.site.register(PlantType)
admin.site.register(WindowType)
