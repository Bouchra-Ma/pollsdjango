from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question
from django.views import generic
from .models import Question
from django.http import Http404
from django.utils import timezone

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    return render(request, "polls/index.html", {"latest_question_list": latest_question_list})

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id, pub_date__lte=timezone.now())
    except Question.DoesNotExist:
        raise Http404("Question non trouvée ou pas encore publiée.")
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # ici, traite le vote (simplifié)
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
