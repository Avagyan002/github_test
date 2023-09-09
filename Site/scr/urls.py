from django.urls import path

from . import views

app_name = 'scr'
urlpatterns = [
    path('register/', views.register, name='register')
]