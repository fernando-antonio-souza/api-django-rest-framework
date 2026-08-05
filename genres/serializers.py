from rest_framework import serializers
from genres.models import Genre



class GenreSerializer(serializers.ModelSerializer): # -> Usada para criar CRUD básicos

    class Meta: # -> configura o comportamento do serializer
        model = Genre # -> indica o model que o serializer vai pegar de base
        fields = "__all__" # -> indica quais campos do model irá pegar , aqui no caso serão todos