from django.shortcuts import  render, redirect
from forms import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django import forms
from django.db import IntegrityError

def register_request(request):

		if request.method == "POST":

			print(request.POST)
		try:
			form = NewUserForm(request.POST)
			print(form.is_valid())
			if form.is_valid():
				user = form.save()
				login(request, user)
				messages.success(request, "Registration successful.")
				return redirect("/sign-in")
			messages.error(request, "Unsuccessful registration. Invalid information.")
			form = NewUserForm()
			return render(request=request, template_name=r"signup.html", context={"register_form": form})
		except:
			return render(request=request, template_name=r"signup.html",context={"register_form": form, "error": "The user already exist pleast try another one"})




def login_request(request,*args,**kwargs):

	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("http://127.0.0.1:8000/")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="signin.html", context={"login_form":form})
def home_view(request):
	return render(request=request, template_name=r"navbar.html", context={"":''})
def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.")
	return redirect("http://127.0.0.1:8000/")
