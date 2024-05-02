from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.
class HelloWorld(View):
    def get(self, request):
        data = {
            'id': 1,
            'title': 'Notebook Gamer',
            'precio': 10000
        }
        return render(request, 'hello.html', context=data)