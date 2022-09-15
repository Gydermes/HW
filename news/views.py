from django.shortcuts import render
from .models import Artiles
from .forms import ActiclesForm
# Create your views here.


def news_home(request):
    news = Artiles.objects.all()
    return render(request, 'news/news_home.html', {"news": news})


def create(request):
    form = ActiclesForm()

    data = {
        'form': form
    }

    return render(request, 'news/create.html', data)
