import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_items_django_server.settings')
os.environ.setdefault('PYTHONDONTWRITEBYTECODE', '1')
os.environ.setdefault('PYTHONUNBUFFERED', '1')

application = get_wsgi_application()