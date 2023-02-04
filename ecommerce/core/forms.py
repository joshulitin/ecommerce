from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
	username = forms.CharField(widget = forms.TextInput(attrs={
		'placeholder': 'Your username',
		'class': 'w-full py-4 px-6'
	}))

	password = forms.CharField(widget = forms.PasswordInput(attrs={
		'placeholder': 'Your password',
		'class': 'w-full py-4 px-6'
	}))

class SignupForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

	username = forms.CharField(widget = forms.TextInput(attrs={
		'placeholder': 'Your username',
		'class': 'w-full py-4 px-6'
	}))

	email = forms.CharField(widget = forms.EmailInput(attrs={
		'placeholder': 'Your email address',
		'class': 'w-full py-4 px-6'
	}))
	
	first_name = forms.CharField(widget = forms.TextInput(attrs={
		'placeholder': 'Your first name',
		'class': 'w-full py-4 px-6'
	}))

	last_name = forms.CharField(widget = forms.TextInput(attrs={
		'placeholder': 'Your last name',
		'class': 'w-full py-4 px-6'
	}))
	password1 = forms.CharField(widget = forms.PasswordInput(attrs={
		'placeholder': 'Your password',
		'class': 'w-full py-4 px-6'
	}))

	password2 = forms.CharField(widget = forms.PasswordInput(attrs={
		'placeholder': 'Repeat password',
		'class': 'w-full py-4 px-6'
	}))

class EditProfileForm(UserChangeForm):
	class Meta:
		model = User
		fields = ('username', 'email', 'first_name', 'last_name')

	username = forms.CharField(disabled=True,widget = forms.TextInput(attrs={
		'placeholder': 'Your username',
		'class': 'w-full py-4 px-6'
	}))
	email = forms.CharField(disabled=True, widget = forms.EmailInput(attrs={
		'placeholder': 'Your email address',
		'class': 'w-full py-4 px-6'
	}) )

	first_name = forms.CharField(widget = forms.TextInput(attrs={
		'placeholder': 'Your first name',
		'class': 'w-full py-4 px-6'
	}))

	last_name = forms.CharField(widget = forms.TextInput(attrs={
		'placeholder': 'Your last name',
		'class': 'w-full py-4 px-6'
	}))
	