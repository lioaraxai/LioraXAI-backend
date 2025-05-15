from .forms import SubscriberForm

def common_forms(request):
    return {
        'subscriber_form': SubscriberForm(),
    } 