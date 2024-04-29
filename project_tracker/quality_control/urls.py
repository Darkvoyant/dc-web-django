from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    # Class-Based Views
    path('', views.MainPage.as_view(), name='main_page'),
    path('bugs/', views.BugsListView.as_view(), name='bugs_list'),
    path('bugs/<int:bug_id>/', views.BugDetailView.as_view(),
         name='bug_detail'),
    path('features/', views.FeaturesListView.as_view(), name='features_list'),
    path('features/<int:feature_id>/', views.FeatureDetailView.as_view(),
         name='feature_detail'),

    # # Function-Based Views
    # path('', views.main_page, name='main_page'),
    # path('bugs/', views.bugs_list, name='bugs_list'),
    # path('features/', views.features_list, name='features_list'),
    # path('bugs/<int:bug_id>/', views.bug_detail, name='bug_detail'),
    # path('features/<int:feature_id>/', views.feature_detail,
    #      name='feature_detail'),

    path('bugs/new/', views.add_bug, name='add_bug'),
    path('features/new/', views.add_feature, name='add_feature'),
]
