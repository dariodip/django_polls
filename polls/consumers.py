from datetime import datetime
import logging
from django.core.cache import cache
from django.conf import settings
from channels import Group
from channels.auth import http_session_user

log = logging.getLogger(__name__)
cache.set('users', "", settings.USER_LASTSEEN_TIMEOUT)
user_list = []

@http_session_user
def ws_connect(message):
    username = message.user.username
    Group('main-group').add(message.reply_channel)

    if username:
        if username not in user_list:
            user_list.extend([username])
    Group('main-group').send({'text': ",".join(user_list)})


@http_session_user
def ws_disconnect(message):
    Group('main-group').discard(message.reply_channel)
    username = message.user.username
    if username and username in user_list:
        user_list.remove(username)
    Group('main-group').send({'text': ",".join(user_list)})
