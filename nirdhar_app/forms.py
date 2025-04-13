from django import forms
from .models import Contact, Subscriber, DemoRequest

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'company', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name*'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address*'}),
            'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message*', 'rows': 5}),
        }

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
        }

class DemoRequestForm(forms.ModelForm):
    COMPANY_SIZE_CHOICES = [
        ('', 'Select company size'),
        ('1-10', '1-10 employees'),
        ('11-50', '11-50 employees'),
        ('51-200', '51-200 employees'),
        ('201-1000', '201-1000 employees'),
        ('1000+', '1000+ employees')
    ]
    
    company_size = forms.ChoiceField(choices=COMPANY_SIZE_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    
    class Meta:
        model = DemoRequest
        fields = ['name', 'email', 'company', 'company_size', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name*'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address*'}),
            'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Name*'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Additional Information', 'rows': 4}),
        } 