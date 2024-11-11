from django.contrib import admin
from .models import Enclos, Animal, Soigneur, Evenement

# Register your models here.
admin.site.register(Enclos)
admin.site.register(Animal)
admin.site.register(Soigneur)
admin.site.register(Evenement)