from django import template
from django.template.loader import render_to_string

register = template.Library()

@register.simple_tag
def bootstrap_field(field, placeholder=None, label=None):
    """Render a form field with Bootstrap styling."""
    if placeholder:
        field.field.widget.attrs['placeholder'] = placeholder
    if label:
        field.label = label
    else:
        field.label = ''  # Hide label if not provided
    
    field.field.widget.attrs['class'] = 'form-control'
    return field

@register.filter
def add_class(field, css_class):
    """Add a CSS class to a form field."""
    return field.as_widget(attrs={"class": css_class}) 