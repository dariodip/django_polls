from django.utils import timezone as d_timezone
from threading import Thread


class LastSeenSaver(Thread):

    def __init__(self, user):
        super(LastSeenSaver, self).__init__()
        self.current_user = user

    def run(self):
        self.current_user.last_seen = d_timezone.now()
        self.current_user.save()


class SimpleMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # before
        try:
            if request.user is not None:
                current_user = request.user
                saver_thread = LastSeenSaver(current_user)
                saver_thread.start()
        except Exception as common_ex:
            print(common_ex)
        finally:
            response = self.get_response(request)
            # after
            return response
