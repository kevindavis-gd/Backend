from django.contrib import admin
from . models import Campus, Room, Building, Equipment

# Register your models here.

admin.site.register(Campus)
admin.site.register(Room)
admin.site.register(Building)
admin.site.register(Equipment)