from django import forms
from django.forms import ModelForm
from .models import BugReport, FeatureReport, Task, Project


class BugReportForm(forms.ModelForm):
    class Meta:
        model = BugReport
        fields = ['title', 'description','project','task','status', 'priority']
    # не работает без динамического обновления формы после выбора нужно проекта
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['task'].queryset = Task.objects.none()
    #     try:
    #         project_id = int(self.data.get('project'))
    #         self.fields['task'].queryset = Task.objects.filter(project_id=project_id)
    #     except (ValueError, TypeError):
    #         pass

class FeatureRequestForm(forms.ModelForm):
    class Meta:
        model = FeatureReport
        fields = ['title', 'description', 'project', 'task', 'status', 'priority']