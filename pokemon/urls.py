from django.contrib.sitemaps.views import index
from django.urls import path, include

from pokemon.views import index, pokemon_edit, pokemon_new #, pokemon_list_html
from rest_framework.routers import DefaultRouter
from pokemon.views import PokemonViewSet


urlpatterns = [
    path('', index),
    # path('pokemon_list.html', pokemon_list_html),
    path('new/', pokemon_new),
    path('<int:pk>/edit/', pokemon_edit),
    # re_path(r'(?P<pk>\d+)', pokemon_edit())
]


router = DefaultRouter()
router.register('pokemons', PokemonViewSet)

urlpatterns += [
    path('api/vi/', include(router.urls))
]

# ModelViewSet 실행URL
# http://localhost:8000/pokemon/api/vi/pokemons/
# http://localhost:8000/pokemon/api/vi/pokemons/1/



