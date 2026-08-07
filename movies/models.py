from django.db import models
from actors.models import Actor
from genres.models import Genre



class Movie(models.Model):
    title = models.CharField(max_length= 500)
    genre = models.ForeignKey(
        Genre,
        on_delete= models.PROTECT, # -> protege a exclusão do gênero
        related_name= "movies", # -> ligação entre as tabelas, por causa da chave estrangeira
    )

    release_data = models.DateField(null = True, blank= True)
    actors = models.ManyToManyField(Actor, related_name= "movies") # -> usando este field consigo adicionar mais de um valor, e  ele pode ser usado em todos os movies
    resume = models.TextField(null= True, blank= True)

    def __str__(self):
        return self.title