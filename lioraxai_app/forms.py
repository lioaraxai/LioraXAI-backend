from django import forms
from .models import Subscriber

# Only keeping SubscriberForm since we're using Elfsight for contact and demo forms
class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
        } 