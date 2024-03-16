from django.contrib import admin
from pets.models import Owner

# Register your models here.
@admin.register(Owner)
class CategoryAdmnin(admin.ModelAdmin):
    pass