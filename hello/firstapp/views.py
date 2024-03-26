import datetime

from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import HttpResponse, \
    HttpResponsePermanentRedirect, \
    HttpResponseRedirect, \
    HttpResponseBadRequest, \
    HttpResponseForbidden


# Create your views here.
def index(request):
    # header = "Фильтры в шаблонах"
    # num = 2
    # value_date = datetime.datetime.now()
    # value_time = datetime.datetime.now()
    # value_title = "это пример использования фильтров"
    # value_upper = "это строка в верхнем регистре"
    # data = {"header": header, "value_date": value_date, "value_time": value_time, "value_title": value_title,
    #         "value_upper": value_upper}
    return render(request, "firstapp/home.html")


def about(request):
    return HttpResponse("<h2>О сайте</h2>")


def contact(request):
    return HttpResponseRedirect("/about")
    # return HttpResponse("<h2>Контакты</h2>")


def products(request, productid=1):
    category = request.GET.get("cat", "Не задана")
    output = "<h2>Продукт № {0} Категория: {1}</h2>" \
        .format(productid, category)
    return HttpResponse(output)


def users(request):
    id = request.GET.get("id", "Не задано")
    name = request.GET.get("name", "Не задано")
    output = "<h2>Пользователь</h2> <h3>id: {0} Имя: {1}</h3>" \
        .format(id, name)
    return HttpResponse(output)


def details(request):
    return HttpResponsePermanentRedirect("/")


def access(request, age):
    if age not in range(1, 111):
        return HttpResponseBadRequest("Некорректные данные")
    if age > 17:
        return HttpResponse("Доступ разрешен")
    else:
        return HttpResponseForbidden("Доступ заблокирован: недостаточно лет")
