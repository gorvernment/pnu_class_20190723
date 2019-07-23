from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Pokemon

class PokemonAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'page_tag']

    def page_tag(self, pokemon):
        tag = '<a href="{}" target="_blank">링크</a>'.format(pokemon.page_url)
        return mark_safe(tag)

admin.site.register(Pokemon, PokemonAdmin)


