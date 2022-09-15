from django.shortcuts import render
from django.shortcuts import redirect
from .services import cat_services as services

def index_view(request):
    return render(request, 'catapp/index.html', context={})

def create_view(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        if name:
            services.create_cat(name)
            return redirect('catapp:game')
    return redirect('catapp:index')

def game_view(request):
    cat = services.get_cat()
    if cat:
        return render(request, 'catapp/game.html', context={
                                                        'cat':cat, 
                                                        'actions':['Поиграть', 'Покормить', 'Уложить спать']})
    return redirect('catapp:index')

def apply_view(request):
    if request.method == 'POST':
        action = request.POST.get('action', None)
        if action:
            services.apply_action(action)
            return redirect('catapp:game')
    return redirect('catapp:index')
