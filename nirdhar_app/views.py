from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from .forms import ContactForm, SubscriberForm, DemoRequestForm
from .models import Contact
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    # Handle newsletter subscription
    if request.method == 'POST' and 'subscribe' in request.POST:
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for subscribing to our newsletter!")
            return redirect('/')
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def features(request):
    return render(request, 'features.html')

def pricing(request):
    return render(request, 'pricing.html')

@csrf_exempt  # Temporarily exempt CSRF for static site integration
def contact(request):
    print(f"Contact form request received. Method: {request.method}")
    
    # Get form data from either GET or POST
    if request.method == 'POST':
        print(f"POST data: {request.POST}")
        form_data = request.POST
    elif request.method == 'GET' and any(key in request.GET for key in ['name', 'email', 'message']):
        print(f"GET data with form params: {request.GET}")
        form_data = request.GET
    else:
        # Just display the empty form
        print("Rendering empty contact form")
        return render(request, 'contact.html')
    
    # Process form data from either source
    try:
        # Get form data
        name = form_data.get('name')
        email = form_data.get('email')
        company = form_data.get('company', '')  # Optional field
        phone = form_data.get('phone', '')      # Optional field
        message = form_data.get('message')
        
        # Validate required fields
        if not name or not email or not message:
            print("Missing required fields")
            messages.error(request, "Please fill out all required fields.")
            return render(request, 'contact.html')
        
        # Create and save the contact object
        contact = Contact(
            name=name,
            email=email,
            company=company,
            phone=phone,
            message=message
        )
        contact.save()
        
        print(f"Contact form saved with ID: {contact.id}")
        messages.success(request, "Thank you for contacting us! We'll get back to you soon.")
        
        # Redirect to contact page
        return redirect('/contact/?success=true')
        
    except Exception as e:
        print(f"Error saving contact form: {str(e)}")
        messages.error(request, "There was an error processing your request. Please try again.")
        return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def careers(request):
    return render(request, 'careers.html')

def demo(request):
    if request.method == 'POST':
        form = DemoRequestForm(request.POST)
        if form.is_valid():
            form.save()
            
            # Send email notification
            try:
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                company = form.cleaned_data['company']
                
                # This would normally use settings.EMAIL_HOST_USER, but for local dev we'll just print
                print(f"Email would be sent: Demo request from {name} ({email}) at {company}")
                
                messages.success(request, "Thank you for requesting a demo! We'll be in touch shortly.")
                return redirect('/demo/')
            except Exception as e:
                print(f"Error sending email: {e}")
                messages.success(request, "Your demo request has been received. We'll be in touch shortly.")
                return redirect('/demo/')
    return render(request, 'demo.html')

def privacy(request):
    return render(request, 'privacy.html')

def services(request):
    return render(request, 'services.html')

def team(request):
    return render(request, 'team.html')

def terms(request):
    return render(request, 'terms.html')

# Handle .html extension redirects
def html_redirect(request, page_name):
    """Redirect .html URLs to their proper Django URL patterns"""
    # Extract the base path regardless of where the request comes from
    if page_name == 'index':
        return redirect('/')
    else:
        return redirect('/' + page_name + '/')
