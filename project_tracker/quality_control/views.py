from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.


def main_page(request):
    bug_url = reverse('quality_control:bug')
    feature_url = reverse('quality_control:feature')
    html = (f"<h1>Система контроля качеств</h1>"
            f"<a href='{bug_url}'>Список всех багов</a> <br>"
            f"<a href='{feature_url}'>Список запросов на улучшение </a>")
    return HttpResponse(html)


def bug(request):
    return HttpResponse("Баги")


def feature(request):
    return HttpResponse("Фичи")


def bug_detail(request, bug_id):
    return HttpResponse(f"Детали бага {bug_id}")


def feature_detail(request, feature_id):
    return HttpResponse(f"Детали улучшения {feature_id}")