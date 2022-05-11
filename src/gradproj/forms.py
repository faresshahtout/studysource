from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'placeholder': 'E-mail','class':'input_box'}))
	username=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username','class':'input_box'}))
	password1 =forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password','class':'input_box'}))
	password2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Confirm Your Password','class':'input_box'}))
	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user