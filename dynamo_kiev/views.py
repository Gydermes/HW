from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'dynamo_kiev/ss.html')


def about(request):
    return render(request, 'dynamo_kiev/free.html')

