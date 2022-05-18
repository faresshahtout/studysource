from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
import questions
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django.forms.widgets import PasswordInput, TextInput

# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'placeholder': 'E-mail','class':'input_box'}))
	username=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'College ID','class':'input_box'}))
	password1 =forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password','class':'input_box','type':'password'}))
	password2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Confirm Your Password','class':'input_box','type':'password'}))
	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput





class MyAuthForm(AuthenticationForm):
    class Meta:
        model = questions
        fields = ['username','password']
    def __init__(self, *args, **kwargs):
        super(MyAuthForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
        self.fields['username'].label = False
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password'})
        self.fields['password'].label = False