from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import BugReport, FeatureReport
from django.views import View
from django.views.generic import ListView
from django.views.generic import DetailView
from .forms import BugReportForm, FeatureRequestForm
# Create your views here.


# Class-Based Views
class MainPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'quality_control/index.html')
    # def get(self, request, *args, **kwargs):
    #     bug_url = reverse('quality_control:bugs_list')
    #     feature_url = reverse('quality_control:feature_list')
    #     html = (f"<h1>Система контроля качеств</h1>"
    #             f"<a href='{bug_url}'>Список всех багов</a> <br>"
    #             f"<a href='{feature_url}'>Список запросов на улучшение </a>")
    #     return HttpResponse(html)


class BugsListView(ListView):
    model = BugReport
    template_name = 'quality_control/bugs_list.html'
    context_object_name = 'bugs_list'
    # def get(self, request, *args, **kwargs):
    #     bugs = self.get_queryset()
    #     response_html = '<h2>Список багов</h2><ul>'
    #     for bug in bugs:
    #         response_html += (f'<li><a href="{bug.id}/">{bug.title} '
    #                           f'Статус: {bug.get_status_display()}</a></li>')
    #     response_html += '</ul>'
    #     return HttpResponse(response_html)


class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    template_name = 'quality_control/bug_detail.html'
    context_object_name = 'bug'
    # def get(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     bug = self.object
    #     response_html = (f'<h1>{bug.title}</h1>'
    #                      f'<p>Проект: {bug.project}</p>'
    #                      f'<p>Задача: {bug.task}</p>'
    #                      f'<p>Статус: {bug.get_status_display()}</p>'
    #                      f'<p>Приоритет: {bug.priority}</p>'
    #                      f'<p>Описание:</p> <p>{bug.description}</p>')
    #     return HttpResponse(response_html)


class FeaturesListView(ListView):
    model = FeatureReport
    template_name = 'quality_control/features_list.html'
    context_object_name = 'features_list'
    # def get(self, request, *args, **kwargs):
    #     features = self.get_queryset()
    #     response_html = '<h2>Список предложенных улучшений</h2><ul>'
    #     for feature in features:
    #         response_html += (f'<li><a href="{feature.id}/">{feature.title} '
    #                           f'Статус: {feature.get_status_display()} </a></li>')
    #     response_html += '</ul>'
    #     return HttpResponse(response_html)


class FeatureDetailView(DetailView):
    model = FeatureReport
    pk_url_kwarg = 'feature_id'
    template_name = 'quality_control/feature_detail.html'
    context_object_name = 'feature'
    # def get(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     feature = self.object
    #     response_html = (f'<h1>{feature.title}</h1>'
    #                      f'<p>Проект: {feature.project}</p>'
    #                      f'<p>Задача: {feature.task}</p>'
    #                      f'<p>Статус: {feature.get_status_display()}</p>'
    #                      f'<p>Приоритет: {feature.priority}</p>'
    #                      f'<p>Описание:</p> <p>{feature.description}</p>')
    #     return HttpResponse(response_html)


def main_page(request):
    return render(request, 'quality_control/index.html')
    # bug_url = reverse('quality_control:bugs_list')
    # feature_url = reverse('quality_control:feature_list')
    # html = (f"<h1>Система контроля качеств</h1>"
    #         f"<a href='{bug_url}'>Список всех багов</a> <br>"
    #         f"<a href='{feature_url}'>Список запросов на улучшение </a>")
    # return HttpResponse(html)


# Function-Based Views
def bugs_list(request):
    bugs = BugReport.objects.all()
    return render(request, 'quality_control/bugs_list.html',
                  {'bug_list': bugs})
    # bugs = BugReport.objects.all()
    # response_html = '<h2>Список багов</h2><ul>'
    # for bug in bugs:
    #     response_html += (f'<li><a href="{bug.id}/">{bug.title} '
    #                       f'Статус: {bug.get_status_display()}</a></li>')
    # response_html += '</ul>'
    # return HttpResponse(response_html)


def features_list(request):
    features = FeatureReport.objects.all()
    return render(request, 'quality_control/features_list.html',
                  {'feature_list': features})
    # response_html = '<h2>Список предложенных улучшений</h2><ul>'
    # for feature in features:
    #     response_html += (f'<li><a href="{feature.id}/">{feature.title} '
    #                       f'Статус: {feature.get_status_display()} </a></li>')
    # response_html += '</ul>'
    # return HttpResponse(response_html)


def bug_detail(request, bug_id):
    bug = get_object_or_404(BugReport, id=bug_id)
    return render(request, 'quality_control/bug_detail.html', {'bug': bug})
    # response_html = f'<h1>{bug.title}</h1><p>{bug.description}</p>'
    # return HttpResponse(response_html)


def feature_detail(request, feature_id):
    feature = get_object_or_404(FeatureReport, id=feature_id)
    return render(request, 'quality_control/feature_detail.html',
                  {'feature': feature})
    # response_html = f'<h1>{feature.title}</h1><p>{feature.description}</p>'
    # return HttpResponse(response_html)


def add_bug(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bugs_list')
    else:
        form = BugReportForm()
    return render(request, 'quality_control/bug_report_form.html',{'form': form})


def add_feature(request):
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:features_list')
    else:
        form = FeatureRequestForm()
    return render(request, 'quality_control/feature_request_form.html',{'form': form})