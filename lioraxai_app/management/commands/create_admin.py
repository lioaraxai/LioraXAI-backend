from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os
import secrets

class Command(BaseCommand):
    help = 'Creates a superuser if none exists'

    def handle(self, *args, **options):
        username = 'admin'
        email = 'admin@example.com'
        
        # Get password from environment or generate random secure password
        password = os.environ.get('ADMIN_PASSWORD')
        if not password:
            password = secrets.token_urlsafe(12)
            self.stdout.write('Generated random password: ' + password)
            self.stdout.write('IMPORTANT: Save this password securely!')
        
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, email, password)
            self.stdout.write(self.style.SUCCESS(f'Successfully created superuser {username}'))
            return
            
        self.stdout.write(self.style.WARNING(f'Superuser {username} already exists')) 