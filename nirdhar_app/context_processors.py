from .forms import ContactForm, SubscriberForm, DemoRequestForm

def common_forms(request):
    return {
        'contact_form': ContactForm(),
        'subscriber_form': SubscriberForm(),
        'demo_form': DemoRequestForm(),
    } 