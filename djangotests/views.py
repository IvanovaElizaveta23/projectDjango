from requests import request
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import *
from .serializers import *


class TestPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 4


class QuestionPagination(PageNumberPagination):
    page_size = 1


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    pagination_class = TestPagination
    #permission_classes = (IsAuthenticated, )

    @action(methods=['get'], detail=True)
    def question(self, request, pk=None):
        questions = Question.objects.filter(test_id=pk)

        paginator = QuestionPagination()
        page = paginator.paginate_queryset(questions, self.request)

        if page is not None:
            serializer = QuestionSerializer(page, many=True, context={'request': request})
            return paginator.get_paginated_response(serializer.data)

        serializer = QuestionSerializer(questions, many=True, context={'request': request})
        return Response(serializer.data)


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    @action(methods=['get'], detail=True)
    def answer(self, request, pk=None):
        answers = Answer.objects.filter(quest_id=pk)
        return Response({'quest': int(pk), 'answers': AnswerSerializer(answers, many=True).data})


class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

    def create(self, request, *args, **kwargs):
        serializer = SessionSerializer(data=request.data)
        if serializer.is_valid():
            test = serializer.validated_data.get('test')
            if test.quantity_attempts is None or \
                    test.quantity_attempts >= Session.objects.filter(test=test.pk).count():
                serializer.save(user=self.request.user, time=None)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnswerUserViewSet(viewsets.ModelViewSet):
    queryset = AnswerUser.objects.all()
    serializer_class = AnswerUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = AnswerUserSerializer(data=request.data)
        if serializer.is_valid():
            if self.quantityСheck(serializer):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response({'error': 'Превышено колличество допустимых ответов'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def quantityСheck(self, serializer):
        question = serializer.validated_data.get('ques')
        rightAnswersCount = Answer.objects.filter(quest=question.pk, right=True).count()
        answersUserCount = len(serializer.validated_data.get('answers').split(','))
        if rightAnswersCount >= answersUserCount:
            return True
        return False


class AnswerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(methods=['get'], detail=True)
    def test(self, request, pk=None):
        tests = Test.objects.filter(cat_id=pk)
        return Response({'cat': int(pk), 'tests': TestSerializer(tests, many=True).data})


class DifficultionViewSet(viewsets.ModelViewSet):
    queryset = Difficultion.objects.all()
    serializer_class = DifficultionSerializer

    @action(methods=['get'], detail=True)
    def test(self, request, pk=None):
        tests = Test.objects.filter(dif_id=pk)
        return Response({'dif': int(pk), 'tests': TestSerializer(tests, many=True).data})


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=['get'], detail=True)
    def session(self, request, pk=None):
        sessions = Session.objects.filter(user_id=pk)
        return Response({'user': int(pk), 'results': SessionSerializer(sessions, many=True).data})
