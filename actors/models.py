from django.db import models

NATIONALITIES_CHOICES = (
    ('MX', 'Mexicano'),
    ('US', 'Americano'),
    ('JP', 'Japonês'),
    ('KR', 'Coreano'),
    ('CN', 'Chinês'),
    ('IN', 'Indiano'),
    ('UK', 'Britânico'),
    ('CA', 'Canadense'),
    ('AU', 'Australiano'),
    ('BR', 'Brasileiro'),
    ('RU', 'Russo'),
    ('FR', 'Francês'),
    ('DE', 'Alemão'),
    ('IT', 'Italiano'),
    ('ES', 'Espanhol'),
    ('AR', 'Argentino'),
    ('CO', 'Colombiano'),
    ('PE', 'Peruano'),
    ('VE', 'Venezuelano'),
    ('CL', 'Chileno'),
    ('EC', 'Equatoriano'),
    ('BO', 'Boliviano'),
    ('UY', 'Uruguaio'),
    ('PY', 'Paraguaio'),
    ('CR', 'Costarriquenho'),
    ('PA', 'Panamenho'),
    ('CU', 'Cubano'),
    ('DO', 'Dominicano'),
    ('GT', 'Guatemalteco'),
    ('SV', 'Salvadorenho'),
    ('HN', 'Hondurenho'),
    ('NI', 'Nicaraguense'),
)

class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(
        max_length=100,
        choices=NATIONALITIES_CHOICES,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name