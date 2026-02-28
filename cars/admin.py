# admin.py
from django.contrib import admin
from .models import Car, CarImage, InterestSetting
from .models import About, Employee, Contact

class CarImageInline(admin.TabularInline):
    model = CarImage
    extra = 1
    
admin.site.register(CarImage)
admin.site.register(About)
admin.site.register(Employee)
admin.site.register(Contact)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    inlines = [CarImageInline]
    list_display = ('title', 'price', 'is_promo', 'is_electric', 'transmission')
    list_filter = ('is_promo', 'is_electric', 'transmission')
    search_fields = ('title',)


@admin.register(InterestSetting)
class InterestSettingAdmin(admin.ModelAdmin):
    list_display = ('yearly_interest',)
