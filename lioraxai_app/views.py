from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from .forms import SubscriberForm
from .models import Contact, Subscriber, DemoRequest
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth.models import User
import secrets
from datetime import datetime

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

def features(request):
    # Combined features and services page
    return render(request, 'features.html')

def pricing(request):
    return render(request, 'pricing.html')

@csrf_exempt  # Temporarily exempt CSRF for static site integration
def contact(request):
    # With Elfsight form integration, we only need to render the template
    # Elfsight handles form submission and processing
    return render(request, 'contact.html')

# This function could be moved to a separate utility file
def get_blog_data():
    """Helper function to get sample blog data"""
    featured_post = {
        'title': 'The ROI of AI-Powered Knowledge Management',
        'slug': 'roi-ai-knowledge-management',
        'excerpt': 'Quantifying the business impact of AI knowledge systems is critical for enterprise adoption. Our research across 150+ implementations reveals the key metrics that matter and how to track them effectively.',
        'image_url': 'https://images.unsplash.com/photo-1638202993928-7d113507abdb?q=80&w=1100',
        'category': 'AI Strategy',
        'read_time': 8,
        'author': {
            'name': 'Dr. Sarah Rodriguez',
            'image_url': 'https://randomuser.me/api/portraits/women/23.jpg'
        },
        'published_date': datetime(2023, 4, 14),
        'content': """
        <p>Quantifying the business impact of AI knowledge systems is critical for enterprise adoption. Our research across 150+ implementations reveals the key metrics that matter and how to track them effectively.</p>
        <p>In today's knowledge-driven economy, businesses are increasingly turning to artificial intelligence to manage, distribute, and leverage their organizational knowledge. However, justifying the investment in AI knowledge management systems requires a clear understanding of the return on investment (ROI).</p>
        <h2>Key ROI Metrics for AI Knowledge Management</h2>
        <p>Based on our research across more than 150 enterprise implementations, we've identified the following key metrics that demonstrate the value of AI-powered knowledge management:</p>
        <ul>
            <li><strong>Time Savings:</strong> On average, employees save 5.2 hours per week when using AI knowledge systems to find information.</li>
            <li><strong>Faster Onboarding:</strong> New employee ramp-up time decreases by 47% when AI knowledge tools are implemented.</li>
            <li><strong>Knowledge Retention:</strong> Organizations capture 78% more critical knowledge from departing employees.</li>
            <li><strong>Reduced Support Costs:</strong> Customer support tickets decrease by 35% through better knowledge access.</li>
            <li><strong>Innovation Acceleration:</strong> Time to market for new products decreases by 23% due to better cross-functional knowledge sharing.</li>
        </ul>
        <h2>Measuring Implementation Success</h2>
        <p>To effectively measure the ROI of your AI knowledge management implementation, follow these key steps:</p>
        <ol>
            <li>Establish clear baseline metrics before implementation</li>
            <li>Define specific KPIs aligned with your organizational goals</li>
            <li>Implement incremental measurement at 30, 60, and 90-day intervals</li>
            <li>Capture both quantitative data and qualitative feedback</li>
            <li>Adjust your implementation strategy based on early measurements</li>
        </ol>
        <p>The most successful implementations we've studied all share one common factor: a commitment to measuring outcomes from day one.</p>
        <blockquote>
            "The data doesn't lie—our AI knowledge management system paid for itself within five months, primarily through productivity gains and reduced duplication of effort." — CIO, Fortune 500 Manufacturing Company
        </blockquote>
        <h2>Long-term Value Creation</h2>
        <p>While short-term productivity gains are often the most visible benefit, our research shows that the most significant ROI comes from long-term value creation:</p>
        <ul>
            <li><strong>Institutional Memory:</strong> Organizations build a persistent knowledge base that transcends employee turnover.</li>
            <li><strong>Decision Quality:</strong> Data-backed decisions improve by 42% when relevant knowledge is readily accessible.</li>
            <li><strong>Cultural Transformation:</strong> Knowledge sharing becomes embedded in organizational culture, creating a virtuous cycle of continuous improvement.</li>
        </ul>
        <p>The organizations that realize the highest ROI are those that view AI knowledge management not merely as a technological solution but as a strategic asset that transforms how the organization learns, adapts, and evolves.</p>
        """
    }
    
    blog_posts = [
        {
            'title': 'Breaking Down Knowledge Silos in Enterprise Organizations',
            'slug': 'breaking-knowledge-silos',
            'excerpt': 'How AI-powered systems are helping large organizations connect isolated information and expertise across departments.',
            'image_url': 'https://images.unsplash.com/photo-1655721530791-65e935a9bbf4?q=80&w=600',
            'category': 'Implementation',
            'author': {
                'name': 'Michael Kim',
                'image_url': 'https://randomuser.me/api/portraits/men/42.jpg'
            },
            'published_date': datetime(2023, 3, 28)
        },
        {
            'title': 'Responsible AI: Building Ethical Knowledge Systems',
            'slug': 'ethical-ai-knowledge-systems',
            'excerpt': 'Ethical considerations and best practices for developing AI systems that respect privacy, reduce bias, and maintain transparency.',
            'image_url': 'https://images.unsplash.com/photo-1678822205184-4daeb10fc2b8?q=80&w=600',
            'category': 'Technology',
            'author': {
                'name': 'Aisha Johnson',
                'image_url': 'https://randomuser.me/api/portraits/women/28.jpg'
            },
            'published_date': datetime(2023, 2, 15)
        },
        {
            'title': 'How HealthTech Inc. Reduced Training Time by 68%',
            'slug': 'healthtech-training-case-study',
            'excerpt': 'A detailed case study on how a leading healthcare provider transformed their onboarding process with AI knowledge systems.',
            'image_url': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=600',
            'category': 'Case Study',
            'author': {
                'name': 'David Wong',
                'image_url': 'https://randomuser.me/api/portraits/men/32.jpg'
            },
            'published_date': datetime(2023, 1, 20)
        },
        {
            'title': '5 Ways to Measure Knowledge Management ROI',
            'slug': 'measure-knowledge-management-roi',
            'excerpt': 'Practical metrics and KPIs for tracking the business impact of your organization\'s knowledge management initiatives.',
            'image_url': 'https://images.unsplash.com/photo-1552664730-d307ca884978?q=80&w=600',
            'category': 'Strategy',
            'author': {
                'name': 'Emma Johnson',
                'image_url': 'https://randomuser.me/api/portraits/women/52.jpg'
            },
            'published_date': datetime(2023, 1, 8)
        },
        {
            'title': 'Securing Your AI Knowledge Base: Best Practices',
            'slug': 'securing-ai-knowledge-base',
            'excerpt': 'Essential security measures for protecting sensitive information in your AI-powered knowledge systems.',
            'image_url': 'https://images.unsplash.com/photo-1573167710701-35950a41e251?q=80&w=600',
            'category': 'Technology',
            'author': {
                'name': 'Thomas Nguyen',
                'image_url': 'https://randomuser.me/api/portraits/men/12.jpg'
            },
            'published_date': datetime(2022, 12, 14)
        },
        {
            'title': 'Integrating AI Knowledge Systems with Existing Workflows',
            'slug': 'integrating-ai-knowledge-systems-workflows',
            'excerpt': 'Strategies for seamless implementation that enhances rather than disrupts your team\'s existing processes.',
            'image_url': 'https://images.unsplash.com/photo-1600132806370-bf17e65e942f?q=80&w=600',
            'category': 'Implementation',
            'author': {
                'name': 'Ryan Lee',
                'image_url': 'https://randomuser.me/api/portraits/men/77.jpg'
            },
            'published_date': datetime(2022, 11, 30)
        }
    ]
    
    categories = [
        {'name': 'AI Strategy', 'slug': 'ai-strategy'},
        {'name': 'Implementation', 'slug': 'implementation'},
        {'name': 'Case Study', 'slug': 'case-study'},
        {'name': 'Technology', 'slug': 'technology'},
        {'name': 'Strategy', 'slug': 'strategy'}
    ]
    
    return {
        'featured_post': featured_post,
        'blog_posts': blog_posts,
        'categories': categories
    }

def blog(request):
    # Get blog data
    blog_data = get_blog_data()
    
    return render(request, 'blog.html', blog_data)

def blog_detail(request, slug):
    # Get blog data
    blog_data = get_blog_data()
    
    # Find the post with the matching slug
    post = None
    if blog_data['featured_post']['slug'] == slug:
        post = blog_data['featured_post']
    else:
        for p in blog_data['blog_posts']:
            if p['slug'] == slug:
                post = p
                break
    
    if not post:
        # If post not found, redirect to blog index
        return redirect('blog')
    
    # Get related posts (same category)
    related_posts = [p for p in blog_data['blog_posts'] 
                    if p['category'] == post.get('category') and p['slug'] != slug][:3]
    
    context = {
        'post': post,
        'related_posts': related_posts,
        'categories': blog_data['categories']
    }
    
    return render(request, 'blog_detail.html', context)

def blog_category(request, category_slug):
    # Get blog data
    blog_data = get_blog_data()
    
    # Find the category
    category = None
    for c in blog_data['categories']:
        if c['slug'] == category_slug:
            category = c
            break
    
    if not category:
        # If category not found, redirect to blog index
        return redirect('blog')
    
    # Filter posts by category
    category_posts = [p for p in blog_data['blog_posts'] if p['category'] == category['name']]
    
    context = {
        'category': category,
        'blog_posts': category_posts,
        'categories': blog_data['categories']
    }
    
    return render(request, 'blog.html', context)

def newsletter_subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            # In a real application, we would use the Subscriber model
            # Subscriber.objects.create(email=email)
            messages.success(request, "Thank you for subscribing to our newsletter!")
        else:
            messages.error(request, "Please provide a valid email address.")
    
    # Redirect back to the referring page or blog index
    return redirect(request.META.get('HTTP_REFERER', reverse('blog')))

def team(request):
    return render(request, 'team.html')

def privacy(request):
    return render(request, 'privacy.html')

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
