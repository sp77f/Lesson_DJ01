from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm
def home(request):
    news = News.objects.all()
    return render(request, 'news/news.html', {'news': news})

def create_news(request):
    error = ''
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма была неверной'

    form = NewsForm()
    return render(request, 'news/add_new_post.html', {'form': form, 'error': error})

# Create your views here.
