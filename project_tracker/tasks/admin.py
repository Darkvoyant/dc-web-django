from django.contrib import admin
from .models import Project, Task
from quality_control.models import BugReport, FeatureReport
# Register your models here.


# Inline class for task
class TaskInline(admin.TabularInline):
    model = Task
    extra = 0
    fields = ('name', 'description', 'assignee', 'status', 'created_at',
              'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    can_delete = True
    show_change_link = True


# Inline class for bug report
class BugReportInline(admin.TabularInline):
    model = BugReport
    extra = 0
    fields = ('title', 'description', 'status', 'priority', 'created_at',
              'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    can_delete = False
    show_change_link = True


# Inline class for feature report
class FeatureReportInline(admin.TabularInline):
    model = BugReport
    extra = 0
    fields = ('title', 'description', 'status', 'priority', 'created_at',
              'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    can_delete = False
    show_change_link = True


# Admin class for project
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name', 'description')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'

    # Connect inlines
    inlines = [TaskInline, BugReportInline, FeatureReportInline]


# Admin class for task
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'assignee', 'status', 'created_at',
                    'updated_at')
    list_filter = ('status', 'assignee', 'project')
    search_fields = ('name', 'description')
    list_editable = ('status', 'assignee')
    readonly_fields = ('created_at', 'updated_at')

    # Connect inlines
    inlines = [BugReportInline, FeatureReportInline]
