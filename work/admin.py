from django.contrib import admin
from .models import WorkHistory

# Register your models here.
@admin.register(WorkHistory)
class WorkHistoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'profile', 'work_type', 'worked_at']