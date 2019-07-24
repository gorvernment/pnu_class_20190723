import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView

from pokemon.forms import PokemonForm
from pokemon.models import Pokemon


# @login_required
def index(request):
    qs = Pokemon.objects.all()  # QuerySet 타입
    # return render(request, 'root.html')

    format = request.GET.get("format")
    if format == 'json':
        qs = tuple(qs)
        pokemon_list = [
            {
                'pk': pokemon.pk,
                'name': pokemon.name,
                'photo_url': pokemon.photo.url,
                'page_url': pokemon.page_url,
            }
            for pokemon in qs   # Comprehension 문법
        ]
        # json_string = json.dumps(qs)
        # return HttpResponse(json_string)
        return JsonResponse(pokemon_list, safe=False)

    return render(request, 'pokemon/pokemon_list.html', {
        'pokemon_list': qs,
    })

# def pokemon_list_html(request):
#     qs = Pokemon.objects.all()  # QuerySet 타입
#     # return render(request, 'root.html')
#     return render(request, 'pokemon/pokemon_list.html', {
#         'pokemon_list': qs,
#     })

#
# def pokemon_new(request):
#     if request.method == 'GET':
#         form = PokemonForm()
#     else:
#         # 뷰에서 참조할 수 있는 데이터 목록
#         # request.GET, request.POST, request.FILES
#         form = PokemonForm(request.POST, request.FILES) # insert : instance가 없기 때문
#         if form.is_valid():
#             form.save()  # ModelForm에서만 지원
#             return redirect('/pokemon/')
#         else:
#             form.errors
#
#     return render(request, 'pokemon/pokemon_form.html', {
#         'form': form,
#     })

pokemon_new = CreateView.as_view(
    model=Pokemon,
    form_class=PokemonForm,
    success_url='/pokemon/',
)
#
# def pokemon_edit(request, pk):
#     # 장고에서는 예상치못한 Exception은 500에러로 처리
#     # pokemon = Pokemon.objects.get(pk=pk)    # View에서는 권장하지 않음. Pokemon.DoesNotExist 에러 발생
#     pokemon = get_object_or_404(Pokemon, pk=pk)
#
#     if request.method == 'GET':
#         form = PokemonForm(instance=pokemon)
#     else:
#         # 뷰에서 참조할 수 있는 데이터 목록
#         # request.GET, request.POST, request.FILES
#         form = PokemonForm(request.POST, request.FILES, instance=pokemon) # update : instance가 있기 때문
#         if form.is_valid():
#             form.save()  # ModelForm에서만 지원
#             return redirect('/pokemon/')
#         else:
#             form.errors
#
#     return render(request, 'pokemon/pokemon_form.html', {
#         'form': form,
#     })
#


pokemon_edit = UpdateView.as_view(
    model=Pokemon,
    form_class=PokemonForm,
    success_url='/pokemon/',
)