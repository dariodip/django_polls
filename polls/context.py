from django.contrib.auth import get_user_model
from django.utils import timezone
from django.core.cache import cache
from mysite import settings


def online_users_context(request):
    user_model = get_user_model()
    return {'online_users': [username for username in user_model.objects.all() if username.online()][:5]}
