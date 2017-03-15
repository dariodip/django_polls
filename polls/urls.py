from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from .views import QuestionViewSet, ChoiceViewSet
from . import views, templates

app_name = 'polls'

router = routers.DefaultRouter()
router.register(r'questions', QuestionViewSet)
router.register(r'choice', ChoiceViewSet)

schema_view = get_swagger_view(title='Polls API')

urlpatterns = [
    #  /polls/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /polls/id/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # /polls/id/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # /polls/id/vote
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    # login view
    url(r'^login/$', auth_views.login, {'template_name': 'polls/login.html'}, name="login"),

    # swagger
    url(r'^docs/', schema_view),
]

urlpatterns += router.urls
