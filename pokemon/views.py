from django.http import HttpResponse
from django.shortcuts import render, redirect

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
    if request.method == 'GET':
        form = PokemonForm()
    else:
        # 뷰에서 참조할 수 있는 데이터 목록
        # request.GET, request.POST, request.FILES
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # ModelForm에서만 지원
            return redirect('/pokemon/')
        else:
            form.errors

    return render(request, 'pokemon/pokemon_form.html', {
        'form': form,
    })

def pokemon_edit(request, pk):
    message = "기존 포켓몬 #{} 수정 Form".format(pk)
    return HttpResponse(message)

