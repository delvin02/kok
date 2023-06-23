import os,sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/var/www/html/kck/venv/lib/python3.6/site-packages')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kck.settings')

application = get_wsgi_application()
