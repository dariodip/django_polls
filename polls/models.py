import datetime
from django.db import models
from django.utils import timezone as d_timezone
from django.contrib.auth.models import AbstractUser
from django.core.cache import cache
from mysite import settings


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=d_timezone.now())

    def __str__(self):
        return "[@{}]: {}".format(self.pub_date, self.question_text)

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"

    def __unicode__(self):
        return "{} {}".format(self.question_text, self)

    def was_published_recently(self):
        now = d_timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean =True
    was_published_recently.short_description = 'Published recently?'

    def save(self, *args, **kwargs):
        super(Question, self).save(*args, **kwargs)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class PollUser(AbstractUser):

    def last_seen(self):
        return cache.get('see   n_%s' % self.user.username)

    def online(self):
        if self.last_seen():
            now = datetime.datetime.now()
            if now > self.last_seen() + datetime.timedelta(
                    seconds=settings.USER_ONLINE_TIMEOUT):
                return False
            else:
                return True
        else:
            return False
