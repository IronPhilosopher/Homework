from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


def main_page(request):
    return render(request, 'main_page.html')


def suits(request):
    suit1 = 'Мечи'
    suit2 = 'Жезлы'
    suit3 = 'Кубки'
    suit4 = 'Монеты'
    context = {
        'suit1': suit1,
        'suit2': suit2,
        'suit3': suit3,
        'suit4': suit4,
    }
    return render(request, 'suits.html', context)


def future(request):
    return render(request, 'future.html')
