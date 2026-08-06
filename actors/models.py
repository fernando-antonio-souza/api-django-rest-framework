from django.db import models


# Constante de escolha, pré-determina o preenchimento do campo
NATIONALY_CHOICES = (
    ("USA", "Estados Unidos"),
    ("Brazil", "Brasil"),
)


class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(
        max_length=100,
        choices=NATIONALY_CHOICES,
        blank=True,
        null=True,
    )


    def __str__(self):
        return self.name