
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers

from djangotests.views import *


router = routers.SimpleRouter()
router.register(r'test', TestViewSet, basename='tests')
router.register(r'question', QuestionViewSet, basename='question')
router.register(r'session', SessionViewSet, basename='session')
router.register(r'user-answer', AnswerUserViewSet, basename='user-answer')
router.register(r'answer', AnswerViewSet)
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'difficult', DifficultionViewSet, basename='difficult')
router.register(r'user', UserViewSet, basename='user')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/v1/drf-auth/', include('rest_framework.urls')),

]
