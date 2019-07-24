# from django import forms  # 비교용

from rest_framework import serializers

from pokemon.models import Pokemon


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = '__all__'

