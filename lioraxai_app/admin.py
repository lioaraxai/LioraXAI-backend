from django.contrib import admin
from .models import Contact, Subscriber, DemoRequest

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'company', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'company', 'message')
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'company', 'phone')
        }),
        ('Message', {
            'fields': ('message',)
        }),
        ('System', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('email',)
    readonly_fields = ('created_at',)

class DemoRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'company', 'company_size', 'created_at')
    list_filter = ('created_at', 'company_size')
    search_fields = ('name', 'email', 'company', 'message')
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'phone')
        }),
        ('Company Information', {
            'fields': ('company', 'company_size')
        }),
        ('Request Details', {
            'fields': ('message',)
        }),
        ('System', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

# Register your models here.
admin.site.register(Contact, ContactAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(DemoRequest, DemoRequestAdmin)

# Customize admin site
admin.site.site_header = 'LioraXAI Administration'
admin.site.site_title = 'LioraXAI Admin Portal'
admin.site.index_title = 'Welcome to LioraXAI Admin Portal'
