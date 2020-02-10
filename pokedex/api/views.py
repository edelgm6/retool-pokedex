from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pokedex.api.models import Pokemon
from pokedex.api.serializers import PokemonSerializer

class PokemonList(APIView):
    """
    List all pokemon, or create a new pokemon.
    """
    def get(self, request, format=None):
        pokemon = Pokemon.objects.all()
        serializer = PokemonSerializer(pokemon, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PokemonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PokemonDetail(APIView):
    """
    Delete a pokemon instance.
    """
    def get_object(self, name):
        try:
            return Pokemon.objects.get(name=name)
        except Pokemon.DoesNotExist:
            raise Http404

    def delete(self, request, name, format=None):
        pokemon = self.get_object(name)
        pokemon.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
