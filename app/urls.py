
from django.contrib import admin
from django.urls import path
from actors.views import ActorCreateListView, ActorRetrieverUpdateDestroyView
from genres.views import GenreCreateListView, GenreRetrieveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('genres', GenreCreateListView.as_view(), name = 'genre-create-list'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(), name = 'genre-detail-view'),

    path('actors', ActorCreateListView.as_view(), name = 'actor-crete-list'),
    path('actors/<int:pk>/', ActorRetrieverUpdateDestroyView.as_view(), name = 'actor-detail-view'),
]
