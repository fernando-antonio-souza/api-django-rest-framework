
from django.contrib import admin
from django.urls import path
from actors.views import ActorCreateListView, ActorRetrieverUpdateDestroyView
from genres.views import GenreCreateListView, GenreRetrieveUpdateDestroyView
from movies.views import MovieCreateListView, MovieRetrieveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('genres', GenreCreateListView.as_view(), name = 'genre-create-list'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(), name = 'genre-detail-view'),

    path('actors', ActorCreateListView.as_view(), name = 'actor-crete-list'),
    path('actors/<int:pk>/', ActorRetrieverUpdateDestroyView.as_view(), name = 'actor-detail-view'),

    path('movies', MovieCreateListView.as_view(), name = 'movie-create-list'),
    path('movies/<int:pk>', MovieRetrieveUpdateDestroyView.as_view(), name = 'movie-detail-view'),
]
