from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.shortcuts import redirect


class LoginPageView(TemplateView):
    template_name = 'auth/signin.html'

class RegisterPageView(TemplateView):
    template_name = 'auth/signup.html'

def login(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	try:
		user = authenticate(username=username, password=password)
		if user is not None:
			username = user.username
			return redirect('profile')
		else:
			return render(request, 'auth/signin.html')
			
	except Exception as e:
		return render(request, 'auth/signin.html')


def logout_view(request):
    logout(request)
    return render(request,'auth/register.html',{'error':'no login'})


def register(request):
	if request.method=='POST':
		username = request.POST.get('username')
		email = request.POST.get('email')
		password = request.POST.get('username')
		password_again = request.POST.get('password_again')
		if username and email and password and password_again:
			try:
				user = User.objects.create_user(username,email,password)
				user.is_staff = True
				user.save()
				return redirect('profile')
			except:
				return redirect('signup')

		else:
			return redirect('signup')
	else:
		return redirect('signup')

def profile(request):
	return render(request,'profile.html')