from django.http import HttpResponse
from django.shortcuts import render

from pokemon.forms import PokemonForm
from pokemon.models import Pokemon


def index(request):
    qs = Pokemon.objects.all()  # QuerySet 타입
    # return render(request, 'root.html')
    return render(request, 'pokemon/pokemon_list.html', {
        'pokemon_list': qs,
    })

# def pokemon_list_html(request):
#     qs = Pokemon.objects.all()  # QuerySet 타입
#     # return render(request, 'root.html')
#     return render(request, 'pokemon/pokemon_list.html', {
#         'pokemon_list': qs,
#     })

def pokemon_new(request):
    #return HttpResponse("새 포켓몬 등록 Form")
    form = PokemonForm()
    tag = form.as_table()
    tag = '<table>' + tag + '</table>'
    return HttpResponse(tag)

def pokemon_edit(request, pk):
    message = "기존 포켓몬 #{} 수정 Form".format(pk)
    return HttpResponse(message)

