from django.shortcuts import render
import pandas as p
from sklearn.tree import DecisionTreeClassifier
from django.contrib import messages
import joblib as j
from .models import questions
# Create your views here.
from django.shortcuts import  render, redirect
def questions_view(request):
    p=''
    dir=request.POST
    new_list=list(dir.values())
    print(new_list)
    new_list=new_list[1:]
    if len(new_list)==19:
        last_list = []
        for s in new_list:
            last_list.append(float(s))
        print(last_list)
        model = j.load('studysorce.joblib')
        predictions = model.predict([last_list])

        for p in predictions:
            p

        student = questions(user=request.user, result=p)
        student.save()
    else:
        messages.error(request, "please fill all the required fields.")
        # return(redirect('/questions/'))


    return render(request=request, template_name="question.html", context={})