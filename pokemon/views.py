from django.http import HttpResponse
from django.shortcuts import render

from pokemon.models import Pokemon


def index(request):
    qs = Pokemon.objects.all()
    #return render(request, 'root.html')
    return render(request, 'pokemon/pokemon_list.html', {
        'pokemon_list' : qs,
    })

def pokemon_new(request):
    return HttpResponse("새 포켓몬 등록 Form")

def pokemon_edit(request, pk):
    message = "기존 포켓몬 #{} 수정 Form".format(pk)
    return HttpResponse(message)

