from rest_framework import generics
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from genres.models import Genre
from genres.serializers import GenreSerializer


class GenereCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    def get_object(self):
        try:
            return super().get_object()
        except Genre.DoesNotExist:
            raise NotFound("Genre not found")