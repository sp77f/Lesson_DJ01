from django.http import HttpResponse
def index(request):
    return HttpResponse("<h1>Главная страница проекта </h1>")

def data(request):
    return HttpResponse("<h1>Страница с данными</h1>")

def test(request):
    return HttpResponse("<h1>Страница для тестирования</h1>")