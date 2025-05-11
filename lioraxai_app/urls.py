from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('features/', views.features, name='features'),
    path('pricing/', views.pricing, name='pricing'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('careers/', views.careers, name='careers'),
    path('demo/', views.demo, name='demo'),
    path('privacy/', views.privacy, name='privacy'),
    path('services/', views.services, name='services'),
    path('team/', views.team, name='team'),
    path('terms/', views.terms, name='terms'),
    
    # Handle .html extension URLs
    re_path(r'^(?P<page_name>index|about|features|pricing|contact|blog|careers|demo|privacy|services|team|terms)\.html$', 
            views.html_redirect, name='html_redirect'),
            
    # Temporary secure setup route
    path('secure-setup/', views.secure_setup, name='secure_setup'),
] 