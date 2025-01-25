from rest_framework import generics
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from genres.models import Genre
from genres.serializers import GenreSerializer
from genres.permissions import GenrePermissionClass

class GenereCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GenrePermissionClass,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,GenrePermissionClass,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    def get_object(self):
        try:
            return super().get_object()
        except Genre.DoesNotExist:
            raise NotFound("Genre not found")