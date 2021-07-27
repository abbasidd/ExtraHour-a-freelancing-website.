from django.shortcuts import render
from skill_test.models import *
from django.forms.models import model_to_dict
from django.http import HttpResponse , JsonResponse
from django.core import serializers
import json
from datetime import datetime ,timedelta
from freelancer import models as f_model
from django.views.decorators.csrf import csrf_exempt


def quizes(request):
    quizes = Quiz.objects.all()
    return render(request,'test.html',{'quizes':quizes})


def quiz_taker(request,quiz_id):
    freelancer = f_model.Freelancer.objects.get(user = request.user)
    end_time = datetime.now() + timedelta( minutes = 15)
    quiz = Quiz.objects.get(pk = quiz_id)
    QuizTakers(quiz=quiz,end_time=end_time,freelancer=freelancer).save()
    questions = Question.objects.filter(quiz = quiz).first()
    return render(request,'skill_test.html',{'question':questions})



@csrf_exempt
def user_ans(request):
    # return render(request,'contact.html')#,{'quiz_taker':quiz_taker})
    user_answer = request.POST.get('user_answer')
    question_id = request.POST.get('question_id')
    q_no = int(request.POST.get('q_no'))
    print(question_id)
    print(user_answer)
    
    question1 = Question.objects.get(pk = question_id)
    question = Question.objects.get(pk = (int(question_id)+1))
    freelancer = f_model.Freelancer.objects.get(user= request.user)
    quiz_taker = QuizTakers.objects.filter(freelancer = freelancer)
    quiz_taker = quiz_taker.last() 
    
 


    if user_answer == question1.answer:
        quiz_taker.correct_answers = 1 + quiz_taker.correct_answers
        quiz_taker.save()
    # if q_no == 6 :
    #     return render(request,'quiz_result.html',{'quiz_taker':quiz_taker})
    # q_no = q_no + 1
    # if q_no == quiz_taker.quiz.questions_count:
    #    # question = t_model.Question.objects.all().first()
    #     freelancer = f_model.Freelancer.objects.get(user = request.user)
    #     quiz_taker = QuizTakers.objects.filter(freelancer=freelancer)
    #     quiz_taker = quiz_taker.last()
    # job=j_model.Job.objects.all()
        # return render(request,'contact.html',{'question': question , 'quiz_taker':quiz_taker})
    
    # count = quiz_taker.quiz.questions_count
    count = Question.objects.filter(quiz = quiz_taker.quiz ).last()
    sawal = {'question':question.label,
    'id':int(question_id)+1,
    'choice1':question.choice.choice1,
    'choice2':question.choice.choice2,
    'choice3':question.choice.choice3,
    'q_no':q_no,
    'count':count.id,
    'quiz_taker_id':quiz_taker.id
    } 
    print(type(sawal))
    return HttpResponse(json.dumps(sawal),content_type='text/json-comment-string') 




def result(request , quiz_taker_id):
    quiz_taker = QuizTakers.objects.get( pk = int(quiz_taker_id))
    return render(request,'result.html',{'quiz_taker':quiz_taker}) 
