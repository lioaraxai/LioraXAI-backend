from django.contrib import admin
from .models import Contact, Subscriber, DemoRequest

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'company', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email', 'company', 'message']
    readonly_fields = ['created_at']

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['email', 'created_at']
    list_filter = ['created_at']
    search_fields = ['email']
    readonly_fields = ['created_at']

@admin.register(DemoRequest)
class DemoRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'company', 'company_size', 'created_at']
    list_filter = ['company_size', 'created_at']
    search_fields = ['name', 'email', 'company', 'message']
    readonly_fields = ['created_at']
