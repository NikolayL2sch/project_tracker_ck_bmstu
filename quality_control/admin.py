from django.contrib import admin

from quality_control.models import BugReport, FeatureRequest


@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Main Information', {
            'fields': ('title', 'description', 'project', 'task', 'status'),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    list_display = ('title', 'project', 'task', 'status', 'created_at', 'updated_at')
    list_filter = ('project', 'task', 'status')
    search_fields = ('title', 'project', 'task', 'status')
    list_editable = ('status',)
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at')


@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Main Information', {
            'fields': ('title', 'description', 'project', 'task'),
        }),
        ('Stats', {
            'fields': ('status', 'priority'),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    list_display = ('title', 'project', 'task', 'status', 'priority', 'created_at', 'updated_at')
    list_filter = ('project', 'task', 'status', 'priority')
    search_fields = ('title', 'project', 'task', 'status', 'priority')
    list_editable = ('status', 'priority')
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at')
