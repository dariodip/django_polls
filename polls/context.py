from django.contrib.auth import get_user_model
from django.utils import timezone
from mysite import settings
import datetime


def online_users_context(request):
    time = timezone.now() - timezone.timedelta(seconds=settings.USER_ONLINE_TIMEOUT)
    user_model = get_user_model()
    return {'online_users': user_model.objects.filter(last_login__lt=time)[:5]}
