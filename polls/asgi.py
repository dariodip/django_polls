import os
import channels.asgi
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings)
channel_layer = channels.asgi.get_channel_layer()
pid = os.fork()
if pid == 0:
    os.exec('daphne polls.asgi:channel_layer --port 8888')