from django.contrib import admin
from . models import CarBrand
# Register your models here.
class BrandsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name','slug']

admin.site.register(CarBrand,BrandsAdmin)