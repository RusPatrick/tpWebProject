from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ask', views.newQuestion, name='newQuestion'),
    path('question/<int:questionId>', views.question, name='question'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('tag/<str:tagName>', views.tag, name='tag'),
    path('hot', views.index, name='hot'),
]