from django.urls import path, include
from tasks import views

app_name = 'tasks'

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('another/', views.another_page, name='another_page')
]
