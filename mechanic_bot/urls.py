from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.mechanic_chatbot, name='mechanic_chatbot'),
]
