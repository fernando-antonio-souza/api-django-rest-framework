from django.urls import path
from . import views



urlpatterns = [
    path('actors', views.ActorCreateListView.as_view(), name = 'actor-crete-list'),
    path('actors/<int:pk>/', views.ActorRetrieverUpdateDestroyView.as_view(), name = 'actor-detail-view'),
]