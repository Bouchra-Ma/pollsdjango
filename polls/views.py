
from django.shortcuts import render, get_object_or_404
from .models import Question


def index(request):
    return render(request, "polls/index.html")

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})
