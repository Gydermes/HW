from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse

def index(request):
    data = {
        'title': "Главная страница"
    }

    return render(request, 'dynamo_kiev/ss.html', data)


def about(request):
    return render(request, 'dynamo_kiev/free.html')

