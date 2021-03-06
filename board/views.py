from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse
from .models import Question, Answer
# Create your views here.

def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}

    return render(request, 'question_list.html',context)



def test(request):
    return render(request, 'test.html')

def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'question_detail.html', {'question': question})

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    #question.answer_set.create(content =request.POST.get('content') , create_date=timezone.now())
    answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
    answer.save()
    return redirect('board:detail', question_id=question.id)
