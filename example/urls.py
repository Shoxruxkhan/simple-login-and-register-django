from django.urls import path
from .views import LoginPageView,RegisterPageView,login,logout_view,register,profile

urlpatterns=[
	path('signin/',LoginPageView.as_view(),name='signin'),
	path('signup/',RegisterPageView.as_view(),name='signup'),
	path('login/',login,name='login'),
	path('register/',register,name='register'),
	path('logout/',logout_view,name='logout'),
	path('profile/',profile,name='profile'),
]