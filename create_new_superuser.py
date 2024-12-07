import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

# Delete existing superuser if exists
User.objects.filter(username='superadmin').delete()

# Create new superuser
User.objects.create_superuser(
    username='superadmin',
    email='superadmin@example.com',
    password='superadmin123',
    is_active=True,
    is_staff=True
)
