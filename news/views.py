from django.shortcuts import render, redirect
from .models import Artiles
from .forms import ActiclesForm
# Create your views here.


def news_home(request):
    news = Artiles.objects.all()
    return render(request, 'news/news_home.html', {"news": news})


def create(request):
    error = ''
    if request.method == 'POST':
        form = ActiclesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'форма била неверной'
    form = ActiclesForm
    data = {
        'form': form,
        'error': error
    }

    return render(request, 'news/create.html', data)
