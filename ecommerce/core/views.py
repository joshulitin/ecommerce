from django.shortcuts import render, redirect
from django.contrib.auth import logout
from item.models import Category, Item
from django.contrib import messages
from .forms import SignupForm, EditProfileForm


# Create your views here.
def index(request):
	items = Item.objects.filter(is_sold = False)[0:6]
	categories = Category.objects.all()

	return render(request, 'core/index.html', {
	'categories': categories,
	'items': items,
	})

def contact(request):
	return render(request, 'core/contact.html')

def privacy(request):
	return render(request, 'core/privacy.html')

def terms(request):
	return render(request, 'core/terms.html')

def signup(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)

		if form.is_valid():
			form.save()

			return redirect('/login/')
	else:
		form = SignupForm()

	form = SignupForm()

	return render(request, 'core/signup.html', {
		'form': form
	})

def logout_user(request):
	logout(request)
	messages.success(request, ("You have successfully logged out"))
	return redirect('/login/')

def edit_profile(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance=request.user)

		if form.is_valid():
			form.save()

			return redirect('/login/')
	else:
		form = EditProfileForm(instance=request.user)

	form = EditProfileForm(instance=request.user)

	return render(request, 'core/edit_profile.html', {
		'form': form
	})