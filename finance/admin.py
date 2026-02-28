from django.contrib import admin
from .models import InterestSetting

@admin.register(InterestSetting)
class InterestAdmin(admin.ModelAdmin):
    list_display = ('yearly_interest', 'updated_at')
    ordering = ('-updated_at',)

