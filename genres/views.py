
from genres.models import Genre # importo o model genre, de genres
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from genres.serializers import GenreSerializer


class GenreCreateListView(generics.ListCreateAPIView): # -> realiza a listagem e a criação
    permission_classes = (IsAuthenticated,)
    queryset = Genre.objects.all() # -> informa de onde os dados vêm
    serializer_class = GenreSerializer # -> trata os dados passando de objetos para JSON



class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView): # -> realiza a listagem por id, atualiza e deleta
    permission_classes = (IsAuthenticated,)
    queryset = Genre.objects.all() # -> informa de onde os dados vêm
    serializer_class = GenreSerializer # -> trata os dados passando de objetos para JSON

