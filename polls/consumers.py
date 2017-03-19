from datetime import datetime
import logging
from channels.sessions import channel_session
from channels import Group
from django.core.cache import cache
from django.conf import settings

log = logging.getLogger(__name__)
cache.set('users', "", settings.USER_LASTSEEN_TIMEOUT)
user_list = []

@channel_session
def ws_connect(message):
    appname, username = message['path'][1:].split("/")
    Group('main-group').add(message.reply_channel)

    if username:
        if username not in user_list:
            user_list.extend([username])
    Group('main-group').send({'text': ",".join(user_list)})


@channel_session
def ws_disconnect(message):
    Group('main-group').discard(message.reply_channel)
    appname, username = message['path'][1:].split("/")
    if username:
        if username in user_list:
            user_list.remove(username)
    Group('main-group').send({'text': ",".join(user_list)})
