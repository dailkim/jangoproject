from importlib.resources import path

from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [

    path('', views.index,name='index'),
    path('<int:question_id>',views.detail, name='detail'),
    path('answer/create/<int:question_id>', views.answer_create, name='answer_create')

    #path('index', views.test),
    #path('', views.index),
    #path('<int:question_id>',views.detail)
]