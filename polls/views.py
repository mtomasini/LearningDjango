from django.http import HttpResponse
from django.shortcuts import render

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    #return HttpResponse(f"You're looking at question {question_id}.")
    context = {"question_id" : question_id}
    return render(request, 'polls/detail.html', context)

def results(request, question_id):
    context = {"question_id" : question_id}
    return render(request, 'polls/results.html', context)

def vote(request, question_id):
    context = {"question_id" : question_id}
    return render(request, 'polls/vote.html', context)
    