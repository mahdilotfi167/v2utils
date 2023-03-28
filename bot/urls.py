from django.urls import path
from . import views

urlpatterns = [
    path('hook/', views.telegram_webhook)
]
