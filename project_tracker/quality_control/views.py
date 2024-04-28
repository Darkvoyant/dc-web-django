from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import BugReport, FeatureReport
from django.views import View
from django.views.generic import ListView
from django.views.generic import DetailView
# Create your views here.


# Class-Based Views
class MainPage(View):
    def get(self, request, *args, **kwargs):
        bug_url = reverse('quality_control:bugs_list')
        feature_url = reverse('quality_control:feature_list')
        html = (f"<h1>Система контроля качеств</h1>"
                f"<a href='{bug_url}'>Список всех багов</a> <br>"
                f"<a href='{feature_url}'>Список запросов на улучшение </a>")
        return HttpResponse(html)


class BugsListView(ListView):
    model = BugReport

    def get(self, request, *args, **kwargs):
        bugs = self.get_queryset()
        response_html = '<h2>Список багов</h2><ul>'
        for bug in bugs:
            response_html += (f'<li><a href="{bug.id}/">{bug.title} '
                              f'Статус: {bug.get_status_display()}</a></li>')
        response_html += '</ul>'
        return HttpResponse(response_html)


class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        bug = self.object
        response_html = (f'<h1>{bug.title}</h1>'
                         f'<p>Проект: {bug.project}</p>'
                         f'<p>Задача: {bug.task}</p>'
                         f'<p>Статус: {bug.get_status_display()}</p>'
                         f'<p>Приоритет: {bug.priority}</p>'
                         f'<p>Описание:</p> <p>{bug.description}</p>')
        return HttpResponse(response_html)


class FeaturesListView(ListView):
    model = FeatureReport

    def get(self, request, *args, **kwargs):
        features = self.get_queryset()
        response_html = '<h2>Список предложенных улучшений</h2><ul>'
        for feature in features:
            response_html += (f'<li><a href="{feature.id}/">{feature.title} '
                              f'Статус: {feature.get_status_display()} </a></li>')
        response_html += '</ul>'
        return HttpResponse(response_html)


class FeatureDetailView(DetailView):
    model = FeatureReport
    pk_url_kwarg = 'feature_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        feature = self.object
        response_html = (f'<h1>{feature.title}</h1>'
                         f'<p>Проект: {feature.project}</p>'
                         f'<p>Задача: {feature.task}</p>'
                         f'<p>Статус: {feature.get_status_display()}</p>'
                         f'<p>Приоритет: {feature.priority}</p>'
                         f'<p>Описание:</p> <p>{feature.description}</p>')
        return HttpResponse(response_html)


def main_page(request):
    bug_url = reverse('quality_control:bugs_list')
    feature_url = reverse('quality_control:feature_list')
    html = (f"<h1>Система контроля качеств</h1>"
            f"<a href='{bug_url}'>Список всех багов</a> <br>"
            f"<a href='{feature_url}'>Список запросов на улучшение </a>")
    return HttpResponse(html)


# Function-Based Views
def bugs_list(request):
    bugs = BugReport.objects.all()
    response_html = '<h2>Список багов</h2><ul>'
    for bug in bugs:
        response_html += (f'<li><a href="{bug.id}/">{bug.title} '
                          f'Статус: {bug.get_status_display()}</a></li>')
    response_html += '</ul>'
    return HttpResponse(response_html)


def feature_list(request):
    features = FeatureReport.objects.all()
    response_html = '<h2>Список предложенных улучшений</h2><ul>'
    for feature in features:
        response_html += (f'<li><a href="{feature.id}/">{feature.title} '
                          f'Статус: {feature.get_status_display()} </a></li>')
    response_html += '</ul>'
    return HttpResponse(response_html)


def bug_detail(request, bug_id):
    bug = get_object_or_404(BugReport, id=bug_id)
    response_html = f'<h1>{bug.title}</h1><p>{bug.description}</p>'
    return HttpResponse(response_html)


def feature_detail(request, feature_id):
    feature = get_object_or_404(FeatureReport, id=feature_id)
    response_html = f'<h1>{feature.title}</h1><p>{feature.description}</p>'
    return HttpResponse(response_html)
