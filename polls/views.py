from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question
from django.views import generic
from .models import Question
from django.http import Http404
from django.utils import timezone
from rest_framework import viewsets
from .serializers import QuestionSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class QuestionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

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

@api_view(['GET', 'POST'])
def hello_api(request):
    if request.method == 'GET':
        data = {"message": "Hello Bouchra from GET!"}
        return Response(data)
    
    elif request.method == 'POST':
        name = request.data.get('name', 'inconnu')
        data = {"message": f"Hello {name} from POST!"}
        return Response(data)
