from django.contrib.sitemaps.views import index
from django.urls import path

from pokemon.views import index, pokemon_edit, pokemon_new

urlpatterns = [
    path('', index),
    path('new/', pokemon_new),
    path('<int:pk>/', pokemon_edit),
    # re_path(r'(?P<pk>\d+)', pokemon_edit())

]