from django.shortcuts import render

# Create your views here.
import json
from django.http import JsonResponse 
from django.views.decorators.csrf import csrf_exempt
from genres.models import Genre # importo o model genre, de genres
from django.shortcuts import get_object_or_404
from rest_framework import generics
from genres.serializer import GenreSerializer


class GenreCreateListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer



# @csrf_exempt
# def genre_create_list_view(request):
#     if request.method == "GET":
#         genres = Genre.objects.all() # aqui vai percorrer todos do generos do bd,  e guardar na variável
#         data = [{"id": genre.id, "name": genre.name} for genre in genres] # aqui criei uma lista e dentro um dicionário, e um for para percorrer cada gênero e armazenar no dict
#         return JsonResponse(data, safe = False) # aqui vai retornar em json os dados
#         # safe = False -> controla um objeto para que ele seja serializado

#     elif request.method == "POST": 
#         data = json.loads(request.body.decode("utf-8")) # aqui estou codificando no padrão utf-8 que é um dos mais usadaos
#         new_genre = Genre(name = data["name"]) # aqui crio uma nova variável, onde ela pega os dados name do model de Genre
#         new_genre.save() # aqui salva os dados na variável
#         return JsonResponse(
#             {"id": new_genre.id, "name": new_genre.name},
#             status = 201,
#         ) # aqui vai voltar a resposta em JSON


@csrf_exempt
def genre_detail_view(request, pk): #crio a variável com request, e passo o paramêtro pk, para indicar que quero os id, pois eles são as chaves primárias
    genre = get_object_or_404(Genre, pk = pk) # usei uma função pronta onde ela busca o objeto, se não achar da erro 404.
    
    if request.method == "GET":
        data = {"id": genre.id, "name": genre.name} # pego o id e o name , do model genre
        return JsonResponse(data) # retorno uma resposta em Json
    
    elif request.method == "PUT":
        data = json.loads(request.body.decode("utf-8"))
        genre.name = data["name"] #sobrescrevendo o nome, como o novo nome que eu passar
        genre.save() #salva o nome novo passado no BD
        return JsonResponse(
            {"id": genre.id, "name": genre.name}
        )
    
    elif request.method == "DELETE":
        genre.delete() #deleta do BD
        return JsonResponse(
            {"message": "Gênero excluido com sucesso."},
            status = 204,
        )