from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
	path('', views.index, name = 'index'),
	path('contact/', views.contact, name = 'contact'),
	path('privacy/', views.privacy, name = 'privacy'),
	path('terms/', views.terms, name = 'terms'),
	path('signup/', views.signup, name = 'signup'),
	path('login/', auth_views.LoginView.as_view(template_name = 'core/login.html', authentication_form = LoginForm), name = 'login'),
	path('profile/edit/', views.edit_profile, name='edit_profile'),
	path('logout/', views.logout_user, name='logout'),
	
]