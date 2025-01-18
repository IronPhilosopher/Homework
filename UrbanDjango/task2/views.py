from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


def funcv(request):
    return render(request, 'func.html')

class Classv(TemplateView):
    template_name = 'class.html'
