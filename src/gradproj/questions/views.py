from django.shortcuts import render
import pandas as p
from sklearn.tree import DecisionTreeClassifier
import joblib as j

# Create your views here.
from django.shortcuts import  render, redirect
def questions_view(request):
    dir=request.POST
    new_list=list(dir.values())
    print(new_list)
    new_list=new_list[1:]

    last_list=[]
    for s in new_list:
        last_list.append(float(s))
    print(last_list)
    model = j.load('studysorce.joblib')
    predictions = model.predict([last_list])
    for p in predictions:
        print(p)
    return render(request=request, template_name="question.html", context={})