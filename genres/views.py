from rest_framework import generics
from rest_framework.exceptions import NotFound
from genres.models import Genre
from genres.serializers import GenreSerializer

class GenereCreateListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    def get_object(self):
        try:
            return super().get_object()
        except Genre.DoesNotExist:
            raise NotFound("Genre not found")