from django import forms
from django.forms import ModelForm
from .models import BugReport, FeatureReport

class BugReportForm(ModelForm):
    class Meta:
        model = BugReport
        fields = ['title', 'description', 'project', 'task', 'status', 'priority']

class FeatureRequestForm(forms.ModelForm):
    class Meta:
        model = FeatureReport
        fields = ['title', 'description', 'project', 'task', 'status', 'priority']