from django.contrib import admin
from django.urls import path
from genres.views import GenereCreateListView, GenreRetriveUpdateDestroyView
from actors.views import ActorCreateListView, ActorRetrieveUpdateDestroy
from movies.views import MovieCreateListView, MovieRetrieveUpdateDestroy
from reviews.views import ReviewCreateListView, ReviewRetrieveUpdateDestroyView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('genres/', GenereCreateListView.as_view(), name='genre-create-list'),
    path('genres/<int:pk>/', GenreRetriveUpdateDestroyView.as_view(), name='genre-detail-view'),
    
    path('actors/', ActorCreateListView.as_view(), name='actor-create-list'),
    path('actors/<int:pk>/', ActorRetrieveUpdateDestroy.as_view(), name='actor-detail-view'),

    path('movies/', MovieCreateListView.as_view(), name='movie-create-list'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroy.as_view(), name='movie-detail-view'),

    path('reviews/', ReviewCreateListView.as_view(), name='review-create-list'),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroyView.as_view(), name='review-detail-view'),
]