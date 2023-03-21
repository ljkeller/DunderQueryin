from django.urls import path

from . import views

urlpatterns = [
    path('', views.dunder_ai, name='DunderAI'),
    path('query/', views.query, name='query'),
]
