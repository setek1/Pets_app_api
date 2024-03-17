from django.contrib import admin
from pets.models import Pets

# Register your models here.
@admin.register(Pets)
class PetsAdmin(admin.ModelAdmin):
    pass