from django import forms

from pokemon.models import Pokemon

class PokemonForm(forms.ModelForm):
    #name = forms.CharField()
    class Meta:
        model = Pokemon
        # 리스트 문자열로 참조할 필드를 지정할 수도 있습니다.
        fields = '__all__'