from django.http import HttpResponse
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView

from .models import BugReport, FeatureRequest


def bug_list(request):
    bugs = BugReport.objects.all()
    bugs_html = '<h1>Список багов</h1><ul>'
    for bug in bugs:
        bugs_html += f'<li><a href="{bug.id}/">{bug.title}</a> {bug.status}</li>'
    bugs_html += '</ul>'
    return HttpResponse(bugs_html)


def feature_list(request):
    features = FeatureRequest.objects.all()
    features_html = '<h1>Список улучшений</h1><ul>'
    for feature in features:
        features_html += f'<li><a href="{feature.id}/">{feature.title}</a> {feature.status} {feature.priority}</li>'
    features_html += '</ul>'
    return HttpResponse(features_html)


def index(request):
    bugs_page_url = reverse('quality_control:bug_list')
    features_page_url = reverse('quality_control:feature_list')
    html = f"<h1>Система контроля качества</h1>\
            <a href='{bugs_page_url}'>Список всех багов</a><br><a href='{features_page_url}'>Запросы на улучшение</a>"
    return HttpResponse(html)


def feature_detail(request, feature_id):
    return HttpResponse(f'Детали улучшения {feature_id}')


class IndexView(View):
    def get(self, request, *args, **kwargs):
        bugs_page_url = reverse('quality_control:bug_list')
        features_page_url = reverse('quality_control:feature_list')
        html = (f"<h1>Система контроля качества</h1>\
                    <a href='{bugs_page_url}'>Список всех багов</a><br><a href='{features_page_url}'>Запросы на "
                f"улучшение</a>")
        return HttpResponse(html)


class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        bug = self.object
        response_html = f'<h1>{bug.title}</h1><p><h3>Описание:</h3>{bug.description}</p>'
        response_html += f'<h3>Статус</h3>{bug.status}'
        response_html += f'<h3>Связанное задание:</h3>\
                        <a href="../../../tasks/projects/{bug.project.id}/tasks/{bug.task.id}">{bug.task}</a>'
        response_html += (f'<h3>Связанный проект:</h3>\
                          <a href="../../../tasks/projects/{bug.project.id}">{bug.project}</a>')
        return HttpResponse(response_html)


class FeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        feature = self.object
        response_html = f'<h1>{feature.title}</h1><p><h3>Описание:</h3>{feature.description}</p>'
        response_html += f'<h3>Статус</h3>{feature.status}'
        response_html += f'<h3>Приоритет</h3>{feature.priority}'
        response_html += f'<h3>Связанное задание:</h3>\
                                <a href="../../../tasks/projects/{feature.project.id}/tasks/{feature.task.id}">{feature.task}</a>'
        response_html += (f'<h3>Связанный проект:</h3>\
                                  <a href="../../../tasks/projects/{feature.project.id}">{feature.project}</a>')
        return HttpResponse(response_html)