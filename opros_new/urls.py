from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    # path('users/', views.UserList.as_view()),
    # path('users/<int:pk>/', views.UserDetail.as_view()),
    path('', views.QuizzesListView.as_view(), name='quizzes_list'),
    path('<int:quiz_id>/', views.QuizDetailView.as_view(), name='quizzes'),
    path('dtail_quiz/<int:pk>/', views.QuizzDetailView.as_view(), name='quizzes_detail'),
    path('vopros/<int:pk>/', views.ChoiceDetailView.as_view(), name='quizzes_detail'),


]

urlpatterns = format_suffix_patterns(urlpatterns)