from django.db import models
from movies.models import Movie
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name='reviews')
    stars = models.IntegerField(
        validators=[MinValueValidator(0, 'Avaliação não pode ser inferior do que 0 estrelas'), 
                    MaxValueValidator(5, 'Avaliação não pode ser superior do que 5 estrelas')]
    )
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'Review for {self.movie.title} - {self.stars} stars'
