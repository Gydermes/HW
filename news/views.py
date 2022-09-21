from django.shortcuts import render, redirect
from .models import Artiles
from .forms import ActiclesForm
from django.views.generic import DetailView, UpdateView, DeleteView


def news_home(request):
    news = Artiles.objects.order_by('date')
    return render(request, 'news/news_home.html', {"news": news})

class NewsDetailView(DetailView):
    model = Artiles
    template_name = 'news/details_view.html'
    context_object_name ='article'


class NewsUpdateViews(UpdateView):
    model = Artiles
    template_name = 'news/create.html'

    form_class = ActiclesForm


class NewsDeleteViews(DeleteView):
    model = Artiles
    success_url = '/news/'
    template_name = 'news/news_delete.html'



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
