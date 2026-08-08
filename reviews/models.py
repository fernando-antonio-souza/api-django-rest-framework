from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from movies.models import Movie



class Review(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete= models.PROTECT,
        related_name= "reviews",
    )

    stars = models.IntegerField(
        validators= [ # -> Usado para criar validações, condições de determinadas coisas.
            MinValueValidator(0, "Avaliação não pode ser inferior a 0 estrelas."),
            MaxValueValidator(5, "Avaliaçao não poder ser superior a 5 estrelas.")
            
        ]
    )

    coment = models.TextField(null= True, blank= True)

    def __str__(self):
        return self.movie
