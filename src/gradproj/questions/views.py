from django.shortcuts import render
import pandas as p
from sklearn.tree import DecisionTreeClassifier
from django.contrib import messages
import joblib as j
from .models import questions
# Create your views here.
from django.shortcuts import  render, redirect
def tree_view(request):
    try:
        obj = questions.objects.get(user=request.user)
        context = {
            "Mathematical": obj.Mathematical,
            "Programming": obj.Programming,
            "Theory": obj.Theory,
        }
    except:
        context = {
            "Mathematical": '',
            "Programming": '',
            "Theory": '',
        }
    return render(request=request, template_name=r"tree.html", context=context)
def questions_view(request):
    p=''
    dir=request.POST
    new_list=list(dir.values())

    new_list=new_list[1:]
    if len(new_list)==19:
        try:
            questions.objects.filter(user=request.user).delete()
        except:
            pass
        last_list = []
        for s in new_list:
            last_list.append(float(s))

        model = j.load('studysource.joblib')
        predictions = model.predict([last_list])

        for p in predictions:
            p
        print(p)
        Programming = last_list[:3]
        Mathematical = last_list[7:]
        Theory = last_list[3:7]
        M_prediction = ''
        T_prediction = ''
        P_prediction = ''
        M_counter=0
        T_counter=0
        P_counter=0
        M_length=len(Mathematical)
        T_length=len(Theory)
        P_length=len(Programming)
        if p == 'Programming':
            P_prediction = 'Green'
            for i in Mathematical:
                if i == 1.0:
                    M_counter += 1
            for a in Theory:
                if a == 1.0:
                    T_counter += 1

            if M_counter / M_length >= 0.4:
                M_prediction = 'Orange'
            else:
                M_prediction = 'Red'
            if T_counter / T_length >= 0.4:
                T_prediction = 'Orange'
            else:
                T_prediction = 'Red'
        elif p == 'Mathematical':
            M_prediction = 'Green'
            for i in Programming:
                if i == 1.0:
                    P_counter += 1
            for a in Theory:
                if a == 1.0:
                    T_counter += 1
            if P_counter / P_length >= 0.4:
                P_prediction = 'Orange'
            else:
                P_prediction = 'Red'
            if T_counter / T_length >= 0.4:
                T_prediction = 'Orange'
            else:
                T_prediction = 'Red'
        elif p == 'Theory':
            T_prediction = 'Green'
            for i in Programming:
                if i == 1.0:
                    P_counter += 1
            for a in Mathematical:
                if a == 1.0:
                    M_counter += 1

            if M_counter / M_length >= 0.4:
                M_prediction = 'Orange'
            else:
                M_prediction = 'Red'
            if P_counter / P_length >= 0.4:
                P_prediction = 'Orange'
            else:
                P_prediction = 'Red'
        student = questions(user=request.user, Mathematical=M_prediction,Theory=T_prediction,Programming=P_prediction )
        student.save()
        return redirect('http://127.0.0.1:8000/tree')
    else:
        messages.error(request, "please fill all the required fields.")



    return render(request=request, template_name="question.html", context={})