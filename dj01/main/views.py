from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    #return HttpResponse("<h1>Главная страница проекта </h1>")
    return render(request, 'main/index.html')

def data(request):
    #return HttpResponse("<h1>Страница с данными</h1>")
    return render(request, 'main/data.html')

def test(request):
    return render(request, 'main/tests.html')

def res(request):
    return render(request, 'main/res.html')