from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django.views.generic.edit import FormView
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.decorators import list_route
from rest_framework.response import Response
from .models import Question, Choice, PollUser
from .serializers import QuestionSerializer, ChoiceSerializer
from .forms import UserRegistrationForm

# REST


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [AllowAny]

    @list_route(permission_classes=[AllowAny], url_path='count')
    def count(self, request):
        return Response({'count': Question.objects.count()})

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user if self.request.user is not None else "unknown")


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = [AllowAny]


# WEB APP

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:2]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


class SignupView(FormView):
    template_name = 'polls/signup.html'
    form_class = UserRegistrationForm
    success_url = '/login'

    def form_valid(self, form):
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = PollUser.objects.create_user(username=cleaned_data['username'],
                                                first_name=cleaned_data['first_name'],
                                                last_name=cleaned_data['last_name'],
                                                email=cleaned_data['email'],
                                                password=cleaned_data['password'])
            try:
                user.save()
            except Exception as saving_ex:
                print(saving_ex)
            finally:
                return super(SignupView, self).form_valid(form)


@login_required
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def question_channel(request):
    user_model = get_user_model()
    online_users = [username for username in user_model.objects.all() if username.online()][:5]
    return render(request, "polls/index.html", {
        'online_users': online_users,
    })
