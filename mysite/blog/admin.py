from django.contrib import admin
from .models import Dataset

@admin.register(Dataset)
class DatasetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'created_at')  # fields you want to see
    search_fields = ('name', 'owner__username')           # optional