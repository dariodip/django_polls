from django.utils import timezone as d_timezone
from threading import Thread
from django.core.cache import cache
from django.conf import settings


# DEPRECATED
class ActiveUserMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_user = request.user
        if request.user.is_authenticated():
            now = d_timezone.now()
            cache.set('seen_%s' % current_user.username, now, settings.USER_LASTSEEN_TIMEOUT)
        response = self.get_response(request)
        return response
