from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('features/', views.features, name='features'),
    path('pricing/', views.pricing, name='pricing'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('blog/category/<slug:category_slug>/', views.blog_category, name='blog_category'),
    path('newsletter-subscribe/', views.newsletter_subscribe, name='newsletter_subscribe'),
    path('team/', views.team, name='team'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
    
    # Handle .html extension URLs
    re_path(r'^(?P<page_name>index|features|pricing|contact|blog|team|privacy|terms)\.html$', 
            views.html_redirect, name='html_redirect'),
            
    # Temporary secure setup route
    path('secure-setup/', views.secure_setup, name='secure_setup'),
    
    # Database diagnostic view
    path('db-check/', views.db_check, name='db_check'),
] 