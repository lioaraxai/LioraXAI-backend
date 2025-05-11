from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from .forms import ContactForm, SubscriberForm, DemoRequestForm
from .models import Contact, Subscriber, DemoRequest
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth.models import User
import secrets

# Create your views here.

def index(request):
    if 'subscribed' in request.GET:
        messages.success(request, "Thank you for subscribing to our newsletter!")
    
    # Handle newsletter subscription for non-Formspree fallback
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
    # Display success message when redirected from Formspree
    if 'success' in request.GET:
        messages.success(request, "Thank you for contacting us! We'll get back to you soon.")
        return render(request, 'contact.html')
    
    # Legacy processing for non-Formspree fallback
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

@csrf_exempt  # Temporarily exempt CSRF for static site integration
def demo(request):
    # Display success message when redirected from Formspree
    if 'success' in request.GET:
        messages.success(request, "Thank you for requesting a demo! We'll be in touch shortly.")
        return render(request, 'demo.html')
    
    # Legacy processing for non-Formspree fallback
    print(f"Demo request received. Method: {request.method}")
    
    # Get form data from either POST or GET
    if request.method == 'POST':
        print(f"Demo POST data: {request.POST}")
        form = DemoRequestForm(request.POST)
        if form.is_valid():
            demo_request = form.save()
            print(f"Demo request saved with ID: {demo_request.id}")
            
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
        else:
            print(f"Demo form validation errors: {form.errors}")
    elif request.method == 'GET' and any(key in request.GET for key in ['first_name', 'last_name', 'email']):
        # Handle the static HTML form submission which comes as GET with different field names
        print(f"Demo GET data with form params: {request.GET}")
        
        try:
            # Create form data with the right field names
            form_data = {
                'name': f"{request.GET.get('first_name', '')} {request.GET.get('last_name', '')}".strip(),
                'email': request.GET.get('email', ''),
                'company': request.GET.get('company', ''),
                'company_size': request.GET.get('company_size', ''),
                'phone': request.GET.get('phone', ''),
                'message': request.GET.get('message', '')
            }
            
            # Validate required fields
            if not form_data['name'] or not form_data['email'] or not form_data['company']:
                print("Missing required fields from GET form")
                messages.error(request, "Please fill out all required fields.")
                return render(request, 'demo.html')
            
            # Create and save the demo request manually
            demo = DemoRequest(
                name=form_data['name'],
                email=form_data['email'],
                company=form_data['company'],
                company_size=form_data['company_size'],
                phone=form_data.get('phone'),
                message=form_data.get('message')
            )
            demo.save()
            
            print(f"Demo request saved with ID: {demo.id} (from GET form)")
            messages.success(request, "Thank you for requesting a demo! We'll be in touch shortly.")
            
            # Redirect to demo page with success parameter
            return redirect('/demo/?success=true')
            
        except Exception as e:
            print(f"Error saving demo form from GET: {str(e)}")
            messages.error(request, "There was an error processing your request. Please try again.")
            return render(request, 'demo.html')
    else:
        print("Rendering empty demo form")
        
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

# Secure setup view - only works once and with a token
def secure_setup(request, token=None):
    # This should be a unique token you generate and know
    setup_token = request.GET.get('token')
    
    if not setup_token or setup_token != 'your_secure_token_here':
        return HttpResponse("Unauthorized", status=401)
    
    # Create superuser if none exists
    if not User.objects.filter(is_superuser=True).exists():
        username = 'admin'
        email = 'admin@example.com'
        password = secrets.token_urlsafe(12)  # Generate a secure password
        
        User.objects.create_superuser(username, email, password)
        
        return HttpResponse(f"Superuser created successfully. Username: {username}, Password: {password}<br><br>IMPORTANT: This password will only be shown once! Save it immediately.")
    else:
        return HttpResponse("Superuser already exists")

# Database diagnostic view
def db_check(request):
    try:
        # Test database connection
        from django.db import connections, connection
        from django.db.utils import OperationalError
        
        db_conn = connections['default']
        db_status = "Connected"
        
        try:
            c = db_conn.cursor()
            c.execute("SELECT 1")
            row = c.fetchone()
            if row is None:
                db_status = "Connected but query returned no results"
        except OperationalError as e:
            db_status = f"Error: {str(e)}"
        
        # Check if auth_user table exists
        tables = []
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT table_name FROM information_schema.tables 
                    WHERE table_schema = 'public'
                """)
                tables = [row[0] for row in cursor.fetchall()]
                
                # Check specifically for auth_user
                cursor.execute("""
                    SELECT EXISTS (
                       SELECT FROM information_schema.tables 
                       WHERE table_schema = 'public'
                       AND table_name = 'auth_user'
                    );
                """)
                auth_table_exists = cursor.fetchone()[0]
                
                if not auth_table_exists:
                    # Run migrations for auth app specifically
                    from django.core.management import call_command
                    call_command('migrate', 'auth', '--noinput')
                    call_command('migrate', '--noinput')
                    
                    # Check again
                    cursor.execute("""
                        SELECT EXISTS (
                           SELECT FROM information_schema.tables 
                           WHERE table_schema = 'public'
                           AND table_name = 'auth_user'
                        );
                    """)
                    auth_table_exists_now = cursor.fetchone()[0]
                    tables_status = f"Auth tables were missing. Migration ran: {auth_table_exists_now}"
                else:
                    tables_status = "Auth tables exist"
        except Exception as e:
            tables_status = f"Error checking tables: {str(e)}"
            
        # Check for superuser
        from django.contrib.auth.models import User
        try:
            superusers = User.objects.filter(is_superuser=True)
            users_list = [f"{u.username} ({u.email})" for u in superusers]
            superuser_info = ", ".join(users_list) if users_list else "No superusers found"
        except Exception as e:
            superuser_info = f"Error checking superusers: {str(e)}"
            
        # Create admin user if none exists
        admin_created = False
        try:
            if not User.objects.filter(username='admin').exists() and request.GET.get('create_admin') == '1':
                # Generate secure random password
                import secrets
                admin_password = secrets.token_urlsafe(12)
                
                User.objects.create_superuser('admin', 'admin@example.com', admin_password)
                admin_created = f"Admin user created successfully with password: {admin_password}<br>IMPORTANT: Save this password now! It won't be shown again."
        except Exception as e:
            admin_created = f"Error creating admin: {str(e)}"
                
        # Run migrations
        import sys
        from io import StringIO
        from django.core.management import call_command
        
        migration_output = StringIO()
        try:
            call_command('showmigrations', stdout=migration_output)
            migrations = migration_output.getvalue()
        except Exception as e:
            migrations = f"Error checking migrations: {str(e)}"
            
        return HttpResponse(f"""
            <h1>Database Diagnostic</h1>
            <h2>Connection</h2>
            <p>{db_status}</p>
            
            <h2>Database Tables Status</h2>
            <p>{tables_status}</p>
            
            <h2>Database Tables</h2>
            <ul>
                {''.join(f'<li>{table}</li>' for table in tables)}
            </ul>
            
            <h2>Superusers</h2>
            <p>{superuser_info}</p>
            
            <h2>Admin Creation</h2>
            <p>{'Admin user already exists' if not admin_created else admin_created}</p>
            
            <h2>Migrations</h2>
            <pre>{migrations}</pre>
            
            <h2>Actions</h2>
            <p><a href="/admin/">Go to Admin Login</a></p>
            <p><a href="/db-check/?run_migrations=1">Force Run Migrations</a></p>
            <p><a href="/db-check/?create_admin=1">Create Admin User</a> (only if none exists)</p>
        """, content_type="text/html")
    except Exception as e:
        # Fallback - try to run migrations directly
        if request.GET.get('run_migrations') == '1':
            try:
                from django.core.management import call_command
                call_command('migrate', '--noinput')
                return HttpResponse("Migrations attempted directly. <a href='/db-check/'>Check Again</a>")
            except Exception as sub_e:
                return HttpResponse(f"Migration error: {str(sub_e)}")
        return HttpResponse(f"Diagnostic error: {str(e)}", content_type="text/html")
