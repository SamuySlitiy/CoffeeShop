from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('', views.review_list, name='review_list'), 
    path('add/', views.add_review, name='add_review'), 
    path('login/', LoginView.as_view(template_name='reviews/login.html'), name='login'), 
    path('register/', views.register, name='register'),  
]
