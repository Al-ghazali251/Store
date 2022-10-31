from django.urls import path
from . import views



urlpatterns = [
path('register/', views.register.as_view(), name='register'),
path('login/', views.user_login.as_view(), name='login'),
path('logout/', views.user_logout.as_view(), name='logout'),
]