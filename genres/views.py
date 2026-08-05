from django.shortcuts import render


import json
from django.http import JsonResponse 
from django.views.decorators.csrf import csrf_exempt
from genres.models import Genre # importo o model genre, de genres
from django.shortcuts import get_object_or_404
from rest_framework import generics
from genres.serializers import GenreSerializer


class GenreCreateListView(generics.ListCreateAPIView): # -> realiza a listagem e a criação
    queryset = Genre.objects.all() # -> informa de onde os dados vêm
    serializer_class = GenreSerializer # -> trata os dados passando de objetos para JSON



class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView): # -> realiza a listagem por id, atualiza e deleta
    queryset = Genre.objects.all() # -> informa de onde os dados vêm
    serializer_class = GenreSerializer # -> trata os dados passando de objetos para JSON

