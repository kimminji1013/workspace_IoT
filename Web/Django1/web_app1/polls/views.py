from django.shortcuts import render
from polls.models import Choice, Question

def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    
    context = {'latest_question_list': latest_question_list}

    return render(request, 'polls/index.html', context)




# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/datail.html',{'question':question})