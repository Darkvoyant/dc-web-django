from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('bugs/', views.bug, name='bug'),
    path('features/', views.feature, name='feature'),
    path('bugs/<int:bug_id>', views.bug_detail, name='bug_detail'),
    path('features/<int:feature_id>', views.feature_detail,
         name='feature_detail'),
]
