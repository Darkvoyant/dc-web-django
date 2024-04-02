from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from quality_control import views
# Create your views here.


def main_page(request):
    another_page_url = reverse('tasks:another_page')
    html = (f"<h1>Страница приложения tasks</h1><a href='{another_page_url}"
            f"'>Перейти на другую страницу</a> <br>"
            f"<a href='{reverse('quality_control:main_page')}"
            f"'>Раздел \"Контроль качества\" </a>")
    return HttpResponse(html)


def another_page(request):
    return HttpResponse("Это другая страница приложения tasks.")

