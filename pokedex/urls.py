from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from pokedex.api import views

urlpatterns = [
    path('pokemon/', views.PokemonList.as_view()),
    path('pokemon/<str:name>/', views.PokemonDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
