from django.shortcuts import get_list_or_404
from django.template.context_processors import request
from rest_framework import generics
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin
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



"""Для юзера
Просмотр опросов"""
class QuizzesListView(CreateModelMixin,ListModelMixin,GenericAPIView):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)




# class QuizDetailView(CreateModelMixin,ListModelMixin,GenericAPIView,DestroyModelMixin):
#     serializer_class = QuestionSerializer
#     queryset = Question.objects.all()
#
#     def get(self, request: Request, quiz_id: int) -> Response:
#         quiz_qs = get_list_or_404(Question, quiz_id=quiz_id)
#         serialized_data = QuestionSerializer(quiz_qs, many=True)
#         return Response(serialized_data.data)
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#     # def get_serializer_class(self):
#     #     if self.request.method == 'GET':
#     #         return QuestionSerializer
#     def post_destroy(self,request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
"""Для юзера , удаление ,исправление, отправка вопросов"""
class QuizDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionSerializer
    lookup_url_kwarg = 'quiz_id'
    queryset = Question.objects.all()


"""Для клиента весь доступный список опросов"""
class QuizzDetailView(ListModelMixin,GenericAPIView):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)




class  ChoiceDetailView(generics.CreateAPIView):
    serializer_class = ChoiceSerializer
    queryset = Choice.objects.all()

    def perform_create(self, serializer):
        serializer.save(question_id=self.request.question_id)


