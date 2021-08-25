from django.shortcuts import get_list_or_404
from rest_framework import generics
from rest_framework.views import APIView,Response,Request
from drf_yasg.utils import swagger_auto_schema
from .serializers import *
from django.contrib.auth.models import User
from .models import *


# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = serializers.UserSerializer
#
#
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = serializers.UserSerializer




class QuizzesListView(APIView):

    def get(self, request: Request) -> Response:
        active_quizzes_qs = Quiz.get_active()
        serialized_data = QuizSerializer(active_quizzes_qs, many=True)
        return Response(serialized_data.data)


class QuizDetailView(APIView):

    def get(self, request: Request, quiz_id: int) -> Response:
        ''' Get all quiestions of quiz '''
        quiz_qs = get_list_or_404(Question, quiz_id=quiz_id)
        serialized_data = QuestionSerializer(quiz_qs, many=True)
        return Response(serialized_data.data)



class QuizzDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()


class  ChoiceDetailView(generics.ListCreateAPIView):
    serializer_class = ChoiceSerializer
    queryset = Choice.objects.all()

