from django.urls import path, include

from .views import *

urlpatterns = [
    path('', LoginUser.as_view(), name='login'),
    path('tests/', Tests_list.as_view()),
    path('home/', index, name='home'),
    path('api/', include('tasks.urls')),


]
