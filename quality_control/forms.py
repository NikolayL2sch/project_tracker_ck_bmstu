from django.forms import ModelForm

from .models import BugReport, FeatureRequest


class BugReportForm(ModelForm):
    class Meta:
        model = BugReport
        fields = ['title', 'description', 'project', 'task', 'status']


class FeatureRequestForm(ModelForm):
    class Meta:
        model = FeatureRequest
        fields = ['title', 'description', 'project', 'task', 'priority', 'status']
