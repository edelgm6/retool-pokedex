from rest_framework import serializers
from pokedex.api.models import Pokemon


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ['name','date_added','pokeapi_url']
        read_only_fields = ['date_added']
