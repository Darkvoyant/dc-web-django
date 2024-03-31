from django.contrib import admin
from .models import BugReport, FeatureReport

# Register your models here.


# Admin model for bug report
@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'status', 'priority',
                    'created_at', 'updated_at')
    list_filter = ('status', 'project', 'priority',)
    search_fields = ('name', 'description')
    list_editable = ('status', 'priority')
    readonly_fields = ('created_at', 'updated_at')


# Admin model for feature report
@admin.register(FeatureReport)
class FeatureReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'status', 'priority',
                    'created_at', 'updated_at')
    list_filter = ('status', 'project', 'priority',)
    search_fields = ('name', 'description')
    list_editable = ('status', 'priority')
    readonly_fields = ('created_at', 'updated_at')
